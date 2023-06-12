import requests
import time
import tkinter as tk

def get_crypto_price(crypto):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    crypto_lower = crypto.lower()
    if crypto_lower in data:
        price = data[crypto_lower]["usd"]
        return price
    else:
        return None

def update_price():
    crypto = crypto_entry.get()
    price = get_crypto_price(crypto)
    if price:
        price_label.config(text=f"{crypto.capitalize()} Price (USD): {price}")
        write_to_file(crypto, price)
    else:
        price_label.config(text="Invalid cryptocurrency name.")

def write_to_file(crypto, price):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{current_time} - {crypto}: {price}\n"
    with open("crypto_logs.txt", "a") as file:
        file.write(log_entry)

def on_enter(event=None):
    update_price()
    crypto_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Crypto Price Monitor")

crypto_label = tk.Label(root, text="Enter the name or symbol of the cryptocurrency:")
crypto_label.pack()

crypto_entry = tk.Entry(root)
crypto_entry.pack()
crypto_entry.focus()
crypto_entry.bind("<Return>", on_enter)

enter_button = tk.Button(root, text="Enter", command=on_enter)
enter_button.pack()

price_label = tk.Label(root, text="")
price_label.pack()

root.mainloop()

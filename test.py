import requests
import time
import tkinter as tk
from tkinter import messagebox

class CryptoPriceMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Price Monitor")

        self.create_widgets()
        self.setup_bindings()

    def create_widgets(self):
        self.crypto_label = tk.Label(self.root, text="Enter the name or symbol of the cryptocurrency:")
        self.crypto_label.pack()

        self.crypto_entry = tk.Entry(self.root)
        self.crypto_entry.pack()
        self.crypto_entry.focus()

        self.enter_button = tk.Button(self.root, text="Enter", command=self.on_enter)
        self.enter_button.pack()

        self.price_label = tk.Label(self.root, text="")
        self.price_label.pack()

    def setup_bindings(self):
        self.crypto_entry.bind("<Return>", self.on_enter)

    def get_crypto_price(self, crypto):
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            crypto_lower = crypto.lower()
            if crypto_lower in data:
                return data[crypto_lower]["usd"]
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        return None

    def update_price(self):
        crypto = self.crypto_entry.get()
        if not crypto:
            messagebox.showwarning("Input Error", "Please enter a cryptocurrency name or symbol.")
            return

        price = self.get_crypto_price(crypto)
        if price:
            self.price_label.config(text=f"{crypto.capitalize()} Price (USD): {price}")
            self.write_to_file(crypto, price)
        else:
            self.price_label.config(text="Invalid cryptocurrency name or symbol.")

    def write_to_file(self, crypto, price):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{current_time} - {crypto}: {price}\n"
        with open("crypto_logs.txt", "a") as file:
            file.write(log_entry)

    def on_enter(self, event=None):
        self.update_price()
        self.crypto_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoPriceMonitor(root)
    root.mainloop()

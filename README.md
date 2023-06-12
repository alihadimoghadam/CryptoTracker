# CryptoTracker

CryptoTracker is a simple Python script with a graphical user interface (GUI) that allows you to monitor the prices of various cryptocurrencies using the CoinGecko API. It fetches the current price of a specified cryptocurrency and displays it in the GUI. Additionally, it saves the price logs with timestamps to a text file.

## Features

- Fetches and displays the current price of a cryptocurrency in USD.
- Supports both cryptocurrency symbols and names for retrieving prices.
- Provides a graphical user interface (GUI) for ease of use.
- Automatically updates the price every time the Enter key is pressed or the "Enter" button is clicked.
- Saves the price logs with timestamps to a text file.

## Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)
- `tkinter` library (pre-installed with Python)

## Usage

1. Clone the repository or download the `CryptoTracker.py` file.
2. Install the required `requests` library if not already installed: `pip install requests`.
3. Run the script: `python CryptoTracker.py`.
4. Enter the name or symbol of the cryptocurrency you want to monitor in the GUI.
5. Press the Enter key or click the "Enter" button to fetch the price.
6. The current price will be displayed in the GUI, and the logs will be saved in the "crypto_logs.txt" file.

**Note:** Continuous polling of an API every time the price is updated can be resource-intensive and may violate the API provider's usage limits or terms of service. Make sure to check the API documentation for any rate limits or restrictions before using this code in a production environment.

## License

[MIT License](LICENSE)

Feel free to customize the README file according to your specific project requirements and any additional information you would like to provide to users.
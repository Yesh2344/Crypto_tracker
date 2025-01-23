import requests
import csv
from datetime import datetime
import time
import argparse

def fetch_crypto_data(crypto_ids):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(crypto_ids),
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    response = requests.get(url, params=params)
    return response.json()

def save_to_csv(data, filename):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write header if file is empty
        if file.tell() == 0:
            writer.writerow(["Timestamp", "Cryptocurrency", "Price (USD)", "24h Change (%)"])
        
        # Write data
        for crypto, info in data.items():
            writer.writerow([
                timestamp,
                crypto,
                info['usd'],
                info['usd_24h_change']
            ])

def main(crypto_ids, interval, duration):
    filename = f"crypto_prices_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    end_time = time.time() + (duration * 60 * 60)  # Convert hours to seconds
    
    while time.time() < end_time:
        try:
            data = fetch_crypto_data(crypto_ids)
            save_to_csv(data, filename)
            print(f"Data saved at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            time.sleep(interval * 60)  # Convert minutes to seconds
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(60)  # Wait for 1 minute before retrying

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CryptoTracker: Track cryptocurrency prices")
    parser.add_argument("cryptos", nargs="+", help="List of cryptocurrency IDs to track (e.g., bitcoin ethereum)")
    parser.add_argument("--interval", type=int, default=5, help="Interval between price checks in minutes (default: 5)")
    parser.add_argument("--duration", type=int, default=24, help="Duration to run the tracker in hours (default: 24)")
    
    args = parser.parse_args()
    
    main(args.cryptos, args.interval, args.duration)

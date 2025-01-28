# 🚀 CryptoTracker

## Overview

CryptoTracker is a Python script that allows you to track cryptocurrency prices in real-time, saving historical price data to a CSV file. The script uses the CoinGecko API to fetch current prices and 24-hour price changes for specified cryptocurrencies.

## Features

- 📊 Real-time cryptocurrency price tracking
- 💾 Automatic CSV data logging
- 🕒 Configurable tracking interval
- ⏱️ Adjustable tracking duration
- 🛡️ Error handling and automatic retry mechanism

## Prerequisites

- Python 3.7+
- `requests` library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/crypto-tracker.git
cd crypto-tracker
```

2. Install required dependencies:
```bash
pip install requests
```

## Usage

Run the script with the following command:

```bash
python crypto_tracker.py bitcoin ethereum dogecoin
```

### Command-line Arguments

- `cryptos`: List of cryptocurrency IDs to track (required)
- `--interval`: Interval between price checks in minutes (optional, default: 5)
- `--duration`: Total duration to run the tracker in hours (optional, default: 24)

### Examples

1. Track Bitcoin and Ethereum every 5 minutes for 24 hours:
```bash
python crypto_tracker.py bitcoin ethereum
```

2. Track specific cryptocurrencies with custom interval and duration:
```bash
python crypto_tracker.py bitcoin dogecoin --interval 10 --duration 12
```

## Output

- Creates a CSV file named `crypto_prices_YYYYMMDD_HHMMSS.csv`
- Columns: Timestamp, Cryptocurrency, Price (USD), 24h Change (%)

## Error Handling

- Automatically retries after errors
- Waits 1 minute between retry attempts
- Prints error messages to console

## Dependencies

- `requests`: For making API calls
- `csv`: For writing data to CSV files
- `datetime`: For timestamping
- `time`: For tracking duration and intervals
- `argparse`: For handling command-line arguments

## API

Uses CoinGecko API (https://www.coingecko.com/en/api)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Disclaimer

Cryptocurrency prices are highly volatile. Use this tool for informational purposes only.

@Yeswanth Soma All Copyrights Reserved

For Contact Enquiries:
Email:yeswanthsoma83@gmail.com

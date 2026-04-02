# SGD Currency Converter CLI

A command-line currency converter for Singapore Dollar (SGD) built in Python — no dependencies required.

## Overview

A simple terminal tool that displays live-timestamped SGD exchange rate tables and lets you convert specific amounts across six currencies. Useful as a quick offline reference or a starting point for a more dynamic converter.

## Features

- Formatted conversion tables for standard SGD amounts
- Convert any specific SGD amount to a chosen currency
- View all currency tables at once
- Timestamp shown on launch

## Supported Currencies

| Code | Currency        | Rate (per SGD) |
|------|----------------|----------------|
| USD  | US Dollar       | 0.78           |
| THB  | Thai Baht       | 24.96          |
| CNY  | Chinese Yuan    | 5.56           |
| JPY  | Japanese Yen    | 114.64         |
| GBP  | British Pound   | 0.58           |
| MYR  | Malaysian Ringgit | 3.29         |

> Rates are hardcoded and should be updated manually to reflect current market values.

## Getting Started
```bash
git clone https://github.com/yourusername/sgd-currency-converter
cd sgd-currency-converter
python currency_converter.py
```

No external dependencies — just the Python standard library.

## Usage

| Option | Action |
|--------|--------|
| 1 | View conversion table for a single currency |
| 2 | View conversion tables for all currencies |
| 3 | Convert a specific SGD amount |
| 4 | Exit |

### Example — specific conversion
```
Enter an SGD amount to convert: 250
Enter the currency to convert to: JPY
$250.00 SGD = 28,660.00 JPY
```

### Example — table output
```
SGD -> JPY (Rate: 114.64)
========================================
SGD            JPY
----------------------------------------
$1.00          114.64
$5.00          573.20
$100.00     11,464.00
...
```

## File Structure
```
sgd-currency-converter/
└── currency_converter.py    # Main application
```

## Possible Improvements

- Fetch live rates from an exchange rate API (e.g. [exchangerate-api.com](https://www.exchangerate-api.com))
- Support conversion from currencies other than SGD
- Add a reverse lookup (e.g. JPY → SGD)
- Export tables to CSV

## License

MIT

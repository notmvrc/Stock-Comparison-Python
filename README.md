# Financial Market Analysis Tool

A Python-based tool to automate the comparison of financial assets using historical data. This script normalizes stock prices to a "Base 100" scale, allowing for a direct performance comparison between assets with vastly different price ranges (e.g., comparing a bank stock trading at 3 EUR vs a tech stock trading at 200 USD).

![Stock Performance Chart](stock_performance.png)
(Example output: Comparative analysis of Italian Banks vs US Tech Giants)

## Key Features
* Automated Data Retrieval: Fetches real-time/historical adjusted close prices using the Yahoo Finance API (yfinance).
* Data Normalization: Re-bases all assets to start at 100, enabling relative performance analysis over time.
* Visualization: Generates professional-grade comparative charts using Matplotlib.
* Scalability: The script handles dynamic lists of tickers and automatically adjusts the timeframe.

## Financial Logic: Base 100 Normalization
Comparing raw stock prices is misleading due to different denominations and currencies. This tool applies the following transformation to every data point to simulate relative returns:

$$P_{normalized}(t) = \left( \frac{P_t}{P_0} \right) \times 100$$

Where:
* P_t is the price at time t.
* P_0 is the initial price (investment start date).

This simulates the growth of a hypothetical equal investment (e.g., 100 units) in each asset.

## Technologies Used
* Python 3.10+
* Pandas: For time-series data manipulation.
* Yfinance: For market data extraction.
* Matplotlib: For data visualization.

## How to Run
1. Install the required libraries:
    pip install yfinance matplotlib pandas

2. Run the script:
    python stock_analysis.py

3. The chart will be displayed and saved locally as stock_performance.png.

---
Created by notmvrc

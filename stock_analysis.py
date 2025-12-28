import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# --- CONFIGURATION ---
tickers = ['ISP.MI', 'UCG.MI', 'AAPL', 'MSFT'] 

print(f"1. Downloading data for: {tickers}...")

# MODIFICA: Ho rimosso ['Adj Close'] e uso 'Close' che è più sicuro con la nuova versione
# auto_adjust=True fa sì che i prezzi siano già rettificati
data = yf.download(tickers, start="2023-01-01", auto_adjust=True)['Close']

print("2. Data downloaded successfully!")

# --- FINANCIAL CALCULATIONS ---
# Normalize to Base 100.
normalized_data = (data / data.iloc[0]) * 100

# --- PLOTTING ---
print("3. Generating plot...")
plt.figure(figsize=(12, 6))

# Plot the lines
for c in normalized_data.columns:
    plt.plot(normalized_data.index, normalized_data[c], label=c)

# Chart labels and styling
plt.title('Relative Performance: IT Banks vs US Tech (Base 100)')
plt.xlabel('Date')
plt.ylabel('Investment Value (Start = 100)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Save the chart as an image
filename = 'stock_performance.png'
plt.savefig(filename)
print(f"4. DONE! Chart saved as '{filename}'.")

# Show the chart window
plt.show()
import yfinance as yf
import pandas as pd


# Load a stock
ticker = yf.Ticker("APLD")
income_statement = ticker.financials.T
balance_sheet = ticker.balancesheet.T


def format_number(value):
    return f"{value:,.0f}"

symbol = ticker.info.get("symbol")
industry = ticker.info.get("industryKey")
current_price = ticker.info.get("currentPrice")
m_cap = ticker.info.get("marketCap")
ev = ticker.info.get("enterpriseValue")
beta = ticker.info.get("beta")
high_52 = ticker.info.get("fiftyTwoWeekHigh")
low_52 = ticker.info.get("fiftyTwoWeekLow")
target_high = ticker.info.get("targetHighPrice")
target_low = ticker.info.get("targetLowPrice")
volume = ticker.info.get("volume")
vol_10day = ticker.info.get("averageDailyVolume10Day")
vol_30day = ticker.info.get("averageDailyVolume3Month")
avg_50day = ticker.info.get("fiftyDayAverage")
avg_200day = ticker.info.get("twoHundredDayAverage")
short_rato = ticker.info.get("shortRatio")
outstanding_short = ticker.info.get("sharesPercentSharesOut")
float_short = ticker.info.get("shortPercentOfFloat")
forward_pe = ticker.info.get("forwardPE")
price_book = ticker.info.get("priceToBook")
quick_ratio = ticker.info.get("quickRatio")
return_equity = ticker.info.get("returnOnEquity")

print(f"Symbol: {symbol}")
print(f"Industry: {industry}")
print(f"Current_Price: {current_price}")
print(f"M_Cap: {format_number(m_cap)}$")
print(f"EV: {format_number(ev)}$")
print(f"Beta: {beta}")
print(f"52_Week_High: {high_52}")
print(f"52_Week_Low: {low_52}")
print(f"Target_High: {target_high}")
print(f"Target_Low: {target_low}")
print(f"Volume_1_Day: {format_number(volume)}")
print(f"Avg_Vol_10_Day: {format_number(vol_10day)}")
print(f"Avg_Vol_3_M: {format_number(vol_30day)}")
print(f"50_MA: {avg_50day}")
print(f"200_MA: {avg_200day}")
print(f"Short_Ratio(Days_To_cover): {short_rato}")
print(f"Short_%_Outstanding: {outstanding_short*100}%")
print(f"Short_%_Float: {format_number(float_short*100)}%")
print(f"Forward_PE: {forward_pe}")
print(f"Price_To_Book: {price_book}")
print(f"Quick_ratio: {quick_ratio}")
print(f"Return_On_Equity: {return_equity}")

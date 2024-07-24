import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# Function to fetch stock data
def fetch_stock_data(symbols):
    data = []
    for symbol in symbols:
        ticker = f"{symbol}.NS"
        stock = yf.Ticker(ticker)
        stock_data = stock.history(period="1d")
        if not stock_data.empty:
            data.append({
                'Instrument': symbol,
                'Latest Value': stock_data['Close'].values[0],
                'Open': stock_data['Open'].values[0],
                'High': stock_data['High'].values[0],
                'Low': stock_data['Low'].values[0],
                'Volume': stock_data['Volume'].values[0],
                'Market Cap': stock.info.get('marketCap', None),
                '52-Week High': stock.info.get('fiftyTwoWeekHigh', None),
                '52-Week Low': stock.info.get('fiftyTwoWeekLow', None),
                'PE Ratio': stock.info.get('trailingPE', None),
                'Dividend Yield': stock.info.get('dividendYield', None),
                'Beta': stock.info.get('beta', None)
            })
        else:
            data.append({
                'Instrument': symbol,
                'Latest Value': None,
                'Open': None,
                'High': None,
                'Low': None,
                'Volume': None,
                'Market Cap': None,
                '52-Week High': None,
                '52-Week Low': None,
                'PE Ratio': None,
                'Dividend Yield': None,
                'Beta': None
            })
    return data

st.title("Indian Stock Prices Fetcher")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    stock_symbols = df.iloc[:, 0].tolist()  # Read the first column ignoring the header
    
    if st.button("Fetch Latest Stock Prices"):
        stock_data = fetch_stock_data(stock_symbols)
        result_df = pd.DataFrame(stock_data)
        
        st.write("## Stock Prices")
        st.dataframe(result_df)

        # Generate CSV
        csv = result_df.to_csv(index=False)
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='latest_stock_prices.csv',
            mime='text/csv',
        )

        # Visualizations
        st.write("## Visualizations")

        # Bar plot of stock prices
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x='Latest Value', y='Instrument', data=result_df, ax=ax)
        ax.set_title('Stock Prices')
        st.pyplot(fig)

        # Distribution plot of stock prices
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(result_df['Latest Value'].dropna(), kde=True, ax=ax)
        ax.set_title('Distribution of Stock Prices')
        st.pyplot(fig)

        # Box plot of stock prices
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(x='Latest Value', data=result_df, ax=ax)
        ax.set_title('Box Plot of Stock Prices')
        st.pyplot(fig)
        
        # Line chart of stock prices
        st.write("## Line Chart of Stock Prices")
        for symbol in stock_symbols:
            ticker = f"{symbol}.NS"
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1mo")
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=hist.index, y=hist['Close'], mode='lines', name=symbol))
            fig.update_layout(title=f'Price Trend for {symbol}', xaxis_title='Date', yaxis_title='Price')
            st.plotly_chart(fig)

        # Volume bar chart
        st.write("## Volume Bar Chart")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x='Volume', y='Instrument', data=result_df, ax=ax)
        ax.set_title('Trading Volume')
        st.pyplot(fig)

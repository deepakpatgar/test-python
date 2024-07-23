import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import numpy as np

# Function to fetch market data from yfinance
def fetch_market_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    # Simulate bid and offer volumes
    np.random.seed(42)
    stock_data['Bid_Volume'] = np.random.randint(1000, 5000, size=len(stock_data))
    stock_data['Offer_Volume'] = np.random.randint(1000, 5000, size=len(stock_data))
    return stock_data

# Function to calculate technical indicators
def calculate_technical_indicators(data):
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['EMA_20'] = data['Close'].ewm(span=20, adjust=False).mean()
    
    # Calculate MACD
    data['EMA_12'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['EMA_26'] = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = data['EMA_12'] - data['EMA_26']
    data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
    
    # Calculate Bollinger Bands
    data['BB_Middle'] = data['Close'].rolling(window=20).mean()
    data['BB_Upper'] = data['BB_Middle'] + 2 * data['Close'].rolling(window=20).std()
    data['BB_Lower'] = data['BB_Middle'] - 2 * data['Close'].rolling(window=20).std()
    
    # Calculate RSI
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))
    
    return data

# Function to plot daily trend with technical indicators
def plot_daily_trend_with_indicators(data, ticker):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close'))
    fig.add_trace(go.Scatter(x=data.index, y=data['SMA_20'], mode='lines', name='SMA 20'))
    fig.add_trace(go.Scatter(x=data.index, y=data['SMA_50'], mode='lines', name='SMA 50'))
    fig.add_trace(go.Scatter(x=data.index, y=data['EMA_20'], mode='lines', name='EMA 20'))
    fig.add_trace(go.Scatter(x=data.index, y=data['BB_Upper'], mode='lines', name='BB Upper', line=dict(dash='dash')))
    fig.add_trace(go.Scatter(x=data.index, y=data['BB_Lower'], mode='lines', name='BB Lower', line=dict(dash='dash')))
    fig.update_layout(title=f'Daily Trend with Technical Indicators for {ticker}', xaxis_title='Date', yaxis_title='Price')
    return fig

# Function to plot MACD
def plot_macd(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['MACD'], mode='lines', name='MACD'))
    fig.add_trace(go.Scatter(x=data.index, y=data['Signal_Line'], mode='lines', name='Signal Line'))
    fig.update_layout(title='MACD', xaxis_title='Date', yaxis_title='Value')
    return fig

# Function to plot RSI
def plot_rsi(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['RSI'], mode='lines', name='RSI'))
    fig.update_layout(title='Relative Strength Index (RSI)', xaxis_title='Date', yaxis_title='RSI')
    return fig

# Function to plot day-wise analysis
def plot_daywise_analysis(data):
    data['DayOfWeek'] = data.index.day_name()
    avg_price = data.groupby('DayOfWeek')['Close'].mean().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
    fig = px.bar(avg_price, x=avg_price.index, y='Close', title='Average Closing Price by Day of the Week')
    return fig

# Function to plot bid/offer volumes
def plot_bid_offer_volumes(data):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data.index, y=data['Bid_Volume'], name='Bid Volume', marker_color='blue'))
    fig.add_trace(go.Bar(x=data.index, y=data['Offer_Volume'], name='Offer Volume', marker_color='red'))
    fig.update_layout(title='Bid/Offer Volumes', xaxis_title='Date', yaxis_title='Volume', barmode='group')
    return fig

# Function to plot weekly bid/offer volume trends
def plot_weekly_bid_offer_trends(data):
    data['DayOfWeek'] = data.index.day_name()
    avg_bid_volume = data.groupby('DayOfWeek')['Bid_Volume'].mean().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
    avg_offer_volume = data.groupby('DayOfWeek')['Offer_Volume'].mean().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
    fig = go.Figure()
    fig.add_trace(go.Bar(x=avg_bid_volume.index, y=avg_bid_volume, name='Avg Bid Volume', marker_color='blue'))
    fig.add_trace(go.Bar(x=avg_offer_volume.index, y=avg_offer_volume, name='Avg Offer Volume', marker_color='red'))
    fig.update_layout(title='Weekly Bid/Offer Volume Trends', xaxis_title='Day of the Week', yaxis_title='Volume', barmode='group')
    return fig

# Function to plot sector performance
def plot_sector_performance(tickers, start_date, end_date):
    sector_data = {}
    for ticker in tickers:
        data = yf.download(ticker, start=start_date, end=end_date)
        sector_data[ticker] = data['Close']

    sector_df = pd.DataFrame(sector_data)
    fig = px.line(sector_df, x=sector_df.index, y=sector_df.columns, title='Sector Performance')
    return fig

# Streamlit app layout
st.title("Market Depth Analysis")

# Input: Select market index
market_index = st.selectbox('Select Market Index', ['^NSEI', '^BSESN', '^NSEBANK', '^NIFTY50'])

# Input: Date range
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

# Fetch and display data
if st.button("Analyze"):
    if start_date and end_date:
        try:
            # Fetch data from yfinance
            data = fetch_market_data(market_index, start_date, end_date)
            
            # Calculate technical indicators
            data = calculate_technical_indicators(data)
            
            # Display raw data
            st.subheader("Market Data")
            st.write(data.tail())
            
            # Create two columns for side-by-side visualization
            col1, col2 = st.columns(2)

            # Plot daily trend with technical indicators
            with col1:
                st.subheader("Daily Trend with Technical Indicators")
                daily_trend_fig = plot_daily_trend_with_indicators(data, market_index)
                st.plotly_chart(daily_trend_fig)

            # Plot day-wise analysis
            with col2:
                st.subheader("Day-wise Analysis")
                daywise_analysis_fig = plot_daywise_analysis(data)
                st.plotly_chart(daywise_analysis_fig)
            
            # Plot MACD
            st.subheader("MACD")
            macd_fig = plot_macd(data)
            st.plotly_chart(macd_fig)
            
            # Plot RSI
            st.subheader("RSI")
            rsi_fig = plot_rsi(data)
            st.plotly_chart(rsi_fig)
            
            # Plot bid/offer volumes
            col3, col4 = st.columns(2)
            with col3:
                st.subheader("Bid/Offer Volumes")
                bid_offer_volumes_fig = plot_bid_offer_volumes(data)
                st.plotly_chart(bid_offer_volumes_fig)
            
            # Plot weekly bid/offer volume trends
            with col4:
                st.subheader("Weekly Bid/Offer Volume Trends")
                weekly_bid_offer_trends_fig = plot_weekly_bid_offer_trends(data)
                st.plotly_chart(weekly_bid_offer_trends_fig)

            # Plot sector performance
            st.subheader("Sector Performance")
            sector_tickers = ['^NIFTYIT', '^NIFTYREALTY', '^NIFTYMNC', '^NIFTY100', '^NIFTYMIDCAP150', '^NIFTYSMALLCAP250', '^NIFTYINFRA']
            sector_performance_fig = plot_sector_performance(sector_tickers, start_date, end_date)
            st.plotly_chart(sector_performance_fig)
            
        except Exception as e:
            st.error(f"Error fetching data: {e}")
    else:
        st.error("Please select a valid date range.")

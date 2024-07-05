import streamlit as st
import speedtest
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import time

# Initialize session state
if 'results' not in st.session_state:
    st.session_state['results'] = pd.DataFrame(columns=['Time', 'Download Speed', 'Upload Speed', 'Ping'])

# Function to perform the speed test
def perform_speed_test():
    st.write("Running speed test...")
    progress_bar = st.progress(0)
    for i in range(101):
        progress_bar.progress(i)
        time.sleep(0.05)  # Simulating the speed test delay
    st.spinner()
    stt = speedtest.Speedtest()
    stt.get_best_server()
    download_speed = stt.download() / 1_000_000  # Convert to Mbps
    upload_speed = stt.upload() / 1_000_000  # Convert to Mbps
    ping = stt.results.ping
    return download_speed, upload_speed, ping

# Function to create a gauge plot with customized color ranges and markers
def create_gauge_plot(value, title, max_value):
    color_scale = [
        (0.0, "lightgreen"),
        (0.5, "green"),
        (0.8, "orange"),
        (1.0, "red")
    ]
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={
            'axis': {'range': [None, max_value]},
            'bar': {'color': "rgba(0, 0, 0, 0)"},
            'steps': [
                {'range': [0, max_value * 0.5], 'color': color_scale[0][1]},
                {'range': [max_value * 0.5, max_value * 0.8], 'color': color_scale[1][1]},
                {'range': [max_value * 0.8, max_value], 'color': color_scale[3][1]}],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': value}
        }
    ))
    fig.update_layout(width=300, height=300, margin=dict(l=20, r=20, t=50, b=50))
    return fig

st.set_page_config(layout="wide")
st.title("Internet Speed Test")

if st.button("Start Test"):
    download_speed, upload_speed, ping = perform_speed_test()

    # Store the results in session state
    new_result = pd.DataFrame({
        'Time': [pd.Timestamp.now()],
        'Download Speed': [download_speed],
        'Upload Speed': [upload_speed],
        'Ping': [ping]
    })
    st.session_state['results'] = pd.concat([st.session_state['results'], new_result], ignore_index=True)

    st.subheader("Speed Test Results:")
    st.write(f"Download Speed: {download_speed:.2f} Mbps")
    st.write(f"Upload Speed: {upload_speed:.2f} Mbps")
    st.write(f"Ping: {ping:.2f} ms")

    st.subheader("Visualizations and Statistics:")

    # Place the gauge plots side by side
    col1, col2, col3 = st.columns(3)
    with col1:
        download_gauge = create_gauge_plot(download_speed, "Download Speed (Mbps)", 20)
        st.plotly_chart(download_gauge)
    with col2:
        upload_gauge = create_gauge_plot(upload_speed, "Upload Speed (Mbps)", 5)
        st.plotly_chart(upload_gauge)
    with col3:
        ping_gauge = create_gauge_plot(ping, "Ping (ms)", 900)
        st.plotly_chart(ping_gauge)

    st.subheader("Statistics:")
    st.write("Below are some statistics for the speed test results:")

    stats_df = pd.DataFrame({
        'Metric': ['Mean', 'Median', 'Min', 'Max', 'Standard Deviation'],
        'Download Speed (Mbps)': [0, 0, 0, 0, 0],
        'Upload Speed (Mbps)': [0, 0, 0, 0, 0],
        'Ping (ms)': [0, 0, 0, 0, 0]
    })
    
    # Calculate statistics
    stats_df.loc[:, 'Download Speed (Mbps)'] = [
        st.session_state['results']['Download Speed'].mean(),
        st.session_state['results']['Download Speed'].median(),
        st.session_state['results']['Download Speed'].min(),
        st.session_state['results']['Download Speed'].max(),
        st.session_state['results']['Download Speed'].std()]
    
    stats_df.loc[:, 'Upload Speed (Mbps)'] = [
        st.session_state['results']['Upload Speed'].mean(),
        st.session_state['results']['Upload Speed'].median(),
        st.session_state['results']['Upload Speed'].min(),
        st.session_state['results']['Upload Speed'].max(),
        st.session_state['results']['Upload Speed'].std()]
    
    stats_df.loc[:, 'Ping (ms)'] = [
        st.session_state['results']['Ping'].mean(),
        st.session_state['results']['Ping'].median(),
        st.session_state['results']['Ping'].min(),
        st.session_state['results']['Ping'].max(),
        st.session_state['results']['Ping'].std()]

    st.markdown("""
    <style>
    .dataframe-table {
        border-collapse: collapse;
        width: 100%;
    }
    .dataframe-table th, .dataframe-table td {
        border: 1px solid #ddd;
        padding: 8px;
    }
    .dataframe-table th {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: left;
        background-color: #4CAF50;
        color: white;
    }
    .dataframe-table td {
        text-align: right;
    }
    .dataframe-table tr:nth-child(even){background-color: #f2f2f2;}
    .dataframe-table tr:hover {background-color: #ddd;}
    </style>
    """, unsafe_allow_html=True)

    stats_html = stats_df.to_html(index=False, classes='dataframe-table')
    st.markdown(stats_html, unsafe_allow_html=True)

    # Visualize statistics
    st.write("Statistics Visualizations:")
    stats_fig = px.bar(stats_df, x='Metric', y=['Download Speed (Mbps)', 'Upload Speed (Mbps)', 'Ping (ms)'], barmode='group')
    st.plotly_chart(stats_fig)

    st.subheader("Historical Data:")
    st.write("Here are the latest 10 speed test results:")
    historical_df = st.session_state['results'].tail(10)
    historical_html = historical_df.to_html(index=False, classes='dataframe-table')
    st.markdown(historical_html, unsafe_allow_html=True)

    # Visualize historical data
    st.write("Historical Data Visualizations:")
    time_series_fig = go.Figure()
    time_series_fig.add_trace(go.Scatter(x=st.session_state['results']['Time'], y=st.session_state['results']['Download Speed'], mode='lines+markers', name='Download Speed'))
    time_series_fig.add_trace(go.Scatter(x=st.session_state['results']['Time'], y=st.session_state['results']['Upload Speed'], mode='lines+markers', name='Upload Speed'))
    time_series_fig.add_trace(go.Scatter(x=st.session_state['results']['Time'], y=st.session_state['results']['Ping'], mode='lines+markers', name='Ping'))
    time_series_fig.update_layout(width=1200, height=500, margin=dict(l=20, r=20, t=50, b=50))
    st.plotly_chart(time_series_fig)

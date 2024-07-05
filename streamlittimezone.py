import streamlit as st
import pandas as pd
import pytz
from datetime import datetime
import plotly.express as px

# Function to determine if it's day or night based on time
def is_day(time):
    return 6 <= time.hour < 18

# Create input widgets for date and time
st.title("Time Zone Converter")

current_time = datetime.now()

# Time zone selection
timezones = [
    'Asia/Kolkata', 'UTC', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney',
    'America/Los_Angeles', 'America/Chicago', 'America/New_York',
    'America/Denver', 'America/Phoenix', 'America/Anchorage',
    'Europe/Moscow', 'Australia/Perth',
    'Asia/Dubai', 'Antarctica/Palmer','Africa/Lagos', 'Africa/Nairobi','Asia/Tehran',
    'Asia/Shanghai', 'Asia/Istanbul', 'Asia/Jakarta', 'Asia/Seoul',
    'Asia/Taipei', 'Asia/Bangkok', 'Asia/Kuala_Lumpur', 'Asia/Singapore', 'Asia/Hong_Kong',
    'Asia/Manila', 'Australia/Melbourne', 'Europe/Paris',
    'Europe/Berlin'
]

selected_tz = st.selectbox('Select Time Zone', timezones, index=0)
selected_tz = pytz.timezone(selected_tz)
current_time = current_time.astimezone(selected_tz)

col1, col2, col3 = st.columns(3)

with col1:
    year = st.selectbox('Year', list(range(2000, 2031)), index=current_time.year - 2000)
with col2:
    month = st.selectbox('Month', list(range(1, 13)), index=current_time.month - 1)
with col3:
    day = st.selectbox('Date', list(range(1, 32)), index=current_time.day - 1)

col4, col5, col6, col7 = st.columns(4)

with col4:
    hour = st.selectbox('Hour', list(range(1, 13)), index=(current_time.hour % 12) - 1)
with col5:
    minute = st.selectbox('Minute', list(range(0, 60)), index=current_time.minute)
with col6:
    second = st.selectbox('Second', list(range(0, 60)), index=current_time.second)
with col7:
    ampm = st.selectbox('AM/PM', ['AM', 'PM'], index=0 if current_time.hour < 12 else 1)

# Convert 12-hour time to 24-hour time
if ampm == 'PM' and hour != 12:
    hour += 12
elif ampm == 'AM' and hour == 12:
    hour = 0

# Combine date and time
local_time = datetime(year, month, day, hour, minute, second)
local_dt = selected_tz.localize(local_time)

# Create a DataFrame to store time in different zones
data = []
for tz_name in timezones:
    tz = pytz.timezone(tz_name)
    tz_time = local_dt.astimezone(tz)
    data.append({
        'Time Zone': tz_name,
        'Date': tz_time.strftime('%Y-%m-%d'),
        'Time': tz_time.strftime('%I:%M:%S %p'),
        'Day/Night': 'Day' if is_day(tz_time) else 'Night'
    })

df = pd.DataFrame(data)

# Apply color formatting
def color_day_night(val):
    color = 'lightyellow' if val == 'Day' else 'lightskyblue'
    return f'background-color: {color}'

# Display DataFrame
st.write("Time in Different Time Zones")
st.dataframe(df.style.applymap(color_day_night, subset=['Day/Night']))

# Visualization: Distribution of hours across different time zones
df['Hour'] = df['Time'].apply(lambda x: int(x.split(':')[0]) % 12 + (12 if 'PM' in x else 0))

fig1 = px.histogram(df, x='Hour', color='Time Zone', title='Distribution of Hours Across Time Zones')

# Create a DataFrame for the pie chart
day_night_counts = df['Day/Night'].value_counts().reset_index()
day_night_counts.columns = ['Day/Night', 'Count']

fig2 = px.pie(day_night_counts, values='Count', names='Day/Night', title='Day and Night Distribution')

# Additional visualization: Bar chart of time zones
fig3 = px.bar(df, x='Time Zone', y='Hour', color='Day/Night', title='Time Zones and Hours')

# Additional visualization: Scatter plot of time zones
fig4 = px.scatter(df, x='Time Zone', y='Hour', color='Time Zone', title='Time Zones Scatter Plot')

# Display plots side by side
st.write("Visualizations")
col1, col2 = st.columns(2)
col1.plotly_chart(fig1, use_container_width=True)
col2.plotly_chart(fig2, use_container_width=True) 

col3, col4 = st.columns(2)
col3.plotly_chart(fig3, use_container_width=True)
col4.plotly_chart(fig4, use_container_width=True)





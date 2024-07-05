import streamlit as st
import pandas as pd
import datetime
import calendar
import holidays

# Initialize the events DataFrame in session state
if 'events' not in st.session_state:
    st.session_state.events = pd.DataFrame(columns=['Date', 'Time', 'Event', 'Type'])

def add_event(date, time, event, event_type):
    # Ensure 'Date' is converted to datetime
    date = pd.to_datetime(date)
    new_event = pd.DataFrame({'Date': [date], 'Time': [time], 'Event': [event], 'Type': [event_type]})
    st.session_state.events = pd.concat([st.session_state.events, new_event], ignore_index=True)

def display_events(month, year, indian_holidays):
    st.write(f"## Events in {calendar.month_name[month]} {year}")
    # Ensure 'Date' column is datetime type
    st.session_state.events['Date'] = pd.to_datetime(st.session_state.events['Date'])
    
    # Filter events for the selected month and year
    filtered_events = st.session_state.events[(st.session_state.events['Date'].dt.month == month) &
                                              (st.session_state.events['Date'].dt.year == year)]
    
    # Filter Indian holidays for the selected month and year
    holiday_events = []
    for date, (holiday_name, holiday_type) in indian_holidays.items():
        holiday_date = pd.to_datetime(date)
        if holiday_date.month == month and holiday_date.year == year:
            holiday_events.append({'Date': holiday_date, 'Time': '', 'Event': holiday_name, 'Type': holiday_type})
    
    # Concatenate holiday events with filtered events
    if holiday_events:
        holiday_df = pd.DataFrame(holiday_events)
        filtered_events = pd.concat([filtered_events, holiday_df], ignore_index=True)
    
    # Display the combined events
    if not filtered_events.empty:
        st.table(filtered_events[['Date', 'Time', 'Event', 'Type']])
    else:
        st.write("No events for this month.")

def event_color(event_type):
    colors = {
        "Holiday": "lightgreen",
        "Professional": "lightblue",
        "Personal": "lightcoral"
    }
    return colors.get(event_type, "white")

class EventCalendar(calendar.HTMLCalendar):
    def __init__(self, events, holidays_data):
        super().__init__(calendar.SUNDAY)
        self.events = events
        self.holidays_data = holidays_data

    def formatday(self, day, weekday, theyear, themonth):
        today = datetime.date.today()
        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        
        cssclass = self.cssclasses[weekday]
        if (theyear == today.year and themonth == today.month and day == today.day):
            cssclass += ' current-day'
        
        events_today = self.events[self.events['Date'] == datetime.date(theyear, themonth, day)]
        holiday_info = self.holidays_data.get(datetime.date(theyear, themonth, day), None)

        if holiday_info:
            holiday_name, holiday_type = holiday_info
            color = event_color(holiday_type)
            cssclass += f' holiday-day {holiday_type.lower()}-event'  # Add specific class for holiday types
            return f'<td class="{cssclass}" style="background-color: {color}">{day}</td>'
        elif not events_today.empty:
            event_type = events_today.iloc[0]['Type']  # Assuming one event per day for simplicity
            color = event_color(event_type)
            cssclass += f' event-day {event_type.lower()}-event'  # Add specific class for event types
            return f'<td class="{cssclass}">{day}</td>'
        else:
            return f'<td class="{cssclass}">{day}</td>'

    def formatmonth(self, theyear, themonth, withyear=True):
        v = []
        a = v.append
        a('<table class="table table-bordered">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a('<tr>')
        a('\n')
        a('<th>Sun</th>')
        a('<th>Mon</th>')
        a('<th>Tue</th>')
        a('<th>Wed</th>')
        a('<th>Thu</th>')
        a('<th>Fri</th>')
        a('<th>Sat</th>')
        a('</tr>')
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, theyear, themonth))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)

    def formatweek(self, theweek, theyear, themonth):
        s = ''.join(self.formatday(d, wd, theyear, themonth) for (d, wd) in theweek)
        return f'<tr>{s}</tr>'



def fetch_indian_holidays(year_start, year_end):
    # Example of fetching Indian holidays using the holidays package
    india_holidays = holidays.India(years=range(year_start, year_end+1))
    holiday_data = {}
    for date, name in india_holidays.items():
        holiday_data[date] = (name, "Holiday")  # Assuming all are national holidays

    return holiday_data

st.title("Calendar with Events and Indian Holidays")
st.write("This calendar allows you to add, update, and delete events, and displays Indian holidays.")

# Fetch Indian holidays data for the range of years
indian_holidays = fetch_indian_holidays(2012, 2030)

# Add Event
with st.form("Add Event"):
    st.write("## Add Event")
    event_date = st.date_input("Date", min_value=datetime.date.today())
    event_time = st.time_input("Time")
    event_name = st.text_input("Event")
    event_type = st.selectbox("Type", ["Holiday", "Professional", "Personal"])
    add_event_button = st.form_submit_button("Add Event")

    if add_event_button:
        add_event(event_date, event_time, event_name, event_type)
        st.success(f"Event '{event_name}' added!")

# Calendar View - Month
st.write("## Calendar View - Month")
year_month_slider_key = "year_month_slider"
year_month_year = st.slider("Year", 2012, 2030, datetime.date.today().year, key=f"{year_month_slider_key}_year")
year_month_month = st.slider("Month", 1, 12, datetime.date.today().month, key=f"{year_month_slider_key}_month")
cal = EventCalendar(st.session_state.events, indian_holidays)
html_calendar = cal.formatmonth(year_month_year, year_month_month)
st.components.v1.html(html_calendar, height=600, scrolling=True)

# Display Events for Selected Month and Year
display_events(year_month_month, year_month_year, indian_holidays)

# Check for upcoming events
current_time = datetime.datetime.now()
for index, row in st.session_state.events.iterrows():
    event_time = datetime.datetime.combine(row['Date'], row['Time'])
    if 0 <= (event_time - current_time).total_seconds() <= 300:  # Within 5 minutes
        st.warning(f"Upcoming Event: {row['Event']} at {row['Time']}")

# Adding color coding for events in the calendar view
st.write("## Events with Color Coding")
for index, row in st.session_state.events.iterrows():
    st.markdown(f"<div class='{row['Type'].lower()}-event' style='padding:10px;margin:5px;border-radius:5px;'>"
                f"**{row['Date']} {row['Time']}** - {row['Event']} ({row['Type']})</div>", unsafe_allow_html=True)

def year_view(year, events, holidays_data):
    cal = EventCalendar(events, holidays_data)
    html_calendar = cal.formatyear(year)
    st.components.v1.html(html_calendar, height=800, scrolling=True)

# Calendar View - Year
st.write("## Calendar View - Year")
year_view_slider_key = "year_view_slider"
year_view_year = st.slider("Year", 2012, 2030, datetime.date.today().year, key=f"{year_view_slider_key}_year")
year_view(year_view_year, st.session_state.events, indian_holidays)

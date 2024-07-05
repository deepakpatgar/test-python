from flask import Flask, render_template, request, redirect, url_for
import calendar
from datetime import datetime, timedelta
import holidays
import requests
import ephem
import pytz

app = Flask(__name__)

# Dummy data for events (for demonstration purposes)
events = {
    (2025, 7, 25): "Meeting with Client",
    (2025, 7, 30): "Project Deadline",
    # Add more events here
    (2024, 8, 1): "ETL Project Kick-off Meeting",
    (2024, 8, 15): "PMO Review for ETL Project",
    (2024, 9, 1): "Planning Phase Begins",
    (2024, 9, 15): "Development Phase Start",
    (2024, 10, 1): "Testing Phase Initiation",
    (2024, 10, 15): "CICD Pipeline Implementation",
    (2024, 11, 1): "Deployment to Test Environment",
    (2024, 12, 1): "Production Readiness Assessment",
    (2025, 1, 1): "Go-live on Snowflake Cloud",
    (2025, 2, 1): "Post-production Support Phase Begins",
    (2025, 3, 31): "ETL Project Closure"
    # Add more events as needed
}

# Define timezone for IST (India Standard Time)
IST = pytz.timezone('Asia/Kolkata')

@app.route('/')
def index():
    year = request.args.get('year', datetime.now().year, type=int)
    view = request.args.get('view', 'year')
    month = request.args.get('month', datetime.now().month, type=int)
    week = request.args.get('week', datetime.now().isocalendar()[1], type=int)
    day = request.args.get('day', datetime.now().day, type=int)
    current_date = datetime.now()

    if year < 1900 or year > 2073:
        year = datetime.now().year

    if view == 'year':
        calendar_data = generate_year_view(year)
    elif view == 'month':
        calendar_data = generate_month_view(year, month)
    elif view == 'week':
        calendar_data = generate_week_view(year, week)
    elif view == 'day':
        calendar_data = generate_day_view(year, month, day)
    else:
        calendar_data = generate_year_view(year)

    historical_events = get_historical_events(year, month, day)
    holiday_data = get_holidays(year, month, day)
    

    # Convert current_date to IST
    current_date_ist = current_date.astimezone(IST)

    # Get sunrise and sunset times for the current date in IST
    sunrise, sunset = get_sunrise_sunset(year, month, day)

    # Get moon phase for the current date
    moon_phase = get_moon_phase(year, month, day)

    return render_template('flask_calender_now.html',
                           calendar_data=calendar_data,
                           year=year,
                           view=view,
                           current_date=current_date_ist,
                           historical_events=historical_events,
                           holiday_data=holiday_data,
                           events=events,  # Include events dictionary here
                           sunrise=sunrise,
                           sunset=sunset,
                           moon_phase=moon_phase)

@app.route('/add_event', methods=['POST'])
def add_event():
    date = request.form['date']
    event_description = request.form['event_description']

    # Parse the date string into year, month, and day
    year, month, day = map(int, date.split('-'))

    # Store the event in the events dictionary
    events[(year, month, day)] = event_description

    return redirect(url_for('index', year=year, month=month, day=day))


def generate_year_view(year):
    cal = calendar.Calendar()
    year_view = []
    for month in range(1, 13):
        month_days = cal.monthdayscalendar(year, month)
        month_view = []
        for week in month_days:
            week_view = []
            for day in week:
                if day == 0:
                    week_view.append((day, False, False))
                else:
                    has_event = (year, month, day) in events
                    has_holiday = bool(get_holidays(year, month, day))
                    week_view.append((day, has_event, has_holiday))
            month_view.append(week_view)
        year_view.append((month, calendar.month_name[month], month_view))
    return {'type': 'year', 'data': year_view}

def generate_month_view(year, month):
    cal = calendar.monthcalendar(year, month)
    month_view = []
    for week in cal:
        week_view = []
        for day in week:
            if day == 0:
                week_view.append((day, False, False))
            else:
                has_event = (year, month, day) in events
                has_holiday = bool(get_holidays(year, month, day))
                week_view.append((day, has_event, has_holiday))
        month_view.append(week_view)
    month_name = calendar.month_name[month]
    return {'type': 'month', 'data': month_view, 'month_name': month_name, 'year': year}

def generate_week_view(year, week):
    first_day_of_year = datetime(year, 1, 1)
    start_of_week = first_day_of_year + timedelta(weeks=week - 1)
    start_of_week -= timedelta(days=start_of_week.weekday())
    week_view = [start_of_week + timedelta(days=i) for i in range(7)]
    week_data = []
    for day in week_view:
        has_event = (day.year, day.month, day.day) in events
        has_holiday = bool(get_holidays(day.year, day.month, day.day))
        week_data.append((day.day, has_event, has_holiday))
    return {'type': 'week', 'data': week_data}

def generate_day_view(year, month, day):
    day_view = datetime(year, month, day)
    has_event = (year, month, day) in events
    has_holiday = bool(get_holidays(year, month, day))
    return {'type': 'day', 'data': (day_view.day, has_event, has_holiday)}

def get_historical_events(year, month, day):
    events = {
        (7, 20): "1969: Apollo 11 Moon Landing",
        (12, 25): "Christmas Day",
        (1, 1): "New Year's Day",
        (8, 15): "1947: India's Independence Day",
        (6, 21): "1990: Chandra Shekhar becomes Prime Minister of India",
        (10, 24):"1999: Kargil War officially comes to an end",
        (3, 12): "2003: Indian cricket team wins ICC Cricket World Cup",
        (7, 21): "2004: India's first successful lunar mission, Chandrayaan-1, launched",
        (3, 11): "2011: India becomes World Cup Cricket Champion by defeating Sri Lanka in the final held in Mumbai",
        (6, 18): "2014: Narendra Modi becomes Prime Minister of India",
        (11, 8): "2016: Indian government demonetizes ₹500 and ₹1000 banknotes",
        (3, 24): "2020: India enters nationwide lockdown due to COVID-19 pandemic"
        # Add more historical events here
    }
    return events.get((month, day), None)

def get_holidays(year, month, day):
    us_holidays = holidays.US(years=year)
    india_holidays = holidays.IN(years=year)
    
    date = datetime(year, month, day).date()
    
    us_holiday = us_holidays.get(date, None)
    india_holiday = india_holidays.get(date, None)
    
    holidays_list = []
    
    if us_holiday:
        holidays_list.append((us_holiday, 'us'))
    
    if india_holiday:
        holidays_list.append((india_holiday, 'indian'))
    
    return holidays_list


def get_sunrise_sunset(year, month, day):
    # Example using sunrise-sunset.org API
    date_str = f"{year}-{month}-{day}"
    url = f"https://api.sunrise-sunset.org/json?lat=28.6139&lng=77.2090&date={date_str}&formatted=0"
    response = requests.get(url)
    data = response.json()
    sunrise_utc = data['results']['sunrise']
    sunset_utc = data['results']['sunset']

    # Convert UTC times to IST
    sunrise_utc = datetime.strptime(sunrise_utc, '%Y-%m-%dT%H:%M:%S%z')
    sunset_utc = datetime.strptime(sunset_utc, '%Y-%m-%dT%H:%M:%S%z')
    sunrise_ist = sunrise_utc.astimezone(IST).strftime('%H:%M')
    sunset_ist = sunset_utc.astimezone(IST).strftime('%H:%M')

    return sunrise_ist, sunset_ist

def get_moon_phase(year, month, day):
    phase_date = datetime(year, month, day)
    moon = ephem.Moon(phase_date)
    moon_phase = ephem.Moon(phase_date)
    illumination = moon_phase.phase

    # Determine moon phase
    if 0 <= illumination < 45:
        moon_phase = "New Moon"
    elif 45 <= illumination < 90:
        moon_phase = "First Quarter"
    elif 90 <= illumination < 135:
        moon_phase = "Full Moon"
    else:
        moon_phase = "Last Quarter"

    return moon_phase

if __name__ == '__main__':
    app.run(debug=True)

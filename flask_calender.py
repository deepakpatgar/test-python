from flask import Flask, render_template, request
import calendar
from datetime import datetime, timedelta
import holidays

app = Flask(__name__)

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

    return render_template('flask_calender.html', 
                           calendar_data=calendar_data, 
                           year=year, 
                           view=view, 
                           current_date=current_date,
                           historical_events=historical_events,
                           holiday_data=holiday_data)

def generate_year_view(year):
    cal = calendar.Calendar()
    year_view = []
    for month in range(1, 13):
        month_days = cal.monthdayscalendar(year, month)
        year_view.append((month, calendar.month_name[month], month_days))
    return {'type': 'year', 'data': year_view}

def generate_month_view(year, month):
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    return {'type': 'month', 'data': cal, 'month_name': month_name, 'year': year}

def generate_week_view(year, week):
    first_day_of_year = datetime(year, 1, 1)
    start_of_week = first_day_of_year + timedelta(weeks=week - 1)
    start_of_week -= timedelta(days=start_of_week.weekday())
    week_view = [start_of_week + timedelta(days=i) for i in range(7)]
    return {'type': 'week', 'data': week_view}

def generate_day_view(year, month, day):
    day_view = datetime(year, month, day)
    return {'type': 'day', 'data': day_view}

def get_historical_events(year, month, day):
    events = {
        (7, 20): "1969: Apollo 11 Moon Landing",
        (12, 25): "Christmas Day",
        (1, 1): "New Year's Day",
        # Add more historical events here
    }
    return events.get((month, day), None)

def get_holidays(year, month, day):
    us_holidays = holidays.US(years=year)
    date = datetime(year, month, day)
    return us_holidays.get(date, None)

if __name__ == '__main__':
    app.run(debug=True)

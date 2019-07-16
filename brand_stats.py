import os
import requests
from dotenv import load_dotenv
import datetime
import plotly.plotly as py
import plotly.graph_objs as go


def main():
    load_dotenv()
    get_and_print_diagram_url()

def get_and_print_diagram_url():
    number_of_days = 7
    search_query = 'coca cola'
    mention_statistics = get_last_days_statistics(number_of_days, search_query)
    diagram_url = plot_mention_diagram(mention_statistics, number_of_days)
    print(diagram_url)
    return diagram_url

def get_last_days_statistics(number_of_days, search_query):
    days_timestamps = get_last_days_timestamps(number_of_days)
    posts_stats = []
    for day in days_timestamps:
        date = day[0]
        number_of_posts = get_number_of_posts(day[1], day[2], search_query)
        posts_stats.append((date, number_of_posts))
    return posts_stats

def get_last_days_timestamps(number_of_days):
    today = datetime.date.today()
    timestamps = []
    for day in range(number_of_days):
        date = today - datetime.timedelta(days=day+1)
        date_timestamps = get_date_timestamps(date)
        timestamps.append((date, date_timestamps['day_start'], date_timestamps['day_end']))
    return timestamps    

def get_date_timestamps(date):
    day_start = datetime.datetime(date.year, date.month, date.day, 0, 0, 0)
    day_end = day_start + datetime.timedelta(days=1)
    date_timestamps = {
        'day_start': day_start.timestamp(),
        'day_end': day_end.timestamp()
    }
    return date_timestamps

def get_number_of_posts(start_time, end_time, search_query):
    method_name = 'newsfeed.search'
    payload = {
        'q': search_query,
        'start_time': start_time,
        'end_time': end_time,
    }
    response_data = vk_api_request(method_name, payload)
    number_of_posts = response_data['response']['total_count']
    return number_of_posts

def vk_api_request(method_name, payload):
    vk_access_token = os.getenv('VK_SERVICE_KEY')
    vk_api_version = '5.101'
    vk_url = f'https://api.vk.com/method/{method_name}'
    vk_required_params = {
        'access_token': f'{vk_access_token}',
        'v': f'{vk_api_version}'
    }
    payload.update(vk_required_params) 
    response = requests.post(vk_url, params=payload)
    response.raise_for_status()
    return response.json()

def plot_mention_diagram(mention_statistics, number_of_days):
    days_of_stats = []
    mentions_numbers = []
    for day_stats in mention_statistics:
        days_of_stats.append(day_stats[0].strftime('%d.%m.%Y'))
        mentions_numbers.append(day_stats[1])
    plot_data = [go.Bar(
            x=days_of_stats,
            y=mentions_numbers
    )]
    plot_name = f'Last {number_of_days} days statistics from {days_of_stats[0]}'
    diagram_url = py.plot(plot_data, filename=plot_name, auto_open=False)
    return diagram_url

if __name__ == '__main__':
    main()

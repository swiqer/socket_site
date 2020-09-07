import requests

cities = [
    'Москва',
    'Владивосток',
    'Красноярск',
]


def fix_emoji_bug(weather_string):
    fixed_string = weather_string
    fixed_string = fixed_string.replace('☁️', '🌫')
    fixed_string = fixed_string.replace('☀️', '🌞')
    return fixed_string


def make_url(city):
    return f'http://wttr.in/{city}'


def make_parameters():
    params = {
        'format': 2,    # погода одной строкой
        'M': ''         # скорость ветра в "м/с"
    }
    return params


def what_weather(city):
    try:
        response = requests.get(make_url(city), params=make_parameters())
        if response.status_code == 200:
            s = fix_emoji_bug(response.text.strip())
            result = s.split("🌬️")
            # return response.text.strip()
            return result
        else:
            return '<ошибка на сервере погоды>'

    except requests.ConnectionError:
        return '<сетевая ошибка>'


def main(flag=False, city=''):
    if not flag:
        all_cities = []
        for city in cities:
            all_cities.append([city, what_weather(city)])
        return all_cities
    elif flag:
        return [city, what_weather(city)]


if __name__ == "__main__":
    print('Погода в городах:')
    for c in main():
        print(*c)
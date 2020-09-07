from weather_app import main as weather_func


def context_weather():
    result = weather_func()
    tab = ""
    align = 'style="text-align: center"'
    for i in range(len(result)):
        tab += (f'<tr {align}>'
                f'<th scope="row">{i + 1}</th>'
                f'<td>{result[i][0]}</td>'
                f'<td>{result[i][1][0]}</td>'
                f'<td>🌬️{result[i][1][1]}</td>'
                f'</tr>')
    context = {
        'title': "🌤 Погода сейчас 🌨",
        'tab': tab,
    }
    return context


def context_city_weather(method, city):
    if method == 'POST':
        weather = weather_func(True, city)
        tab = ""
        align = 'style="text-align: center"'
        tab += (f'<tr {align}>'
                f'<th scope="row">{1}</th>'
                f'<td>{city}</td>'
                f'<td>{weather[1][0]}</td>'
                f'<td>🌬️{weather[1][1]}</td>'
                '</tr>')
        all_tab = ('<div class="tab" style="margin-bottom: 4%; margin-left: 20%; margin-right: 20%">'
                   '<table class="table">'
                   '<thead class="thead-light">'
                   '<tr>'
                   '<th style="text-align: center;" scope="col">#</th>'
                   '<th style="text-align: center" scope="col">Город</th>'
                   '<th style="text-align: center" scope="col">Температура и осадки</th>'
                   '<th style="text-align: center" scope="col">Ветер</th>'
                   '</tr>'
                   '</thead>'
                   '<tbody>'
                   f'{tab}'
                   '</tbody>'
                   '</table>'
                   '</div>')
        context = {
            "weather": all_tab
        }
        return context
    return "(weather)"

import urllib.parse
import services


def insert_context(html, context):
    for tag in context:
        html = html.replace(f'({tag})', context[tag])
    return html


def render(name_html, context):
    with open(f'templates/{name_html}') as template:
        if '(' in context and ')' in context:
            return template.read().replace(f"{context}", "")
        return insert_context(template.read(), context)


##################################################################
##################### START VIEWS FUNCTIONS ######################
##################################################################

def index():
    return render('index.html', services.context_weather())


def city_weather(method, city=""):
    try:
        city = urllib.parse.unquote(city)
        print(city)
    except Exception as ex:
        city = "Москва"

    return render('my_city.html', services.context_city_weather(method, city))

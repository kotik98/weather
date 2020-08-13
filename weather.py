# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import requests
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        f = open("app_id.txt")
        app_id = f.read()
        f.close()
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'q': city, 'type': 'like', 'lang': 'ru', 'units': 'metric', 'appid': app_id})
        data = res.json()
        if not valid(data):
            return render_template('index.html', context=[u"Ошибка"])
        context = [u"город: "+city,
                   u"погода: "+data['weather'][0]['description'],
                   u"текущая температура: "+str(data['main']['temp']),
                   u"минимальная температура: "+str(data['main']['temp_min']),
                   u"максимальная температура: "+str(data['main']['temp_max'])]
        return render_template('index.html', context=context)
    return render_template('index.html')


def valid(data):
    if data['cod'] == 200:
        return True
    return False


if __name__ == '__main__':
    app.run()

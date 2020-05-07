import requests
from flask import Flask, render_template,request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == "POST":
        city = request.form.get('city')
    
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=8b09553d7b46332d347729f76bef386c'

        r = requests.get(url.format(city)).json()
        weather = {
            'city' : city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon':r['weather'][0]['icon']
        }
        return render_template('result.html',weather=weather)
    
    return render_template('index.html')

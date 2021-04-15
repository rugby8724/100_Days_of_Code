from flask import Flask, render_template
import random
import requests
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    today = datetime.today()
    random_num = random.randint(1, 10)
    return render_template('index.html', num=random_num, year=today.year)


@app.route('/guess/<name>')
def guess(name):
    param = {
        'name': name
    }
    age_response = requests.get('https://api.agify.io', params=param)
    age_data = age_response.json()
    age = age_data['age']

    gender_response = requests.get('https://api.genderize.io', params=param)
    gender_data = gender_response.json()
    gender = gender_data['gender']

    return render_template('name.html', name=name.title(), age=age, gender=gender)


@app.route('/blog')
def blog():
    blog_url = 'https://api.npoint.io/5abcca6f4e39b4955965'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
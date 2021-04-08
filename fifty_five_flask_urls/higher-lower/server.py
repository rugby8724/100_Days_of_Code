from flask import Flask
import random
app = Flask(__name__)


@app.route('/')
def welcome():
    return '<h1> Guess a number between 1 and 10 </h1>' \
           '<img src="https://media.giphy.com/media/gxxlowyvtfS0M/giphy.gif">'


ran_num = random.randint(1,10)


@app.route('/<int:number>')
def guess(number):
    if number > ran_num:
        return '<h1>To High, Guess a lower number</h1>' \
               '<img src="https://media.giphy.com/media/5fBH6zewW18flWdKE6c/giphy.gif">'
    elif number < ran_num:
        return '<h1>To Low, Guess a higher number</h1>' \
               '<img src="https://media.giphy.com/media/B2HqyXi7r6j9W9cCG2/giphy.gif">'
    else:
        return '<h1>Congrats you got it right!!!</h1>' \
               '<img src="https://media.giphy.com/media/SA613Nxg1h6zO1nRsg/giphy.gif">'


if __name__ == '__main__':
    #run the app in debug mode to auto-reload
    app.run(debug=True)

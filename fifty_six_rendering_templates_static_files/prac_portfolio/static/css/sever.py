from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    #Run the app in debug mode auto-refresh
    app.run(debug=True)
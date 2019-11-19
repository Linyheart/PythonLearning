from flask import Flask, url_for, redirect, render_template
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()

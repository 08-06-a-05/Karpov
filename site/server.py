from flask import *

app = Flask(__name__)

@app.route('/')
def new_main_page():
    return render_template("new_main_page.html")


@app.route('/main_page/')
def main_page():
    return render_template("Main_page.html")

@app.route('/katalog_reno/')
def katalog_reno():
    return render_template("Katalog_reno.html")

@app.route('/buy_car/')
def buy_car():
    return render_template("pokupka.html")

@app.route('/katalog_reno/reno_logan/')
def reno_logan():
    return render_template("Reno_logan_2010.html")

@app.route('/about_us/')
def about_us():
    return render_template("About_us.html")

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)


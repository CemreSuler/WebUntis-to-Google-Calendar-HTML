from flask import Flask, request, render_template
import schedule
import google_cal

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    print("Recieved input:")
    school_input = request.form['school']
    server_input = request.form['server']
    untisid_input = int(request.form['untis-id'])
    username_input = request.form['username']
    password_input = request.form['password']
    calid_input = request.form['cal-id']
    print(type(untisid_input))
    google_cal.start_google_cal(calid_input)
    schedule.addToCalendar(school_input, server_input, untisid_input, username_input, password_input)
    return("Eyyyy hij is beziggg even rustaagg")

if __name__ == "__main__":
    app.run(debug=True)
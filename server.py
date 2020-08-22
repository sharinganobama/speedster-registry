from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
# print(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def add_data(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')


def add_data_csv(data):
    with open('database.csv', mode='a') as database1:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database1, delimiter=',', quotechar=' ',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            add_data_csv(data)
            return redirect('/thank_you.html')
        except:
            return 'Attempt to save was unsuccessful.'
        # return 'FORM SUBMITTED'
    else:
        return 'Something went wrong, please try again.'

# export FLASK_APP=server.py
# export FLASK_DEBUG=1
# flask run

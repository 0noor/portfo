import csv
from flask import Flask, render_template, send_from_directory, request, redirect
import os
app = Flask(__name__)
#print(__name__)


@app.route('/')
def my_home():
    return render_template('./index.html')

#
# @app.route('/works.html')
# def my_work():
#     return render_template('./works.html')
#
#
# @app.route('/about.html')
# def about():
#     return render_template('./about.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('./contact.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong, Try again!'

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# @app.route('/blog')
# def blog():
#     return 'these are my thoughts on blogs'
#
#
# @app.route('/blog/2020/dog')
# def dog():
#     return 'these are my thoughts on dogs'


# # @app.route('/favicon.ico')
# # def favicon():
# #     return send_from_directory(os.path.join(app.route_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

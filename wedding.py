from flask import Flask, url_for, request, jsonify, \
render_template, json, redirect, redirect, session, make_response, flash

application = Flask(__name__)
application.config['SECRET_KEY'] = 'sfh7^erw9*(%sadHGw%R'

# model = MModel()
html_source = ''
 
app = Flask(__name__)

# INDEX
@application.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
    application.run(debug=True)
    # debug di buat False
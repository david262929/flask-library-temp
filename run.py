import os
from app import app
# from flask import Flask
#
# app = Flask(__name__)

# @app.route('/')
# def index():
# 	print('davooo')
# 	return 'aaaaaaaaaa'
# 	# return render_template('index.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5007))
	app.run(port=port)
# main.py --- 
# 
# Filename: main.py
# Author: Louise <louise>
# Created: Sat Apr 18 18:47:03 2020 (+0200)
# Last-Updated: Sat Apr 18 18:56:03 2020 (+0200)
#           By: Louise <louise>
# 
from flask import Flask
from webapp import webapp

def main():
    app = Flask(__name__)
    app.register_blueprint(webapp)
    app.run()
    
if __name__ == "__main__":
    main()

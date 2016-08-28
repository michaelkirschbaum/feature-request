#!/usr/bin/python

from flask import Flask
from flask_sqlalchemy import SQlAlchemy
import sqlalchemy

# setup flask
app = Flask(__name__)

# routes
@app.route("/")
def getForm():
  return render_template('form.html')

@app.route("/submit", methods=['POST'])
def request(): 
  pass

if __name__ == "__main__":
  app.run()

from flask import Flask, Response, request
from flask_restful import  Resource,Api
from main import run_main
import json
import config as cfg

app = Flask(__name__)
api = Api(app)


if __name__ =='__main__':
    app.run(debug = True)   
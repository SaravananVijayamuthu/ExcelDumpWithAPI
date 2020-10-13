from flask import Flask, Response, request
from flask_restful import  Resource,Api
from main import run_main
import json
import config as cfg

app = Flask(__name__)
api = Api(app)

######################
##config
######################
configuration_counts = (cfg.configuration_count)
flag = (cfg.flag)


if __name__ =='__main__':
    app.run(debug = True)   
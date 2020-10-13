from flask import Flask, Response, request
from flask_restful import  Resource,Api
from main import run_main
import json
import model.config as cfg

app = Flask(__name__)
api = Api(app)


######################
##config
######################
configuration_counts = (cfg.configuration_count)
flag = (cfg.flag)


######################
##get run_main()
######################
class GetAll(Resource):
    def get(self,flag):
        try:
            if flag == flag:
                run = run_main(configuration_counts,flag)
                return Response(
                response = json.dumps(run,default=str), 
                status=200,
                mimetype="application/json"
                )
            elif flag != flag:
                run = run_main(configuration_counts,flag)
                return Response(
                response = json.dumps(run,default=str), 
                status=200,
                mimetype="application/json"
                )
        except Exception as e:
            print(e)
            return Response(
            response = json.dumps(
                {"message":"Check Your URL Please!!"},default=str), 
                status=404,
                mimetype="application/json"
                ) 


######################
#single dataset
######################
class Configurations(Resource):
    def get(self, name, flag):
        try:
            if flag == flag:
                for config,cfgval in configuration_counts.copy().items():
                    if config != name:
                        configuration_counts.pop(config)
                con = configuration_counts
                return Response(
                response = json.dumps(run_main(con,flag),default=str), 
                status=200,
                mimetype="application/json"
                )
            elif flag != flag:
                for config,cfgval in configuration_counts.copy().items():
                    if config != name:
                        configuration_counts.pop(config)
                con = configuration_counts
                return Response(
                response = json.dumps(run_main(con,flag),default=str), 
                status=200,
                mimetype="application/json"
                )
        except Exception as e:
            return Response(
            response = json.dumps(
                {"message":"Check Your URL Please!!"},default=str), 
                status=404,
                mimetype="application/json"
                )



######################
##api call
######################
api.add_resource(GetAll,"/configuration/<int:flag>/")
api.add_resource(Configurations,"/configs/<string:name>/<int:flag>/")


if __name__ =='__main__':
    app.run(debug = True)   
# API For Excel-Dump using Flask with mail-service

The entire application is contained within the `main.py` file.

`config.py` is a minimal Rack configuration for Excel-Dump.

`api.py` runs a simplistic test and generates the API
documentation below.

## Note
 It is based on Python 3.x - Make sure your MongoDB is running fine

## Install

    pip install -r requirements.txt

## Run the app

    py api.py

# REST API

The REST API to the example app is described below.

# Flag

If Flag is 0 in URL of API mail won't be sent to the client.
If Flag is 1 in URL of API mail will be sent to the client.

## Get list of Things

### Request

`GET /configuration/<int:flag>/`

   http://127.0.0.1:5000/configuration/0

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    stats_for_1
    --- []
    stats_for_2
    --- []
    stats_for_3
    --- []
    stats_for_4
    --- []
      From  To  Name  Query  Count  Sheet
      
## Create a new Thing

### Request

`GET /configs/<string:name>/<int:flag>/`

     http://127.0.0.1:5000/configs/<string:name>/<int:flag>

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    
    [] 
## Get a specific Thing

### Request

`GET /configs/<string:name>/<int:flag>/`

     http://127.0.0.1:5000/configs/stats_for_2/0

### Response

    HTTP/1.1 200 OK
    Status: 200 OK
    Connection: close
    Content-Type: application/json

    [{"From": "2020-10-06 00:00:00", "To": "2020-10-07 00:00:00", "Name": "sarvi with filter", "Query": {"created_date": {"$gte": "2020-10-06 00:00:00", "$lt": "2020-10-07 00:00:00"}, "client_id": "MNRNJVXE", "function_name": {"$ne": "authorize"}, "user_id": {"$ne": null}}, "Count": 0, "Sheet": "My Sheet"}]

## Get a non-existent Thing

### Request

`GET /configs/<string:name>/<int:flag>/`

    http://127.0.0.1:5000/configs/stats_for_2/0

### Response

    HTTP/1.1 404 Not Found
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 404 Not Found
    Connection: close
    Content-Type: application/json
    Content-Length: 35
    
    {"status": 404, "message": "Check Your URL Please!!"}


# API For Excel-Dump using Flask with mail-service
<p>  
<img src="https://devicons.github.io/devicon/devicon.git/icons/python/python-original.svg" alt="python" width="40" height="40"/>
<img src="https://www.kindpng.com/picc/m/188-1882559_python-flask-hd-png-download.png" alt="Flask" width="40" height="40"/>
<img src="https://devicons.github.io/devicon/devicon.git/icons/mongodb/mongodb-original.svg" alt="mongodb" width="40" height="40"/>
<img src="https://img.icons8.com/dusk/64/000000/postman-api.png" alt="postman" width="40" height="40"/>
</p> 

The entire application is contained within the `main.py` file.

`config.py` is a minimal Rack configuration for Excel-Dump.

`api.py` runs a simplistic test and generates the API
documentation below.

## Note
 It is based on Python 3.x - Make sure your MongoDB is running fine

## Prerequisite
◾ [Python](https://www.python.org/downloads/) 3.8 +

◾ Should have Virtual Environmental variable([venv](https://www.geeksforgeeks.org/create-virtual-environment-using-venv-python/))

◾ [MongoDB](https://www.mongodb.com/try/download)

◾ Any GUI for local Database server [MongoDB-Compass](https://www.mongodb.com/products/compass), [Studio 3T](https://studio3t.com/download/), [Robo 3T](https://robomongo.org/download)

◾ [Postman](https://www.postman.com/)


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


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

<p align="center">
<a href='https://ko-fi.com/C0C12CBIQ' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://cdn.ko-fi.com/cdn/kofi3.png?v=5' border='5' alt='Buy Me a Coffee at ko-fi.com' /></a>
</p>

uri = "mongodb://localhost:27017"
dbname = 'newdb'
is_active=0
new_sheet_name="Main"
is_groupby=0
group_by="function_name"
collection_name='codinglang'
collection_name_alias="Stats"
sender="..."
reciever=["..."]
password="..."
flag = 1


configuration_count = {
    "stats_for_1":{ 
        "name":"Stats with filter",
        "uri" : uri,
        "dbname" : dbname,
        "is_groupby":1,
        "group_by":{
            "client_id":"$client_id",
            "status_code":"$status_code"
        },
        "field_name":"created_date",        
        "is_active":1,
        "new_sheet_name":"My Sheet",
        "collection_name":'statscollection',
        "interval_mode":"day",
        "interval_date":'2020-08-25',
        "interval_time":'00:00:00',              
        'filter':{
                'client_id':'MNRNJVXE',
                'function_name':{'$eq':'authorize'},
                'user_id':{'$ne':None},
                }
        },
    "stats_for_2":{ 
        "name":"sarvi with filter",
        "uri" : uri,
        "dbname" : dbname,
        "is_groupby":1,
        "group_by":{
            "client_id":"$client_id",
            "status_code":"$status_code"
        },
        "field_name":"created_date",
        "is_active":1,
        "new_sheet_name":"My Sheet",
        "collection_name":'codinglang',
        "interval_mode":"day",
        "interval_date":'2020-10-06',
        "interval_time":'00:00:00',            
        'filter':{
            'client_id':'MNRNJVXE',
            'function_name':{'$ne':'authorize'},
            'user_id':{'$ne':None},
            }
        },
    "stats_for_3":{ 
        "name":"Function Name Filter",
        "uri" : uri,
        "dbname" : dbname,
        "is_active":1,
        "is_groupby":1,
        "group_by":{
            "client_id":"$client_id",
            "status_code":"$status_code"
        },
        "field_name":"created_date",
        "new_sheet_name":"Sheet 1",
        "collection_name":'codinglang',
        "interval_mode":"day", 
        "interval_date":'2020-10-06',
        "interval_time":'00:00:00',                 
        'filter':{
            'client_id':'MNRNJVXE',
            'function_name':{'$eq':'authorize'},
            'user_id':{'$ne':None},
            }
        },
    "stats_for_4":{ 
        "name":"Stats for Date Range",
        "uri" : uri,
        "dbname" : dbname,
        "is_active":1,
        "is_groupby":1,
        "group_by":{
            "client_id":"$client_id",
            "status_code":"$status_code"
        },
        "field_name":"created_date",
        "new_sheet_name":new_sheet_name,
        "collection_name":'codinglang',
        "interval_mode":"day",
        "interval_date":'2020-08-25',
        "interval_time":'00:00:00',               
        'filter':{
                'client_id':'MNRNJVXE',
                'function_name':{'$eq':'authorize'},
                'user_id':{'$ne':True},
        }
    }
}


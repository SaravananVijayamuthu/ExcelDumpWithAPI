from pymongo import MongoClient
from shutil import copyfile
import pandas as pd
import datetime
import csv
import schedule
import string
import yagmail
import xlsxwriter
import os
import config as cfg


######################
##Creating Connection
######################
client=MongoClient(cfg.uri)
db_name=cfg.dbname
db=client[db_name]


######################
##Count all docs
######################
def docs_count():
    for i in range(len(cfg.configuration_count)):
        total_documents=db[cfg.configuration_count["stats_for_{}".format(i+1)]["collection_name"]].count_documents({})
        total_documents_list.append(total_documents)
    return total_documents_list


######################
##Count in Query & Range
######################
def docs_count_interval_day(start_date_time,end_date_time,collection_name,query): #search_date="current_date"
    get_count_date=db[collection_name].count_documents(query)
    return get_count_date


######################
##Find Results(Aggregate)
######################
def aggregate_fucntion(start_date,end_date,group_by):
    records=db[cfg.collection_name].aggregate([
        {"$match":{}},
        {"$group":{"_id":group_by,"Count":{"$sum":1}}}
    ])
    return list(records)


######################
##Creating Data for Excel
######################
reports_array=[]
def build_excel_data(From,To,name,query,count,sheet):
    report={
        "From":str(From),
        "To":str(To),
        "Name":name,
        "Query":query,
        "Count":count,
        "Sheet":sheet
    }
    reports_array.append(report)



######################
##Checks and Converstions
######################
def from_main(con):
    for cfgkey,cfgval in con.items():
        collection_name=cfgval["collection_name"]
        if cfgval["is_active"]== 1:
            if cfgval["interval_mode"] == 'day':
                print(cfgkey)
                if not cfgval["interval_date"] or not cfgval["interval_date"].strip():
                    previous_date=datetime.date.today()-datetime.timedelta(days=1)
                    start_date_str=str(previous_date)+" "+"00:00:00"
                    start_date=datetime.datetime.strptime(start_date_str,'%Y-%m-%d %H:%M:%S')
                    end_date_str=str(datetime.date.today())+" "+"00:00:00"
                    query1={cfgval["field_name"]:{'$gte':start_date,'$lt':end_date}}
                    query2=cfgval["filter"]
                    query=query1.copy()
                    query.update(query2)
                    end_date=datetime.datetime.strptime(end_date_str,'%Y-%m-%d %H:%M:%S')
                    docs_in_collection_range_day = docs_count_interval_day(start_date,end_date,collection_name,query)
                    print("---",aggregate_fucntion(start_date,end_date,cfgval["group_by"]))
                    build_excel_data(start_date,end_date,cfgval["name"],query,docs_in_collection_range_day,cfgval["new_sheet_name"])
                else :
                    start_date_time_str=cfgval["interval_time"]
                    if not cfgval["interval_time"]:
                        start_date_time_str="00:00:00" 
                        print("hello")           
                    start_date_str=cfgval["interval_date"]+" "+start_date_time_str
                    start_date=datetime.datetime.strptime(start_date_str,'%Y-%m-%d %H:%M:%S')
                    end_date_str_1=start_date.date()+datetime.timedelta(days=1)
                    end_date_str=str(end_date_str_1)+" "+start_date_time_str
                    end_date=datetime.datetime.strptime(end_date_str,'%Y-%m-%d %H:%M:%S')
                    query1={cfgval["field_name"]:{'$gte':start_date,'$lt':end_date}}
                    query2=cfgval["filter"]
                    query=query1.copy()
                    query.update(query2)
                    docs_in_collection_range_day = docs_count_interval_day(start_date,end_date,collection_name,query)
                    print("---",aggregate_fucntion(start_date,end_date,cfgval["group_by"]))
                    build_excel_data(start_date,end_date,cfgval["name"],query,docs_in_collection_range_day,cfgval["new_sheet_name"])

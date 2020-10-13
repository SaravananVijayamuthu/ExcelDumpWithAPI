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
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
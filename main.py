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
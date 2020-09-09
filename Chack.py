import json
import requests
import pandas as pd



with open('tmp/Crawl.json' , "rb") as read_file:
    mylist = list(read_file)

    read = str(mylist)
    replac = read.replace('\\n', '')
    print(replac)
    

   
        



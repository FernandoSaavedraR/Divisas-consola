import csv
import os
from classes.exchange import Exchange
import click
class convert_service:
    def __init__(self,table_name):
        self.table_name = table_name

    def export(self,data):
        export_table = 'exports/release.csv'
        exchanges = data
        with open(export_table, mode="w+",newline='') as f:
            writer = csv.DictWriter(f,fieldnames=['exchange','value','country'])
            writer.writeheader()
            for data in exchanges:
                temp_dict = {
                    "exchange":data["exchange"],
                    "value":data["value"],
                    "country":data["country"]
                }
                writer.writerow(temp_dict)
    def one_to_all(self,listE,baseC,quantity,release):
        new_list = list()
        tempValue = None
        for x in listE:
            if(x["exchange"]==baseC):
                tempValue = x["value"]
        if tempValue:
            for x in listE:
                temp = Exchange(x["exchange"],round(quantity*float(tempValue)/float(x["value"]),2),x["country"],x["uid"])
                new_list.append(temp.to_dict())
        if(release.capitalize() =="Yes"):
            self.export(new_list)
        return new_list

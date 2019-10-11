import csv
import os
import click
from classes.exchange import Exchange
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

    def one_to_one(self,listE,baseC,nextC,quantity):
        temp_list = self.one_to_all(listE,baseC,quantity,"No")
        conversion = [x for x in temp_list if nextC == x["exchange"]]
        if(len(conversion)>0):
            return conversion[0]
        else:
            return False
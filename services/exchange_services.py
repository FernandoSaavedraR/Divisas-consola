import csv
import os
from classes.exchange import Exchange

class Exchange_services:
    def __init__(self,table_name):
        self.table_name = table_name
    def create_exchange(self,exchange):
        with open(self.table_name,mode='a+',newline='') as f:
            writer = csv.DictWriter(f,fieldnames=Exchange.schema())
            writer.writerow(exchange.to_dict())

    def list_exchanges(self):
        f=open(self.table_name,mode='a+',newline='')
        f.close()
        with open(self.table_name,mode='r',newline='') as f:
            reader = csv.DictReader(f,fieldnames=Exchange.schema())
            return list(reader)

    def exist_exchange(self,exchange):
        exchange = exchange.to_dict()
        exchanges = self.list_exchanges()
        validator = True
        for value in exchanges:
            if value['exchange'] == exchange['exchange']:
                validator = False
        return validator
    
    def delete_exchange(self,exchange):
        validator =  self.exist_exchange(exchange)
        if(validator):
            return "currency is not in the list"
        else:
            tmp_table = self.table_name+'.tmp'
            exchanges = self.list_exchanges()
            temp_list = [exchangeR for exchangeR in exchanges if exchangeR['exchange']!=exchange.exchange]
            with open(tmp_table,mode='w+',newline='') as f:
                writer = csv.DictWriter(f,fieldnames=Exchange.schema())
                writer.writerows(temp_list)    
            os.remove(self.table_name)
            os.rename(tmp_table,self.table_name)

            return "currency updated"

    def update_exchange(self,exchange):
        validator = self.exist_exchange(exchange)
        exchange = exchange.to_dict()
        if(validator):
            return "currency is not in the list"
        else:
            tmp_table = self.table_name+'.tmp'
            exchanges = self.list_exchanges()
            tmp_list =[]
            for value in exchanges:
                if value['exchange'] == exchange['exchange']:
                    tmp_list.append(exchange)
                else:
                    tmp_list.append(value)
            with open(tmp_table,mode='w+',newline='') as f:
                writer = csv.DictWriter(f,fieldnames=Exchange.schema())
                writer.writerows(tmp_list)    
            os.remove(self.table_name)
            os.rename(tmp_table,self.table_name)

    def export(self):
        export_table = 'exports/data.csv'
        exchanges = self.list_exchanges()
        with open(export_table, mode="w+",newline='') as f:
            writer = csv.DictWriter(f,fieldnames=Exchange.schema())
            writer.writeheader()
            writer.writerows(exchanges)

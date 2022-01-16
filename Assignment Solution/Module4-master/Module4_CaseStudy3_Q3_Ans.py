import pandas as pd
import os
new_dataframe = pd.DataFrame(
    {
        "account_number":[296809,98022,563905,9335,659366],
        "name":['Carroll PLC','Heidenreich-Bosco','Kerluke, Reilly and Bechtelar','Waters-Walker','Waelchi-Fahey'],
        "item_code":['QN-82852','MJ-21460','AS-93055','AS-93055','AS-93055'],
        "category":['Belt','Shoes','Shirt','Shirt','Shirt'],
        "quantity":[13,19,12,5,18],
        "unit":[4,5,3,6,8],
        "price":[234,564,565,335,345],
        "net_price":[234,564,565,335,345],
        "date":['2014-09-27 07:13:03','2014-07-29 02:10:4','2014-03-01 10:51:24','2013-11-17 20:41:11','2014-01-03 08:14:27']
    }
)
# print new_dataframe
new_dataframe.to_csv("c:/temp/output.csv")
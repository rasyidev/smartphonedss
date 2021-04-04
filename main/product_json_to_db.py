from mysql.connector import Error
import mysql.connector
import json
from models import Smartphone

smartphone_id = 2
smartphone = Smartphone.objects.get(id=smartphone_id)

file = open('product_Xiaomi-Redmi-Note-9-RAM-4GB-ROM-64GB.json')
data = json.load(file)

products = data
print(len(products))
mydb = None

try:
   mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="smartphonedss"
   )
except Error as e:
   print("Database Error nih:", e)

def insert_to_db(data):
   if mydb is not None:
      # print(mydb.is_connected())
      if mydb.is_connected():
         cursor = mydb.cursor()
         try:
            sql_query = f"""insert into main_product values(
               '', 
               '{data['seller']}', 
               '{data['product_rank']}', 
               '{data['price']}', 
               '{data['product_url']}', 
               70
               )"""

            # print(sql_query)
            cursor.execute(sql_query)
            mydb.commit()
            print(f"Sukses menginputkan data {data['seller']}")
         except Error as e:
            print("Error:", e.msg)

for product in products:
   insert_to_db(product)
   
# print(products)
# print(smartphone)
# general_name = smartphone['general_name']
# cpu = smartphone['cpu']
# url = smartphone['url']
# img_url = smartphone['img_url']
# main_cam = smartphone['main_cam']
# selfie_cam = smartphone['selfie_cam']
# battery = smartphone['battery']
# # print("main cam nih: ", smartphone['main_cam'])
# print("main cam nih: ", main_cam)


# # print(mydb.is_connected())



# for x in smartphone['varian']:
#    data = {}
#    data['name'] = x['name']
#    data['ram'] = x['ram']
#    data['cpu'] = x['cpu']
#    data['storage'] = x['storage']
#    data['battery'] = battery
#    data['url'] = url
#    data['img_url'] = img_url
#    data['main_cam'] = main_cam
#    data['selfie_cam'] = selfie_cam

#    insert_to_db(data)
#    # print(data)
#    print("-------------------------")

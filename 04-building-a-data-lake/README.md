# Building a Data Lake
Project: Building an ETL Pipeline to Transform Data in Data Lake (From Landing Zone to Cleaned Zone)

## ขั้นตอนการทำ
1. ใน CodeSpace ให้ไปหาโฟลเดอร์ที่ต้องการโดยใช้คำสั่ง 
```sh
cd 04-building-a-data-lake
```

2. เพื่อให้เราสามารถสร้างไฟล์ได้จาก Jupyter Lab ให้รันคำสั่งด้านล่างนี้
```sh
sudo chmod 777 .
```
3. แล้วค่อยรัน
```sh
docker-compose up
```
4. เข้าไปยัง ports 8888 โดยจะเชื่อมต่อไปยัง Jupyter Lab ให้นำเลข token จาก terminal มาใส่ เพื่อ log in เข้าระบบ
5. เมื่อสามารถเชื่อมต่อเข้าใช้ data lake บน Jupyter Lab ได้แล้ว 

## etl_local.ipynb
6. ให้ import spark เข้ามาใช้ใน python
```sh
from pyspark.sql import SparkSession
```
7. จากนั้น ทำการเชื่อมต่อ spark
```sh
spark = SparkSession.builder \
    .appName("ETL") \
    .getOrCreate()
```
8. ทดลองเรียกดูข้อมูลจาก file data
```sh
data.show()
```
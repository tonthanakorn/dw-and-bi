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
9. หรือใช้คำสั่ง spark.sql แล้วเขียนเป็น sql เพื่อเรียกดูข้อมูลใน table ได้ผลลัพธ์เหมือนนกัน
```sh
data.createOrReplaceTempView("staging_events")

table = spark.sql("""
    select
        *
    from
        staging_events
""").show()
```
10. สามารถสร้าง events เพื่อเก็บข้อมูลแยกตามที่ต้องการ เช่น การสร้าง folder actors, repos เก็บข้อมูลเป็น file csv
```sh
output_csv = "output_csv"
output_parquet = "output_parquet"
```
```sh
table.write.partitionBy("year").mode("overwrite").csv(output_csv)
```
```sh
table.write.partitionBy("date").mode("overwrite").csv(destination)
```
```sh
destination = "events"
```
```sh
table.write.partitionBy("year", "month", "day").mode("overwrite").csv(destination)
```
```sh
table.write.partitionBy("date").mode("overwrite").csv(destination)
```
11. เช่น folder actors ต้องการเก็บข้อมูล column actor login , id , actor url เป็นต้น
```sh
table = spark.sql("""
    select
        actor.login
        , id as event_id
        , actor.url as actor_url
    from
        staging_events
""")
destination = "actors"
table.write.mode("overwrite").csv(destination)
```
12. หรือ folder repos ต้องการเก็บข้อมูล column repo.name , id , repo.url เป็นต้น
```sh
table = spark.sql("""
    select
        repo.name
        , id as event_id
        , repo.url as repo_url
        
    from
        staging_events
""")
destination = "repos"
table.write.mode("overwrite").csv(destination)
```

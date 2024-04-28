# Building a Data Pipelines
Project: Creating and Automating a Set of Data Pipelines with Airflow

## ขั้นตอนการทำ
1. ใน CodeSpace ให้ไปหาโฟลเดอร์ที่ต้องการโดยใช้คำสั่ง 
```sh
cd 05-creating-and-scheduling-data-pipelines
```
2. เพื่อให้เราสามารถเชื่อมต่อกับ Apache Airflow ให้รันคำสั่งด้านล่างนี้
```sh
docker-compose up
```
3. เข้าไปยัง ports 8080 โดยจะเชื่อมต่อไปยัง Apache Airflow ให้ดู Username และ Password จากไฟล์ docker-compose.yaml มาใส่ เพื่อ log in เข้าระบบ

4. การ Load File, การสร้าง Tables และการ Process ทำด้วยไฟล์ etl.py 

5. ใน Airflow สร้าง connection ให้สามารถติดต่อกับ Postgres โดยไปที่  Admin -> Connections
```sh
ใส่ข้อมูลดังนี้
Connection Id : my_postgres_conn
Connection Type : Postgres
Host : postgres
Database : airflow
Port : 5432
```
6. เท่านี้ก็สามารถสร้าง Airflow ใน Dags ได้สำเร็จ

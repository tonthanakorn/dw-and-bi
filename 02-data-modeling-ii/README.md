# DS525 Data Warehouse and Business Intelligence

## What is this Data Modeling II ?

Project: Building a Data Modeling with Cassandra (NoSQL) นี้ ออกแบบมาเพื่อเก็บข้อมูลเหตุการณ์ (Event) ที่เกิดขึ้นใน Github จาก Data ที่มีอยู่ โดยเก็บใน NoSQL database อย่าง Apache Cassandra โดยประกอบด้วย 3 Table ได้แก่
<ol>
  <li>events table ใช้เก็บ Data Event ต่าง ๆ ที่เกิดขึ้น ว่าใครเป็นผู้กระทำ (actor_id) และกระทำใน Repository ใด (repo_id) โดยมี primary key เป็น event_id และ event_type</li>
  <li>actors table ใช้เก็บ Data ของ Actor (ผู้กระทำ) ว่า id นี้ คือใคร โดยมี primary key เป็น actor_id </li>
  <li>repos table ใช้เก็บ Data ของ Repository (พื้นที่เก็บข้อมูล) ว่าการกระทำนี้กระทำใน Repository ใด (name) โดยมี primary key เป็น repo_id</li>
</ol>

## Benefits of this Data Model

Project: Building a Data Modeling with Cassandra (NoSQL)  นี้ สามารถทำให้ทราบว่าเหตุการณ์ต่าง ๆ ที่เกิดขึ้น (Event) เกิดจากใคร (Actor) และกระทำใน Repository ใด
เพื่อให้สามารถติดตามกิจกรรม (event) ของผู้ใช้งาน (actor) และวิเคราะห์ทิศทางของเหตุการณ์ที่เกิดขึ้นในพื้นที่เก็บข้อมูล
(Repository) นั้น ๆ ได้

## instruction ใน Terminal

เปลี่ยนพื้นที่ไปที่ 02-data-modeling-ii โดยใช้คำสั่ง
```sh
 cd 02-data-modeling-ii/
```

ติดตั้ง Cassandra โดยใช้คำสั่ง 
```sh
docker-compose up
```

ติดตั้ง Python เพื่อให้ codespace สามารถรันโค้ด Python ได้ โดยใช้คำสั่ง
```sh
pip install psycopg2
```

ติดตั้ง Cassandra Module สำหรับเชื่อมต่อระหว่าง Cassandra และ Python โดยใช้คำสั่ง
```sh
pip install cassandra-driver
```

ทำ ETL จากข้อมูล JSON โหลดเข้าไปใน Cassandra โดยใช้คำสั่ง
```sh
python etl.py
```

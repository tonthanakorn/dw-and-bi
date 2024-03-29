# Data Modeling I

## What is this Data Model ?

```sh
Data Model นี้ ออกแบบมาเพื่อเก็บข้อมูลเหตุการณ์ (Event) ที่เกิดขึ้นใน Github จาก Data ที่มีอยู่ โดยประกอบด้วย 3 Table 
```

[![image.png](https://i.postimg.cc/j5rGdCNk/image.png)](https://postimg.cc/HJBS6Y6Q)

[![image.png](https://i.postimg.cc/1zt3yCGj/image.png)](https://postimg.cc/nXyJk1w4)

[![image.png](https://i.postimg.cc/MZstTvJ3/image.png)](https://postimg.cc/K4Mtpczt)

[![image.png](https://i.postimg.cc/YSbL3L3J/image.png)](https://postimg.cc/06KN5Qhf)

```sh
1. events ใช้เก็บ Data Event ต่าง ๆ ที่เกิดขึ้น ว่าใครเป็นผู้กระทำ (actor_id) และกระทำใน Repository ใด (repo_id) 
```

[![image.png](https://i.postimg.cc/k4NJc0qD/image.png)](https://postimg.cc/8J5gknFV)

```sh
2. actors ใช้เก็บ Data ของ Actor (ผู้กระทำ) ว่า id นี้ คือใคร (login)
```

[![image.png](https://i.postimg.cc/pTPb2pMX/image.png)](https://postimg.cc/TyNH02PZ)

```sh
3. repos ใช้เก็บ Data ของ Repository (พื้นที่เก็บข้อมูล) ว่าการกระทำนี้กระทำใน Repository ใด (name)
```

[![image.png](https://i.postimg.cc/bvsL1P0H/image.png)](https://postimg.cc/VSPjc3Vd)


### Benefits of this Data Model

```sh
Data Model นี้ สามารถทำให้ทราบว่าเหตุการณ์ต่าง ๆ ที่เกิดขึ้น (Event) เกิดจากใคร (Actor) และกระทำใน Repository ใด
เพื่อให้สามารถติดตามกิจกรรม (event) ของผู้ใช้งาน (actor) และวิเคราะห์ทิศทางของเหตุการณ์ที่เกิดขึ้นในพื้นที่เก็บข้อมูล
(Repository) นั้น ๆ ได้
```

## instruction ใน Terminal

เปลี่ยนพื้นที่ไปที่ 01-data-modeling-i โดยใช้คำสั่ง
```sh
 cd 01-data-modeling-i/
```
ลงเว็ปเซิฟเวอร์ docker nginx
```sh
docker run -p 8080:80 ngix
```

ติดตั้ง Postgres โดยใช้คำสั่ง 
```sh
docker-compose up
```

ติดตั้ง Python เพื่อให้ codespace สามารถรันโค้ด Python ได้ โดยใช้คำสั่ง
```sh
pip install psycopg2
```

ทำสร้าง Table ไปยัง Postgres โดยใช้คำสั่ง
```sh
python create_tables.py
```

ทำ ETL จากข้อมูล JSON โหลดเข้าไปใน Postgres โดยใช้คำสั่ง
```sh
python etl.py
```

# Data Modeling I

## What is this Data Model ?

```sh
Data Model นี้ ออกแบบมาเพื่อเก็บข้อมูลเหตุการณ์ (Event) ที่เกิดขึ้นใน Github จาก Data ที่มีอยู่ โดยประกอบด้วย 3 Table 

(https://i.postimg.cc/j5rGdCNk/image.png)

[![image.png](https://i.postimg.cc/1zt3yCGj/image.png)](https://postimg.cc/nXyJk1w4)

[![image.png](https://i.postimg.cc/MZstTvJ3/image.png)](https://postimg.cc/K4Mtpczt)

[![image.png](https://i.postimg.cc/YSbL3L3J/image.png)](https://postimg.cc/06KN5Qhf)

1. events ใช้เก็บ Data Event ต่าง ๆ ที่เกิดขึ้น ว่าใครเป็นผู้กระทำ (actor_id) และกระทำใน Repository ใด (repo_id) 

[![image.png](https://i.postimg.cc/k4NJc0qD/image.png)](https://postimg.cc/8J5gknFV)

2. actors ใช้เก็บ Data ของ Actor (ผู้กระทำ) ว่า id นี้ คือใคร (login)

[![image.png](https://i.postimg.cc/pTPb2pMX/image.png)](https://postimg.cc/TyNH02PZ)

3. repos ใช้เก็บ Data ของ Repository (พื้นที่เก็บข้อมูล) ว่าการกระทำนี้กระทำใน Repository ใด (name)

[![image.png](https://i.postimg.cc/bvsL1P0H/image.png)](https://postimg.cc/VSPjc3Vd)

```
### Benefits of this Data Model

```sh
Data Model นี้ สามารถทำให้ทราบว่าเหตุการณ์ต่าง ๆ ที่เกิดขึ้น (Event) เกิดจากใคร (Actor) และกระทำใน Repository ใด
เพื่อให้สามารถติดตามกิจกรรม (event) ของผู้ใช้งาน (actor) และวิเคราะห์ทิศทางของเหตุการณ์ที่เกิดขึ้นในพื้นที่เก็บข้อมูล
(Repository) นั้น ๆ ได้
```

## Getting Started

```sh
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

### Prerequisite when install psycopg2 package

For Debian/Ubuntu users:

```sh
sudo apt install -y libpq-dev
```

For Mac users:

```sh
brew install postgresql
```

## Running Postgres

```sh
docker-compose up
```

To shutdown, press Ctrl+C and run:

```sh
docker-compose down
```

## Running ETL Scripts

```sh
python create_tables.py
python etl.py
```

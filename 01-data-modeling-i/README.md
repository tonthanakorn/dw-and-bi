# Data Modeling I

## Data model

```sh
Data Model นี้ ออกแบบมาเพื่อเก็บข้อมูลเหตุการณ์ (Event) ที่เกิดขึ้นใน Github จาก Data ที่มีอยู่ โดยประกอบด้วย 3 Table ได้แก่
1. events ใช้เก็บ Data Event ต่าง ๆ ที่เกิดขึ้น ว่าใครเป็นผู้กระทำ (actor_id) และกระทำใน Repository ใด (repo_id) 
2. actors ใช้เก็บ Data ของ Actor (ผู้กระทำ) ว่า id นี้ คือใคร (login)
3. repos ใช้เก็บ Data ของ Repository (พื้นที่เก็บข้อมูล) ว่าการกระทำนี้กระทำใน Repository ใด (name)
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

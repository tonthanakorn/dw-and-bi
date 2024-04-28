# Analytics Engineering

## ขั้นตอนการทำ
1. ใน CodeSpace ให้ไปหาโฟลเดอร์ที่ต้องการโดยใช้คำสั่ง 
```sh
cd 06-analytics-engineering
```
2. หลังจากนั้นให้เปิดการเชื่อมต่อเพื่อใช้งาน postgres บน dbt โดยใช้คำสั่ง
```sh
docker-compose up
```
3. เชื่อมต่อเพื่อใช้งาน postgres บน dbt ได้ที่ port 3000 โดยสามารถดู Username และ Password ได้จากไฟล์ docker-compose.yml และ sign in เพื่อเข้าสู่ระบบ
4. เปิดการใช้ virtual environment โดยใช้คำสั่ง
```sh
python -m venv ENV
source ENV/bin/activate
```
5. ติดตั้งเพื่อใช้งาน dbt เข้ากับ postgres โดยใช้คำสั่ง
```sh
pip install dbt-core dbt-postgres
```
6. สร้าง dbt project โดยใช้คำสั่ง
```sh
dbt init
```
และสร้าง project , dbname , host ,pass , port , shchema , threads , type , user
7. แก้ไข the dbt profile --> folder ds525 --> folder model ---> สร้าง file profiles.yml (เอา code ที่ได้มาเก็บไว้) โดยใช้คำสั่ง
```sh
code ~/.dbt/profiles.yml
```
8. ลอง Test การเชื่อมต่อกับ dbt โดยใช้คำสั่ง
```sh
dbt debug
```
ถ้าขึ้นข้อความว่า "All checks passed!". ถือว่า ok
9. เข้าไปโฟลเดอร์ที่ต้องการ โดนใช้คำสั่ง
```sh
cd ds525
```
10. ทำการ dbt create models โดยใช้คำสั่ง
```sh
dbt debug
dbt run
dbt test
```

## Documentaion Analytics Engineering
เมื่อทำการเชื่อมต่อการใช้งานกับ dbt และ postgres เรียบร้อยแล้ว
1. ทำการเชื่อมต่อ tables โดยใช้คำสั่ง
```sh
dbt run
```
2. create folder models --> create folder staging --> create โดยใช้คำสั่ง
stg__jaffle_shop_customers.sql 
```sh
select * from {{source('jaffle_shop','jaffle_shop_customers')}}
```
stg__jaffle_shop_order.sql
```sh
select * from {{source('jaffle_shop','jaffle_shop_orders')}}
```
3. create folder models --> create folder marts --> create jaffle_shop_obt.sql โดยใช้คำสั่ง
```sh
select 
    o.id as order_id
    , o.user_id
    , c.first_name
    , c.last_name
    , o.order_date
    , o.status as order_status

from {{ ref('stg__jaffle_shop_orders')}} as o
join {{ ref('stg__jaffle_shop_customers')}} as c 
on o.user_id = c.id
```
หลังจากนี้ผู้ใช้สามารถดึงข้อมูลจาก jaffle_shop_obt.sql ไปใช้งานต่อได้


```bash
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

```bash
cd ds525
dbt debug
dbt run
dbt test
```
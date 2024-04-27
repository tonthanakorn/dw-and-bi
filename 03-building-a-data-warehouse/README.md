# DS525 Data Warehouse and Business Intelligence
Project: Building an ETL Pipeline for a Cloud Data Warehouse (Google BigQuery) จะเรียนรู้เรื่องการนำข้อมูลจาก json github ไปยัง Google BigQuery 

## ขั้นตอนการทำ
1. เข้าไปยัง Google Cloud Platform (GCP) จากนั้นสร้าง Dataset โดยเลือกเป็น single region
2. ในหน้า Console ให้เลือก Service ชื่อว่า IAM & Admin ไปยังแถบซ้ายมือ เลือก Service Accounts และเลือก CREATE SERVICE ACCOUNT 
3. ระบุชื่อ (ในที่นี้ระบุว่า etl to bigqury) และกำหนด role (ในที่นี้ระบุว่า owner) และเลือก DONE
4. จากนั้น ให้กำหนด KEY โดยเลือกที่ SERVICE ACCOUNT ที่เราสร้าง > MANAGE KEY > ADD KEY > Create new key > JSON จากนั้นกด OK
5. ใน CodeSpace ให้ไปหาโฟลเดอร์ที่ต้องการโดยใช้คำสั่ง 
```sh
cd 03-building-a-data-warehouse
```
6. สร้าง environment โดยใช้คำสั่ง
```sh
python -m venv ENV
source ENV/bin/activate
```
7. สร้าง packages ต่างๆ โดยใช้คำสั่ง
```sh
pip install -r requirements.txt
```
8. run ไฟล์ etl โดยใช้คำสั่ง
```sh
python etl_bigquary.py
```
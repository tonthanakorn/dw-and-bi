# Data Modeling I

### Data model

```sh
Data Model นี้ ออกแบบมาเพื่อเก็บข้อมูลเหตุการณ์ (Event) ที่เกิดขึ้นใน Github จาก Data ที่มีอยู่ โดยประกอบด้วย 3 Table ได้แก่
1. events ใช้เก็บ Data Event ต่าง ๆ ที่เกิดขึ้น ว่าใครเป็นผู้กระทำ (actor_id) และกระทำใน Repository ใด (repo_id) 
2. actors ใช้เก็บ Data ของ Actor (ผู้กระทำ) ว่า id นี้ คือใคร (login)
3. repos ใช้เก็บ Data ของ Repository (พื้นที่เก็บข้อมูล) ว่าการกระทำนี้กระทำใน Repository ใด (name)
```

# **Using MySQL CLI: Instructions**

## **1️⃣ Connecting to MySQL CLI**
To access MySQL via the command line:

```sh
mysql -u root -p
```
- `-u root`: Specifies the MySQL user (replace `root` with your username if needed).
- `-p`: Prompts for the password (enter the MySQL root password when asked).

## **2️⃣ Creating a Database**
To create a new database:

```sql
CREATE DATABASE divine_comedy_db;
```

To verify that the database has been created:

```sql
SHOW DATABASES;
```

## **3️⃣ Selecting a Database**
Before executing queries, select the database you want to use:

```sql
USE divine_comedy_db;
```

## **4️⃣ Deleting a Database**
⚠ **Warning: This action is irreversible!**

To permanently delete a database:

```sql
DROP DATABASE divine_comedy_db;
```

To avoid errors if the database doesn’t exist:

```sql
DROP DATABASE IF EXISTS divine_comedy_db;
```

## **5️⃣ Creating a Table**
Example of creating a table inside the database:

```sql
CREATE TABLE author (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);
```

To verify table creation:

```sql
SHOW TABLES;
```

## **6️⃣ Inserting Data**
To insert a record into a table:

```sql
INSERT INTO author (name) VALUES ('Dante Alighieri');
```

To check if data was inserted:

```sql
SELECT * FROM author;
```

## **7️⃣ Deleting Data**
To delete all records from a table:

```sql
DELETE FROM author;
```

To delete specific records:

```sql
DELETE FROM author WHERE name = 'Dante Alighieri';
```

## **8️⃣ Exiting MySQL CLI**
To exit the MySQL command line:

```sh
exit
```

---

### **🚀 Quick Command Summary**
| Command | Description |
|---------|-------------|
| `mysql -u root -p` | Connect to MySQL |
| `CREATE DATABASE db_name;` | Create a new database |
| `SHOW DATABASES;` | List all databases |
| `USE db_name;` | Select a database |
| `DROP DATABASE db_name;` | Delete a database (irreversible) |
| `SHOW TABLES;` | List all tables in the database |
| `EXIT;` | Quit MySQL CLI |

---
### **🔥 Now you're ready to manage MySQL databases using the command line!** 🚀


# PAU SIBAS - Attendance Management System

A web-based **Attendance Management System** developed for the **DTS304 – Data Management I Project** at Pan-Atlantic University.

The system is built using **Streamlit** for the frontend and **PostgreSQL** for backend data storage, providing a simple, secure, and interactive platform for managing attendance records.

---

## 🚀 Technologies Used

* **Frontend Framework:** Streamlit
* **Backend Database:** PostgreSQL
* **Programming Language:** Python
* **Authentication:** bcrypt (password hashing)
<!-- * **Data Processing:** pandas -->

---

## 📦 Project Structure

```text
SIBAS/
│
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
│
├── pages/
│   ├── login.py
│   ├── admin.py
│   ├── lecturer.py
│   └── student.py
│
├── src/
│   ├── auth.py
│   ├── database.py
│   └── queries.py
│
├── database/
├── utils/
├── assets/
│
├── app.py
├── requirements.txt
├── script1_schema.sql
├── script2_admin_task.py
└── README.md
```

### Folder Overview

| Folder/File             | Description                                               |
| ----------------------- | --------------------------------------------------------- |
| `.streamlit/`           | Streamlit configuration and database credentials          |
| `pages/`                | Role-based UI pages (Admin, Lecturer, Student, Login)     |
| `src/`                  | Core logic (authentication, database connection, queries) |
| `database/`             | Database-related resources                                |
| `utils/`                | Helper functions and utilities                            |
| `assets/`               | Static files such as images and icons                     |
| `app.py`                | Main entry point of the application                       |
| `requirements.txt`      | Project dependencies                                      |
| `script1_schema.sql`    | Database schema creation script                           |
| `script2_admin_task.py` | Admin setup or initialization script                      |

---

## ⚙️ How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/e-abbah/SIBAS.git
cd SIBAS
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit psycopg2-binary bcrypt pandas
```

---

### 3. Configure Database

Create a `.streamlit` folder (if not already present), then add a file called:

```text
.streamlit/secrets.toml
```

Add your PostgreSQL configuration:

```toml
[postgres]
host = "localhost"
database = "sibas_db"
user = "postgres"
password = "YOUR_LOCAL_POSTGRES_PASSWORD"
port = 5432
```

---

### 4. Create the Database

Run the SQL schema file in PostgreSQL:

```bash
script1_schema.sql
```

This will create all required tables.

---

### 5. Run the Application

```bash
streamlit run app.py
```

Then open your browser at:

```
http://localhost:8501
```

---

## ✨ Features

* User authentication (Admin, Lecturer, Student)
* Secure password hashing using bcrypt
* Attendance recording and tracking
* Role-based dashboards
* PostgreSQL database integration
* Interactive Streamlit UI
* Data reporting and visualization

---

## 👥 User Roles

### Admin

* Manage system users
* View attendance reports
* System configuration

### Lecturer

* Mark attendance
* View class attendance records

### Student

* View personal attendance
* Track attendance history

---

## 🧠 Notes

* Ensure PostgreSQL is running before starting the app
* Keep your `secrets.toml` file secure and never commit it to GitHub
* Always install dependencies before running the project

---

## 📄 License

This project is developed for academic purposes under DTS304 coursework at Pan-Atlantic University.

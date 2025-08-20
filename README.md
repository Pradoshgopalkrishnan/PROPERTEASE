# Propertease – Real Estate Management System

A robust real estate management solution built with **Python**, **Tkinter**, and **MySQL** to streamline property, customer, and agent operations.  
Propertease features an intuitive graphical interface (Tkinter) and secure data handling with environment-based configuration.

---

## 📖 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Setup & Usage](#-setup--usage)
- [Output](#-output)
- [File Structure](#-file-structure)
- [Security Guidelines](#-security-guidelines)
- [Future Enhancements](#-future-enhancements)
- [Contributors](#-contributors)

---

## ✨ Features

- **Property Management**: Add, update, and track properties and details in the system.
- **Customer & Agent Records**: Register customers and agents, assign properties.
- **Graphical User Interface**: Tkinter-based login, data entry, visualization.
- **MySQL Integration**: Fast, reliable backend data storage and retrieval.
- **Modular Python Code**: Easy to maintain, extend, and collaborate on.
- **Secure Credentials**: All sensitive info managed through `.env` (never shared).
- **Cross-Platform**: Runs on standard Windows, MacOS, and Linux setups.

---

## 🛠️ Tech Stack

- Python 3.x
- Tkinter (GUI)
- MySQL
- `mysql-connector-python`
- `python-dotenv` (for .env handling)

---

## 🚀 Setup & Usage

1. **Clone the Repository**
git clone https://github.com/Pradoshgopalkrishnan/propertease.git
cd propertease

text

2. **Install Dependencies**
pip install mysql-connector-python python-dotenv

text

3. **Set up the MySQL Database**
- Start your MySQL service.
- Import schema and initial data:
  ```
  mysql -u your_mysql_user -p < "PROPERTEASE BACKEND.sql"
  ```

4. **Configure Environment Variables**
- Create a `.env` file with:
  ```
  DB_HOST=localhost
  DB_USER=your_mysql_user
  DB_PASS=your_mysql_password
  DB_NAME=propertease
  ```
- **Do not commit `.env`!**

5. **Launch the Application**
python "SOURCE CODE.py"

text

---

## 📷 Output (Sample)

- Property and agent entry confirmation dialogs.
- Listings and searches in the GUI.
- Error handling for missing or invalid info.
- Secure login window for database connection.

---

## 🗂️ File Structure

propertease/
├── .gitignore
├── .env # Private, not committed
├── PROPERTEASE BACKEND.sql # Database schema
├── SOURCE CODE.py # Main app code
└── README.md # This file

text

---

## 🔒 Security Guidelines

- **.env is always ignored.**
- Never upload passwords or private configs.
- Provide `.env.example` for others to set up.

---

## 🔮 Future Enhancements

- Property image upload and display in GUI.
- Email/SMS notifications for property status.
- Analytics dashboard (sales, agent activities).
- Role-based access for agents/admins.
- Export property and customer reports.

---

## 👥 Contributors

- Project developed for academic and learning purposes.
- Mentor: SMT Indrani Haridasan
- Thanks to open-source contributors and the Python/MySQL communities.

---

## 📚 References

- Official Python/Tkinter/MySQL documentation.
- Example textbooks and online resources.

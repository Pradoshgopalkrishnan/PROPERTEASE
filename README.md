


# README.md
```

```markdown
# Propertease

Propertease is a real estate management application built with **Python**, **Tkinter**, and **MySQL**.  
It provides a graphical interface for managing customers, properties, and agents, with all data securely stored in a relational MySQL database.

---

## Features

- User-friendly GUI built with Tkinter
- Manage Customer, Properties, and Agent tables
- MySQL database connectivity using `mysql.connector`
- Secure credential management using a `.env` file and `python-dotenv`
- Properly ignores sensitive files using `.gitignore`

---

## Setup Instructions

### 1. Clone the Repository

```

git clone https://github.com/Pradoshgopalkrishnan/propertease.git
cd propertease

```

### 2. Install Python Dependencies

```

pip install mysql-connector-python python-dotenv

```

Tkinter is usually installed with Python by default.

### 3. Set Up the MySQL Database

- Start your MySQL server.
- Create a new database, for example `propertease`.
- Import the provided SQL file to set up the initial schema:
```

mysql -u your_mysql_user -p < "PROPERTEASE BACKEND.sql"

```

### 4. Configure Environment Variables

Create a `.env` file (in the same folder as your code) containing your database credentials:

```

DB_HOST=localhost
DB_USER=your_mysql_user
DB_PASS=your_mysql_password
DB_NAME=propertease

```

**NEVER share or commit your real `.env` file.**

### 5. Run the Application

```

python "SOURCE CODE.py"

```

---

## .gitignore Settings

Your `.gitignore` should include:

```

.env
__pycache__/
*.pyc

```

---

## Security and Collaboration

- Always keep your `.env` file private and out of version control.
- For sharing setup, provide a `.env.example` file (with placeholders, not real credentials).

---

## File Structure

```

propertease/
├── .gitignore
├── .env                \# Your private credentials (never in git)
├── PROPERTEASE BACKEND.sql  \# Database setup script
├── SOURCE CODE.py      \# Main Python code
└── README.md           \# Project documentation (this file)

```

---

## Contributing

Pull requests and suggestions are welcome! Open an issue or submit a PR with improvements.

---

## License

MIT License

Copyright (c) 2025 Pradosh Gopalkrishnan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---


```

<div style="text-align: center">⁂</div>




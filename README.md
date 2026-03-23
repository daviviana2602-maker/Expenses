# 📊 Expenses Tracker
A simple Python CLI program to track and manage personal expenses, categorized as residential or variable, using PostgreSQL for data storage.

-------------------------------------------------------------------------------------------------

# 🛠 Features

- Register expenses with description, category, amount, and date.
- Generate reports for a specific date range:
- Total expenses
- Total residential expenses
- Total variable expenses
- View a detailed table of all expenses in a given period.
- Colorful and clear CLI interface for easy usage.

-------------------------------------------------------------------------------------------------

# 📝 Technologies Used

- Python 3.x
- SQLAlchemy (ORM)
- PostgreSQL
- Colorama (for terminal colors)
- Tabulate (for pretty tables)
- Custom utility module (fanymodules) for input validation

-------------------------------------------------------------------------------------------------

# ⚙ Setup Instructions

- Clone the repository
- git clone https://github.com/YOUR_USERNAME/expenses.git
- cd expenses
- Install dependencies
- pip install sqlalchemy psycopg2-binary colorama tabulate
- Configure PostgreSQL
- Update the DATABASE_URL in main.py:
- DATABASE_URL = "postgresql+psycopg2://username:password@localhost:5432/database_name"
- Make sure the PostgreSQL server is running.
- Run the program
- python main.py

-------------------------------------------------------------------------------------------------

# 🧭 How to Use

- Menu Options

Register Expense – Enter expense details (description, category, value, date)
Report by Period – Shows total, residential, and variable expenses in a selected date range
View Expense Table – Shows a detailed table of all expenses in a selected date range

- Exit Program

-------------------------------------------------------------------------------------------------

# 💡 Notes

- All inputs are validated using the custom fanymodules library.
- Dates must be entered in DD/MM/YYYY format.
- Supports both residential (fixed) and variable (flexible) expenses.

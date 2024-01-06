 Employee Management System

This repository contains a simple Employee Management System implemented in Python, utilizing MySQL for data storage. The system includes functionalities for managing personal details, office details, and salary details of employees.

 Features:
1. Personal Details:
   - Capture and store personal information such as name, city, date of birth, and phone number.

2. Office Details:
   - Record and manage office-related data including employee code, name, post, joining date, and basic pay.

3. Salary Management:
   - Enter and calculate salary details based on the employee's working days, final pay, year, and month.

 How to Run:
1. Database Setup:
   - Ensure you have MySQL installed on your system.
   - Create a database named 'demo' and execute the SQL scripts for creating tables (office, personal, salary).

2. Run the Application:
   - Execute the 'main()' function to interact with the Employee Management System.

3. Functionalities:
   - Choose options to add/view employee personal details, office details, and salary information.
   - Enter 9 to quit the program.

 Additional Scripts:
- officetab.py:
   - Defines a script to create the 'office' table in the 'demo' database.

- persontab.py:
   - Creates the 'personal' table in the 'demo' database for storing personal details.

- saltab.py:
   - Contains a script to create the 'salary' table in the 'demo' database.

 Note:
- Ensure that you have change the connection object details of personal host name password
  and database name
- Ensure that the MySQL server is running and accessible.
- Make sure to install the required Python library `mysql-connector` using:
  bash
  pip install mysql-connector
  

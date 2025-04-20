## Smart POS 💸

A Point of Sale web app for businesses built with Python and Django for learning purposes.


## Table of Contents:
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Run it locally](#run-it-locally)

## Features
- Login Page with User authentication
- Dashboard Page with statistics and graphs
- DataTables with print, copy, to CSV, and to PDF buttons
- Categories and Products Management
- Customer Management
- Sales Management


## Tech Stack

- Frontend: HTML, CSS, JavaScript, Boostrap, SweetAlert, DataTables
- Backend: Django, Python, Ajax, SQLite 

## Installation

### Prerequisites
- [Python 3.x](https://www.python.org/downloads/)
- [pip package manager](https://pip.pypa.io/en/stable/installation/)
- [git](https://git-scm.com/downloads)
  
    
  1. Clone or download the repository:

  ` git clone https://github.com/bilalahmedss/Smart_POS`

  2. Go to the project directory

  ` cd smart-pos`

  3. Create a virtual environment :

  PowerShell:
  ```
   python -m venv venv
   venv\Scripts\Activate.ps1
  ```

  4. Install dependencies:  
  ` pip install -r requirements.txt`
  
  5.  Update pip and setuptools  
  ` python -m pip install --upgrade pip setuptools`  
  
  6. Install GTK to create the PDF files:  
   [Official documentation](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation)
  
  7. Windows Users (IMPORTANT)‼:

     Only Windows 11 64-bit is supported ‼

     After installing GTK, you need to add it to your system's Path environment variable. Follow these steps:

      - Assuming you installed GTK at:
        `C:\Program Files\GTK3-Runtime Win64\bin`  
        This will be your new variable that you need to add to Path
        
      - Refer to this tutorial for detailed instructions on adding to the Path environment variable:
        [Tutorial add to the Path enviroment variable](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/)  
    
      - If you encounter an error such as "cannot load library," refer to this documentation for troubleshooting:
        [Missing Library Error](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#missing-library)  
  
  9. Restart your computer: After completing the steps above, it is essential to restart your computer for the changes to take effect properly. ‼
  
## Run it locally
After restarting your computer

1. Go to the project directory: `cd Smart_POS`

2. Activate the virtual enviroment

    PowerShell:
    ```
     venv\Scripts\Activate.ps1
    ```
3. Go to the django_pos folder: `cd django_pos`

4. Make database migrations:  
  `python manage.py makemigrations` and 
  `python manage.py migrate`

5. Create superuser `python manage.py createsuperuser` 
  
   with the following data, or with the data you prefer:
   `username: admin,
    password: admin,
    email: admin@admin`

7. Run the server: `python manage.py runserver`

8. Open a browser and go to: `http://127.0.0.1:8000/`

9. Log In with your superuser credentials.
    
[Back to top ⬆️](#smart-pos-)

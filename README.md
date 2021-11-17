# thuattoangomcum_degsinerHT_NT.io
# welcome to my project specialized cluster collection algorithm

## Features of this Project
### A. Admin Users Can
1. Manage student scores(Add, Update and detele)
2. Training course(Add, Update and delete)
3. Specialized(Add, Update and delete)
4. Training program(Add, Update and delete)
5. Manage User(Add,Update and delete)
6. Advice information(Add,Update and delete)
### C. Students Can
1. View consultation results
2. Add a score of specialized expertise for comparison
3. Add points in list columns when they see the wrong point

## How to Install and Run this project?

### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*Alternative to Pip is Homebrew*

### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install Django
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```

For Mac
```
$  source venv/bin/activate
```

**3. Clone this project**
```
$  git clone https://github.com/hoangpam/thuattoangomcum_degsinerHT_NT.io
```

Then, Enter the project
```
$  cd myproject
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip install -r requirements.txt
```
**6.  Found setup apply uour project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions, student.**
``
$ python manage.py migrate
``
**7. Add the hosts**

- Got to settings.py file 
- Then, On allowed hosts, Add [‘*’]. 
```python
ALLOWED_HOSTS = ['*']
```
*No need to change on Mac.*


**6. Now Run Server**

Command for PC:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver

Workshop RBFA
=============

Introduction
------------


Goals of the project
--------------------
1. Deploy Hello-World App Engine
2. Create Cron Job, every 5 minutes,
3. Insert row to bigquery table (with current timestamp)
4. Upload file to cloud storage bucket (with current timestamp)
5. Update entity in Datastore (change timestamp to current timestamp)

Imprtant files and why we use them
----------------------------------
1. README.md:
2. requirements.txt: 
3 .gitignore:
4. mypy.ini:
5. .flake8:


Used tools and how to use them
------------------------------
### pre-commits 
black and isort (run by typing 'pre-commit' in terminal)

### mypy 
(run for all files by typing 'mypy .')

### flake8 
(run for all files by typing 'flake8')

### functions framework
run functions localy by typing 'functions-framework --target=<name_of_function> --port=8080'


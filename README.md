Workshop RBFA
=============

Introduction
------------
The repository is an onboarding project for developers joining the RBFA dev team. The main goal of this workshop is to learn how to use some basic functionalities of the Google Cloud Platform like Bigquery, Storage and Datastore.
An API is written in Python using FastAPI. For each of the different endpoints, a seperate file is created.  

Goals of the project
--------------------
1. Deploy a first app on App Engine. 'Hello world is shown after calling a certain url together with the current timestamp.
3. Insert a row into a Google Bigquery table that contains all the previous added timestamps. 
4. Upload file to a bucket in Google Cloud Storage each time an endpoint is called. The file itself is a temporary generated CSV file on the local computer and its name contains the current timestamp. 
5. First create, and than update an entity 'Timestamp' in Datastore each time an endpoint is called.
5. Create Cron Job, every 5 minutes, that calls all the previous endpoints.

Imprtant files and why we use them
----------------------------------
1. **README.md**: This is the documentation of the repository. In fact, you are now reading the README file. 
2. **requirements.txt**: This file is a type of file that usually stores information about all the libraries, modules, and packages in itself that are used while developing a particular project.
While developing a project, we generally used a particular version of packages. Later on, the package manager or maintainer may make some changes, and these modifications can easily break your entire application. 
Therefore it is too much work to keep track of every modification in the packages. Specifically, where the project is way too big, it is essential to keep track of each package we are using to avoid unexpected surprises.
3. **.gitignore**: In this file we can define which directories or files shouldn't be uploaded to the git repository. For example, the /venv directory (for the virtual environment) shouldn't be included while pushing to the repo. 
4. **mypy.ini**: In the mypy.ini file we should always speciy which version of python is used, and we can also define which files or directories shouldn't be checked by mypy.
5. **.flake8**: In this file we can define which directories, files, errors or specific errors for certain files or directories shoudn't be checked by flake8. 


Used tools and how to use them
------------------------------
1. **pre-commits black and isort**: a pre-commit is done before we commit certain changes to our local repo. We can add multiple one or more hooks to our pre-commit config file. This way certain rules are being checked before it is too late. 
To know more about pre-commit, or to check which hooks are available, go to https://pre-commit.com/.
Black is a Python code formatter. Check https://github.com/psf/black for more information on Black. 
Isort is a Python utility / library to sort imports, and automatically separate them into sections by type. Check https://github.com/PyCQA/isort to know more about Isort. 
We can run our pre-commit hooks by typing this command in the root of our project: 
```console
~$ pre-commit run --all-files
```

2. **mypy**: Mypy is an optional static type checker for Python that aims to combine the benefits of dynamic typing and static typing. See https://pypi.org/project/mypy/ for more info. 
We can run for all files by typing this command in the root of our project:
```console
~$ mypy .
```

3. **flake8**: flake8 is  wrapper wich verifies pep8, which is a convention for Python coding. 
We can run flake8 for all files by typing this command in the root of the project: 
```console
~$ flake8
```

4. **functions framework**: Google's function framework is made to give developpers the opportunity to test their Google Cloud Functions before they deploy them. Check https://cloud.google.com/functions/docs/functions-framework for more information. 
After installation, run your functions localy by typing this command:
```console
~$ functions-framework --target=<name_of_function> --port=8080
```

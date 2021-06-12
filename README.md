#  Luthor Backend

This is a migration to django from Laravel project. This is the backend for assistance app 

### [Original Repository](https://github.com/wmartzh/luthor)


## Requirements
  - Python 
  - Poetry
  - Django
  - Rest Framework
 
## Setup

Install using Pip 

    pip install -r requirements.txt

Install using Poetry

    poetry install 

Running migrations

     python manage.py makemigrations
     python manage.py migrate

     ## version 3 
     python3 manage.py makemigrations
     python3 manage.py migrate

## Run API

     python manage.py runserver

     ## version 3 
     python3 manage.py runserver

# Flask for data strucure

Implement the following data structures from scratch in python

* linked list
* bash table
* binary search tree
* stack
* queue

Build an API server using flask and these data structures

## Requirement

* Flask
* flask_sqlalchemy
* SQLAlchemy
* Faker (for generating dummy data)

## Usage

**Building a virtual environment**

```bash=
$ python3 -m venv .venv
$ python3 -r requirements.txt
```

**Building a database**

```bash=
$ python3
>>> from server import db
>>> db.create_all()
>>> exit()
```

**Generate dummy data**

generate 200 users and 200 blogs.

```bash=
$ python3 generate_dummpy_date.py
```

**Start server**

```bash=
$ python3 server.py
```

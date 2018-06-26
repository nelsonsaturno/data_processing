# Data Processing App

Django project to process data about financial securities.

Getting Started
---------------

Development setup.

### Prerequisites

* Install Python 3.6
* Install [pip](https://pip.pypa.io/en/stable/installing/)
* Install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)

### Installing

Go to the main path of the project (where manage.py is located) and create a new virtual environment

```
mkvirtualenv <virtualenv_name> [-a <path_to_project>] [-r requirements.txt] [-p "python3.6"]
```

Enter in the virtual environment if you are not inside yet

```
workon <virtualenv_name>
```

Install external libraries if you haven't used [-r requirements.txt] in the previous step

```
pip install -r requirements.txt
```

Edit $VIRTUAL_ENV/bin/postactivate and add the line below

```
export DATABASE_URL=postgres://<user>:<password>@<host>:<port>/<db_name>
```

Re-enter into the virtual environment

```
deactivate
workon <virtualenv_name>
```

Migrate the Database

```
python manage.py migrate
```

You could use sample data for your DB
(Note: you might have to add more data to have the security prices up-to-date.)

```
python manage.py loaddata calculator_seed.json
```

Execute the project

```
python manage.py runserver --noreload 127.0.0.1:8000
```

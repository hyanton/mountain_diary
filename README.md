#### FLASK API for Mountain Diary

### Terminal commands
Make sure you have `pip3`, `python 3.7` and `virtualenv` installed.
```
Initial installation with pip3

$ pip3 install -r requirements.txt
```    

Make sure to run the initial migration commands to update the database.
```
$ python3 manage.py db init

$ python3 manage.py db migrate --message 'initial database migration'

$ python3 manage.py db upgrade
```

Run flask (in development).
```
$ python3 manage.py run
``` 

### Viewing the API ###
```
Open the following url on your browser to view swagger documentation
http://127.0.0.1:5019/
```

### Run with Docker
```
$ docker build -t mountain-diary .

$ docker run -p 5019:5019 --name mountain-diary mountain-diary 
```



### Extension:
- Restful: [Flask-restplus](http://flask-restplus.readthedocs.io/en/stable/)

- SQL ORM: [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/en/2.x/)
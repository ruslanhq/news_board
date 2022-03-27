# Simple News Board application

## Setup


The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/ruslanhq/news_board.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv venv
$ source venv/bin/activate
```
Create file `local_settings.py` like `local_settings_example.py` on the `news_board` directory.

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
Or you can run command:
```sh
(env)$ docker-compose up
```

And navigate to `http://127.0.0.1:8000/api/post/`.

## Postman

Collection link:
`https://www.getpostman.com/collections/2ca28c10cef697c9279c`

## Heroku

Deployment link:
`https://limitless-escarpment-94655.herokuapp.com/api/`

Use follow `login:admin` and `password:admin` to login.


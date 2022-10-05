# Parrallel Request Processing using FastAPI, plus Async Task scheduling with Celery

## Installation
```bash
$ python -m venv venv && source ./venv/bin/activate # Optional Create and activate a virtual environment
$ pip install -r requirements.txt
$ gunicorn -k uvicorn.workers.UvicornWorker -w 2 main:app 
```

In this configuration a single gunicorn worker manages 2 UnicornWorkers which process the incoming requests.

## Celery and Flower monitor

Celery uses a redis running on the standard 6379 port. Configurations can be updated by added env variables.
The dedicated Flower monitor looks at the task broker, in this case redis, to construct the dashboard.

Spawn a Celery worker that will look at and process tasks in the "universities" and "university" queues.
```bash
$ celery -A main.celery worker --loglevel=info -Q universities,university # Start celery worker for the specified queues
```
Run the Flower monitor on 5555 port.
By default it monitors all queues.
```bash
$ celery -A main.celery flower --port=5555
```
## Swagger
For the ease of testing, APIs can be invoked through swagger ui sitting at
```http://localhost:8000/docs```

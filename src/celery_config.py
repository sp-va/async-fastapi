from celery import Celery

worker = Celery(
    "tasks",
    broker="pyamqp://vadim:qwerasdf@172.18.0.2:5672/myvhost",
    backend="rpc://"
)

worker.autodiscover_tasks()
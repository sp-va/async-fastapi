from celery import Celery

worker = Celery(
    "tasks",
    broker="pyamqp://vadim:qwerasdf@rabbitmq:5672/myvhost",
    backend="rpc://"
)

worker.autodiscover_tasks()
from celery import Celery
from subprocess import run

worker = Celery(
    "tasks",
    broker="pyamqp://vadim:qwerasdf@rabbitmq:5672/myvhost",
    backend="rpc://",
    include=["celery_worker.tasks"]
)

worker.autodiscover_tasks(["celery_worker",])

if __name__ == "__main__":
    run(["python", "-m", "celery", "-A", "celery_config", "worker"])

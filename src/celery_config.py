from celery import Celery
from subprocess import run

worker = Celery(
    "tasks",
    broker="pyamqp://vadim:qwerasdf@rabbitmq:5672/myvhost",
    backend="rpc://",
    include=["src.celery_worker.tasks"]
)

worker.autodiscover_tasks()

if __name__ == "__main__":
    run(["python", "-m", "celery", "-A", "src.celery_config.worker", "worker"])

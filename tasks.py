from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command


logger = get_task_logger(__name__)


@shared_task
def publish_scheduled():
    call_command("publish_scheduled", )
    logger.info("The publish_scheduled task just ran.")


@shared_task
def searchpromotions_garbage_collect():
    call_command("searchpromotions_garbage_collect", )
    logger.info("The searchpromotions_garbage_collect task just ran.")


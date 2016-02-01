# -*- coding: utf-8 -*-
__author__ = 'klaswikblad'


from celery import Celery
import os
REDIS_SERVER = "192.168.0.16"
REDIS_PORT = "6379"
app = Celery('tasks',broker="redis://{}:{}/0".format(REDIS_SERVER, REDIS_PORT), backend="redis://{}:{}/1".format(REDIS_SERVER, REDIS_PORT))

CELERY_IMPORTS = ('tasks', )

standard_que= "pi-standard"

app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPTED_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='Europe/Stockholm',
    CELERY_ALWAYS_EAGER=False,
    CELERY_ENABLE_UTC=False,
    CELERY_CREATE_MISSING_QUEUES = False,
    CELERY_DEFAULT_QUEUE=standard_que,
    CELERY_DEFAULT_EXCHANGE=standard_que,
    CELERY_DEFAULT_EXCHANGE_TYPE="direct",
    CELERY_DEFAULT_ROUTING_KEY=standard_que,
    CELERY_IMPORTS=('tasks', ),
    CELERY_QUEUES = {
                     standard_que:
                         {'exchange': standard_que, 'exchange_type': 'direct', 'routing_key': standard_que}
                     }
)
#app.autodiscover_tasks('readfeeds.jobs')

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

from __future__ import absolute_import, unicode_literals
from celery import Celery

#tasks list
tasks_list = ['celeryapp.tasks','celeryapp.task1']
app = Celery(main='celeryapp',include=tasks_list)
app.config_from_object('celeryapp.celery_config')


if __name__ == '__main__':
    app.start()

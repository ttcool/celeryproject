from __future__ import absolute_import, unicode_literals
from celery import Celery

#tasks list
tasks_list = ['celeryschedule.tasks','celeryschedule.task1']
app = Celery(main='celeryschedule',include=tasks_list)
app.config_from_object('celeryschedule.celery_config')


if __name__ == '__main__':
    app.start()

from celery.schedules import crontab  
from kombu import Exchange,Queue
from datetime import timedelta

BROKER_URL = 'redis://192.168.5.108:6379/0'  
CELERY_RESULT_BACKEND = 'redis://192.168.5.108:6379/1'  
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_QUEUES = (
          Queue("default_schedule", Exchange("default_schedule"), routing_key="default_schedule"),
          Queue("for_task_schedule_a", Exchange("for_task_schedule_a"), routing_key="task_schedule_a"),
          Queue("for_task_schedule_b", Exchange("for_task_schedule_b"), routing_key="task_schedule_b")
)


CELERY_ROUTES = {
  'celeryschedule.tasks.add':{"queue":"for_task_schedule_a","routing_key":"task_schedule_a"},
  'celeryschedule.tasks.mul':{"queue":"for_task_schedule_b","routing_key":"task_schedule_b"},
  '*':{"queue":"default_schedule","routing_key":"default_schedule"}
}

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERYBEAT_SCHEDULE = {
  'deal-every-30-seconds': {
     'task': 'celeryschedule.tasks.add',
     'schedule': timedelta(seconds=30),
     'args': [3,4]
  },
  'deal-every-10-seconds': {
     'task': 'celeryschedule.tasks.mul',
     'schedule': timedelta(seconds=10),
     'args': [5,6]
  },
  'deal-every-monday-morning': {
     'task': 'celeryschedule.task1.hello',
     'schedule': crontab(hour=7, minute=30, day_of_week=1),
     'args': ['hello','world']
  },
}

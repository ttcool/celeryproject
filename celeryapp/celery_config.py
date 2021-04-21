from celery.schedules import crontab  
from kombu import Exchange,Queue
from datetime import timedelta

BROKER_URL = 'redis://192.168.5.108:6379/2'  
CELERY_RESULT_BACKEND = 'redis://192.168.5.108:6379/3'  
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 60*60*24 

CELERY_QUEUES = (
          Queue("default", Exchange("default"), routing_key="default"),
          Queue("for_taska", Exchange("for_taska"), routing_key="task_a"),
          Queue("for_taskb", Exchange("for_taskb"), routing_key="task_b")
)


CELERY_ROUTES = (
[('celeryapp.tasks.add',{"queue":"for_taska","routing_key":"task_a"}),
  ('celeryapp.tasks.mul',{"queue":"for_taskb","routing_key":"task_b"}),
  ('*',{"queue":"default","routing_key":"default"}),
],
)

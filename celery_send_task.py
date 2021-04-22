#from scrapyproj.scrapytask import scrapyjd

#res = scrapyjd.delay()
#print(res)

from celery import Celery

app = Celery('celeryapp',broker='redis://192.168.5.108:6379/2',backend='redis://192.168.5.108:6379/3')
result = app.send_task('celeryapp.task1.hello',['hello','world'],queue='default')
print(result.successful())

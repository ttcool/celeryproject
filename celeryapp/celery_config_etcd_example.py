from celery.schedules import crontab  
from kombu import Exchange,Queue
from datetime import timedelta

import etcd3
import json
import socket


class ConnectEtcdCluster(object):
    """
    (host=(('127.0.0.1', 4001), ('127.0.0.1', 4002), ('127.0.0.1', 4003)))
    """

    def __init__(self, hosts):
        self.hosts = hosts

    def con(self, port='2379',
            ca_cert=None, cert_key=None, cert_cert=None, timeout=None,
            user=None, password=None, grpc_options=None):
        try:
            for item in self.hosts:
                etcd_sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                Etcd_Result = etcd_sk.connect_ex((item[0], item[1]))
                if Etcd_Result == 0:
                    con = etcd3.client(item[0], item[1], ca_cert=ca_cert, cert_key=cert_key, cert_cert=cert_cert,
                                       timeout=timeout, user=user, password=password, grpc_options=grpc_options)
                    return con
            raise {'status_code': 0, 'data': "can't connect etcd...."}
        except Exception as e:
            print({'status_code': 0, 'data': "can't connect etcd...."})


etcd_cluster = ConnectEtcdCluster((('192.168.2.241', 2379), ('192.168.2.242', 2379), ('192.168.2.243', 2379)))
con = etcd_cluster.con(ca_cert='ca.pem', cert_key='etcd-key.pem', cert_cert='etcd.pem')
data, meta = con.get('/celeryapp_config')
config_json = json.loads(data.decode())


BROKER_URL = config_json["BROKER_URL"]
CELERY_RESULT_BACKEND = config_json["CELERY_RESULT_BACKEND"]  
CELERY_ACCEPT_CONTENT = config_json["CELERY_ACCEPT_CONTENT"]
CELERY_TASK_SERIALIZER = config_json["CELERY_TASK_SERIALIZER"]
CELERY_RESULT_SERIALIZER = config_json["CELERY_RESULT_SERIALIZER"]
CELERY_TASK_RESULT_EXPIRES = config_json["CELERY_TASK_RESULT_EXPIRES"]

CELERY_QUEUES = (
          Queue(config_json["CELERY_QUEUES"][0], Exchange(config_json["CELERY_QUEUES"][0]), routing_key=config_json["CELERY_QUEUES"][0]),
          Queue(config_json["CELERY_QUEUES"][1], Exchange(config_json["CELERY_QUEUES"][1]), routing_key=config_json["CELERY_QUEUES"][1]),
          Queue(config_json["CELERY_QUEUES"][2], Exchange(config_json["CELERY_QUEUES"][2]), routing_key=config_json["CELERY_QUEUES"][2]),
          Queue(config_json["CELERY_QUEUES"][3], routing_key=config_json["CELERY_QUEUES"][3]),
)


CELERY_ROUTES = config_json["CELERY_ROUTES"]

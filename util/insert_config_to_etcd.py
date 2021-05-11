import json
import etcd3
import socket

from etcdclusterclient import ConnectEtcdCluster


config_list = {
    "BROKER_URL": "redis://192.168.5.108:6379/2",
    "CELERY_RESULT_BACKEND": "redis://192.168.5.108:6379/3",
    "CELERY_ACCEPT_CONTENT": ["json"],
    "CELERY_TASK_SERIALIZER": "json",
    "CELERY_RESULT_SERIALIZER": "json",
    "CELERY_TASK_RESULT_EXPIRES": 60 * 60 * 24,
    "CELERY_ROUTES": {
        'celeryapp.tasks.add': {'queue': 'for_taska', 'routing_key': 'task_a'},
        'celeryapp.tasks.mul': {'queue': 'for_taskb', 'routing_key': 'task_b'},
        'celeryapp.scrapybrandgoods.get_good': {'queue': 'for_scrapybrand',
                                                'routing_key': 'for_scrapybrand'},

    },
    "CELERY_QUEUES": ["default", "for_taska", "for_taskb", "for_scrapybrand"],
}

if __name__ == '__main__':
    etcd_cluster_client = ConnectEtcdCluster(
        (('192.168.2.241', 2379), ('192.168.2.242', 2379), ('192.168.2.243', 2379)))
    con = etcd_cluster_client.con(ca_cert='ca.pem', cert_key='etcd-key.pem', cert_cert='etcd.pem')
    con.put('/celeryapp_config', json.dumps(config_list))

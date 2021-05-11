import json
import etcd3
import socket
import subprocess
from etcdclusterclient import ConnectEtcdCluster

def watch_worker():
    print('watching worker!')
    etcd_cluster_client = ConnectEtcdCluster(
        (('192.168.2.241', 2379), ('192.168.2.242', 2379), ('192.168.2.243', 2379)))
    con = etcd_cluster_client.con(ca_cert='ca.pem', cert_key='etcd-key.pem', cert_cert='etcd.pem')
    iterators, cancel = con.watch('/celeryapp_config')
    for event in iterators:
        cmd = r'supervisorctl -i restart celeryapp celeryappflow'
        status, output = subprocess.getstatusoutput(cmd)
        print(output)

if __name__ == '__main__':
    watch_worker()

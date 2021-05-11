import etcd3
import socket

class ConnectEtcdCluster(object):
    """
    (host=(('127.0.0.1', 4001), ('127.0.0.1', 4002), ('127.0.0.1', 4003)))
    """

    def __init__(self, hosts):
        self.hosts = hosts

    def con(self,port='2379',
           ca_cert=None, cert_key=None, cert_cert=None, timeout=None,
           user=None, password=None, grpc_options=None):
        try:
            for item in self.hosts:
                etcd_sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                Etcd_Result = etcd_sk.connect_ex((item[0],item[1]))
                if Etcd_Result == 0:
                    con=etcd3.client(item[0],item[1],ca_cert=ca_cert,cert_key=cert_key,cert_cert=cert_cert,timeout=timeout,user=user,password=password,grpc_options=grpc_options)
                    return con
            raise {'status_code': 0, 'data': "can't connect etcd...."}
        except Exception as e:
            raise {'status_code': 0, 'data': "can't connect etcd...."}

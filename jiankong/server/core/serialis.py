#coding:utf-8
import global_setting
from conf import hosts
import pickle

def host_config_serializer(host_ip):
    applied_services=[]
    configs={
             'services':{}
             }
    for group in hosts.monitored_groups:
        if host_ip in group.hosts:
            applied_services.extend(group.services)
        applied_services=set(applied_services)
    
    for service in applied_services:
        service=service() #实例化类  后面才能调用里面的name字段
        configs['services'][service.name]=[service.interval,
                                           service.plugin_name,
                                           ]
        return configs
def flush_all_host_configs_into_redis():
    applied_hosts = []
    redis =RedisHelper()
    for group in hosts.monitored_groups:
        applied_hosts.extend(group.hosts)
    applied_services=set(applied_services)
    for host_ip in applied_hosts:
        host_config=host_config_serializer(host_ip)
        key = 'HostConfig:%s' % host_ip
        redis.set(key,pickle.dumps(host_config))
    return True
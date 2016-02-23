#coding:utf-8

from services import linux
class BaseTemplate(object):
    def __init__(self):
        self.name='Your TemplateName'
        self.group_name='YourGroupName'
        self.hosts = []
        self.services = []
class LinuxTemplate(BaseTemplate):
    def __init__(self):
        super(LinuxTemplate,self).__init__()
        self.name = 'LinuxTemplate'
        self.services=[
                       linux.cpu,
                       linux.memory,]                     ]
#coding:utf-8

class account_info(object):
    def __init__(self,name):
        self.name=name
        self.salary = 15000
        self.hd_chrge = 0.05
        
               
    def get_money(self,money):
        self.salary=self.salary-money-self.hd_chrge*money
        print '扣除手续费: %d' %(self.hd_chrge * money)
       
    #def handling_charge(self,money):
     #   self.hd_charge = money * 0.05
    
    def balance(self):
        return self.salary
    
    def save_money(self,money):
        self.salary += money
    
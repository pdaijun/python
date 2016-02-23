#coding:utf-8
from django.utils.safestring import mark_safe
def int_page(page,default):
    try:
        page= int(page)
    except  :
        page = default 
    return page

class INIT_PAGE(object):
    '''
    '''
    #获取当前页数，总条数，间隔条目
    def __init__(self,crrut_page,count_data,pre_item=5):
        self.Crrut_Page=crrut_page
        self.Count_Data=count_data
        self.Pre_item=pre_item
    #算出一页的起始条目
    @property
    def Start(self):
        return (self.Crrut_Page-1)*self.Pre_item
    #算数一页的结束条目
    @property
    def End(self):
        return self.Crrut_Page*self.Pre_item
    
    #算出总页数
    @property
    def Count_Page(self):
        temp=divmod(self.Count_Data, self.Pre_item)
        if temp[1]==0:
            Count_page=temp[0]
        else:
            Count_page=temp[0]+1
        return Count_page


    #开始分页
    def Html_Page(self):    
        html_page=[]
        #定义首页 当页起始为1的时候为首页       
        first_html='<a href="/index/%d">首页</a>' %(1)
        #定义下一页，当前页加1
        if self.Crrut_Page < self.Count_Page:
            next_html='<a href="/index/%d">下一页</a>' %(self.Crrut_Page+1)
        else:
            next_html='<a href="/index/%d">下一页</a>' %(self.Crrut_Page)  
        html_page.append(first_html)
        html_page.append(next_html)  
        #定义显示多少个页码
        if self.Crrut_Page >5:
            begin_page=self.Crrut_Page-6
        else:
            begin_page=0
        end_page_temp=self.Crrut_Page+5 
        if end_page_temp < self.Count_Page:
            if end_page_temp >10:
                end_page=end_page_temp
            else:
                end_page=11
        else:
            end_page=self.Count_Page
        #for i in range(count_page):
        #定义页
        for i in range(begin_page,end_page):
            if self.Crrut_Page==i+1:
                a_html='<a class="selectd" href="/index/%d">%d</a>' %(i+1,i+1)
            else:
                a_html='<a href="/index/%d">%d</a>'%(i+1,i+1)
            html_page.append(a_html)
        #定义下一页
        if self.Crrut_Page > 1:
            top_html='<a href="/index/%d">上一页</a>' %(self.Crrut_Page-1)
        else:
            top_html='<a href="/index/%d">上一页</a>' %(self.Crrut_Page)
        end_html='<a href="/index/%d">尾页</a>' %(self.Count_Page)   
        html_page.append(top_html)
        html_page.append(end_html)
        pages=mark_safe(''.join(html_page))   
        return pages
from import_lib import *

scope_list = ['whoAreYou', 'eat_type', 'normal', 'child', 'dead', 'BMI', 'time', 'cart', 'store', 'bar', 'menu']
name = ''
# 1
order = {}
dic = {}
# 2
store_name = ""
flink = ""
ulink = ""
#3
User_Dict = {'Annie' : '1_3_yyt47e7sDQvCmsPbUfJd4byJFt8p3favwgQUTjHA' , 'Anderson' : '1NmlieN4u9w0Eju1LFJq580U7BpHGZaLM_hBui26Rfa4'}

def t(eng, chinese):
    return chinese if 'zh' in session_info.user_language else eng

def clear_scope(current):
    for scope in scope_list:
        if current not in scope_list:
            clear(scope)

def show_time():
    with use_scope('time', if_exist = 'remove'):
        clear_scope('time')
        now_now = datetime.now()
        #put_text(now_now.year, now_now.month, now_now.day, now_now.hour, now_now.minute)
        return [now_now.year, now_now.month, now_now.day, now_now.hour, now_now.minute]


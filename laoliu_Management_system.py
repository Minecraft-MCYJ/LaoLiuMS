#老六成绩管理系统，你值得拥有
#参考文献:422,262

import os
import time
import shutil
import json

print('System启动中...')

Path_Account = os.path.exists('Account')
if Path_Account == True:
    print('Account文件夹已找到！')
    time.sleep(1)
    print('所有账号:',end='')
    with open('Account\\list.txt',encoding='UTF-8') as f:
        Account = f.read()
        Account = Account.split('\n')
        for account in Account:
            time.sleep(0.5)
            print(''.join(account))
else:
    print('Account文件夹未找到，正在创建中...')
    os.makedirs('Account')
    with open('Account\\list.txt','w+',encoding='UTF-8') as f:
        f.write('')

title_msg = '''老六成绩管理系统，你值得拥有
1.登录账号
2.添加账号
3.删除账号
4.退出'''

print(title_msg)

while True:
    login_mode = input('请选择:')
    if login_mode == '1' or login_mode == '2' or login_mode == '3' or login_mode == '4':
        login_mode = int(login_mode)
        break
    else:
        continue
print('你的选择:',end='')
if login_mode == 1:
    print('登录账号')
elif login_mode == 2:
    print('添加账号')
elif login_mode == 3:
    print('删除账号')
elif login_mode == 4:
    exit()
time.sleep(1)

def main(admin=None):
    print(admin,'你好!',sep=',')
    with open(f'Account\\{admin}\\Information\\Information.json','r',encoding='UTF-8') as f:
        Information = json.load(f)
    print('帐号列表信息:',Information)
    while True:
        title = '''1.添加成绩
2.删除成绩
3.查询成绩
4.列出成绩
5.退出
6.更换账号'''
        print(title)
        input_ = input('请选择:')
        if input_ in ['1','2','3','4','5','6']:
            print('你的选择:',end='')
            if input_ == '1':
                while True:
                    print('添加成绩')
                    math = input('请输入数学成绩:')
                    chinese = input('请输入语文成绩:')
                    english = input('请输入英语成绩:')
                    name_ = input('请输入该学生姓名:')
                    cache = {'math':math,'chinese':chinese,'english':english}
                    Information[name_] = cache
                    print('json格式预览',Information,sep=':')
                    YORN = input('是否继续添加?[Y/任意一个键]:')
                    if YORN == 'Y' or YORN == 'y':
                        with open(f'Account\\{admin}\\Information\\Information.json','w+',encoding='UTF-8') as f:
                            json.dump(Information,f,indent=4,ensure_ascii=False)
                        continue
                    else:
                        with open(f'Account\\{admin}\\Information\\Information.json','w+',encoding='UTF-8') as f:
                            json.dump(Information,f,indent=4,ensure_ascii=False)
                        break
            elif input_ == '5':
                exit()
            elif input_ == '6':
                Ac = input('\n请输入切换的账号：')
                global Account
                if Ac in Account:
                    print(f'已找到该账号 <name:{Ac}>')
                    main(Ac)
                else:
                    print(f'未找到该账号 <name:{Ac}>')
            elif input_ == '2':
                print('删除成绩')
                print('所有成绩')
                for cache_name,cache in Information.items( ):
                    print('学生 :',cache_name,'  ','数学',cache['math'],'     ','语文',cache['chinese'],'     ','英语',cache['english'])
                popuser = input('请输入要删除的成绩(填写用户名):')
                try:
                    Information.pop(popuser)
                    with open(f'Account\\{admin}\\Information\\Information.json','w+',encoding='UTF-8') as f:
                        json.dump(Information,f,indent=4,ensure_ascii=False)
                    print('删除成功!')
                except:
                    print('此用户不存在!')
            elif input_ == '3':
                print('查询成绩')
                print('预览所有',Information,sep=':')
                name_ = input('请输入学生姓名:')
                try:
                    print(Information[name_])
                    cj = Information[name_]
                    print('学生 :',name_,'  ','数学',cj['math'],'     ','语文',cj['chinese'],'     ','英语',cj['english'])
                except:
                    print('未找到该学生!')
            elif input_ == '4':
                print('列出成绩')
                for cache_name,cache in Information.items( ):
                    print('学生 :',cache_name,'  ','数学',cache['math'],'     ','语文',cache['chinese'],'     ','英语',cache['english'])
            else:
                break
        else:
            print('暂无该选项')
            break

if login_mode == 3:
    delname = input('请输入要删除的账号名称:')
    Path_del = os.path.exists(f'Account\\{delname}')
    if Path_del == False:
        print('未创建该用户!')
    else:
        print('已找到该用户!')
        run_ = input('你确定吗?[按下任意键继续/N]')
        if run_ == 'N' or run_ == 'n':
            exit()
        else:
            pass
        with open('Account\\list.txt','r',encoding='UTF-8') as f:
            list_ = f.read()
        list_ = list_.split('\n')
        list_.remove(delname)
        with open('Account\\list.txt','w+',encoding='UTF-8') as f:
            for i in list_:
                f.write('\n')
                f.write(i)
        shutil.rmtree(f'Account\\{delname}')
        print('删除完毕!')
if login_mode == 2:
    name = input('请输入账号名称:')
    try:
        os.makedirs(f'Account\\{name}')
        os.makedirs(f'Account\\{name}\\Information')
    except FileExistsError:
        print(f'你已创建了这个账号了!<name:{name}>')
    else:
        with open(f'Account\\{name}\\{name}.txt','w+',encoding='UTF-8') as f:
            f.write(name)
        with open(f'Account\\{name}\\Information\\Information.json','w+',encoding='UTF-8') as f:
            f.write(r'{}')
        with open(f'Account\\list.txt','a',encoding='UTF-8') as f:
            f.write(name+'\n')
        print('账号创建完毕！')
        time.sleep(1)
        main(admin=name)
if login_mode == 1:
    user = input('请输入账号名:')
    if user in Account:
        print(f'已找到该用户!<name:{user}>')
        main(admin=user)
    else:
        print('尚未找到此用户,请先创建该用户!')
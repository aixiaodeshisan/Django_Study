#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件：views.py
@说明：跟接收浏览器请求，进行处理，返回页面相关。模型
@时间：2019/12/23 11:29:12
@作者：MrShiSan
@版本：1.1，引入mysql
@运行环境：Python3.5 + Django1.8.2
'''

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader,RequestContext

# Create your views here.
# 定义视图
''' TODO:查找视图过程
1. 在浏览器地址栏中输入url
2. 请求到网站后，获取url信息
3. 然后与编写好的URLconf逐条匹配
    3.1 如果匹配成功则调用对应的视图函数
    3.2 如果所有的URLconf都没有匹配成功，则返回404错误
'''
# def index(request):
#     # # 使用视图调用模板
#     # # 1.获取模板
#     # template=loader.get_template('booktest/index.html')
#     # # 2.定义上下文
#     # context=RequestContext(request,{'title':'图书列表','list':range(10)})
#     # # 3.渲染模板
#     # return HttpResponse(template.render(context))

#     # render(request,"路径","上下文字典")函数封装上述三操作，
#     # 1.定义上下文字典
#     context = {'title':'图书馆列表','list':range(10)}
#     # 2.remder 传参数调用模板（调用前端页面）
#     return render(request,"booktest/index.html",context)
#     pass

''' TODO:完整项目的搭建
    1.定义视图
    2.定义URLconf
    3.定义模板
'''
# from booktest.models import BookInfo

# # 首页展示所有图书
# def index(request):
#     # 查询所有图书
#     booklist = BookInfo.books.all()
#     # 将图书列表传到模板，然后渲染模板
#     return render(request,"booktest/index.html",{'booklist':booklist})
#     pass

# # 详细页
# def detail(request,bid):
#     # 根据图书编号对应图书
#     book = BookInfo.books.get(id = int(bid))
#     # 获得关联集合:查找book图书中的所有英雄信息,django中提供关联的操作方式
#     heros = book.heroinfo_set.all()
#     # 将图书信息传递到模板中，然后渲染模板
#     return render(request, 'booktest/detail.html', {'book':book,'heros':heros})

#     pass

''' @note 定义视图,增删改查mysql
'''

from datetime import date
from booktest.models import *
from django.db.models import F          # 调用F对象进行属性间的比较查询，F(属性名)
from django.db.models import Q          # 调用Q对象进行属性间的逻辑关系吧比较查询，Q(属性名__运算符=值)
from django.db.models import Sum        # 配合aggregate()过滤器调用聚合函数 求和
from booktest.models import AreaInfo    # 自关联对象

# 查询所有图书并显示
def index(request):
    ''' @note 在index视图中编写如下查询代码：
        实现sql中where的功能，调用过滤器filter()、exclude()、get()
        通过"属性名_id"表示外键对应对象的id值
            属性名称__比较运算符=值
        1) 查询等,exact：表示判等。
        2) 模糊查询
            contains：是否包含。
            startswith、endswith：以指定值开头或结尾。
        3) 空查询
            isnull：是否为null。
        4) 范围查询
            in：是否包含在范围内。
        5) 比较查询
            gt、gte、lt、lte：大于、大于等于、小于、小于等于。
            不等于的运算符，使用exclude()过滤器。
        6) 日期查询
            year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算。
    '''
    booklist = 0
    list = 0
    select_chose = 18       # 字段查询操作选择开关
    create_chose = 1        # 新建

    # 属性名称__比较运算符=值
    if select_chose == 1:                                                      # @remind 查询所有书籍
        list = BookInfo.books.all()
    elif select_chose == 2:     
        # list = BookInfo.objects.filter(id__exact=3)                          # @remind 默认objects属性，但是重写了BookInfo管理器位books                                              # 查询编号为1的图书。
        list = BookInfo.books.filter(id__exact=3)
    elif select_chose == 3:                                                    # @remind 查询书名包含'传'的图书。
        list = BookInfo.books.filter(btitle__contains='传')
    elif select_chose == 4:                                                    # @remind 查询书名以'部'结尾的图书
        list = BookInfo.books.filter(btitle__endswith='部')
    elif select_chose == 5:                                                    # @remind 查询书名不为空的图书。
        list = BookInfo.books.filter(btitle__isnull=False)
    elif select_chose == 6:                                                    # @remind 查询编号为1或3或5的图书
        list = BookInfo.books.filter(id__in=[1, 3, 5])
    elif select_chose == 7:                                                    # @remind 查询编号大于3的图书
        list = BookInfo.books.filter(id__gt=3)
    elif select_chose == 8:                                                    # @remind 查询编号不等于3的图书
        list = BookInfo.books.exclude(id=3)

        ''' @note 属性间比较,F对象
            两个属性怎么比较呢，用F对象，被定义在django.db.models中
        '''
    elif select_chose == 9:                                                    # 查询阅读量大于等于评论量的图书。
        list = BookInfo.books.filter(bread__gte=F('bcomment'))
    elif select_chose == 10:                                                   # 查询阅读量大于2倍评论量的图书。
        list = BookInfo.books.filter(bread__gt=F("bcomment")*2)
        
        ''' @note 属性间的逻辑关系，Q对象可以使用&、|连接，&表示逻辑与，|表示逻辑或。或必须用Q对象
            几种可以不用Q对象就能表示的逻辑关系
            （1）与：多个过滤器逐个调用表示逻辑与关系，同sql语句中where部分的and关键字。
        '''
    elif select_chose == 11:
        list = BookInfo.books.filter(bread__gt=20,id__lt=3)                   # 查询阅读量大于20，并且编号小于3的图书
        # 或用下述语句
        # list = BookInfo.books.filter(bread__gt=20).filter(id__lt=3)
    elif select_chose == 12:                                                    # 查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
        list = BookInfo.books.filter(Q(bread__gt=20) | Q(pk__lt=3))
    elif select_chose == 13:                                                    # 查询编号不等于3的图书。
        list = BookInfo.books.filter(~Q(id=3))    
    elif select_chose == 14:
        ''' @note 聚合函数包括：Avg，Count，Max，Min，Sum     
            使用aggregate()过滤器调用聚合函数   
            aggregate(Sum('bread'))
            返回值是一个字典类型：
                {'聚合类小写__属性名':值}
                如:{'sum__bread':3}
        ''' 
        
        list = BookInfo.books.aggregate(Sum('bread'))                         # 查询图书的总阅读量
    elif select_chose == 15:
        # 但使用count时一般不使用aggregate()过滤器。返回一个数字
        list = BookInfo.books.count()                                         # 查询图书总数
    elif select_chose == 16:
        ''' @note 查询集
        1.查询集表示从数据库中获取的对象集合，在管理器上调用某些过滤器方法会返回查询集
          查询集可以含有零个、一个或多个过滤器
          过滤器基于所给的参数限制查询的结果
          从Sql的角度，查询集和select语句等价，过滤器像where和limit子句。
        2.两大特性
          惰性执行：创建查询集不会访问数据库，直到调用数据时，才会访问数据库，
                   调用数据的情况包括迭代、序列化、与if合用。
          缓    存：使用同一个查询集，第一次使用时会发生数据库的查询，然后把结果缓存下来，
                   再次使用这个查询集时会使用缓存的数据。
        3.限制查询集
          可以对查询集进行取下标或切片操作，等同于sql中的limit和offset子句。
          注意：不支持负数索引。

        '''
        list=BookInfo.books.all()[0:2]                                            # 获取第1、2项，运行查看。
    elif select_chose == 17:
        ''' @note 关联查询
            1.通过对象执行关联查询
                在定义模型类时，可以指定三种关联关系，最常用的是一对多关系，
                    由一到多的访问语法：
                        b = BookInfo.books.get(id=1)
                        b.heroinfo_set.all()
                    由多到一的访问语法:
                        h = HeroInfo.books.get(id=1)
                        h.hbook
                    访问一对应的模型类关联对象的id语法:
                        hero.hbook_id
            2.通过模型类执行关联查询
                关联模型类名小写__属性名__条件运算符=值
                    如果没有"__运算符"部分，表示等于，结果和sql中的inner join相同。
                
        '''
        booklist = BookInfo.books.get(pk=2)                                           # 查询编号为2的图书。
        list = booklist.heroinfo_set.all()                                              # 获得图书的所有英雄
    elif select_chose == 18:  
        # 由多模型类条件查询一模型类数据:(多查一)
        #   关联模型类名小写__属性名__条件运算符=值 
        # 在这里重写了books方法                                                         
        list = BookInfo.books.filter(heroinfo__hcomment__contains='八')               # 查询图书，要求图书中英雄的描述包含'八'
    elif select_chose == 19:
        # 由一模型类条件查询多模型类数据: 语法如下：
        #    一模型类关联属性名__一模型类属性名__条件运算符=值
        list = HeroInfo.books.filter(hbook__btitle='天龙八部')                         # 查询书名为“天龙八部”的所有英雄。
    
    if create_chose == 1:
        # 调用模型类里面重写的数据库增加函数，ORM,测试成功
        # book = BookInfo.books.create_book("射雕英雄传",date(1980,5,1),14,30)
        list = BookInfo.books.all()
        pass
    ''' @note autidiHttpReqeust对象 //@HttpReqeust
        1.服务器接收到http协议的请求
        2.服务器根据报文创建HttpRequest对象
        3.视图的第一个参数必须是HttpRequest对象，即request
        4.django.http模块中定义了HttpRequest对象的API
            属性：(下面除非特别说明，属性都是只读的)
                path：一个字符串，表示请求的页面的完整路径，不包含域名和参数部分。
                method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'。
                    在浏览器中给出地址发出请求采用get方式，如超链接。
                    在浏览器中点击表单的提交按钮发起请求，如果表单的method设置为post则为post请求。
                encoding：一个字符串，表示提交的数据的编码方式。
                    如果为None则表示使用浏览器的默认设置，一般为utf-8。
                    这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值。
                GET：QueryDict类型对象，类似于字典，包含get请求方式的所有参数。
                    QueryDict对象
                        定义在django.http.QueryDict
                        HttpRequest对象的属性GET、POST都是QueryDict类型的对象
                        和字典不一样，处理一键多值情况，一个GET/POST 多个值
                            如果一个键同时拥有多个值将获取最后一个值
                            如果键不存在则返回None值，可以设置默认值进行后续处理
                        使用
                            dict.get('键',默认值)：方法get()：根据键获取值，只能获取最后一个值或默认值
                            getlist()：方法getlist()：根据键获取值，值以列表返回，可以获取指定键的所有值

                POST：QueryDict类型对象，类似于字典，包含post请求方式的所有参数。
                FILES：一个类似于字典的对象，包含所有的上传文件。
                COOKIES：一个标准的Python字典，包含所有的cookie，键和值都为字符串。
                session：一个既可读又可写的类似于字典的对象，表示当前的会话，只有当Django 启用会话的支持时才可用，详细内容见"状态保持"。
                运行服务器，在浏览器中浏览首页，可以在浏览器“开发者工具”中的Network看到请求信息
    '''
    # 1.输出 HttpReqeust对象 的path、encoding
    path_encode = 'path = %s,encoding = %s' % (request.path,request.encoding)
    return render(request,'booktest/index.html',{'list':list,'booklist':booklist,"path_encode":path_encode})       
    # return render(request,'404.html',{'list':list,'booklist':booklist}) 

# 2.输出 HttpReqeust对象 的method属性
def method_show(request):
    # 返回的是request对象方法属性
    return HttpResponse(request.method)

''' @note GET属性
    1.请求格式
        在请求地址末尾使用？，之后以“键=值”的格式拆分，多个键值对之间以＆连接
        http://www.itcast.cn/?a=10&b=20&c=python
        拆解请求参数
        a=10&b=20&c=python
    2.注意
        键是开发人员在编写代码时确定下来的
        值是根据数据生成的
'''
''' @note POST属性
    使用form表单请求时，方法方式为post继承发起post方式的请求，
    需要使用HttpRequest对象的POST属性接收参数，POST属性是一个QueryDict类型的对象。
'''
def show_reqarg(request):
    if request.method == 'GET':
        a = request.GET.get('a') #获取请求参数a
        b = request.GET.get('b') #获取请求参数b
        c = request.GET.get('c') #获取请求参数c
        # 开始调用
        return render(request, 'booktest/show_getarg.html', {'a':a, 'b':b, 'c':c})
    else:
        name = request.POST.get('uname') #获取name
        gender = request.POST.get('gender') #获取gender
        hobbys = request.POST.getlist('hobby') #获取hobby
        return render(request, 'booktest/show_postarg.html', {'name':name, 'gender':gender, 'hobbys':hobbys})
    
''' @note HttpResponse对象
    1.视图在接收请求并处理后，必须返回HttpResponse对象或子对象
      HttpRequest对象由Django创建
      但HttpResponse对象由开发人员创建
    2.属性
        content：表示返回的内容。
        charset：表示response采用的编码字符集，默认为utf-8。
        status_code：返回的HTTP响应状态码。
        content-type：指定返回数据的的MIME类型，默认为'text/html'。
    3.方法
        _init_：创建HttpResponse对象后完成返回内容的初始化。
        set_cookie：设置Cookie信息。
            set_cookie(key, value='', max_age=None, expires=None)
                cookie是网站以键值对格式存储在浏览器中的一段纯文本信息，用于实现用户跟踪。
                max_age是一个整数，表示在指定秒数后过期。
                expires是一个datetime或timedelta对象，会话将在这个指定的日期/时间过期。
                max_age与expires二选一。
                如果不指定过期时间，在关闭浏览器时cookie会过期。
        delete_cookie(key)：删除指定的key的Cookie，如果key不存在则什么也不发生。
        write：向响应体中写数据。
'''
# request是服务器自己生成的，但是HttpResponse对象得自己定义并返回
# 常见的3中定义过程：
# 1.直接返回数据
def index2(request):
    str='<h1>hello world</h1>'
    return HttpResponse(str)
# 2.调用模板
def index3(request):
    #加载模板
    t1=loader.get_template('booktest/index3.html')
    #构造上下文
    context=RequestContext(request,{'h1':'hello,正在调用模板进行HttpResponse响应'})
    #使用上下文渲染模板，生成字符串后返回响应对象
    return HttpResponse(t1.render(context))
# 3.调用模板简写函数render
def index4(request):
    return render(request, 'booktest/index4.html', {'h1': '正在调用简写模板进行HttpResponse响应'})

''' @note 子类JsonResponse
    1.在浏览器中使用javascript发起ajax请求时，返回json格式的数据,需要用子类JsonResponse来接受响应数据
      类JsonResponse继承自HttpResponse对象，被定义在django.http模块中，创建对象时接收字典作为参数。
        JsonResponse对象的content-type为'application/json'。
    2.jquery是javascripe的一个库
'''
from django.http import JsonResponse

# json1用于显示主页
def json1(request):
    return render(request,'booktest/json1.html')
# json2用于解析数据，并在前端页面上显示
def json2(request):
    return JsonResponse({'h1':'hello','h2':'world'})

# 创建新图书
def create(request):
    book=BookInfo()
    book.btitle = '流星蝴蝶剑'
    book.bpub_date = date(1995,12,30)
    book.save()
    #转向到首页
    return redirect('/')

''' @note 子类HttpResponseRedirect
    1.当一个逻辑处理完成后,不需要向客户端呈现数据,而是转回到其它页面
      如添加成功、修改成功、删除成功后显示数据列表
      而数据的列表视图已经开发完成，此时不需要重新编写列表的代码，而是转到这个视图就可以
      此时就需要模拟一个用户请求的效果
      从一个视图转到另外一个视图，就称为重定向。
    2.HttpResponseRedirect对象实现重定向功能，这个类继承自HttpResponse，
      被定义在django.http模块中，返回的状态码为302。
'''
from django.http import HttpResponseRedirect

# 定义重定义向视图，转向首页
def red1(request):
    return HttpResponseRedirect('/')
# 重定向简写函数redirect
from django.shortcuts import redirect

def red2(request):
    return redirect('/')

''' @note 状态保持
    1.背景
        浏览器请求服务器是无状态的。无状态指一次用户请求时，
        浏览器、服务器无法知道之前这个用户做过什么，每次请求都是一次新的请求。
        无状态的应用层面的原因是：浏览器和服务器之间的通信都遵守HTTP协议。
        根本原因是：浏览器与服务器是使用Socket套接字进行通信的，
        服务器将请求结果返回给浏览器之后，会关闭当前的Socket连接，
        而且服务器也会在处理页面完毕之后销毁页面对象。
    2.有时需要保存下来用户浏览的状态，比如用户是否登录过，浏览过哪些商品等。 
        实现状态保持主要有两种方式：
            在客户端存储信息使用Cookie。
                有时也用其复数形式Cookies
                指某些网站为了辨别用户身份、进行session跟踪而储存在用户本地终端上的数据（通常经过加密）
                流程:
                    服务器产生Cookie，
                    发送给User_Agen（一般是浏览器）
                    浏览器会将Cookie的key/value保存到某个目录下的文本文件内
                    下次请求同一网站时就发送该Cookie给服务器（前提是浏览器设置为启用cookie）
                        Cookie的特点：
                            Cookie以键值对的格式进行信息的存储。
                            Cookie基于域名安全，不同域名的Cookie是不能互相访问的，如访问itcast.cn时向浏览器中写了Cookie信息，
                            使用同一浏览器访问baidu.com时，无法访问到itcast.cn写的Cookie信息。
                            当浏览器请求某网站时，会将浏览器存储的跟网站相关的所有Cookie信息提交给网站服务器。
            在服务器端存储信息使用Session。
'''
import json
''' @note 解决Django中set_cookie()不能存储中文字符串问题
    json.dumps(username):把字符串username转换为python程序可识别的二进制数据
    json.loads(username):把python中username二进制数据转为json字符串格式
'''
# 设置Cookie
def cookie_set(request):
    response = HttpResponse("<h1>设置Cookie，请查看响应报文头</h1>")
    # 中文出现存不进去cookie
    response.set_cookie('my_cookie', json.dumps('你好'))
    return response
# 读取Cookie
def cookie_get(request):
    response = HttpResponse("读取Cookie，数据如下：<br>")
    if 'my_cookie' in request.COOKIES:
        response.write('<h1>' + json.loads(request.COOKIES['my_cookie']) + '</h1>')
    return response

''' @note Session
    1.对于敏感、重要的信息，要储在服务器端
      如用户名、余额、等级、验证码等信息。
          在服务器端进行状态保持的方案就是Session。
    2.Sesion 依赖于 Cookie
        所有请求者的Session都会存储在服务器中，服务器如何区分请求者和Session数据的对应关系呢？
            使用Session后,在Cookie中存储一个sessionid的数据
            每次请求时浏览器都会将这个数据发给服务器
            服务器在接收到sessionid后,会根据这个值找出这个请求者的Session
        存储Session时，键与Cookie中的sessionid相同
        值是开发人员设置的键值对信息，进行了base64编码，过期时间由开发人员设置。
    3.通过HttpRequest对象的session属性进行会话的读写操作
        写：
            request.session['键']=值
        读：
            request.session.get('键',默认值)
        清除：
            request.session.clear()     清除所有session，在存储中删除值部分。
            request.session.flush()     清除session数据，在存储中删除session的整条数据。
            del request.session['键']   删除session中的指定键及值，在存储中只删除某个键及对应的值。
        设置会话的超时时间，如果没有指定过期时间则两个星期后过期：
            request.session.set_expiry(value)
                如果value是一个整数，则为s
                如果value为0，那么用户会话的Cookie将在用户的浏览器关闭时过期。
                如果value为None，那么会话永不过期。  
        session能存储中文字符串问
'''
# 写session
def session_test(request):
    request.session['h1']='你好'
    return HttpResponse('写session')

# 读session
def session_read_test(request):
    h1=request.session.get('h1')
    return HttpResponse(h1)

# 删除session
def session_delete_test(request):
    delete_chose = 3
    if(delete_chose == 1):
        # 逐条键及值的删除,但是并没有同步到数据库
        del request.session['h1']
    elif(delete_chose == 2):
        # 把所有的session键值删除，清除session中的缓存数据（不管缓存与数据库的同步）
        request.session.clear()
    elif(delete_chose == 3):
        # 把所有的session键值删除,将session的缓存中的数据与数据库同步
        request.session.flush()

    return HttpResponse('ok')

''' @note 使用Redis存储Session
    1.会话还支持文件、纯cookie、Memcached、Redis等方式存储，下面演示使用redis存储。
        pip install django-redis-sessions==0.5.6
    2.Redis的的是完全开源免费的，遵守BSD协议，是一个高性能的键值数据库。是当前最热门的的的NoSql数据库之一，也被人们称为数据结构服务器。
'''
def session_redis_test(request):
    request.session['h1']='hello'
    return HttpResponse('ok')

''' @note 模板语言
    1.变量(不能以下划线开头)
        {{变量}}
    2.标签
        {%代码段%}
            1.for标签语法：
                {%for item in 列表%}
                循环逻辑
                {{forloop.counter}}表示当前是第几次循环，从1开始
                {%empty%}
                列表为空或不存在时执行此逻辑
                {%endfor%}    
            2.if标签语法：
                {%if ...%}
                逻辑1
                {%elif ...%}
                逻辑2
                {%else%}
                逻辑3
                {%endif%}
            3.比较运算符：
                ==、!=、<、>、<=、>=
            4.布尔运算符：
                and、or、not
    3.过滤器
        语法：（变量|过滤器:参数）
            用管道符号|来应用过滤器
            用于进行计算、转换操作
            可以使用在变量、标签中
            如果过滤器需要参数，则使用冒号:传递参数
                常见参数设定：
                    长度length，返回字符串包含字符的个数，或列表、元组、字典的元素个数。
                    默认值default，如果变量不存在时则返回默认值。
                       data|default:'默认值'
                    日期date，用于对日期类型的值进行字符串格式化，常用的格式化字符如下：
                        value|date:"Y年m月j日  H时i分s秒"
                        {{book.bpub_date|date:"Y-m-j"}}
                            Y表示年，格式为4位，y表示两位的年。
                            m表示月，格式为01,02,12等。
                            d表示日, 格式为01,02等。
                            j表示日，格式为1,2等。
                            H表示时，24进制，h表示12进制的时。
                            i表示分，为0-59。
                            s表示秒，为0-59。
    4.自定义过滤器
        过滤器就是python中的函数，，注册后就可以在模板中进行过滤器使用
'''

def temp_var(request):
    dict={'title':'字典键值'}
    book=BookInfo()
    book.btitle='对象属性'
    context={'dict':dict,'book':book}
    return render(request,'booktest/temp_var.html',context)

def temp_tags(request):
    context={'list':BookInfo.books.all()}
    return render(request,'booktest/temp_tag.html',context)

def temp_filter(request):
    context={'list':BookInfo.books.all()}
    return render(request,'booktest/temp_filter.html',context)

''' @note 模板继承
    1.模板继承和类的继承含义一样，主要为了提高代码重用
        典型应用：网站的头部、尾部信息。
    2.父模板
        如果发现在多个模板中某些内容相同，那就应该把这段内容定义到父模板中
            标签block：用于在父模板中预留区域，留给子模板填充差异性的内容，名字不能相同
                      为了更好的可读性，建议给endblock标签写上名字，这个名字与对应的block名字相同
                {%block 名称%}
                预留区域，可以编写默认内容，也可以没有默认内容
                {%endblock  名称%}
    3.子模板
        标签extends：继承，写在子模板文件的第一行。
            {% extends "父模板路径"%}

'''
# 模板继承测试
def temp_inherit(request):
    context={'title':'模板继承','list':BookInfo.books.all()}
    return render(request,'booktest/temp_inherit.html',context)
''' @note HTML转义
    1.模板对所有传递的文字进行输出时，并在以下字符自动转义。
        < --- &lt
        > --- &gt
        ' --- &#39
        " --- &quot
        & --- &amp
    2.转义
        过滤器escape可以实现对变量的html转义，默认模板就会转义，一般省略：
            {{t1|escape}}
        关闭转义
            {{data|safe}}
        标签autoescape：设置一段代码都局部转义，接受on，off参数。
            on开启，off关闭
            {%autoescape off%}
            ...
            {%endautoescape%}
        弦字面值
            对于在模板中硬编码的html串联，不会转义。
'''
def html_escape(request):
    context={'content':'<h1>hello world</h1>'}
    return render(request,'booktest/html_escape.html',context)

''' @note CSRF
    1.全拼为Cross Site Request Forgery，译为跨站请求伪造
    2.CSRF指攻击者盗用了你的身份，以你的名义发送恶意请求
    3.CSRF能够做的事情包括：以你名义发送邮件，发消息，盗取你的账号，甚至于购买商品，
      虚拟货币转账......造成的问题包括：个人隐私泄露以及财产安全。
    4.安全编程的几点重要原则
        重要信息如金额、积分等，采用POST方式传递
        启用CSRF中间件，默认启用
        在form表单中post提交时加入标签csrf_token
    5.当启用中间件并加入标签csrf_token后，会向客户端浏览器中写入一条Cookie信息，
      这条信息的值与隐藏域input元素的value属性是一致的，提交到服务器后会先由csrf中间件进行验证，
      如果对比失败则返回403页面，而不会进行后续的处理。
'''
# 创建视图login，login_check, post和post_action
def login(reqeust):
    return render(reqeust, 'booktest/login.html')

def login_check(request):
    username = request.POST.get('username') #获取用户名
    password = request.POST.get('password') #获取密码

    # 校验
    if username == 'smart' and password == '123':
        # 注意在进行保存进入数据库的时候务必保证要数据库服务器是打开的，否则会报500错误
        request.session['username']   = username   #记住登录用户名
        request.session['islogin'] = True          #判断用户是否已登录
        return redirect('/post/')
    else:
        return redirect('/login/')

def post(request):
    return render(request, 'booktest/post.html')

def post_action(request):
    if request.session['islogin']:
        username = request.session['username']
        return HttpResponse('用户'+username+'发了一篇帖子')
    else:
        return HttpResponse('发帖失败')

''' @note 验证码
    1.在用户注册、登录页面，为了防止暴力请求，可以加入验证码功能，
      如果验证码错误，则不需要继续处理，可以减轻业务服务器、数据库服务器的压力。
        安装包Pillow3.4.1。
    2.过程
      随机生成字符串后存入session中，用于后续判断
      视图返回mime-type为image/png
'''
# 以下代码中用到了Pillow中的：Image、ImageDraw、ImageFont对象及方法。
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO

# 绘制验证码
def verify_code(request):
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    # bgcolor = (random.randrange(90, 100), random.randrange(
    #     20, 100), 255)
    bgcolor = (255,255,255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(100, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    buf = BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

# 调用验证码
def verify_show(request):
    return render(request,'booktest/verify_show.html')

# 开始验证
def verify_yz(request):
    yzm = request.POST.get('yzm')
    verifycode = request.session['verifycode']
    if yzm == verifycode:
        response=HttpResponse('ok')
        # return render(request,'booktest/index.html',{'yzm':yzm,'verifycode':verifycode})
    else:
        response = HttpResponse('no')
        # return render(request,'booktest/index.html',{'yzm':yzm,'verifycode':verifycode})
    return response


''' @note 反向解析
    1.背景
        随着功能的增加会出现更多的视图，可能之前配置的正则表达式不够准确
        于是就要修改正则表达式，但是正则表达式一旦修改了，之前所有对应的超链接都要修改
        麻烦，而且可能还会漏掉一些超链接忘记修改，所以反向解析应运而生
    2.步骤
        1）在test1/urls.py中为include定义namespace属性。
            url(r'^',include('booktest.urls',namespace='booktest')),
        2）在booktest/urls.py中为url定义name属性，并修改为fan2。
            url(r'^fan2/$', views.fan2,name='fan2'),
        3）在模板中使用url标签做超链接，此处为templates/booktest/fan1.html文件
        4）回到浏览器中，后退，刷新，查看源文件如下图，两个链接地址一样。
        5) 此时可以随便更改正则，都不会影响更改链接了
        6）反向解析也可以应用在视图的重定向中
            from django.shortcuts import redirect
            from django.core.urlresolvers import reverse

            return redirect(reverse('booktest:fan2'))
    3.总结：
        在定义url时，需要为include定义namespace属性，为url定义name属性，使用时，
        在模板中使用url标签，在视图中使用reverse函数，根据正则表达式动态生成地址，减轻后期维护成本。
'''
def fan1(request):
    return render(request,'booktest/fan1.html')

def fan2(request):
    return HttpResponse('fan2')

''' @note URL中的参数（位置、关键字参数）
    1.有些url配置项正则表达式中是有参数的，那么如何传递参数。
    2.
'''
from django.core.urlresolvers import reverse
# 传递位置参数
def fan3(request, a, b):
    return HttpResponse(a+b)
# 调用重定向进行反向解析
def fan4(request):
    return redirect(reverse('booktetst:fan3', args=(4,3)))
# 关键字参数,主要区别在于正则表达式上
def fan5(request, id, age):
    return HttpResponse(id+age)

# 调用重定向进行反向解析
def fan51(request):
    return redirect(reverse('booktest:fan5',kwargs={'id':100,'age':18}))
''' @todo 静态文件的处理
    1. 项目中的CSS、图片、js都是静态文件
        一般会将静态文件放到一个单独的目录中，以方便管理
        在html页面中调用时，也需要指定静态文件的路径，Django中提供了一种解析的方式配置静态文件路径。
        静态文件可以放在项目根目录下，也可以放在应用的目录下，由于有些静态文件在项目中是通用的，所以推荐放在项目的根目录下，方便管理。
'''
def static_test(request):
    return render(request,'booktest/static_test.html')

''' @todo 中间件视图调用
'''

def mid_test(request):
    print('======mid_test======')
    # @audit-ok 专门出现异常并测试自定义异常中间件，测试成功
    # raise Exception('自定义异常')
    return render(request,'booktest/mid.html')
    pass
# 逻辑删除指定编号的图书
def delete(request,id):
    book=BookInfo.books.get(id=int(id))
    book.delete()
    # 转向到首页
    return redirect('/')

# 查询广州市的信息
def area(request):
    area = AreaInfo.books.get(pk=440100)
    return render(request, 'booktest/area.html', {'area': area})

# 位置参数
# def show_arg(request,id):
#     return HttpResponse('show_arg %s'%id)

# 关键字参数,必须要有一个参数名为id1，否则报错
def show_arg(request,id1):
    return HttpResponse('show_arg %s'%id1)

# 全局403、404、500错误自定义页面显示
from django.shortcuts import render_to_response

# 页面找不到
def page_not_found(request):
    # 一次性地载入某个模板文件，渲染它，然后将此作为 HttpResponse返回。
    return render_to_response('404.html')

# 服务器错误
def page_error(request):
    return render(request, '500.html')

# 禁止访问页面
def permission_denied(request):
    return render(request, '403.html')

# @note 自定义表单开始上传图片
def pic_upload(request):
    return render(request,'booktest/pic_upload.html')

# @note 创建视图pic_handle，用作接收表单保存图片,这里只是完成图片并保存上传的代码,
# @audit-ok 需要保存数据到表中需要在modle中创建PicTest对象完成保存
from django.conf import settings
from django.http import HttpResponse

def pic_handle(request):
    f1 = request.FILES.get('pic')
    fname = '%s/booktest/%s'%(settings.MEDIA_ROOT,f1.name)
    with open(fname,'wb') as pic:
        for c in f1.chunks():
            pic.write(c)
    return HttpResponse('OK')

# @note 在html显示图片，根据数据库中保存的上传路径显示
def pic_show(request):
    pic = PicTest.objects.get(id=1)
    context = {'pic':pic}
    return render(request,'booktest/pic_show.html',context)

''' @todo Django数据分页
    1.Django提供了数据分页的类，
        这些类被定义为django / core / paginator.py中。
        类Paginator用于对列进行页面n条数据的分页运算。
    2.Paginator类实例对象
        方法_ init_（列表，int）：返回分页对象，第一个参数为列表数据，第二个参数为每页数据的条数。
        
        属性count：返回对象总数。
        属性num_pages：返回页面总数。
        属性page_range：返回页码列表，从1开始，例如[1、2、3、4]。

        方法page（m）：返回Page类实例对象，表示第m页的数据，下标以1开始。
    3.Page类实例对象
        调用Paginator对象的page（）方法返回Page对象，不需要手动构造。
        属性object_list：返回当前页对象的列表。
        属性编号：返回当前是第几页，从1开始。
        属性paginator：当前页面对应的Paginator对象。
        方法has_next（）：如果有下一页返回True。
        方法has_previous（）：如果有上一页返回True。
        方法len（）：返回当前页面对象的个数。
'''
from django.core.paginator import Paginator
from booktest.models import AreaInfo
...
# @todo 参数pIndex表示：当前要显示的页码
def page_test(request,pIndex):
    # 查询所有的地区信息
    list1 = AreaInfo.objects.filter(aParent__isnull=True)
    # 将地区信息按一页10条进行分页
    p = Paginator(list1, 10)
    # 如果当前没有传递页码信息，则认为是第一页，这样写是为了请求第一页时可以不写页码
    if pIndex == '':
        pIndex = '1'
    # 通过url匹配的参数都是字符串类型，转换成int类型
    pIndex = int(pIndex)
    # 获取第pIndex页的数据
    list2 = p.page(pIndex)
    # 获取所有的页码信息
    plist = p.page_range
    # 将当前页码、当前页的数据、页码信息传递到模板中
    return render(request, 'booktest/page_test.html', {'list': list2, 'plist': plist, 'pIndex': pIndex})

''' Django中使用jquery的ajax进行数据交互
    1.query框架中提供了$.ajax、$.get、$.post方法，用于进行异步交互，
        由于Django中默认使用CSRF约束，推荐使用$.get。
'''
from django.http import JsonResponse

# @todo 提供显示下拉列表的控件，供用户操作
def area1(request):
    return render(request,'booktest/area1.html')

# @todo 获取省信息
def area2(request):
    # 获取省名不为空的所有数据
    list = AreaInfo.objects.filter(aParent__isnull=True)
    list2 = []
    for item in list:
        list2.append([item.id, item.atitle])
    return JsonResponse({'data': list2})

# @todo 根据编号获取对应的子级信息,如果传递的是省编号则获取市信息，如果传递的是市编号则获取区县信息。
def area3(request, pid):
    list = AreaInfo.objects.filter(aParent_id=pid)
    list2 = []
    for item in list:
        list2.append([item.id, item.atitle])
    return JsonResponse({'data': list2})

''' @todo Django第三方包的测试
    1.第三方库
        富文本编辑器
            即可通过富文本编辑器，网站的编辑人员能够使用offfice一样编写出漂亮的，
            所见即所得的页面。此处以tinymce为例，其他富文本编辑器的使用也是类似的。
                pip install django-tinymce==2.6.0

        全文检索
        发送邮件
        celery
    2.布署
        当项目开发完成后，需要将代码放到服务器上，这个过程称为布署，
        服务器上需要有一个运行代码的环境，这个环境一般使用uWSGI+Nginx。
'''

def third_pack_test(request):
    return render(request,'booktest/third_party_pack.html')

# @note 自定义视图使用富文本编辑器
def editor(request):
    return render(request, 'booktest/editor.html')

''' @note 富文本编辑器内容的显示
    1.通过富文本编辑器产生的字符串是包含html的，在模板中显示字符串时，默认会进行html转义，
        如果想正常显示需要关闭转义：
            方式一：过滤器安全
            方式二：标签自动转义关闭
'''

def show_tinymce(request):
    goods=GoodsInfo.objects.get(pk=1)
    context={'g':goods}
    return render(request,'booktest/show_tinymce.html',context)


''' @note 使用全文检索（第三方库）
    1.按照配置，在管理管理中添加数据后，会自动为数据创建索引，可以直接进行搜索，可以先创建一些测试数据。
'''
def query(request):
    return render(request,'booktest/query.html')

# @note 发送邮件(第三方，以XXX.@160.com),Django的中内置了邮件发送功能
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
...
def send(request):
    msg='<a href="a href="http://www.baidu.com" target="_blank">点击激活</a>'
    send_mail('注册激活','',settings.EMAIL_FROM,
              ['z2607293749@163.com'],
              html_message=msg)
    return HttpResponse('ok')

''' @note-ok Celery-分布式任务类别
    1.情景：用户发起request，并等待response返回。在这些views中，可能需要执行一段耗时的程序，
        那么用户就会等待很长时间，造成不好的用户体验，比如发送邮件、手机验证码等
    2.celeryz主要解决：将耗时的程序放到celery中执行
    3.celery名词：
        任务task：就是一个Python函数。
        队列queue：将需要执行的任务加入到队列中。
        工人worker：在一个新进程中，负责执行队列中的任务。
        代理人broker：负责调度，在布置环境中使用redis。
'''

import time
from booktest import tasks

def sayhello(request):
    # @audit-ok 测试
    print('hello ...')
    time.sleep(2)
    print('world ...')
    return HttpResponse("hello world")
    # @audit-ok 调用任务task模块
    tasks.sayhello.delay()
    return HttpResponse("hello world")

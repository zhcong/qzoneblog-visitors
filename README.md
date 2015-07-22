#qzoneblog-vistior
###功能
***
这是记录每条说说访问者的脚本程序，每个一段时间将说说的访问者记录到visitors.log这个文件中。
###键盘输入
***
    QQ number
你的QQ号码

    QQ password
你的QQ密码

    blog number(blog number,qq number)
说说ID，如果你监视的是他人的说说，还需要他/她的QQ号码，半角逗号隔开；如果监视的仅仅是自己的说说，只需输入说说ID即可。至于说说ID，需要使用F12开发者工具找到形如"462a993d41acaf556fc40320"的字符串

    Pause(seconds, at last 15s)
每次获得数据的间隔时间，单位秒，由于qq的接口响应时间过慢，最少15秒(可以修改源代码)
###错误
***
因为每次只能得到6条数据，如果短时间内访问量巨大，会使得许多访客无法被记录
###感谢
***
>http://www.jianshu.com/p/4217d8f3574b
>

主要是这里提供了QQ空间的登录代码，在此感谢
>http://g.qzone.qq.com/cgi-bin/friendshow/cgi_get_visitor_single?uin=QQ号&appid=311&blogid=说说ID&ref=qzfeeds&beginNum=1&param=说说ID
>

这是得到访问者的接口
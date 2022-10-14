#内置字符串处理方法
s="Python"
s.lower()#全部小写
s.upper()#全部大写


s1="广东 培正 学院"
s1.split()#用空格做划分
s1.split("培")#用”培“做划分


s2="qwertyqwertyqwerty"
s2.count("e")#统计e的个数
s2.replace("e","**")#把e用**代替


s3="python"
s4=s3.center(20,"*")#两边补星号，少于字符串宽度不改变
s4.strip("*")#两边去掉


s5="12345"
"%",join(s5)#用%分割



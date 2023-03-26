A = "The society of the 21st century is a product of informationization,digitization and networking. With the rapid development of the Internet, in order tointegrate many Internet applications into people's daily life, the online orderingsystem, as an online ordering method, provides A more convenient eating experience.In this graduation project, most of the system interface uses JSP language for designand processing, and HTML language is added to the interface design to make the pagemore beautiful and harmonious, and then the JavaScript scripting language is used toprocess the pages in the system to make the page more beautiful and harmonious. Theeffect presented is more beautiful and simple. Regarding the design of themanagement function of the system, that is, the background, Servlet is used to handlethe interactive implementation in the system, and the programming is applied toJavaSE, which supports the development of Java Web services, and involves JDBCconnection among 13 core technologies of JavaEE. Database, JSP simplifies thecreation process of system pages and maintains the website, the database selects the MySQL database commonl used in class."
B = "The society of the 21st century is a product of informationization,digitization and networking. With the rapid development of the Internet, in order tointegrate many Internet applications into people's daily life, the online orderingsystem, as an online ordering method, provides A more convenient eating experience.In this graduation project, most of the system interface uses JSP language for designand processing, and HTML language is added to the interface design to make the pagemore beautiful and harmonious, and then the JavaScript scripting language is used toprocess the pages in the system to make the page more beautiful and harmonious. Theeffect presented is more beautiful and simple. Regarding the design of themanagement function of the system, that is, the background, Servlet is used to handlethe interactive implementation in the system, and the programming is applied toJavaSE, which supports the development of Java Web services, and involves JDBCconnection among 13 core technologies of JavaEE. Database, JSP simplifies thecreation process of system pages and maintains the website, the database selects the MySQL database commonl used in class."
C = "在浏览器中输入pubmed，打开pubmed网页。进入到pubmed官网首页后，在搜索框中输入关键词，点击search进行查找。在左边的工具栏中进行选择，以便缩小范围方便查找。论文下面如果出现Free article，则表示该文献是免费下载使用的；其他情况则需要购买服务。如果需要下载则点击标题，进入文章的主页面。点击Full text links按钮，再点击article tools，再点击Download Pdf进行下载即可。相关信息MEDLINE是权威的文摘类医学文献数据库之一，1996年起向公众开放。而PubMed是互联网上使用最广泛的免费MEDLINE检索工具，是美国国家医学图书馆所属的国家生物技术信息中心于2000年4月开发的一个基于WEB的生物医学信息检索系统，也是NCBI Entrez数据库查询系统中的一个。PubMed数据库包含超过3200万篇生物医学文献和摘要。不提供期刊文章的全文，但是通常会附有指向全文的链接。PubMed系统的特征工具栏提供辅助检索功能、侧栏提供其它检索如期刊数据库检索、主题词数据库检索和特征文献检索。提供原文获取服务免费提供题录和文摘，可与提供原文的网址链接，提供检索词自动转换匹配，操作简便、快捷。本文到此结束，希望对大家有所帮助。"
list1 = A.split()
for test1 in list1:
    print(test1, end=" | ")
count = list1.count("is")
print("\n")
print(count)
print("\n")
tuple2 = tuple(B.split())
for test2 in tuple2:
    print(test2, end=" ")
print()

for i in C:
    print(i, end=" | ")
print()
count2 = C.count("在")
print(count2)




print()
print("=" * 300)

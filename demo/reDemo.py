#!/user/bin/python
# -*- coding:utf-8 -*-

import re




if __name__=='__main__':
    print re.match('ni da ye', 'ni da ye de').span()
    print re.match('ni da ye','wo ri ni da ye')

    line = "Cats are smarter than dogs"

    matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

    if matchObj:
        print "matchObj.group() : ", matchObj.group()
        print "matchObj.group(1) : ", matchObj.group(1)
        print "matchObj.group(2) : ", matchObj.group(2)
    else:
        print "No match!!"

    phone = "2004-959-559 # 这是一个国外电话号码"

    # 删除字符串中的 Python注释
    num = re.sub(r'#.*$', "", phone)
    print "电话号码是: ", num

    # 删除非数字(-)的字符串
    num = re.sub(r'\D', "", phone)
    print "电话号码是 : ", num
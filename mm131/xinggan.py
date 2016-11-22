import urllib2
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

count = 21443

for i in xrange(54,82):
    print 'page --> %d -  start' % i
    root = ''
    if i == 1:
        root = 'http://www.mm131.com/xinggan/'
    else:
        root = 'http://www.mm131.com/xinggan/list_6_%d.html' % i
    print(root)

    req = urllib2.urlopen(root)
    html_content = req.read()

    linkPattern = re.compile(r'http://www.mm131.com/xinggan/\d{1,6}\.html')
    list_urls = linkPattern.findall(str(html_content))
    print list_urls[0:len(list_urls) - 11]
    print "page  %d has %d pic list " % (i, len(list_urls[0:len(list_urls)-11]))

    for k in range(0, len(list_urls) - 11):
        page = list_urls[k]
        print page

        try:
            page_req = urllib2.urlopen(page)
            if req.getcode()==200:
                page_buf = page_req.read()
                page_urls = re.findall(r'\d{1,6}_\d{1,3}\.html', page_buf)
                print "page  %d de di  %d pic list has %d pic" % (i, k+1,len(page_urls)-1)
                print page_urls

                # for html_url in page_urls:
                # len(page_urls) - 1
                for j in range(0, len(page_urls) - 1):
                    url = ''
                    if j == 0:
                        url = page
                    else:
                        url = 'http://www.mm131.com/xinggan/' + page_urls[j]
                    print url

                    try:
                        html_req = urllib2.urlopen(url)

                        if req.getcode()==200:
                            html_buf = html_req.read()
                            pat = re.compile(r'<img alt="(\S*)" src="(\S*)"')
                            pic_def = pat.findall(str(html_buf))
                            pat = re.compile(r'http://img1.mm131.com/.*.jpg')
                            pic_urls = pat.findall(str(pic_def))
                            print pic_urls

                            for pic_url in pic_urls:
                                path = 'F:\sexy\mm131\inggan'
                                isExists = os.path.exists(path)
                                if not isExists:
                                    os.makedirs(path)
                                    print path + 'create success'

                                pic = urllib2.urlopen(pic_url)
                                buf = pic.read()

                                count = count + 1
                                f = open(path + '/' + str(count) + '.jpg', "wb")
                                f.write(buf)
                                f.close()
                                print "page  %d de di  %d pic list de di %d pic craw sucess" % (i, k+1, j+1)
                                print (count)

                        else:
                            print 'open pic html fail'
                    except:
                        print 'pic craw _ except'

            else: print 'open one list fail'
        except:
            print 'list craw except'

print 'page --> %d -  end' % i
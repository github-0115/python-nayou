import urllib2
import re
import os
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

count = 0

for i in xrange(1,30):
    print 'page --> %d -  start' % i
    root = 'http://www.ivrfans.cn/xinggan/list_8_%d.html' % i
    req = urllib2.urlopen(root)
    html_content = req.read()

    list_urls = re.findall(r'/xinggan/.+\.html', html_content)
    print list_urls

    for list_url in list_urls:
        page = 'http://www.ivrfans.cn' + list_url
        print page

        try:
            page_req = urllib2.urlopen(page)
            if req.getcode()==200:
                page_buf = page_req.read()
                page_urls = re.findall(r'/xinggan/.+/\d{5}_\d{1,3}\.html', page_buf)
                print len(page_urls)
                print page_urls

                for html_url in page_urls[3:len(page_urls)-1]:
                    url = 'http://www.ivrfans.cn' + html_url
                    print url
                    try:
                        html_req = urllib2.urlopen(url)

                        if req.getcode()==200:
                            html_buf = html_req.read()
                            pat = re.compile(r'<img class="petImg" src="(\S*)"')
                            pic_urls = pat.findall(html_buf)
                            print pic_urls

                            for pic_url in pic_urls:
                                path = '/media/deepir/DATA/func/xinggan'
                                isExists = os.path.exists(path)
                                if not isExists:
                                    os.makedirs(path)
                                    print path + ' create success'

                                f = open(path+'/'+str(time.time())+'.jpg',"wb")
                                req = urllib2.urlopen(pic_url)
                                buf = req.read()
                                f.write(buf)
                                f.close()
                                count = count + 1
                                print count

                        else:
                            print 'fail'
                    except:
                        print 'craw _ except'


            else: print 'fail'
        except:
            print 'craw except'

    print 'page --> %d -  end' % i


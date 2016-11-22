import urllib2
import re
import os
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

count = 0

for i in xrange(0,61):
    print 'page --> %d -  start' % i
    root = 'http://www.ivrfans.cn/nvyou/list_6_%d.html' % i
    req = urllib2.urlopen(root)
    html_content = req.read()

    list_urls = re.findall(r'/nvyou/.+\.html', html_content)
    print list_urls

    for list_url in list_urls:
        page = 'http://www.ivrfans.cn' + list_url
        print page

        try:
            page_req = urllib2.urlopen(page)
            if req.getcode()==200:
                page_buf = page_req.read()
                page_urls = re.findall(r'/nvyou/.+\/.+\.html', page_buf)
                print len(page_urls)
                print page_urls

                for html_url in page_urls:
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
                                path = '/home/deepir/sexy/'+str(i)
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


    # for html_url in listurl[:1]:
    #     urls =html_url.split('.')
        # for j in xrange(3, 4):
        #     print j
        #     a = 'http://www.ivrfans.cn'+urls[0]+'_%d.html' % j
        #     print a
        #     req = urllib2.urlopen(a)
        #
        #     if req.getcode()==200:
        #         print req.code
        #     else:
        #         print 'fail'
        #     buf = req.read()
        #
        #     page_urls = re.findall(r'/nvyou/.+\/.+\.html', buf)

            # pic_urls = re.findall(r'http:.+\.jpg',buf)
            #
            # # pic_urls = re.findall(r'/nvyou/.+\/.+\.html', buf)
            # print pic_urls
            # print len(pic_urls)
            #
            # j = 0
            # for pic_url in pic_urls:
            #     f = open('/home/deepir/sexy/test/'+str(time.time())+str(j)+'.jpg',"wb")
            #     req = urllib2.urlopen(pic_url)
            #     buf = req.read()
            #     f.write(buf)
            #     f.close()
            #     j = j + 1

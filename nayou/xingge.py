import urllib2
import re
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

count = 0

for i in xrange(1,48):
    print 'page --> %d -  start' % i
    root = 'http://www.ivrfans.cn/xingge/list_7_%d.html' % i
    req = urllib2.urlopen(root)
    html_content = req.read()

    list_urls = re.findall(r'/xingge/.+/\d{3,6}\.html', html_content)
    print 'page %d  have %d url is:%s' % (i,len(list_urls),list_urls)

    for list_url in list_urls:
        page = 'http://www.ivrfans.cn' + list_url
        print page

        try:
            page_req = urllib2.urlopen(page)
            if page_req.getcode()==200:
                page_buf = page_req.read()
                page_urls = re.findall(r'/xingge/.+/\d{3,6}_\d{1,3}\.html', page_buf)
                print len(page_urls)
                print page_urls

                for html_url in page_urls[2:len(page_urls)-1]:
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
                                path = '/media/deepir/DATA/func/sexy_all/xingge'
                                isExists = os.path.exists(path)
                                if not isExists:
                                    os.makedirs(path)
                                    print path + ' create success'

                                req = urllib2.urlopen(pic_url)
                                buf = req.read()
                                # print buf

                                count = count + 1

                                f = open(path+'/'+str(count)+'.jpg',"wb")
                                f.write(buf)
                                f.close()
                                print i
                                print count
                                # print 'page %d count %d' % i, count

                        else:
                            print 'fail'
                    except:
                        print 'craw _ except'


            else: print 'fail'
        except:
            print 'craw except'

    print 'page --> %d -  end' % i




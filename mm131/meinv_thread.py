import urllib2
import re
import sys

import my_threading

reload(sys)
sys.setdefaultencoding('utf-8')

count = 0

for i in xrange(1, 21):
    print 'page --> %d -  start' % i
    root = 'http://www.27270.com/ent/rentiyishu/list_32_%d.html' % i
    print(root)

    req = urllib2.urlopen(root)
    html_content = req.read()

    linkPattern = re.compile(r'http://www.27270.com/ent/rentiyishu/\d{1,5}\/\d{1,8}.html')
    list_urls = linkPattern.findall(str(html_content))
    print len(list_urls)

    page_lists = []
    for k in range(0, len(list_urls) - 1):
        for j in range(k + 1, len(list_urls)):
            if list_urls[k].__eq__(list_urls[j]):
                break
            if j == len(list_urls) - 1:
                page_lists.append(list_urls[k])
    print "page  %d has %d pic list " % (i, len(list_urls[0:len(page_lists) - 33]))
    print page_lists

    #len(page_lists) - 33
    for k in range(0, len(page_lists) - 33):
        page = page_lists[k]
        splitStrs = page.split('/')
        pic_count = 0
        reqCode = 200
        while reqCode == 200:

            pic_count = pic_count + 1
            page_url = 'http://www.27270.com/ent/rentiyishu/' + splitStrs[len(splitStrs) - 2] + '/' + splitStrs[len(splitStrs) - 1].split('.')[0] + '_' + str(pic_count) + '.html'
            print page_url

            try:
                page_req = urllib2.urlopen(page_url)
                if req.getcode() == 200:
                    page_buf = page_req.read()

                    # pat = re.compile(r'<img alt="(\S*)" src="(.*?\.jpg)" />')
                    # pic_def = pat.findall(str(page_buf))
                    pat = re.compile(r'http://t2.27270.com/uploads/tu/\d{1,9}/.*?\.jpg')
                    pic_urls = pat.findall(str(page_buf))
                    print pic_urls

                    if len(pic_urls) != 0:
                        count = count + 1
                        try:
                            thread1 = my_threading.myThread(1, "Thread-" + str(count), pic_urls[0], count, i, k,
                                                            pic_count)
                            thread1.daemon = True
                            thread1.start()
                        except:
                            print "page  %d de di  %d pic list de di %d pic craw fail" % (i, k + 1, pic_count)

                    if len(pic_urls) == 0:
                        reqCode = 400
                        print "page  %d de di  %d pic list has %d pic already download" % (i, k + 1, pic_count - 1)

                else:
                    print 'open one list fail'
            except:
                print 'list craw except'

import urllib2
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

count = 5863

for i in xrange(7, 8):
    print 'page --> %d -  start' % i
    root = 'http://www.27270.com/ent/meinvtupian/list_11_%d.html' % i
    print(root)

    req = urllib2.urlopen(root)
    html_content = req.read()

    linkPattern = re.compile(r'http://www.27270.com/ent/meinvtupian/\d{1,5}\/\d{1,7}.html')
    list_urls = linkPattern.findall(str(html_content))
    print len(list_urls)

    page_lists = []
    for k in range(0, len(list_urls) - 1):
        for j in range(k + 1, len(list_urls)):
            if list_urls[k].__eq__(list_urls[j]):
                break
            if j == len(list_urls) - 1:
                page_lists.append(list_urls[k])
    print "page  %d has %d pic list " % (i, len(list_urls[0:len(page_lists) - 11]))
    print page_lists

    for k in range(0, len(page_lists) - 11):
        page = page_lists[k]
        splitStrs = page.split('/')
        pic_count = 0
        reqCode = 200
        while reqCode == 200:
            pic_count = pic_count + 1
            page_url = 'http://www.27270.com/ent/meinvtupian/' + splitStrs[len(splitStrs) - 1].split('.')[
                0] + '_' + str(
                pic_count) + '.html'
            print page_url
            try:
                page_req = urllib2.urlopen(page_url)
                if req.getcode() == 200:
                    page_buf = page_req.read()

                    pat = re.compile(r'<img alt="(\S*)" src="(.*?\.jpg)" />')
                    pic_def = pat.findall(str(page_buf))
                    pat = re.compile(r'http://t2.27270.com/uploads/tu/\d{1,7}/\d{1,4}/.*?\.jpg')
                    pic_urls = pat.findall(str(pic_def))
                    print pic_urls

                    if len(pic_urls) != 0:
                        pic = urllib2.urlopen(pic_urls[0])
                        buf = pic.read()
                        count = count + 1
                        f = open('F:\sexy\sexymeinv' + '/' + str(count) + '.jpg', "wb")
                        f.write(buf)
                        f.close()
                        print "page  %d de di  %d pic list de di %d pic craw sucess" % (i, k + 1, pic_count)
                        print (count)

                    if len(pic_urls) == 0:
                        reqCode = 400
                        print "page  %d de di  %d pic list has %d pic already download" % (i, k + 1, pic_count - 1)

                else:
                    print 'open one list fail'
            except:
                print 'list craw except'

import urllib.request
import re
import os

count = 0

for i in range(10,12):
    print ('page --> %d -  start' % i)
    root=''
    if i==1:
        root = 'http://www.souutu.com/mnmm/index.html'
    else:
        root = 'http://www.souutu.com/mnmm/index_%d.html' % i
    print(root)

    response = urllib.request.urlopen(root)
    html_content = response.read()

    linkPattern = re.compile(r'http://www.souutu.com/mnmm/.*?.html')
    urls = linkPattern.findall(str(html_content,"utf-8"))
    page_lists = []
    for k in range(0,len(urls)-1):
        for j in range(k+1, len(urls)):
            if urls[k].__eq__(urls[j]):
                break
            if j==len(urls)-1:
                page_lists.append(urls[k])
    print("page  %s  " % i)
    print("has %d page list " % len(page_lists))
    print(page_lists)

    for page_list in page_lists:
        print (page_list)

        try:
            page_response = urllib.request.urlopen(page_list)
            if page_response.getcode()==200:
                page_buf = page_response.read()
                linkPattern = re.compile(r'http://www.souutu.com/mnmm/.*/\d{3,6}_\d{1,3}\.html')
                page_urls = linkPattern.findall(str(page_buf, "utf-8"))
                print ("page has %d pic " % len(page_urls))
                print (page_urls[2:])

            for pic_url in page_urls[2:]:
                    print (pic_url)
                    try:
                        pic_response = urllib.request.urlopen(pic_url)

                        if pic_response.getcode()==200:
                            pic_buf = pic_response.read()
                            pat = re.compile(r'<img id="bigImg" src="(\S*)"')
                            pic_urls = pat.findall(str(pic_buf, "utf-8"))
                            print (pic_urls)

                            for pic_url in pic_urls:
                                path = 'F:\sexy\mnmm'
                                isExists = os.path.exists(path)
                                if not isExists:
                                    os.makedirs(path)
                                    print( path + ' create success')

                                pic = urllib.request.urlopen(pic_url)
                                buf = pic.read()

                                count = count + 1
                                f = open(path+'/'+str(count)+'.jpg',"wb")
                                f.write(buf)
                                f.close()

                                print (i)
                                print (count)

                        else:
                            print( 'fail')
                    except:
                        print( 'craw _ except')

            else: print( 'fail')
        except:
            print ('craw except')

    print ('page --> %d -  end' % i)




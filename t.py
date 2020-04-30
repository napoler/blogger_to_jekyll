# # import xml.dom.minidom as xmldom
# # 读取xml文件

# import xml.dom.minidom as xmldom


# def parse_xml(fn):
#     xml_file = xmldom.parse(fn)
#     eles = xml_file.documentElement
#     print(eles.tagName)
#     # xmin = eles.getElementsByTagName("xmin")[0].firstChild.data
#     # xmax = eles.getElementsByTagName("xmax")[0].firstChild.data
#     # ymin = eles.getElementsByTagName("ymin")[0].firstChild.data
#     # ymax = eles.getElementsByTagName("ymax")[0].firstChild.data
#     # print(xmin, xmax, ymin, ymax)
#     # return xmin, xmax, ymin, ymax


# def test_parse_xml():
#     blogger_xml="/mnt/data/下载/blog-04-30-2020.xml"
#     parse_xml(blogger_xml)


# if __name__ == "__main__":
#     test_parse_xml()

# https://stackoverflow.com/questions/15676333/how-to-parse-the-xml-file-in-the-google-blogger-in-python
# blogger_xml="/mnt/data/下载/blog-04-30-2020.xml"


# blogger_xml=input("输入blogger_xml目录：")
# url=input("输入博客原始url不包含http:// or https：//")
url="terry-chen.blogspot.com"
blogger_xml="/mnt/data/下载/blog-04-30-2020.xml"


import feedparser
import html2markdown
import time
# import tkitText
import hashlib, binascii

def md5(string):
    # 对要加密的字符串进行指定编码
    string = string.encode(encoding ='UTF-8')
    # md5加密
    # print(hashlib.md5(string))
    # 将md5 加密结果转字符串显示
    string = hashlib.md5(string).hexdigest()
    # print(string)
    return string

d = feedparser.parse(blogger_xml)
# print(d.entries[0].keys())
blog_url="https://"+url
blog_urls="https://"+url

for i, entry in enumerate( d.entries):
    # print (entry.title_detail)
    if len(entry.title_detail['value'])>0:
        pass
    else:
        continue
    # print (entry.title)
    # print(entry.content)
    md=html2markdown.convert(entry.content[0]["value"])


    # t=time.strptime(entry.published,'%Y-%m-%d')
    t=entry.published[:10]
    title=entry.title_detail["value"].replace(' ', '').replace('。', '').replace('，', '')
    filename="out/"+t+"-"+title+".md"

    # print(filename)
    tags=[]


    for tag in entry.tags:
        if tag['term']=="http://schemas.google.com/blogger/2008/kind#post" or  tag['term']=="http://schemas.google.com/blogger/2008/kind#settings":
            pass
        else:
            tags.append(tag['term'])
    if "http://schemas.google.com/blogger/2008/kind#settings" == entry.tags[0]['term']:
        continue
    elif "http://schemas.google.com/blogger/2008/kind#template"==entry.tags[0]['term']:
        continue
    # print(" ".join(tags))
    # print(entry.link.replace("https://terry-chen.blogspot.com",''))
    # print(entry.link)
    link=entry.link.replace(blog_url,'').replace(blog_urls,'')
    if "blogger.com" in link:
        continue
        link="/post/"+link[-24:]
    print(entry.tags)
    print(link)
    h="---\n"
    h=h+"layout: post\n"
    h=h+'title: "'+entry.title+'"\n'
    h=h+"permalink: '"+link+"'\n"
    
    h=h+"comments: 1\n"
    h=h+"categories: Default\n"
    h=h+"tags: "+" ".join(tags)+"\n"
    # h=h+"comments: 1\n"
    h=h+"---\n"

    md=h+md

    # print(md)
    # print(entry.tags)
    # tt=tkitText.Text()
    # print(entry.id)

    # print(entry.updated)
    # if entry.guidislink==True:
    #     print("oooo")
    # else:
    #     continue

    try :
        f = open(filename,'w')
        f.write(md)
        f.close()
    except:
        # title=md5(title)
        # filename="out/"+t+"-"+title+".md"  
        # f.write(md)
        # f.close()
        pass

    # if i >100:
    #     break
    # print (entry.content[0]["value"])
    # print (entry.content)

#     for k in entry.keys():
#         print(entry.k)
# print(d.entries[0].keys())


    
import linecache,requests,os,random,threading,time
def img_name():
    with open('./img_name.txt','r',encoding='UTF-8') as f:
        name = [' '.join([i.strip() for i in price.strip().split('\t')]) for price in f.readlines()]
    return name

def img_urls():
    with open('./img_urls.txt','r',encoding='UTF-8') as f:
        name = [' '.join([i.strip() for i in price.strip().split('\t')]) for price in f.readlines()]
    return name

def rename(path):
    i = random.randint(0,10)
    path1 = path + '%s' %(i)
    os.rename(path, path1)

def get_url():
    urls = img_urls()
    names = img_name()
    start_save_img(urls,names)

def save_img(url,name,i):
    try:
        print("-----------正在下载图片 %s" % (url),i)
        response = requests.get(url,timeout=(None))
        img = response.content
        path = './img/%s.jpg' % (name)
        if os.path.exists(path):
            rename(path)
            with open(path, 'wb') as f:
                f.write(img)
        else:
            with open(path, 'wb') as f:
                f.write(img)
        time.sleep(1)
    except Exception as ex:
        with open('./error.txt',mode='a') as f:
            f.write(url)
            f.write('\n')
            f.close()


def start_save_img(urls,names):
    for i in range(len(urls)):
        th = threading.Thread(target=save_img,args=(urls[i],names[i],i))
        th.start()

if __name__ == '__main__':
    get_url()

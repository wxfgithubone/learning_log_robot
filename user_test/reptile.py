# Time：2020/8/26  Author：王哈哈
# -*-coding:utf-8 -*-
from lxml import etree
from multiprocessing import Process
import requests, time, logging, re, os, traceback, urllib3, random

urllib3.disable_warnings()  # 消除警告
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 '
                  '(KHTML, like Gecko)Chrome/83.0.4103.116 Safari/537.36'
}  # 伪装请求头
now_time = time.strftime('%y-%m-%d %H-%M-%S')
day_time = time.strftime('%y-%m-%d')


def reptile_book(d, n):
    """爬取全书网，d,n表示几到几之间的书的ID，如1-10"""
    base_url = 'https://www.xs4.cc/'
    s_t = time.perf_counter()  # 计数器，统计耗时
    for num in range(d, n):
        ks_time = time.perf_counter()
        book_url = f'{base_url}0_{num}/'
        req = requests.get(url=book_url, headers=header, verify=False)
        req.encoding = 'gbk'

        bookName = re.findall('<h1>(.*?)</h1>', req.text, re.S)[0]  # 书名
        book_article = re.findall('html">(.*?)</a></dd>', req.text, re.S)  # 章节
        article_link = re.findall('<dd><a href="/(.*?)">', req.text, re.S)  # 章节链接

        logging.basicConfig(level='DEBUG', filename=f'data/log/{bookName}.log', filemode='a')
        logging.debug(f"书名{bookName}；爬取时间{now_time}")

        lists = []  # 子列表储存章节和链接，方便本地排序
        for i in range(9, 19):  # 前十章
            lists.append([book_article[i], f"{base_url}{article_link[i]}"])

        if os.path.exists(f'data/book/{num:03}{bookName}'):  # 判断文件夹是否存在，这里为相对路径
            pass
        else:
            os.mkdir(f'data/book/{num:03}{bookName}')

        for j in enumerate(lists):  # 遍历章节列表
            st_time = time.perf_counter()
            res_zw = requests.get(url=j[1][1], headers=header, verify=False)
            res_zw.encoding = 'gbk'
            book_m = re.findall('<div id="content">(.*?)</div>', res_zw.text, re.S)[0]  # 每章具体内容
            book_m = book_m.replace('&nbsp;', '').replace('<br />', '')  # 切菜
            if os.path.exists(f'data/book/{num:03}{bookName}/{j[0]+1:04}{j[1][0]}.txt'):
                pass
            else:
                try:
                    with open(f'data/book/{num:03}{bookName}/{j[0]+1:04}{j[1][0]}.txt', 'w+') as file:
                        file.write(book_m)  # 写入
                except FileNotFoundError as e:
                    print(f"无法打开文件请检查路径\n异常{e}")
                    logging.error(traceback.format_exc() + now_time)
                except OSError:
                    logging.error(traceback.format_exc() + now_time)
                else:
                    file.close()
                    end_time = time.perf_counter() - st_time
                    logging.debug(f"爬取：{j[1][0]}；耗时{end_time}秒")
                finally:
                    print(f"正在爬取：{j[1][0]}")
        js_time = time.perf_counter() - ks_time
        logging.debug(f"小说名：{bookName}；爬取该书耗时{js_time}秒")
    en_t = time.perf_counter() - s_t
    logging.debug(f"总耗时{en_t}秒")


def reptile_video(d, n):
    """爬取梨视频的视频，d,n同上，专题ID"""
    base_url1 = 'http://www.pearvideo.com/'
    for num in range(d, n):
        url = f'{base_url1}category_2'  # 8889可更换为num
        req = requests.get(url=url, headers=header, verify=False)

        html_doc = req.content.decode('utf-8')
        tree = etree.HTML(html_doc)
        video = tree.xpath('//*[@id="categoryList"]/li/div/a/@href')
        video_1 = tree.xpath('//*[@id="categoryList"]/li/div/a/div[2]/text()')

        title = re.findall('<h1 class="category-title">(.*?)<span>', req.text, re.S)[0]

        if os.path.exists(f'data/video/li_shipin/{title}{day_time}'):
            pass
        else:
            os.mkdir(f'data/video/li_shipin/{title}{day_time}')  # 因视频每天会更新故在文件夹后面加上当天时间

        for video_url, video_text in zip(video, video_1):
            startTime = time.perf_counter()
            # 拼接url
            movie_url = f'{base_url1}{video_url}'
            # 获取每个url的网页text
            movie_id_ = requests.get(movie_url, headers=header, verify=False).text
            # 获取视频里层播放mp4的url地址 []
            movie_mp4_url = re.findall(
                'sdflvUrl="",hdUrl="",sdUrl="",ldUrl="",srcUrl="(.*?)",vdoUrl=srcUrl', movie_id_
            )
            # url在[]列表里 没有遍历出来 所以用索引下标[0]
            mp4 = requests.get(movie_mp4_url[0], verify=False).content
            if os.path.exists(f'data/video/li_shipin/{title}{day_time}/{video_text}.mp4'):
                pass
            else:
                try:
                    with open(f'data/video/li_shipin/{title}{day_time}/{video_text}.mp4', 'wb') as f:
                        f.write(mp4)
                except OSError:
                    logging.error(traceback.format_exc() + time.strftime('%y-%m-%d %H:%M:%S'))
                else:
                    f.close()
                    endTime = time.perf_counter() - startTime
                    print("正在下载视频.... (%s)" % video_text)
                    print(f"耗时{endTime}耗时")


def reptile_img(d, n):
    """爬取彼岸图网"""
    base_url = 'http://pic.netbian.com'
    for i in range(d, n):
        url = '{}/4kmeinv/index_{}.html'.format(base_url, i)
        req = requests.get(url=url, headers=header)
        req.encoding = 'gbk'
        title = re.findall('<b>(.*?)</b>', req.text, re.S)
        jpg = re.findall('<img src="(.*?)"', req.text, re.S)
        dicts = {}
        for i in range(0, len(title) - 2):
            dicts[title[i]] = f'{base_url}{jpg[i]}'
        for k, v in dicts.items():
            r = requests.get(v)
            if random.randint(1, 4) == 1:  # 随机生成一个图片格式
                fot = 'jpg'
            elif random.randint(1, 4) == 2:
                fot = 'png'
            elif random.randint(1, 4) == 3:
                fot = 'jpeg'
            else:
                fot = 'webp'
            with open('data/img/bull_img/{}.{}'.format(k, fot), 'wb') as f:
                f.write(r.content)
            f.close()
            print(f"正在下载图片：{k}....")


if __name__ == '__main__':
    print(f"开始:{time.ctime()}")
    threads = [
        Process(target=reptile_book, args=(13, 15)),
        Process(target=reptile_video, args=(1, 2)),
        Process(target=reptile_img, args=(2, 4))
    ]  # 线程组

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"结束:{time.ctime()}")


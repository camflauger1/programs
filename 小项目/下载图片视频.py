# -*- encoding: 'utf-8' -*-

import os, time
import urllib.request
import re
import sys, hashlib
import opencv


def download_image(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    return data


# 下载图片
def get_image(html):
    regx = r'http://[\S+]*\.jpg'
    pattern = re.compile(regx)
    image = re.findall(pattern, repr(html))
    path = r'F:\命运\图片'
    if not os.path.exists(path):
        os.makedirs(path)
        print("文件夹成功创建！")
    for i in image:
        img = download_image(i)
        img1 = i.split("/")[-1]
        with open(path + '\\' + img1, 'wb') as fp:
            fp.write(img)
        print("%s下载完毕！" % img1)
    return


# 下载视频
def get_video(url, page, path):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                             ' (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    # req = urllib.request.Request(r'http://www.budejie.com/video/%s' % page, headers=headers)
    req = urllib.request.Request(url + page, headers=headers)
    html = urllib.request.urlopen(req)
    data = html.read()
    reg = r'data-mp4="(.*?)"'
    # path = r'F:\命运\mp4'
    if not os.path.exists(path):
        os.makedirs(path)
        print("文件夹成功创建！")
    for i in re.findall(reg, repr(data)):
        print(i)
        filename = i.split("/")[-1]
        print("正在下载%s" % filename)
        urllib.request.urlretrieve(i, (path + '//' + filename))


def one_choice():
    msg = "下载图片输入：1\n下载视频输入：2\n批量修改文件名字输入3\n删除文件输入4\n删除重复文件\n输入："
    choice = int(input(msg))
    while choice < 1 or choice > 5:
        choice = input("请重新输入：" + msg)
    if choice == 1:
        url = input("请输入网址：例如：" + str('http://pic.yesky.com/') + '\n' + '存储地址在：'
                    + str(r'F:\命运\图片') + '\n输入:')
        get_image(download_image(url))
    elif choice == 2:
        num1 = input(
            "请输入网址:例如" + str('http://www.budejie.com/video/') + '\n存储地址在：' + str(r'F:\命运\mp4') + '\n输入:')
        num2 = int(input("请输入下载页数："))
        num3 = input('请输入要保存的路径，如' + str(r'F:\命运\mp4') + '\n输入:')
        for i in range(1, num2 + 1):
            get_video(num1, str(i), num3)
    elif choice == 4:
        num1 = input("请输入路径：例如：" + str(r'F:\命运\图片') + '\n输入：')
        num2 = input("请输入要删除的文件类型（如 txt）\n 输入：")
        delete_file(num1, num2)
    elif choice == 5:
        num1 = input("请输入路径：例如：" + str(r'F:\命运\图片') + '\n输入：')
        delete_same_file(num1)
    else:
        path = input("请输入路径：例如：" + str(r'F:\命运\图片') + '\n输入：')
        form = input("请输入要修改成的文件类型(如 MP3)\n输入：")
        change_name(path, form)


# 批量修改文件名字
def change_name(path, form):
    # path = r'F:\命运\图片'
    photo_list = os.listdir(path)
    num = 1
    new_name = str(num) + '.' + form
    while new_name + '.' + form in photo_list:
        num += 1
    for name in photo_list:
        new_name = str(num) + '.' + form
        try:
            os.rename(path + '//' + name, path + '//' + new_name)
        except FileExistsError:
            continue
        num += 1
        print(name, '已被修改为', new_name)


# 删除指定文件夹下的指定类型的文件
def delete_file(path, form):
    file_list = os.listdir(path)
    for file in file_list:
        if file.split('.')[-1] == form:
            os.remove(path + '\\' + file)
            print(file, '已删除！')


# 获取md5值
def get_md5(file):
    if not os.path.isfile(file):
        return
    fd = open(file, 'rb')
    md5 = hashlib.md5()
    md5.update(fd.read())
    fd.close()
    return md5.hexdigest()


# 删除重复文件
def delete_same_file(path):
    all_file = []
    md5_list = []
    size_list = []

    # start = time.time()
    # path = unicode(path, 'utf-8')
    for path, dir, filelist in os.walk(path):
        for filename in filelist:
            all_file.append(os.path.join(path, filename))

    for photo in all_file:
        size = os.path.getsize(photo)
        if size not in size_list:
            size_list.append(size)
        else:
            md5sum = get_md5(photo)
            if md5sum not in md5_list:
                md5_list.append(md5sum)
            else:
                os.remove(photo)
                print(photo, "已删除！")


def main():
    msg1 = "输入 quit 结束！输入任意字符开始！"
    choice1 = input(msg1)
    while choice1 != 'quit':
        one_choice()


if __name__ == '__main__':
    main()


#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from PIL import Image


# 修改图片名
def change_pic_name(path, pic_type):
    # 获取文件夹内所有文件
    all_dir = os.listdir(path)
    for item in all_dir:
        file_path = os.path.join(path, item)

        # 获取文件名中最大名字
        def get_max_name_num():
            k = 0
            num = []
            # 获取图片名字不带后缀
            for i in os.path.splitext(file_path)[0]:
                num.append(i)
            for i in range(len(num)):
                if str(i) in num:
                    k = i + 1
            return k

        name_num = get_max_name_num()
        if os.path.isdir(file_path):
            # 获取根目录路径、子目录路径、根目录和子目录下所有文件名
            for root, subDir, files in os.walk(file_path):

                for file in files:
                    print('file:', file)
                    # if file.endswith(('.bmp', '.jpg', '.gif', '.png')):
                    if file.endswith('.mp4'):
                        pic_name = os.path.join(root, file)
                        new_pic_name = os.path.join(root, str(name_num))
                        new_pic_name += pic_type
                        try:
                            os.rename(pic_name, new_pic_name)
                        except FileExistsError:
                            pass
                        print(file + '————>' + str(name_num) + pic_type)
                        name_num += 1


# 修改单张图片尺寸
def convertjpg(jpgfile, outdir, width=283, height=402):
    img = Image.open(jpgfile)
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
    except Exception as e:
        print(e)


# 批量修改图片尺寸
def change_chara(path, out_path, width=283, height=402):
    all_dir = os.listdir(path)
    for item in all_dir:
        file_path = os.path.join(path, item)
        if os.path.isdir(file_path):
            # 获取根目录路径、子目录路径、根目录和子目录下所有文件名
            for root, subDir, files in os.walk(file_path):

                # 分割原文件夹目录，获取子文件夹路径
                out_path_list = root.split('\\')
                out_path_name = out_path_list[-2] + '\\' + out_path_list[-1]

                for file in files:
                    if file.endswith(('.bmp', '.jpg', '.gif', '.png')):
                        path_name = os.path.join(root, file)
                        end_out_path_name = os.path.join(out_path, out_path_name)
                        im = Image.open(path_name)
                        m, n = im.size
                        convertjpg(path_name, end_out_path_name, width, height)
                        print('%s-%s  ————> %s-%s' % (m, n, width, height), '图片大小修改成功')


# 主函数
def main():
    path = r'F:\命运'
    # ty = '.png'
    out_path = r'F:\搞笑视频\mp4'
    ty = '.mp4'
    change_pic_name(path, ty)
    # change_chara(path, out_path)


if __name__ == '__main__':
    main()


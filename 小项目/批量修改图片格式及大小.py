from PIL import Image
import os.path
import glob
import os


def convertjpg(jpgfile, outdir, width=283, height=402):
    img = Image.open(jpgfile)
    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
    except Exception as e:
        print(e)


image = r'\*.jpg"'
path1 = r"E:\相片\四班\杨浩森"
orign = os.listdir(path1)
print(orign)

k = 0
for i in orign:
    # path4 = path1 + '\\' + str(orign[k])
    orign1 = os.path.join(path1, i)
    print(orign1)
    # list1 = os.listdir(orign1)
    # print(list1)
    for jpgfile in orign1:
        path7 = os.path.join(orign1, jpgfile)
        convertjpg(path7, orign1)
    k += 1
    print(orign[k] + ' 处理完毕')


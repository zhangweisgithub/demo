# !/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random


def validate_picture():
    total = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345789'
    # 图片大小130x50
    width = 130
    height = 50
    # 先生成一个新图片对象
    im = Image.new('RGB', (width, height), 'white')
    # 设置字体
    font = ImageFont.truetype('C:\\Windows\\Fonts\\Calibri.ttf', 50)
    # font = ImageFont.load_default().font
    # 创建draw对象
    draw = ImageDraw.Draw(im)
    str1 = ''
    # 输入每一个文字
    for item in range(5):
        text = random.choice(total)
        str1 += text
        draw.text((5 + random.randint(4, 7) + 20 * item, 5 + random.randint(3, 7)), text=text, fill='blue', font=font)

    # 划几根干扰线
    for num in range(8):
        x1 = random.randint(0, width / 2)
        y1 = random.randint(0, height / 2)
        x2 = random.randint(0, width)
        y2 = random.randint(height / 2, height)
        draw.line(((x1, y1), (x2, y2)), fill='black', width=1)

    # 模糊下，加个滤镜
    im = im.filter(ImageFilter.FIND_EDGES)
    return im, str1


if __name__ == '__main__':
    im, str1 = validate_picture()
    print(str1)

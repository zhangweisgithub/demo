# !/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.cnblogs.com/fu-yong/p/8811851.html

"""
open()  #打开图片

new(mode,size,color)   #创建一张空白图片

save("test.gif","GIF")   #保存（新图片路径和名称，保存格式）

size()   #获取图片大小

thumbnail(weight,high)   #缩放图片大小（宽，高）

show()    #显示图片

blend(img1,img2,alpha)   #两张图片相加，alpha表示img1和img2的比例参数。

crop()   #剪切，提取某个矩阵大小的图像。它接收一个四元素的元组作为参数，各元素为（left, upper, right, lower），坐标系统的原点（0, 0）是左上角。

rotate(45)    #逆时针旋转45度

transpose()    #旋转图像
    transpose(Image.FLIP_LEFT_RIGHT)       #左右对换。
    transpose(Image.FLIP_TOP_BOTTOM)       #上下对换。
    transpose(Image.ROTATE_90)             #旋转 90 度角。
    transpose(Image.ROTATE_180)            #旋转 180 度角。
    transpose(Image.ROTATE_270)            #旋转 270 度角。

paste(im,box)#粘贴box大小的im到原先的图片对象中。

convert()    #用来将图像转换为不同色彩模式。

filters()     #滤镜
    BLUR   #虚化
    EMBOSS
resize((128,128))     #resize成128*128像素大小

convert("RGBA")    #图形类型转换

getpixel((4,4))   #获取某个像素位置的值

putpixel((4,4),(255,0,0))    #写入某个像素位置的值

"""

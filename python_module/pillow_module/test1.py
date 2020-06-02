# !/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
"""
生成一张固定尺寸固定颜色的图片
"""
# 获取一个Image对象，参数分别是RGB模式。宽150，高30，红色
image = Image.new('RGB', (150, 30), 'red')
# 保存到硬盘，名为test1.png格式为png的图片
image.save(open('./photos/test1.png', 'wb'), 'png')

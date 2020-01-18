# !/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from tqdm import tqdm

alist = list('letters')
bar = tqdm(alist)
for letter in bar:
    bar.set_description(f"Now get {letter}")

"""
Now get s: 100%|██████████| 7/7 [00:00<00:00, 6813.68it/s]
"""

"""============================================"""

pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    pbar.set_description("Processing %s" % char)


# 一共200个，每次更新10，一共更新20次
with tqdm(total=200) as pbar:
    for i in range(20):
        pbar.update(10)
        time.sleep(0.1)


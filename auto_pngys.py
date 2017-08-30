#!/usr/bin/env python
#encoding=utf-8
#-*- coding: utf-8 -*-
import tinify
import os
# key 可以去网站注册 会得到一个key
# 批量压缩png文件的脚本
tinify.key='v5b0JQQwVO9UReHYk-VGJ1VtJ1wBPgiu'



pngpath="/Users/wuyan/Desktop/android/sdcr/SmallWallet/res/drawable-xhdpi"

for i in os.listdir(pngpath):
    if(i==".DS_Store"):
        print "有隐藏文件"
        continue
    else:
        if os.path.splitext(i)[1] == ".png":
            source = tinify.from_file(os.path.join(pngpath, i))
            opt = pngpath + 'optimize'
        if not os.path.exists(opt):
            os.makedirs(opt)
        source.to_file(os.path.join(opt, i))
print('压缩完毕')

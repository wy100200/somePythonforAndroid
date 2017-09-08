#!/usr/bin/env python
#encoding=utf-8
#-*- coding: utf-8 -*-
import tinify
import os
import shutil
import sys
# key 可以去网站注册 会得到一个key 免费key 一个月压缩500张
# 批量压缩png文件的脚本
tinify.key='v5b0JQQwVO9UReHYk-VGJ1VtJ1wBPgiu'


print "脚本名：", sys.argv[0]

projectPath =sys.argv[1]
print projectPath

print os.listdir(projectPath)

os.chdir(projectPath)#转到工程目录下

pngPaths = []


for i in os.listdir(projectPath):
    if(i==".DS_Store"):
        print "有隐藏文件"
        continue
    else:
        if "dpi" in  i :
            pngPaths.append(i)


print pngPaths

pngOptimizePaths = []


for pngpath in pngPaths:
    for i in os.listdir(pngpath):
        if (i == ".DS_Store"):
            print "有隐藏文件"
            continue
        else:
            if os.path.splitext(i)[1] == ".png":
                source = tinify.from_file(os.path.join(pngpath, i))
                opt = pngpath + 'optimize'
                if not os.path.exists(opt):
                    os.makedirs(opt)
                    pngOptimizePaths.append(opt)
                source.to_file(os.path.join(opt, i))


print pngOptimizePaths


for pngPath in  pngPaths:
    shutil.rmtree(pngPath)

for pngOptimizePath in pngOptimizePaths:
    print pngOptimizePath
    renamePath =pngOptimizePath.replace("optimize","")
    print renamePath
    os.renames(pngOptimizePath, renamePath)


print('压缩完毕')

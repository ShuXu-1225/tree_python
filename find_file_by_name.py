#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import os

count = 0


def getFileName():
    while True:
        name = input("please type in file name: ")
        if name == '':
            print('your input cannot be --> none <--\n')
        else:
            return name


def findFileByName(fName, path):
    global count
    count = count + 1
    if count % 5000 == 0:
        print('searching -> ', int(count / 5000))

    # 列举路径下 名词类似输入规则的 文件
    [setResult(path, x) for x in os.listdir(path) if
     os.path.isfile(os.path.join(path, x)) and fName in os.path.split(os.path.join(path, x))[1]]

    [findFileByName(fName, os.path.join(path, y)) for y in os.listdir(path) if os.path.isdir(os.path.join(path, y))]


def setResult(path, res):
    if len(path) > 0 and len(res) > 0:
        print(path, res)


def doFileSearch():
    fName = getFileName()
    path = os.path.abspath('E:\\workspaces_cordova')

    print('- name ------> ', fName)  # abc
    print('- path ------> ', path)  # e:\
    print('******* seraching now *******')

    findFileByName(fName, path)


doFileSearch()

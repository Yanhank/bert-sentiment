# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File:           pre_process.py
   Author:         icelights
   Date：          2019/6/24 0024
-------------------------------------------------

"""


import codecs
import os
import traceback


def combine(root_path, save_path):
    sub_path = os.listdir(root_path)
    print(sub_path)
    with codecs.open(os.path.join(save_path, 'neg.train'), 'a', encoding='utf-8') as fn,\
    codecs.open(os.path.join(save_path, 'pos.train'), 'a', encoding='utf-8') as fp:
        for sub in sub_path:
            if os.path.isdir(os.path.join(root_path, sub)):
                fsn_path = os.path.join(root_path, sub, 'neg.txt')
                print(fsn_path)
                fsn = codecs.open(fsn_path, 'rb', encoding='utf-8')
                for ni in fsn.readlines():
                    try:
                        fn.write(ni)
                    except:
                        traceback.print_exc()

                fsn.close()
                fsp = codecs.open(os.path.join(root_path, sub, 'pos.txt'), 'rb', encoding='utf-8')
                for pi in fsp.readlines():
                    try:
                        fp.write(pi)
                    except:
                        traceback.print_exc()
                fsp.close()


def handle_dev_test(root_path):

    with codecs.open(os.path.join(root_path, 'neg.test'), 'a', encoding='utf-8') as fn, codecs.open(
        os.path.join(root_path, 'pos.test'), 'a', encoding='utf-8') as fp:
        num = 0
        for i in range(0, 2000):
            neg_file = 'neg.{}.txt'.format(i)
            pos_file = 'pos.{}.txt'.format(i)
            with codecs.open(os.path.join(root_path, 'test_ChnSentiCorp', neg_file), 'r', encoding='utf-8') as fsn:
                n = fsn.read()
                fn.write(n.replace(' ', '').replace('\r', '').replace('\n', '')+'\n')
            with codecs.open(os.path.join(root_path, 'test_ChnSentiCorp', pos_file), 'r', encoding='utf-8') as fsp:
                p = fsp.read()
                fp.write(p.replace(' ', '').replace('\r', '').replace('\n', '')+'\n')



if __name__ == '__main__':
    flag = 2
    if flag == 1:
        path = './corpus/raw'
        combine(path, './corpus')
    elif flag == 2:
        root_path = './corpus'
        handle_dev_test(root_path)


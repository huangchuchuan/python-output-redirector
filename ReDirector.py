# -*- coding: utf-8 -*-
# @Author  : Huangcc

import sys


class ReDirector:
    def __init__(self, filename='result.log'):
        self.buff = ''
        self.filename = filename
        self.__console__ = sys.stdout

    def write(self, output_stream):
        self.buff += output_stream

    def to_console(self):
        sys.stdout = self.__console__
        print self.buff
        sys.stdout.flush()

    def to_file(self):
        with open(self.filename, 'a') as f:
            sys.stdout = f
            print self.buff
            sys.stdout.flush()

    def flush(self):
        self.to_console()
        self.to_file()
        self.buff = ''

    def close(self):
        if self.buff:
            self.flush()
        sys.stdout = self.__console__


if __name__ == '__main__':
    r_obj = ReDirector()  # ReDirector将标准输出的引用存起来然后提供一个buff
    sys.stdout = r_obj  # 将当前的标准输出变量指向ReDirector
    sys.stderr = r_obj  # 将当前的错误输出变量指向ReDirector
    print 'should be redirect'
    sys.stderr.write('should be redirect too')
    r_obj.flush()  # 将自身buff写入目标buff中
    r_obj.close()  # 还原标准输出变量的值
    print 'output to console directly'
    sys.stderr = sys.stdout  # 还原错误输出到标准输出变量

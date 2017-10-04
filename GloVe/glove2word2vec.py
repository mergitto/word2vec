#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
   argvs = sys.argv  # コマンドライン引数を格納したリストの取得
   argc = len(argvs) # 引数の個数

   if (argc != 2):   # 引数が足りない場合は、その旨を表示
       print('Usage: # python %s filename' % argvs[0])
       quit()

   line_count = 0 # 行数
   vector_size = 0 # 次元数
   # 1度目のファイルアクセスで、行数と次元数を確認
   with open(argvs[1], "r") as fin:
       for line in fin:
           line_count += 1
       # 最後に次元数を確認
       vector = line.rstrip().split(' ')
       vector_size = len(vector) - 1
   # 2度目のファイルアクセスで、word2vec形式のものを標準出力
   with open(argvs[1], "r") as fin:
       print(line_count, vector_size)
       for line in fin:
           print(line, end="")

if __name__ == "__main__":
   main()

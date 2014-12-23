# coding=utf-8
#!/usr/bin/env python
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from collections import defaultdict
import re


split = re.compile(ur'[，。！；‘“、~？ ]{1,}').split



def recognition(file_name, window=2):
    word_count = defaultdict(int)
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip().decode('utf-8')
            for words in split(line):
                for i in range(0, len(words)):
                    word_count[words[i: i + 2]] += 1
    return sorted(word_count.items(), key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    for i in recognition('d:/773.txt', window=2)[:200]:
        print i[0], i[1]

# coding=utf-8
#!/usr/bin/env python

import os
import random

rand_range = lambda a, b: random.randint(b, a)


def read_file(path):
    if not (os.path.isfile(path) and os.path.exists(path)):
        raise IOError, path
    contents = []
    with open(path) as f:
        contents.extend([line.strip() for line in f.readlines()])
    return contents


def read_file_set(path):
    contents = []
    contents.extend({line for line in read_file(path)})
    return contents


def write_file(path, contents=[]):
    # if not os.path.isfile(path):
    #     raise IOError, path
    with open(path, 'w') as f:
        [f.write(line + '\n') for line in contents]


def split(file_path, max_file, min_file):
    if not (isinstance(max_file, int) and isinstance(min_file, int) and max_file >= min_file and min_file > 0):
        raise TypeError(
            "must be int and max_file > min_file > 0"), max_file, min_file

    contents = read_file_set(file_path)
    file_len = len(contents)
    if file_len < (max_file + min_file):
        raise UserWarning, max_flie, min_file
    count_percent = float(max_file) + float(min_file)
    max_len = long(file_len * (max_file / count_percent))
    max_contents = [contents[i] for i in range(max_len)]
    min_contents = [contents[i] for i in range(max_len, file_len)]
    write_file('%s_%s' % (file_path, max_len), max_contents)
    write_file('%s_%s' % (file_path, (file_len - max_len)), min_contents)


def split_random(file_path, max_percent, min_percent, rand_times=0.5):
    if not (isinstance(max_percent, int) and isinstance(min_percent, int) and max_percent >= min_percent and min_percent > 0):
        raise TypeError(
            "must be int and max_file > min_percent > 0"), min_percent, min_percent

    contents = read_file(file_path)
    file_len = len(contents)
    random_times = file_len * rand_times
    print file_len
    __rand = 0
    for _ in range(long(random_times)):
        __index1 = rand_range(file_len - 1 , 0)
        __index2 = rand_range(file_len - 1 , 0)
        __rand = __rand + 1
        tmp = contents[__index1]
        contents[__index1] = contents[__index2]
        contents[__index2] = tmp
    print __rand
    max_len = long(
        file_len * (float(max_percent) / (float(max_percent) + float(min_percent))))
    write_file('train.txt' , contents[0:max_len])
    write_file('text.txt' , contents[max_len:])


if __name__ == "__main__":
    # split("/home/lixuze/project/ad/ad_notad_data/final.seg" , 4 , 1)
    # x = read_file_set("/home/lixuze/project/ad/pos.txt.seg")
    # write_file("/home/lixuze/project/ad/ad_zhang.data",
    #            ['广告\t%s' % i.split('\t')[1] for i in x])
    split_random('data.txt' ,3 , 1 , 1.0)

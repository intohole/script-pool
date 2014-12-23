#coding=utf-8






import os 

if __name__ == '__main__':
    file_handle = open('d:/english.txt' , 'w')

    english = 'd:/data/english/'
    for file_name in os.listdir(english):
        file_path = '%s%s' % (english , file_name)
        if os.path.isfile(file_path):
            with open(file_path) as f:
                for line in f.readlines():
                    file_handle.write(line)
        elif os.path.isdir(file_path):
            for child_path in os.listdir(file_path):
                child_file = '%s/%s' % (file_path , child_path)
                with open(child_file) as f:
                    for line in f.readlines():
                        file_handle.write(line)
    file_handle.close()
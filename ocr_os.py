# encoding:utf-8

import os
# import shutil
from PIL import Image


def image_train_name(path, suffix_write_path, write_path):

    if os.path.exists(suffix_write_path):
        os.remove(suffix_write_path)
    if os.path.exists(write_path):
        os.remove(write_path)
    # image_folder = './data/image_train'
    # if os.path.exists(image_folder):
    #     shutil.rmtree(image_folder)
    # os.makedirs(image_folder)

    with open(suffix_write_path, 'a+', encoding='utf8') as suffix_write_f, open(write_path, 'a+', encoding='utf8') as write_f:
        base_dir = 'data/image_train/20181218_{}.png'
        i = 0
        for file_name in os.listdir(path):
            if file_name.split('.')[-1] == 'zip':
                continue
            for d in os.listdir(os.path.join(path, file_name)):
                image_path_suffix = base_dir.format(i)

                img_path_tmp = '.'.join(d.split('.')[:-1])
                img_path_tmp_s = img_path_tmp.split('_')
                image_path = '_'.join(img_path_tmp_s[1:]) if len(img_path_tmp_s) > 1 else img_path_tmp

                img_read_path = os.path.join(path, file_name, d)
                image = Image.open(img_read_path)
                image.save(image_path_suffix)
                suffix_write_f.write(image_path_suffix + '\n')
                write_f.write(image_path + '\n')
                i += 1


if __name__ == '__main__':
    file_dir = './data/file_pic'
    suffix_write_path = './data/image_path_suffix.txt'
    write_path = './data/image_path.txt'
    image_train_name(file_dir, suffix_write_path, write_path)

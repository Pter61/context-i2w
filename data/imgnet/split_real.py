import pandas as pd
import argparse
import os
from tqdm import tqdm
import shutil
# shutil.copy(f, f_out)
def parse_args():
    parser = argparse.ArgumentParser('')

    parser.add_argument('--data_path', type=str, help='path data files',
                        default='./datasets/cir/data/imgnet/')
    parser.add_argument('--save_path', type=str, help='path to save files',
                        default='./datasets/cir/data/imgnet/real/')
    args = parser.parse_args()
    return args

args = parse_args()

def check_folder_exist(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

def split_images(path, save_path):
    query_file_path = os.path.join(path, "imgnet_real_query.txt")
    img_path = os.path.join(path, "imgnet_val_2012")

    with open(query_file_path, "r") as f:
        query_lines = f.readlines()
    # print(type(txt))
    for query_line in tqdm(query_lines):
        # print(query_line.split(' ')[0].split('/'))
        img_folder, imgname = query_line.split(' ')[0].split('/')[2], query_line.split(' ')[0].split('/')[3]
        # print(img_folder, imgname)
        src_path = os.path.join(img_path, imgname)
        tgt_path = os.path.join(save_path, img_folder)

        assert os.path.isfile(src_path)
        check_folder_exist(tgt_path)
        shutil.copy(src_path, tgt_path)
        # print(src_path, "\n", tgt_path)

    print("Done!")

if __name__ == "__main__":
    split_images(args.data_path, args.save_path)
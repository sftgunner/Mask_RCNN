import argparse
import os

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--input-folder', help='the full path of the input directory', nargs='?',default="../Lane-Detection-Tracking/media/")
args,unknownargs = parser.parse_known_args()


dirs = os.listdir(os.path.expanduser(args.input_folder))

for dir in dirs:
    totaldir = os.path.join(args.input_folder,dir)
    print(f"python image.py --input-folder {totaldir}")
    os.system(f"python image.py --input-folder {totaldir}")
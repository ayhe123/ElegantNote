import os
import argparse
import re


def change_one_file(fsrc, fdst, args):
    """按照 args 修改 fsrc 的样式并保存到 fdst"""
    context = fsrc.read()
    arg_tex = ','.join([f'{k}={v}' for k, v in args.items()])
    context = re.sub(r'\\documentclass.+\{elegantnote\}',
                     r'\\documentclass['+arg_tex+r']{elegantnote}',
                     context)
    if fdst is not None:
        fdst.write(context)
    else:
        with open(fsrc.name, 'w', encoding='utf-8') as fp:
            fp.write(context)


parser = argparse.ArgumentParser(
    description="将使用elegantnote的.tex文件转换成命令行参数中的样式")
parser.add_argument(
    "--fsrc", type=argparse.FileType('r'),
    help="要修改样式的文件, 不填则就地转换目录下所有的.tex文件")
parser.add_argument(
    "--fdst", type=argparse.FileType('w'),
    help="修改完样式的文件, 只在填了fsrc时有效, 不填则就地转换")
parser.add_argument(
    "-c", "--color", help="(elegantnote的参数)主题", default='black')
parser.add_argument(
    "-d", "--device", help="(elegantnote的参数)设备", default='normal')
parser.add_argument(
    "-l", "--lang", help="(elegantnote的参数)语言", default='cn')
parser.add_argument(
    "-b", "--mode", help="(elegantnote的参数)背景颜色")
parser.add_argument(
    "-m", "--math", help="(elegantnote的参数)数学字体")
parser.add_argument(
    "-z", "--chinesefont", help="(elegantnote的参数)中文字体")
args = parser.parse_args()

args_dict = {k: v for k, v in args.__dict__.items()
             if v is not None and k not in ('fsrc', 'fdst')}

if args.fsrc is not None:
    change_one_file(args.fsrc, args.fdst, args_dict)
else:
    files = [f for f in os.listdir()
             if f.rpartition('.')[-1] == 'tex']
    for f in files:
        with open(f, 'r', encoding='utf-8') as fp:
            change_one_file(fp, None, args_dict)

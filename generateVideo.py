# coding=utf-8
import cv2
import os.path
import sys


def generateVideo(rootdir, output, type, scale, fps):
    """
    视频组帧程序，用于满足由单帧影像组成视频的需求

    :param rootdir: 用户输入存放影像的文件夹目录，如E:\L0
    :param output: 输出视频路径
    :param type: 考虑到适用性，增加了影像文件类型的选择，如tif、jpg、png等
    :param scale: 考虑原始影像可能非常大，如4096*3072，直接拼接成视频可能不方便观看,因此设置了缩放因子，这样可以指定输出视频的大小
    :param fps: 用于控制输出视频帧率
    :return: 空
    """

    separator = os.path.sep

    print "Processing...\n"

    # list，用于存放遍历得到的用户指定类型的影像文件
    paths = []

    # 遍历
    for parent, dirname, filenames in os.walk(rootdir):
        for filename in filenames:
            # 判断，如果是用户指定的类型则添加到list，否则什么也不做
            # 这里用endswith更好一些，因为如果用contains，有可能有些文件是".tif.xml"
            # 这样即使不是tif，但是还是会被加进来，但用endswith就不会了
            if filename.endswith(type):
                paths.append(parent + separator + filename)

    paths.sort()
    if paths.__len__() is not 0:
        for path in paths:
            print path
    print paths.__len__(), "frames were found."

    # 读取第一张影像，获取其大小，然后计算输出视频的大小
    tem = cv2.imread(paths[0])
    width = int(scale * tem.shape[1])
    height = int(scale * tem.shape[0])

    # 指定输出视频的编码器以及相关参数
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output, fourcc, fps, (width, height))

    # 用于统计进度的循环变量
    count = 0

    # 循环处理每一帧，组成视频
    for items in paths:
        frame = cv2.imread(items)
        frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
        out.write(frame)
        count += 1
        print items + "  " + ((count * 1.0 / paths.__len__()) * 100).__str__() + " %"

    # 释放VideoWriter对象
    out.release()

    print "--------------------------------"
    print "Output Video Information:"
    print "Output path:" + output
    print "Width:" + width.__str__()
    print "Height:" + height.__str__()
    print "FPS:" + fps.__str__()
    print "Frames:" + paths.__len__().__str__()
    print "Time:" + (paths.__len__() * 1.0 / fps * 1.0).__str__() + " s"
    print "--------------------------------"


if sys.argv.__len__() == 2 and sys.argv[1] == "help":
    print("用于将一帧帧的影像组成视频，支持自定义视频宽高、fps\n")
    print("脚本启动命令格式：")
    print("scriptname.py:[rootdir] [output] [type] [scale] [fps]")
    print("\n函数帮助:")
    exec "help(generateVideo)"
elif sys.argv.__len__() == 6:
    generateVideo(sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]))
else:
    print("Input \"scriptname.py help\" for help information.")

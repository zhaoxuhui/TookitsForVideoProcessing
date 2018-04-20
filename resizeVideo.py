# coding=utf-8
import cv2
import os.path
import sys


def resizeVideo(video_path, out_path, ratio):
    """
    对视频进行缩放

    :param video_path: 视频路径
    :param out_path: 输出视频名称
    :param ratio: 缩放比例
    :return: 空
    """

    separator = os.path.sep

    # 需要处理的视频文件
    cap = cv2.VideoCapture(video_path)

    # 获取视频的总帧数、fps
    frames = int(cap.get(7))
    fps = int(cap.get(5))
    width = int(cap.get(3))
    height = int(cap.get(4))
    new_width = int(ratio * width)
    new_height = int(ratio * height)

    print frames, 'frames in total.'

    print '---Resizing---'

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(out_path, fourcc, fps, (new_width, new_height))

    # 循环输出帧
    for i in range(0, frames, 1):
        ret, frame = cap.read()
        if frame is None:
            break
        else:
            res = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
            out.write(res)
            print 'Resizing...', round((i * 1.0 / (frames)) * 100, 2), "% finished."
    # 释放对象
    cap.release()
    out.release()


if sys.argv.__len__() == 2 and sys.argv[1] == "help":
    print("用于对视频进行缩放\n")
    print("脚本启动命令格式：")
    print("scriptname.py:[video_path] [out_path] [ratio]")
    print("\n函数帮助:")
    exec "help(resizeVideo)"
elif sys.argv.__len__() == 4:
    resizeVideo(sys.argv[1], sys.argv[2], float(sys.argv[3]))
else:
    print("Input \"scriptname.py help\" for help information.")

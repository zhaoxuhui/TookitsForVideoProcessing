# coding=utf-8
import cv2
import os.path
import sys


def clipVideo(video_path, out_path, start, end):
    """
    截取视频片段

    :param video_path: 视频路径
    :param out_path: 输出视频名称
    :param start: 起始时间，单位为秒
    :param end: 结束时间，单位为秒
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

    print (frames.__str__() + ' frames in total.')

    # 计算需要输出的帧数
    startIndex = int(start * fps)
    endIndex = int(end * fps)
    if endIndex > frames:
        endIndex = frames
    rangeFrames = endIndex - startIndex

    # 判断如果小于0，返回
    if rangeFrames < 0:
        print ('Error.')
        exit()

    # 输出提示信息
    print (rangeFrames.__str__() + ' frames are going to be outputted.')

    print ('---Cutting---')

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(out_path, fourcc, fps, (width, height))

    cap.set(cv2.CAP_PROP_POS_FRAMES, startIndex)

    # 循环输出帧
    for i in range(startIndex, endIndex, 1):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if frame is None:
            break
        else:
            out.write(frame)
            print ('Cutting...' + round(((i - startIndex) * 1.0 / (rangeFrames)) * 100, 2).__str__() + "% finished.")
    # 释放对象
    cap.release()
    out.release()


if sys.argv.__len__() == 2 and sys.argv[1] == "help":
    print("用于剪切视频片段\n")
    print("脚本启动命令格式：")
    print("scriptname.py:[video_path] [out_path] [start] [end]")
    print("\n函数帮助:")
    exec ("help(clipVideo)")
elif sys.argv.__len__() == 5:
    clipVideo(sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]))
else:
    print("Input \"scriptname.py help\" for help information.")

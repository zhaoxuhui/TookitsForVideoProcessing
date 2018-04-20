# coding=utf-8
import cv2
import os.path
import sys


def splitVideo(video_path, out_path, interval, start, end):
    """
    拆分视频

    :param video_path: 视频路径
    :param out_path: 输出影像的文件夹
    :param interval: 采样间隔，1表示逐帧输出
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

    print frames, 'frames in total.'

    # 计算需要输出的帧数
    startIndex = int(start * fps)
    endIndex = int(end * fps)
    if endIndex > frames:
        endIndex = frames
    rangeFrames = endIndex - startIndex

    # 判断如果小于0，返回
    if rangeFrames < 0:
        print 'Error.'
        exit()

    # 输出提示信息
    print rangeFrames / interval, 'frames are going to be outputted.'

    print '---Cutting---'

    cap.set(cv2.CAP_PROP_POS_FRAMES, startIndex)

    # 循环输出帧
    for i in range(startIndex, endIndex, interval):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if frame is None:
            break
        else:
            # 输出影像文件
            cv2.imwrite(out_path + separator + "%04d" % (startIndex + i + 1) + ".jpg", frame)
            print 'Cutting...', round(((i - startIndex) * 1.0 / (rangeFrames)) * 100, 2), "% finished."
    # 释放对象
    cap.release()


if sys.argv.__len__() == 2 and sys.argv[1] == "help":
    print("用于将视频拆分成一帧帧的图像，便于后续处理，支持设置起始、结束位置以及采样间隔\n")
    print("脚本启动命令格式：")
    print("scriptname.py:[video_path] [out_path] [interval] [start] [end]")
    print("\n函数帮助:")
    exec "help(splitVideo)"
elif sys.argv.__len__() == 6:
    print("calibrationWithCamera")
    splitVideo(sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]))
else:
    print("Input \"scriptname.py help\" for help information.")

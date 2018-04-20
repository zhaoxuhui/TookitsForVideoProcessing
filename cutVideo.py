# coding=utf-8
import cv2
import sys


def cutVideo(input_path, out_path, left_top_x, left_top_y, right_bottom_x, right_bottom_y):
    """
    视频画幅裁剪，用于实现对ROI的提取

    :param input_path: 输入视频路径
    :param out_path: 输出视频路径
    :param left_top_x: 左上角点x坐标
    :param left_top_y: 左上角点y坐标
    :param right_bottom_x: 右下角点x坐标
    :param right_bottom_y: 右下角点y坐标
    :return: 空
    """

    cap = cv2.VideoCapture(input_path)

    width = int(cap.get(3))
    height = int(cap.get(4))
    total = int(cap.get(7))

    print 'x:', width, 'y:', height

    fps = 20
    waitTime = 1
    count = 0

    if cap.get(5) != 0:
        waitTime = int(1000.0 / cap.get(5))
        fps = cap.get(5)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(out_path, fourcc, fps, (right_bottom_x - left_top_x, right_bottom_y - left_top_y))

    while cap.isOpened():
        ret, frame = cap.read()
        if frame is None:
            break
        else:
            res = frame[left_top_y:right_bottom_y, left_top_x:right_bottom_x, :]

            out.write(res)
            cv2.imshow("frame", res)
            count += 1
            print round((count * 1.0 / total) * 100, 2), '%'
            k = cv2.waitKey(waitTime) & 0xFF
            if k == 27:
                break

    cap.release()
    out.release()


if sys.argv.__len__() == 2 and sys.argv[1] == "help":
    print("对视频画面大小进行裁剪，提取感兴趣区域\n")
    print("脚本启动命令格式：")
    print("scriptname.py:[input_path] [out_path] [left_top_x] [left_top_y] [right_bottom_x] [right_bottom_y]")
    print("\n函数帮助:")
    exec "help(cutVideo)"
elif sys.argv.__len__() == 7:
    input_path = sys.argv[1]
    out_path = sys.argv[2]
    left_top_x = float(sys.argv[3])
    left_top_y = float(sys.argv[4])
    right_bottom_x = float(sys.argv[5])
    right_bottom_y = float(sys.argv[6])
    cutVideo(input_path, out_path, left_top_x, left_top_y, right_bottom_x, right_bottom_y)
else:
    print("Input \"scriptname.py help\" for help information.")

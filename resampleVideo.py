# coding=utf-8
import cv2

# 用于视频解帧，实现由视频到帧图像的功能

# 输入需要处理的视频文件
video_path = raw_input("Input path of video:\n")
cap = cv2.VideoCapture(video_path)

# 获取视频的总帧数、fps
frames = int(cap.get(7))
fps = int(cap.get(5))

print frames, 'frames in total.'

# 输入输出影像的文件夹
out_path = raw_input("Input save path of frames:\n")

# 输入采样间隔
interval = 1
interval = input("Input interval of frames(1 means output every frame):\n")

# 输入开始时间
start = 0
start = input("Input start time of output(e.g. 10.3 means starts from 10.3 second):\n")

# 输入结束时间
end = 0
end = input("Input end time of output(e.g. 20.1 means ends at 20.1 second):\n")

# 计算需要输出的帧数
startIndex = int(start * fps)
endIndex = int(end * fps)
rangeFrames = endIndex - startIndex
count = 0

# 判断如果小于0，返回
if rangeFrames < 0:
    print 'Error.'
    exit()

# 输出提示信息
print rangeFrames / interval, 'frames are going to be outputted.'

# 读取开始帧之前的内容，将将读取帧数定位到startIndex
for i in range(startIndex):
    ret, frame = cap.read()
    print "Pre-processing...", round((i * 1.0 + 1) / startIndex * 100, 2), '%'

print '---Cutting---'

# 循环输出帧
for i in range(startIndex, endIndex, interval):
    ret, frame = cap.read()
    if frame is None:
        break
    else:
        # 输出影像文件
        cv2.imwrite(out_path + "\\" + "%04d" % (i + 1) + ".jpg", frame)
        count += 1
        print 'Cutting...', round((count * 1.0 / (rangeFrames / interval)) * 100, 2), "% finished."
# 释放对象
cap.release()
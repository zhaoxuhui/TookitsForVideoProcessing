# coding=utf-8
import cv2

# 视频裁剪程序，用于满足视频时长裁剪的需求

# 输入需要处理的视频文件
video_path = raw_input("Input path of video:\n")
cap = cv2.VideoCapture(video_path)

# 获取视频的总帧数、fps
frames = int(cap.get(7))
fps = int(cap.get(5))

print (round(frames / fps, 2)).__str__(), 'seconds(', frames, 'frames', ') in total.'

# 输入输出影像的文件夹
out_path = raw_input("Input save path of video:\n")

# 输入开始时间
start = 0
start = input("Start second of output( >=0 ):\n")

# 输入结束时间
end = 0
str = "End second of output( <" + (frames / fps).__str__() + " )\n"
end = input(str)

# 计算需要输出的帧数
startIndex = int(start * fps)
endIndex = int(end * fps)
rangeFrames = endIndex - startIndex
count = 0

video_h = int(cap.get(4))
video_w = int(cap.get(3))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(out_path, fourcc, fps, (video_w, video_h))

# 判断如果小于0，返回
if rangeFrames < 0:
    print 'Error.'
    exit()

# 输出提示信息
print rangeFrames, 'frames are going to be outputted.'

# 读取开始帧之前的内容，将将读取帧数定位到startIndex
for i in range(startIndex):
    ret, frame = cap.read()
    print "Pre-processing...", round((i * 1.0 + 1) / startIndex * 100, 2), '%'

print '---Cutting---'

# 循环输出帧
for i in range(startIndex, endIndex):
    ret, frame = cap.read()
    if frame is None:
        break
    else:
        # 输出影像文件
        out.write(frame)
        count += 1
        print 'Cutting...', round((count * 1.0 / rangeFrames) * 100, 2), "% finished."
# 释放对象
cap.release()
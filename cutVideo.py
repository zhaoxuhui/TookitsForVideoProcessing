# coding=utf-8
import cv2

# 视频画幅裁剪，用于实现对ROI的提取

input_path = raw_input("Video path:\n")

out_path = raw_input("Out path:\n")

cap = cv2.VideoCapture(input_path)

width = int(cap.get(3))
height = int(cap.get(4))
total = int(cap.get(7))

print 'x:', width, 'y:', height

left_top_x = input("left-top x:\n")

left_top_y = input("left-top y:\n")

right_bottom_x = input("right-bottom x:\n")

right_bottom_y = input("right-bottom y:\n")

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
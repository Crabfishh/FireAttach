# import numpy as np
# import cv2
# from socket import *
#
# sock = socket(AF_INET, SOCK_DGRAM) # 创建UDP套接字
# Host = '10.151.9.214'
# Port = 5005
# sock.bind((Host,Port))
# sock.setblocking(0) # 设置为非阻塞模式
# # 非阻塞模式 当程序碰到耗时操作，分发给别的线程，主线程继续执行，这样可以提升程序的效率
#
# while True:
#     data = None
#     try:
#         #640*400 *3 *1  = 768000
#         data, address = sock.recvfrom(921600)
#         receive_data = np.frombuffer(data, dtype='uint8')
#         img = cv2.imdecode(receive_data, 1)
#
#         cv2.imshow('server', img)
#     except BlockingIOError as e:
#         pass
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cv2.destroyAllWindows()
#
# # import cv2
# # import numpy as np
# #
# # cap = cv2.VideoCapture('http://192.168.123.15:9205/video')  # 替换成你的摄像头地址或索引
# #
# # while True:
# #     ret, frame = cap.read()
# #     if not ret:
# #         break
# #
# #     # 在这里调用 YOLOv5 模型进行检测，将 frame 传递给模型
# #
# #     cv2.imshow('Frame', frame)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break
# #
# # cap.release()
# # cv2.destroyAllWindows()



import numpy as np
import cv2
from socket import *
import API_use
import tempfile
import os

def main():
    sock = socket(AF_INET, SOCK_DGRAM) # 创建UDP套接字
    Host = '10.151.9.214'
    Port = 5005
    sock.bind((Host,Port))
    sock.setblocking(0) # 设置为非阻塞模式


    while True:
        data = None
        try:
            # 640*400 *3 *1  = 768000
            data, address = sock.recvfrom(921600)
            receive_data = np.frombuffer(data, dtype='uint8')
            img = cv2.imdecode(receive_data, 1)
            print("Successed to catch the video now began to detect...")

            # 保存图像到临时文件
            temp_dir = tempfile.mkdtemp()
            temp_file_path = os.path.join(temp_dir, 'temp_image.jpg')
            cv2.imwrite(temp_file_path, img)

            img0 = API_use.run(source = temp_file_path)
            # 运行目标检测
            # img_with_detections = run_object_detection(img, model)
            # 在窗口中显示图像
            cv2.imshow('server', img0)
        except BlockingIOError as e:
            pass
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

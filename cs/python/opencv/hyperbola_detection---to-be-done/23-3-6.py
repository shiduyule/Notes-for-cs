import cv2
import os
#%% 定义函数
def extract_frames(video_path, output_folder, interval):
    # 创建输出文件夹（如果不存在）
    os.makedirs('%f-split'%video_path, exist_ok=True)
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)   
    # 确定帧率和总帧数
    fps = cap.get(cv2.CAP_PROP_FPS)  # fps 是帧率的
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # frame_count 是总帧数
    
    
    
    interval = 
    
    # 计算每个间隔需要跳过的帧数
    interval_frames = int(fps * interval)
    # 初始化帧计数器
    count = 0
    # 循环读取视频帧
    while cap.isOpened():
        # 读取一帧
        ret, frame = cap.read()
        if ret:
            # 如果是间隔帧，保存图像
            if count % interval_frames == 0:
                frame_path = os.path.join(output_folder, f"frame_{count}.jpg")
                cv2.imwrite(frame_path, frame)
            # 增加帧计数器
            count += 1
            # 如果已经读取完所有帧，停止循环
            if count >= frame_count:
                break
        else:
            break    
    # 释放视频对象
    cap.release()
extract_frames("video.avi", "frames", 1.0)

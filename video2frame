import cv2

video_path = 'E:/bad_apple.mp4'
pic_path = 'E:/BadApple/'
video = cv2.VideoCapture(video_path)
count = 1
while video.isOpened():
    flag, img = video.read()
    if not flag:
        break
    cv2.imwrite(pic_path + str(count) + '.jpg',img)
    print(count, 'Succeed!')
    count += 1

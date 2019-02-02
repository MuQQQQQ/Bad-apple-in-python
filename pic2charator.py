import cv2
import time
import pickle
import tkinter
path = "E:/BadApple/"                                                                               #图片文件夹地址
total = 6558
total_str = []                                                                                      #每一副图片是列表的一个元素
for count in range(1, total + 1):
    height = 540                                                                                    #图片高度及宽度
    width = 720
    pic_str = ''                                                                                    #存放当前处理的图片生成的字符画
    pic_path = path + str(count) + '.jpg'
    img = cv2.imread(pic_path, cv2.IMREAD_GRAYSCALE)                                                #以灰度形式打开图片
    for col in range(0, height, 12):                                                                #遍历每一个像素
        pic_str1 = ''
        pic_str2 = ''
        for row in range(0, width, 6):
            ch1 = [' ', '.', ':', '+', 'c', 'X', 'F', 'M', '@'][int(img[col, row] / 29)]            #灰度值越高字符密度越小
            ch2 = [' ', '.', ':', '+', 'c', 'X', 'F', 'M', '@'][int((255-img[col, row]) / 29)]      #灰度值越高字符密度越大
            pic_str1 += ch1
            pic_str2 += ch2
        pic_str += pic_str2[::-1] + '  |  ' + pic_str1 + '\n'                                       #pic_str2[::-1]倒置字符串
    total_str.append(pic_str)
    print(count,'has been character-picture!')
with open(path+'0.dat', 'wb') as fp:
    pickle.dump(total_str, fp)

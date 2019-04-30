from pytesseract import image_to_string
import cv2
import numpy as np
im_gray = cv2.imread('front3.jpg', cv2.IMREAD_GRAYSCALE)
#(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
im_bw = im_gray


thresh = 90
im_bw = cv2.threshold(im_bw, thresh, 255, cv2.THRESH_BINARY)[1]



kernel=np.ones((2,2),np.uint8)
kernel1=np.ones((3,3),np.uint8)
im_bw=cv2.dilate(im_bw,kernel,iterations = 1)
im_bw=cv2.erode(im_bw,kernel1,iterations = 1)
for i in range(8):
	im_bw=cv2.blur(im_bw,(2,2))

kernel2 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
im_bw= cv2.filter2D(im_bw, -1, kernel2)

cv2.imwrite('bla.png',im_bw)
pic = im_gray[50:350,50:275]
cv2.imwrite('ola.png',pic)
Name = im_bw[150:315, 400:1000]
cv2.imwrite('yarab2.png',Name)
address = im_bw[300:450, 400:1000]
cv2.imwrite('yarab.png',address)
ID = im_bw[500:560,400:1000]
name=image_to_string(Name,lang="ara")
add=image_to_string(address,lang="ara")
IDNumber=image_to_string(ID,lang="eng")
IDNumber= ''.join(IDNumber.split())
print(IDNumber)
if IDNumber[0]=='2': 
	year = '19' + IDNumber[1:3]
else:
	year = '20' + IDNumber[1:3]
month = IDNumber[3:5]
day = IDNumber[5:7]
BDate = year + '/' + month + '/'+ day
ocr_output=open("text.txt","w+")
ocr_output.write(name)
ocr_output.write('\n')
ocr_output.write(add)
ocr_output.write('\n')
ocr_output.write(IDNumber)
ocr_output.write('\n')
ocr_output.write(BDate)
ocr_output.close()


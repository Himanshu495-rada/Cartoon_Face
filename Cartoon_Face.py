import cv2
import numpy as np
from tkinter import filedialog
try:
	num_down = 2
	num_bilateral = 7

	img_file = filedialog.askopenfilename()

	img = cv2.imread(str(img_file))
	img = cv2.resize(img, (800,800))

	for _ in range(num_down):
	    img = cv2.pyrDown(img)

	for _ in range(num_bilateral):
	    img = cv2.bilateralFilter(img, d=9, sigmaColor=9, sigmaSpace=7)

	for _ in range(num_down):
	    img = cv2.pyrUp(img)

	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img_blur = cv2.medianBlur(img_gray, 7)

	img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)
	img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2BGR)
	img_cartoon = cv2.bitwise_and(img, img_edge)

	a = int(input("1: Display Image\n2: Save Image\n"))
	if a == 1:
		print("Press any key to exit")
		cv2.imshow("Cartoon", img_cartoon)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	elif a == 2:
		name = input("Filename:  ")
		cv2.imwrite(name,img_cartoon)
except:
	print("Please use another image")

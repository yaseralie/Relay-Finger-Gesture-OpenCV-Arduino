import cv2
import time
import os
import HandTrackingModule as htm
import serial 

#Setting for COM Port
ser = serial.Serial(port='COM3', baudrate=9600, timeout=1)

#Seting for cam
#wCam, hCam = 720, 480
wCam, hCam = 900, 506
cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)

overlayList = []
#print(len(overlayList))

pTime = 0
detector = htm.handDetector(detectionCon=0.75)
tipIds = [4, 8, 12, 16, 20]
lamp = 6
lamp_before=6
attempt = 0
pesan=""
color = (0, 0, 255)
while True:
	success, img = cap.read()
	img = detector.findHands(img)
	lmList = detector.findPosition(img, draw=False)
	# print(lmList)
	if len(lmList) != 0:
		fingers = []
		# Thumb
		if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
			fingers.append(1)
		else:
			fingers.append(0)
		# 4 Fingers
		for id in range(1, 5):
			if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
				fingers.append(1)
			else:
				fingers.append(0)
		totalFingers = fingers.count(1)

		if totalFingers!=lamp_before and attempt==0:
			lamp = int(totalFingers)
			#print(lamp)
			if lamp!=0 and lamp!=5:
				pesan = "Lamp No." + str(lamp) + " selected"
				color = (255, 0, 0)
						
			if totalFingers == 0 and lamp_before!=5 and lamp_before!=6:
				pesan = "Turn OFF lamp no: " + str(lamp_before)
				color = (0, 0, 255)
				print(pesan)

				command = str(lamp_before) + "off"
				ser.write(command.encode())
				ser.close
				print(command)

				attempt=0

			if totalFingers == 5 and lamp_before!=0 and lamp_before!=6:
				pesan="Turn ON lamp no: " + str(lamp_before)
				color = (0, 255, 0)
				print(pesan)

				command = str(lamp_before) + "on"
				ser.write(command.encode())
				ser.close
				print(command)

				attempt=0
			lamp_before=int(totalFingers)
		
		attempt=attempt+1

		if attempt==8:
			attempt=0			
			

	cv2.putText(img, pesan, (10, img.shape[0] - 30),
		cv2.FONT_HERSHEY_COMPLEX, 0.80, color, 2)	
	cv2.imshow("Image", img)
	cv2.waitKey(3)

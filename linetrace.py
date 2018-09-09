#Import modules
import picamera
import picamera.array
import time
import cv2
import numpy as np
import explorerhat

#Initialize camera
camera = picamera.PiCamera()




while(1):

        camera.resolution = (96,64)
        rawCapture = picamera.array.PiRGBArray(camera)
        #Let camera warm up
        time.sleep(0.4)

	#Capture image
	camera.capture(rawCapture, format="bgr")
	img = rawCapture.array

	#Convert to Grayscale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	#Blur image to reduce noise
	blurred = cv2.GaussianBlur(gray, (9, 9), 0)

	#Perform canny edge-detection
	edged = cv2.Canny(blurred, 50, 150)

	#Perform hough lines probalistic transform
	lines = cv2.HoughLinesP(edged,1,np.pi/180,1,1,1)

	#Draw lines on input image
	if(lines != None):
    	    for x1,y1,x2,y2 in lines[0]:
		if (y2 < 30 ):
			if ( x2 < 30):
				print("turn to left")
                                explorerhat.motor.one.forwards(60)
                                explorerhat.motor.two.forwards(0)
                                time.sleep(0.5)
                                explorerhat.motor.one.forwards(0)
                                explorerhat.motor.two.forwards(0)
                                time.sleep(0.2)
	                elif ( x2 < 66) :
				print("go straight")
                                explorerhat.motor.one.forwards(60)
                                explorerhat.motor.two.forwards(60)
                                time.sleep(0.5)
                                explorerhat.motor.one.forwards(0)
                                explorerhat.motor.two.forwards(0)
				time.sleep(0.2)
                                
	                else:
				print("turn to right")
                                explorerhat.motor.one.forwards(0)
                                explorerhat.motor.two.forwards(60)
                                time.sleep(0.5)
                                explorerhat.motor.one.forwards(0)
                                explorerhat.motor.two.forwards(0)
				time.sleep(0.2)

                        print('x1:{0}, y1:{1},x2:{2}, y2:{3}'.format(x1, y1,x2, y2 ))
	                break

        	cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
                #cv2.imshow("line detect test", img) 
		#cv2.waitKey(0)
                #cv2.destroyAllWindows()

	
	#k = cv2.waitKey(1)
        #if k == ord('q'):
            #break
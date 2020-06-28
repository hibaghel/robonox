# import the necessary packages
import time
import cv2
import argparse
from pyzbar import pyzbar
from imutils.video import VideoStream
import imutils

# all the valid pincodes which are to be detected
# pincode and coressponding return type 
__pincodes = {"175005" : 1,
			  "160063" : 2, 
			  "140012": 3}

def __detect(frame):
	# resize for easier processing 
	frame = imutils.resize(frame, width=400)
	barcodes = pyzbar.decode("frame")

	# if no barcode is found, return None
	if len(barcodes) == 0:
		return None
	
	# loop over different barcodes found 

	for barcode in barcodes:
		# read barcode data  
		barcodeData = barcode.data.decode("utf-8")

		# check barcode data for a valid pincode, return the cart number if found
		if barcodeData in __pincodes:
			return __pincodes[barcodeData]
	
	return None

def scan_video():
	# start recording from PiCamera 
	vs = VideoStream(usePiCamera=True).start()
	time.sleep(2.0)

	# keep looping over the frames
	while True:
		# grab the current frame and then handle if the frame is returned
		# from either the 'VideoCapture' or 'VideoStream' object,
		# respectively
		frame = vs.read()
	
		# break if no frame is detected
		if frame is None:
			break

		# detect the barcode in the image
		pin = __detect(frame)

		# if a barcode was found, return pincode
		if pin is not None:
			return pin
		
		return None

import cv2 as cv

#Displaying image on new window....

#img = cv.imread('image.jpg')
#cv.imshow('ImageWindow', img)
#cv.waitKey()


#------------------------------------------------------------------------


#Displaying Video on new window....

# capture = cv.VideoCapture('abc.mp4')

# while True:
# 	isTrue, frame = capture.read()
# 	cv.imshow('Video',frame)

# 	if cv.waitKey(20) & 0xFF==ord('d'):
# 		break

# capture.release()
# cv.destroyAllWindows()


#------------------------------------------------------------------------


#Displaying Image on new window with a scalable size....

def rescale(frame, scale=0.5):
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	dimension = (width,height)
	return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

img = cv.imread('image.jpg')
rescale_img = rescale(img)
cv.imshow('ImageWindow', rescale_img)
cv.waitKey()


#------------------------------------------------------------------------


#Displaying Video on new window with a scalable size....

# def rescale(frame, scale=0.5):
# 	width = int(frame.shape[1] * scale)
# 	height = int(frame.shape[0] * scale)
# 	dimension = (width,height)
# 	return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

# capture = cv.VideoCapture('abc.mp4')

# while True:
	
# 	frame_resized = rescale(frame)

# 	cv.imshow('Resized_Video',frame_resized)

# 	if cv.waitKey(20) & 0xFF==ord('d'):
# 		break

# capture.release()
# cv.destroyAllWindows()


#------------------------------------------------------------------------



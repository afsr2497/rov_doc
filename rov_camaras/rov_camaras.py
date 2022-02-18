import cv2

fuente = "rtsp://192.168.226.201:554"

rov_cam = cv2.VideoCapture(fuente)
while(rov_cam.isOpened()):
    ret,img = rov_cam.read()
    if ret == True:
        cv2.imshow('rov_vid',img)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
rov_cam.release()
cv2.destroyAllWindows()
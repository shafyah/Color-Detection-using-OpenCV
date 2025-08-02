import cv2 

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while True:
        _,frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        height,width,_ = frame.shape

        cx = int (width / 2)
        cy = int (height / 2)

        pixel_center = hsv_frame [cy, cx ]
        hue_value = pixel_center[0]

        if (0 <= hue_value <= 5) or (170 <= hue_value <= 179):
                color = "RED"
        elif 6 <= hue_value <= 15:
                 color = "ORANGE"
        elif 16 <= hue_value <= 25:
                 color = "YELLOW"
        elif 26 <= hue_value <= 85:
                   color = "GREEN"
        elif 86 <= hue_value <= 125:
                  color = "BLUE"
        elif 126 <= hue_value <= 169:
                 color = "VIOLET"
        else:
                  color = "Undefined"

        pixel_center_bgr = frame [cy,cx]
        b,g,r =int( pixel_center_bgr[0]) ,int (pixel_center_bgr [1] ),int (pixel_center_bgr[2])
        
        
        cv2.putText(frame, color, (10,70), 0, 1.5,(b,g,r),2)
        cv2.circle(frame, (cx, cy), 5,(25,25,25),3)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27: 
                break
        
cap.release()
cv2.destroyAllWindows()
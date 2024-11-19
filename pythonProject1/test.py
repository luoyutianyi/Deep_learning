import cv2
vc = cv2.VideoCapture('"F:\h\铜矿\铜铜特攻队PW114514\可莉.mp4"')
if vc.isOpened():
    open , frame = vc.read()
else:
    open = False
while open:
    ret,frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.show('result', gray)
        if cv2.waitKey(10) & 0xFF ==27:
            break
vc.release()
cv2.destroyAllWindows()
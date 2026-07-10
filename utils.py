import time
import cv2

# init " pTime = time.time() " before the While loop
def get_fps(cap, pTime,type='default'):
    if type == "default":
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        return fps, pTime

    elif type =="cap":
        fps= cap.get(cv2.CAP_PROP_FPS)
        if fps<= 0:
            return 30, pTime
        return fps, pTime
    else:
        return 30, pTime

def HUD(img,fingers):
    overlay_box = img.copy()
    cv2.rectangle(overlay_box, (1080, 315), (1280, 415), (183, 81, 93), cv2.FILLED)

    cv2.addWeighted(overlay_box, 0.45, img, 0.55, 0, img)

    cv2.rectangle(img, (1080, 315), (1280, 415), (255, 255, 255), 2)

    text = f"Count: {fingers}"
    cv2.putText(img, text, (1100, 375), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.9, (255, 255, 255), 2, cv2.LINE_AA)

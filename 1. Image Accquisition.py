import cv2
import numpy as np

img = cv2.imread('snek.jpg', 0)
cv2.imshow('Snek', img)

k = cv2.waitKey(0)

if k == 27:
    # Wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):
    # Wait for 's' key to save and exit
    cv2.imwrite('snek-grayscale.jpg', img)
    cv2.destroyAllWindows()

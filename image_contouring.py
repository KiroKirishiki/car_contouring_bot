import numpy as np
import cv2 as cv2

def auto_canny(image, sigma = 0.33):
    # Compute the median of the image
    v = np.median(image)
    # Apply Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(max(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    # return the edged image
    return edged

def get_contours(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Add blur
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    # Find Canny edges
    edged = auto_canny(blurred)
    # Finding Contours
    contours, hierarchy = cv2.findContours(edged,
                                       cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

# Draw all contours on white background
def draw_contours(contours, image):
    # Create white background with the shape of the image
    whiteimage = np.zeros([image.shape[0], image.shape[1], 3], dtype=np.uint8)
    whiteimage.fill(255)
    # Apply contours on the white background
    cv2.drawContours(whiteimage, contours, -1, (0, 0, 0), 3)
    return whiteimage
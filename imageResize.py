import cv2

image = cv2.imread("image1.png")
window_name = "image"
cv2.imshow(window_name,image)

scale_percent = 50

width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)

dsize = (width, height)

output = cv2.resize(image, dsize)

cv2.imwrite("resized.png", output)
cv2.waitKey(0)
# cv2.destroyAllWindows()

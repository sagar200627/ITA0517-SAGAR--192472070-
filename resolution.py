import cv2

# Read the input image
img = cv2.imread("image1.jpg")

# Check if image is loaded
if img is None:
    print("Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Enhance the image using Histogram Equalization
enhanced = cv2.equalizeHist(gray)

# Display images
cv2.imshow("Original Image", gray)
cv2.imshow("Enhanced Image", enhanced)

# Save the enhanced image
cv2.imwrite("enhanced_image.jpg", enhanced)

cv2.waitKey(0)
cv2.destroyAllWindows()
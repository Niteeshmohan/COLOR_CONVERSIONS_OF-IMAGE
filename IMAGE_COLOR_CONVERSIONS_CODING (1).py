i)Read and Display an Image
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('img1.jpg')
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')  
plt.show()

ii)Draw Shapes and Add Text

1)Draw a line from the top-left to the bottom-right of the image.
img=cv2.imread('img1.jpg')
cv2.line(img, (0, 0), (1200, 1200), (0, 255, 0), 7)
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')  
plt.show()

2) Draw a circle at the center of the image.
img=cv2.imread('img1.jpg')
cv2.circle(img, (600, 600), 100, (255, 0, 0), thickness=12)
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')  
plt.show()

3) Draw a rectangle around a specific region of interest in the image.
img=cv2.imread('img1.jpg')
img = cv2.rectangle(img,(0, 0) ,(1200, 1200), (0,0,255), 15)
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')  
plt.show()

4) Add the text "GROOT" at the top-left corner of the image.
img = cv2.imread("img1.jpg")
img = cv2.resize(img,(500,550))
font = cv2.FONT_HERSHEY_SIMPLEX
res = cv2.putText(img,"GROOT", (10,50), font,1, (255, 255, 255),7)
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')  
plt.show()

iii)Image Color Conversion

##Convert the image from RGB to HSV and display it
Display the original image
img = cv2.imread('img1.jpg', 1)
img = cv2.resize(img, (500, 550))
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title('Original Image')  
plt.axis('off')
plt.show()

Convert to HSV and display
hsv2_rgb= cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
plt.imshow(hsv2_rgb)
plt.title('RGB to HSV')
plt.axis('off')
plt.show()

###Convert the image from RGB to GRAY and display it.
img = cv2.imread('img1.jpg', 1)
img = cv2.resize(img, (500, 550))
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title('Original Image')  
plt.axis('off') 
plt.show()


gray_image = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
plt.imshow(gray_image,cmap='gray')#display it as a grayscale image
plt.title('RGB to GRAY')
plt.axis('off')
plt.show()

###Convert the image from RGB to YCrCb and display it.
img = cv2.imread('img1.jpg', 1)
img = cv2.resize(img, (500, 550))
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title('Original Image')  
plt.axis('off') 
plt.show()

ycrcb_image = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2YCrCb)
plt.imshow(ycrcb_image)
plt.title('RGB to YCrCb')
plt.axis('off')
plt.show()

4)Convert the HSV image back to RGB and display it.
img = cv2.imread('img1.jpg', 1)
img = cv2.resize(img, (500, 550))
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title('Original Image')  
plt.axis('off') 
plt.show()

rgb_converted = cv2.cvtColor(hsv2_rgb, cv2.COLOR_HSV2RGB)
plt.imshow(rgb_converted)
plt.title('HSV to RGB')
plt.axis('off')
plt.show()

###Access and Manipulate Image Pixels
img = cv2.imread('img1.jpg', 1)
img = cv2.resize(img, (500, 550))
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title('Original Image')  
plt.axis('off') 
plt.show()

img[150:200, 150:200] = [255, 255, 255] 
img_modified = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_modified)
plt.title('Image with white Square')
plt.axis('off')
plt.show()

###Image Resizing
img = cv2.imread("img1.jpg")
img = cv2.resize(img,(750,450))
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb) 
plt.axis('off') 
plt.show()

###Image Cropping
import cv2;
img = cv2.imread('img1.jpg')
crop=img[100:400, 250:550];
img_rgb = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.axis('off')
plt.show()

###Image Flipping
1) Flip the original image and display it.
img = cv2.imread('img1.jpg')
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
image_rgb = cv2.cvtColor(rotated_img, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')  
plt.title('Flipped Image')  
plt.show()

2)Flip the original image vertically and display it.
img = cv2.imread('img1.jpg')
flipped_image = cv2.flip(img, 0)
image_rgb= cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')  
plt.title('Vertically Flipped Image')  
plt.show()

###Write and Save the Modified Image
img = cv2.imread("img1.jpg")
img = cv2.resize(img,(300,300))
cv2.imwrite('groot.jpg',img)

# COLOR_CONVERSIONS_OF-IMAGE
## AIM
Write a Python program using OpenCV that performs the following tasks:

i) Read and Display an Image.

ii) 	Draw Shapes and Add Text.

iii) Image Color Conversion.

iv) Access and Manipulate Image Pixels.

v) Image Resizing

vi) Image Cropping

vii) Image Flipping

viii)	Write and Save the Modified Image


## Software Required:
Anaconda - Python 3.7
## Algorithm:
### Step1:
Load an image from your local directory and display it.
### Step2:
o	Draw a line from the top-left to the bottom-right of the image.
o	Draw a circle at the center of the image.
o	Draw a rectangle around a specific region of interest in the image.
o	Add the text "OpenCV Drawing" at the top-left corner of the image.

### Step3:
o	Convert the image from RGB to HSV and display it.
o	Convert the image from RGB to GRAY and display it.
o	Convert the image from RGB to YCrCb and display it.
o	Convert the HSV image back to RGB and display it.

### Step4:
o	Access and print the value of the pixel at coordinates (100, 100).
o	Modify the color of the pixel at (200, 200) to white.

### Step5:
o	Resize the original image to half its size and display it.
### Step6:
o	Crop a region of interest (ROI) from the image (e.g., a 100x100 pixel area starting at (50, 50)) and display it.
### Step7:
o	Flip the original image horizontally and display it.
o	Flip the original image vertically and display it.

### Step8:
o	Save the final modified image to your local directory.


## Program 
### Developed By: NITEESH M
### Register Number: 212222230098


### i)Read and Display an Image                                             
<table>
<tr>
<td>
      
```
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('img1.jpg')
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')  
plt.show()
```

</td>
<td>
   
![Screenshot 2024-09-24 174708](https://github.com/user-attachments/assets/bf3ccb01-1682-43c8-a091-acff1a370827)
         
<td>
      
</tr>
</table>

### ii)Draw Shapes and Add Text

#### 1)Draw a line from the top-left to the bottom-right of the image.
<table>
<tr>
<td>

```
img=cv2.imread('img1.jpg')
cv2.line(img, (0, 0), (1200, 1200), (0, 255, 0), 7)
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')  
plt.show()
```      
</td>

<td>
  
![Screenshot 2024-09-24 174726](https://github.com/user-attachments/assets/325d7621-886b-4c36-865e-d42a422a8f82)

</td>
</tr>
</table>

#### 2) Draw a circle at the center of the image.

<table>
<tr>
<td>

```
img=cv2.imread('img1.jpg')
cv2.circle(img, (600, 600), 100, (255, 0, 0), thickness=12)
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')  
plt.show()
```
</td>
<td>

![Screenshot 2024-09-24 174747](https://github.com/user-attachments/assets/6f8394bd-fb9f-46d6-9bc0-0d31654f1058)

</td>
</tr>
</table>

#### 3) Draw a rectangle around a specific region of interest in the image.
<table>
<tr>
<td>

 ```
img=cv2.imread('img1.jpg')
img = cv2.rectangle(img,(0, 0) ,(1200, 1200), (0,0,255), 15)
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')  
plt.show()
```
</td>
<td>
  
![Screenshot 2024-09-24 174805](https://github.com/user-attachments/assets/cd539c8e-a0cf-49ec-b02e-1a82e617a9ae) 
</td>
</tr>
</table>


#### 4) Add the text "GROOT" at the top-left corner of the image.
<table>
<tr>
<td>

```
img = cv2.imread("img1.jpg")
img = cv2.resize(img,(500,550))
font = cv2.FONT_HERSHEY_SIMPLEX
res = cv2.putText(img,"GROOT", (10,50), font,1, (255, 255, 255),7)
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')  
plt.show()
```
</td>
<td>
  
![Screenshot 2024-09-24 174817](https://github.com/user-attachments/assets/1f7f1db4-9957-497c-a6d8-58aae1ff7e15)

</td>
</tr>
</table>

### iii)Image Color Conversion
#### 1)Convert the image from RGB to HSV and display it


##### Display the original image
```
img = cv2.imread('img1.jpg', 1)
img = cv2.resize(img, (500, 550))
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title('Original Image')  
plt.axis('off')
plt.show()
```
##### Convert to HSV and display
```
hsv2_rgb= cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
plt.imshow(hsv2_rgb)
plt.title('RGB to HSV')
plt.axis('off')
plt.show()
```
#### OUTPUT
<table>
<tr>
<td> 
  
![Screenshot 2024-09-24 174841](https://github.com/user-attachments/assets/a1cfc79e-abdb-4ab2-82ca-78511287b817)
</td>
<td>
  
![Screenshot 2024-09-24 174902](https://github.com/user-attachments/assets/9fff09be-6c28-4cc9-91d4-f1fc34646d75)

</td>
</tr>
</table>

#### 2) Convert the image from RGB to GRAY and display it.

```
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
```

#### OUTPUT
<table>
<tr>
<td> 
  
![Screenshot 2024-09-24 174841](https://github.com/user-attachments/assets/ee2af843-bbb6-49c8-b0a8-290a479e6102)

</td>
<td>
  
![Screenshot 2024-09-24 174920](https://github.com/user-attachments/assets/574d60a3-b4cd-418d-8a88-b7a08a3569a9)


</td>
</tr>
</table>

#### 3)Convert the image from RGB to YCrCb and display it.

```
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
```

#### OUTPUT
<table>
<tr>
<td> 
  
![Screenshot 2024-09-24 174841](https://github.com/user-attachments/assets/549dcddc-8dc3-492b-b259-8783f2c57b06)


</td>
<td>
  

![Screenshot 2024-09-24 174938](https://github.com/user-attachments/assets/cf4c3107-a5e0-44bd-b7d9-baee9807fc9e)


</td>
</tr>
</table>

#### 4)Convert the HSV image back to RGB and display it.
```
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
```

#### OUTPUT
<table>
<tr>
<td> 
  
![Screenshot 2024-09-24 174841](https://github.com/user-attachments/assets/9794f764-2480-47c6-b2ff-debc22222d87)

</td>
<td>
  
![Screenshot 2024-09-24 175003](https://github.com/user-attachments/assets/a3afbc22-80b2-433a-b874-43fc0731701b)

</td>
</tr>
</table>



### iv)Access and Manipulate Image Pixels
```
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
```

#### OUTPUT

<table>
<tr>
<td> 
  
![Screenshot 2024-09-24 174841](https://github.com/user-attachments/assets/b4027398-199e-40a3-a504-430e121ba282)


</td>
<td>
  
![Screenshot 2024-09-24 175022](https://github.com/user-attachments/assets/96756559-dcfe-4041-8b63-a42979048dbb)


</td>
</tr>
</table>

### v)Image Resizing
```
img = cv2.imread("img1.jpg")
img = cv2.resize(img,(750,450))
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb) 
plt.axis('off') 
plt.show()
```

#### OUTPUT
<table>
<tr>
<td> 
  
![Screenshot 2024-09-24 174841](https://github.com/user-attachments/assets/b4027398-199e-40a3-a504-430e121ba282)


</td>
<td>
  
![Screenshot 2024-09-24 175039](https://github.com/user-attachments/assets/453e025e-436c-46fe-96f4-6a2b65a0d4d9)


</td>
</tr>
</table>


### vi)Image Cropping
```
import cv2;
img = cv2.imread('img1.jpg')
crop=img[100:400, 250:550];
img_rgb = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.axis('off')
plt.show()
```
#### OUTPUT

<table>
<tr>
<td> 
  
![Screenshot 2024-09-24 174841](https://github.com/user-attachments/assets/b4027398-199e-40a3-a504-430e121ba282)


</td>
<td>
  
![Screenshot 2024-09-24 175055](https://github.com/user-attachments/assets/330c3915-e726-4d65-9187-dcab02c80473)

</td>
</tr>
</table>

### vii)Image Flipping
#### 1) Flip the original image and display it.
```
img = cv2.imread('img1.jpg')
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
image_rgb = cv2.cvtColor(rotated_img, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')  
plt.title('Flipped Image')  
plt.show()
```

#### OUTPUT

<table>
<tr>
<td> 
  
![Screenshot 2024-09-24 174841](https://github.com/user-attachments/assets/b4027398-199e-40a3-a504-430e121ba282)


</td>
<td>
  
![Screenshot 2024-09-24 184240](https://github.com/user-attachments/assets/d9dd9fe4-7008-4135-ba4c-05ecff13710e)


</td>
</tr>
</table>

#### 2)Flip the original image vertically and display it.

```
img = cv2.imread('img1.jpg')
flipped_image = cv2.flip(img, 0)
image_rgb= cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')  
plt.title('Vertically Flipped Image')  
plt.show()
```
#### OUTPUT

<table>
<tr>
<td> 
  
![Screenshot 2024-09-24 174841](https://github.com/user-attachments/assets/b4027398-199e-40a3-a504-430e121ba282)


</td>
<td>
  
![Screenshot 2024-09-24 175123](https://github.com/user-attachments/assets/dc21f12b-fd3c-4ca7-8508-4b282e67bb28)


</td>
</tr>
</table>


### viii)Write and Save the Modified Image

```
img = cv2.imread("img1.jpg")
img = cv2.resize(img,(300,300))
cv2.imwrite('groot.jpg',img)
```
#### OUTPUT

![Screenshot 2024-09-24 175138](https://github.com/user-attachments/assets/5205e292-4144-4781-a8a9-502d5d9feb93)




## Result:
Thus the images are read, displayed, and written ,and color conversion was performed  successfully using the python program.








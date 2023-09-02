import cv2
#Image Resizer
print("IR 1.1 Created by MD ISTYAK")

#Configurable Parameters
source="asta.jpg"
destination="newImage.jpg"
scale_percent=40

src=cv2.imread(source, cv2.IMREAD_UNCHANGED)
#cv2.imshow("title",src)

#Percent by which the mage is resized
#Calculate the 50 % of original dimensions
new_width=int(src.shape[1]*scale_percent/100)
new_height=int(src.shape[0]*scale_percent/100)

#resize image
output=cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination,output)
cv2.waitKey(0)

#showing process
print(".........")
print("Process Start")
print("-------------")
print("Process Ended")
print(".........")

print("Image Resizing Completed")




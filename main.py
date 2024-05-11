import qrcode
import cv2 

path=input("write your path here")
img = qrcode.make(path)
# saving the qrcode image
img.save('image/MyQRCode.png')
# showing qrcode 
image = cv2.imread(r'image/MyQRCode.png')  
window_name = 'QR Code'
cv2.imshow(window_name, image) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
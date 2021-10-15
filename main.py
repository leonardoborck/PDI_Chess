import cv2

imagemOriginal = cv2.imread("dataset/1b1b2K1-1r6-2P4p-1b1p4-4N1k1-3B2Q1-2q5-2N2q2.jpeg")
imagemCinza = cv2.cvtColor(imagemOriginal, cv2.COLOR_BGR2GRAY)
ret,imagemThreshold = cv2.threshold(imagemCinza,90,255,cv2.THRESH_BINARY_INV)
imgCanny = cv2.Canny(imagemThreshold, 0, 50, apertureSize=5)
area = 10
cont = 0
for i in range(25,imgCanny.shape[0],50):
    for j in range(15,imgCanny.shape[1],50):
        for aux in range(0,20):            
            pixel = imgCanny[i,j+aux]
            if(pixel == 255):
                cont+=pixel
        for aux in range(0,20):
            pixel = imgCanny[i+(aux-area),j]
        media = cont/(area*4)
        cont = 0
        print(media)
                
cv2.imshow("Imagem Original",imagemOriginal)
cv2.imshow("Limiarizada",imgCanny)


import cv2

imagemOriginal = cv2.imread("dataset/1B1B2K1-1B6-5N2-6k1-8-8-8-4nq2.jpeg")
imagemCinza = cv2.cvtColor(imagemOriginal, cv2.COLOR_BGR2GRAY)
ret,imagemThreshold = cv2.threshold(imagemCinza,90,255,cv2.THRESH_BINARY_INV)
area = 10
cont = 0
for i in range(25,imagemThreshold.shape[0],50):
    for j in range(15,imagemThreshold.shape[1],50):
        for aux in range(0,20):            
            pixel = imagemThreshold[i,j+aux]
            if(pixel == 255):
                cont+=pixel
        media = cont/(area*2)
        cont = 0
        if(media>10):
            print("peca")
cv2.imshow("Imagem Original",imagemOriginal)
cv2.imshow("Limiarizada",imagemThreshold)


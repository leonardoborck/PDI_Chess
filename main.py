import cv2
imagemOriginal = cv2.imread("dataset/1b1b2K1-1r6-2P4p-1b1p4-4N1k1-3B2Q1-2q5-2N2q2.jpeg")
imagemCinza = cv2.cvtColor(imagemOriginal, cv2.COLOR_BGR2GRAY)
#blur = cv2.GaussianBlur(imagemCinza, (7, 7), 0)
ret,imagemThreshold = cv2.threshold(imagemCinza,90,255,cv2.THRESH_BINARY_INV)
imgCanny = cv2.Canny(imagemThreshold, 0, 50, apertureSize=5)
area = 0
cont = 0

#PEGA REGIAO CENTRAL DA CASA
for i in range(15,imgCanny.shape[0],50):
    for j in range(15,imgCanny.shape[1],50):
        #MAPEIA CANTO SUPERIOR ESQUERDO
        for aux_i in range(0,10):
                for aux_j in range(0,10):
                    pixel = imgCanny[i+aux_i-13,j+aux_j-13]
                    cont+= pixel
                    imagemOriginal[i+aux_i-13,j+aux_j-13][0] = 255
                    imagemOriginal[i+aux_i-13,j+aux_j-13][1] = 0
                    imagemOriginal[i+aux_i-13,j+aux_j-13][2] = 0
                    area+=1
        media_canto_sup = cont/area
        cont = 0
        area = 0
        #MAPEIA CANTO INFERIOR DIREITO
        for aux_i in range(0,10):
                for aux_j in range(0,10):
                    pixel = imgCanny[i+aux_i+23,j+aux_j+23]
                    cont+= pixel
                    imagemOriginal[i+aux_i+23,j+aux_j+23][0] = 255
                    imagemOriginal[i+aux_i+23,j+aux_j+23][1] = 0
                    imagemOriginal[i+aux_i+23,j+aux_j+23][2] = 0
                    area+=1
        media_canto_inf = cont/area
        cont = 0
        area = 0
        #MAPEIA REGIAO CENTRAL
        for aux_i in range(0,20):
            for aux_j in range(0,20):            
                pixel = imgCanny[i+aux_i,j+aux_j]
                cont+=pixel
                imagemOriginal[i+aux_i,j+aux_j][0] = 255
                imagemOriginal[i+aux_i,j+aux_j][1] = 0
                imagemOriginal[i+aux_i,j+aux_j][2] = 0
                area+=1

        #LOGICA DE COMPARAÇÃO
        #=================================================================
        media_centro = cont/area
        #print("canto: ",media_canto," media centro: ",media_centro)
        cont = 0
        area = 0
        media_cantos = (media_canto_sup + media_canto_inf)/2
        resultado = abs(abs(media_centro) - abs(media_cantos))
        print(media_centro,media_cantos,resultado)

        #=================================================================
        
        #DESENHA NA TELA MASCARA VERMELHA
        if(resultado>40):
            for aux_i in range(0,50):
                for aux_j in range(0,50):
                    imagemOriginal[i+aux_i-15,j+aux_j-15][2] = 255

cv2.imshow("Original",imagemOriginal)                
cv2.imshow("Limiarizada",imgCanny)


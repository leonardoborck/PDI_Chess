import cv2


# Feito em 11/10/2021

def encontrapecas(imgOriginal):
    # TRANSFORMA EM ESCALA DE CINZA
    imgCinza = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(imgCinza, (7, 7), 0)

    # BINARIZAÇÃO DA IMAGEM (PRETO E BRANCO)
    ret, imgThreshold = cv2.threshold(blur, 90, 255, cv2.THRESH_OTSU)

    # BORDAS DA IMAGEM
    imgCanny = cv2.Canny(imgThreshold, 0, 50, apertureSize=3)

    area = 0
    cont = 0

    # PEGA REGIAO CENTRAL DA CASA
    for i in range(15, imgCanny.shape[0], 50):
        for j in range(15, imgCanny.shape[1], 50):
            # MAPEIA CANTO SUPERIOR ESQUERDO
            for auxLinha in range(0, 10):
                for auxColuna in range(0, 10):
                    pixel = imgCanny[i + auxLinha - 13, j + auxColuna - 13]
                    cont += pixel
                    # imgOriginal[i + auxLinha - 13, j + auxColuna - 13][0] = 255
                    # imgOriginal[i + auxLinha - 13, j + auxColuna - 13][1] = 0
                    # imgOriginal[i + auxLinha - 13, j + auxColuna - 13][2] = 0
                    area += 1
            mediaCantoSup = cont / area
            cont = 0
            area = 0
            # MAPEIA CANTO INFERIOR DIREITO
            for auxLinha in range(0, 10):
                for auxColuna in range(0, 10):
                    pixel = imgCanny[i + auxLinha + 23, j + auxColuna + 23]
                    cont += pixel
                    # imgOriginal[i + auxLinha + 23, j + auxColuna + 23][0] = 255
                    # imgOriginal[i + auxLinha + 23, j + auxColuna + 23][1] = 0
                    # imgOriginal[i + auxLinha + 23, j + auxColuna + 23][2] = 0
                    area += 1
            mediaCantoInf = cont / area
            cont = 0
            area = 0
            # MAPEIA REGIAO CENTRAL
            for auxLinha in range(0, 20):
                for auxColuna in range(0, 20):
                    pixel = imgCanny[i + auxLinha, j + auxColuna]
                    cont += pixel
                    # imgOriginal[i + auxLinha, j + auxColuna][0] = 255
                    # imgOriginal[i + auxLinha, j + auxColuna][1] = 0
                    # imgOriginal[i + auxLinha, j + auxColuna][2] = 0
                    area += 1

            # LOGICA DE COMPARAÇÃO
            # =================================================================
            mediaCentro = cont / area
            # print("canto: ",media_canto," media centro: ",media_centro)
            cont = 0
            area = 0
            mediaCantos = (mediaCantoSup + mediaCantoInf) / 2
            resultado = abs(abs(mediaCentro) - abs(mediaCantos))
            # print(mediaCentro, mediaCantos, resultado)

            # DESENHA NA TELA MASCARA VERMELHA
            if (resultado != 0):
                for auxLinha in range(0, 50):
                    for auxColuna in range(0, 50):
                        imgOriginal[i + auxLinha - 15, j + auxColuna - 15][2] = 255
            # =================================================================
    cv2.imshow("Limiarizada", imgThreshold)
    cv2.imshow("canny", imgCanny)
    return imgOriginal


# MAIN
imgOriginal = cv2.imread("test/1B6-1k3B2-8-8-8-1N5p-K3b3-2Q1b3.jpeg")
imgResultado = encontrapecas(imgOriginal)
cv2.imshow("Original", imgResultado)
cv2.waitKey(0)
cv2.destroyAllWindows()

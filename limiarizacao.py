import cv2

img = cv2.imread("teste2.jpeg", cv2.IMREAD_COLOR) #imagem original
#suave = cv2.GaussianBlur(img, (7, 7), 0)  # função que aplica blur
limiar = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # imagem que será alterada

cv2.imshow("original",img) # print imagem original
for x in range(img.shape[0]): #altura
    for y in range(img.shape[1]): #largura
        if limiar[x, y][0] > 98:  # Tudo que for maior que 160 é considerado branco
            limiar[x, y] = 255  # branco
        else:
            limiar[x, y] = 0  # preto

cv2.imshow("limiarizacao", limiar) #mostra saida
cv2.imwrite("lana_limiar.png", limiar) #gera arquivo de saida

cv2.waitKey(0) #aguarda apertar alguma tecla para fechar
cv2.destroyAllWindows() #fecha todas as janelas criadas

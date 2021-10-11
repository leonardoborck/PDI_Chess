import cv2

# CONVERSÃO BGR PARA ESCALA DE CINZA (MÉDIA)
img = cv2.imread("teste.jpeg", cv2.IMREAD_COLOR)
ponderada = cv2.cvtColor(img, 0)
aritmetica = cv2.cvtColor(img, 0)

# Ponderada B G R
for x in range(ponderada.shape[0]):  # Altura
    for y in range(ponderada.shape[1]):  # Largura
        pixel = ponderada[x, y]
        pixel2 = (0.114*pixel[0] + 0.587*pixel[1] + 0.299*pixel[2])
        ponderada[x, y] = pixel2

# Aritimetica B G R
for x in range(aritmetica.shape[0]):  # Altura
    for y in range(aritmetica.shape[1]):  # Largura
        pixel = aritmetica[x, y]
        pixel2 = (1*pixel[0] + 1*pixel[1] + 1*pixel[2])/3
        aritmetica[x, y] = pixel2
        
cv2.imshow("ponderada", ponderada)
cv2.imshow("aritmetica", aritmetica)
cv2.imshow("original", img)
cv2.imwrite('teste2.jpeg', ponderada)

cv2.waitKey(0)
cv2.destroyAllWindows()

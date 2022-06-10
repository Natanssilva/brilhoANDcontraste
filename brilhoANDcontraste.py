# o comando import cv2 é para acessar a biblioteca  envolvendo a construção do módulo
import cv2     # aimportação das biblioetcas
import numpy as np    # numpy é outra biblioetca 
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

#contraste e brilho
img_in = cv2.imread('data/t1.jpg',0)    # carrega uma imagem do arquivo especificado (imread) / leitura da imagem
a =  -1
b = 1

img_out = a*img_in + b

img_out = np.array(img_out, dtype = np.uint8)      # array é uma estrutura de dados, ou seja, são feitos para guardar e  organizar dados.


cv2_imshow(img_in)
cv2_imshow(img_out)                 #  a função imshow exibe o valor baixo (e qualquer valor menor que baixo) como preto e exibe o valor alto (e qualquer valor maior que alto) como branco. 
'''                                       
cv2.imshow('in', img_in)
cv2.waitKey(0)                                   
cv2.imshow('out', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# a linha 20 e 21 é para mostrar a imagem com a função imshow
#  waitKey é para esperar uma tecla ser pressionada

#  o código inteiro tem a função de trazer uma imagem da biblioetca e alterar o brilho e o contraste
# Para alterar onivel contraste e o brilho , é necessario alterar o valor e multplicar 
# quando o brilho é ajustado, o resto da imagem corresponde de acordo ou seja, aumenta e diminui respectivamente
#  por ultimo, quando o ajuste do contraste é termiando e feito,todos os tons médios são deletados e a imagem ficará com uma porcentagem de tons pretos e brancos / escuros, maiores.
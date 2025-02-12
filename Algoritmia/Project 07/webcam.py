'''
     Programador....: (C) Teodoro Poulson
     Data...........: 05/02/2025
     Observações....: Programa em Open CV
                      Como ativar a Webcam
'''

import cv2 as cv 

webcam = cv.VideoCapture(0)

if not webcam.isOpened:
     print("Não foi possível aceder à webcam")
     exit()

while True: 
   retorno, frame = webcam.read()

   if not retorno:
      print("Erro na captura de webcam")
      break
   
   cv.imshow('Imagem Capturada pela webca,',frame)
   

   if cv.waitKey(1) == ord('q'):
      break

webcam.release()
cv.destroyAllWindows()
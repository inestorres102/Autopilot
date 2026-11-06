import cv2
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(script_dir, "practica_autopilot.mp4")

cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    
    # Comprobación: si 'ret' es False, no hay frame y salimos del bucle
    if not ret:
        print("Fin del vídeo o no se encontró el archivo mp4.")
        break

    # Usamos una variable distinta para no destruir la imagen a color
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Mostrar el video original en ventana
    cv2.imshow('Original', frame)

    # Aplicamos la detección de bordes sobre la imagen en grises
    edges = cv2.Canny(frame_gray, 100, 200)

    cv2.imshow('Edges', edges)

    # Esperamos la tecla Esc para detener la ejecución
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
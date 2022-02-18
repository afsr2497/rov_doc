# CAMARAS DEL ROV

Esta documentacion muestra el proceso de extraccion de video de las cámaras a utilizar en el ROV y la medicion de las principales características de las imágenes extraidas. Se utiizara el lenguaje de programacion python y el protocolo rtsp para la extraccion del video utilizando la libreria de opencv.

![image-20220218124249800](/home/alexander/snap/typora/49/.config/Typora/typora-user-images/image-20220218124249800.png)

Las conexiones principales son mostradas en la imagen de arriba mientras que la señal (1) es conectada a traves de un conector coaxial a un capturador de video.

### Camara Fija UWC-325

La cámara UWC-325 se conecta un capturador con la configuracion de 50Hz como frecuencia de captura y con IP 192.168.226.201. Dichos datos se encuentran internamente en el capturador. La configuracino rtsp se realiza internamente en el apartado config/rtsp permitiendo el acceso remoto de cualquier cliente sin identificacion, la fuente rtsp para esta camara es:

```python
fuente = "rtsp://192.168.226.201:554"
```



### Camara PT UWC-330

La cámara UWC-330 se conecta un capturador con la configuracion de 60Hz como frecuencia de captura y con IP 192.168.226.202. Dichos datos se encuentran internamente en el capturador. La configuracino rtsp se realiza internamente en el apartado config/rtsp permitiendo el acceso remoto de cualquier cliente sin identificacion, la fuente rtsp para esta camara es:

```python
fuente = "rtsp://192.168.226.201:554"
```

### Script de python para la jetson nano

Para la visualizacion de las cámaras se ha utilizado el siguiente script de python en donde la variable fuente toma el valor de la camara correspondiente

```python
import cv2

fuente = "fuente_camara_rtsp"

rov_cam = cv2.VideoCapture(fuente)
while(rov_cam.isOpened()):
    ret,img = rov_cam.read()
    if ret == True:
        cv2.imshow('rov_vid',img)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
rov_cam.release()
cv2.destroyAllWindows()
```

Luego de correr el script de python con ambas cámaras se obtuvo el siguiente resultado:

![resultado](/home/alexander/Documents/docs_personales/rov_doc/rov_camaras/resultado.jpeg)
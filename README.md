# Actividad 3 - Métodos de aprendizaje supervisado

### Introducción

Este código implementa un modelo de aprendizaje supervisado utilizando un árbol de decisión, con el objetivo de predecir el nivel de congestión en un sistema de transporte.

### Objetivo

Desarrollar un modelo de aprendizaje supervisado utilizando un árbol de decisión que permita predecir el nivel de congestión en un sistema de transporte masivo a partir de variables como hora, cantidad de pasajeros, velocidad y clima.

### Dataset

Se utilizó un dataset simulado que representa el comportamiento del sistema de transporte.
Las variables utilizadas son:

* Hora: momento del día
* Pasajeros: cantidad de usuarios
* Velocidad: velocidad promedio del vehículo
* Clima: 0 = soleado, 1 = lluvia
* Congestión: baja, media o alta

### Tecnologías utilizadas

Para el desarrollo del proyecto se utilizaron las siguientes herramientas:

* Python
* Pandas
* Scikit-learn

### Resultados

El modelo logró predecir el nivel de congestión con una precisión aproximada de:

<img width="660" height="193" alt="image" src="https://github.com/user-attachments/assets/1351690c-dbb4-443f-ab4a-3e06a3e562a1" />

Además, se compararon los valores reales con los predichos para analizar el desempeño del modelo.

### Conclusiones

El uso de aprendizaje supervisado permitió identificar patrones en los datos del sistema de transporte.
El modelo de árbol de decisión mostró buenos resultados en la predicción de la congestión, aunque se recomienda utilizar un conjunto de datos más amplio para mejorar su precisión.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# =========================
# 1. DATASET
# =========================
data = {
    "hora": [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],
    "pasajeros": [50,80,90,85,40,35,30,25,30,45,60,85,100,95,70,50],
    "velocidad": [35,20,15,18,40,42,45,50,40,35,30,20,10,12,25,30],
    "clima": [0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0],  # 0=soleado, 1=lluvia
    "congestion": [
        "Baja","Alta","Alta","Alta","Baja","Baja","Baja","Baja",
        "Baja","Baja","Media","Alta","Alta","Alta","Media","Baja"
    ]
}

df = pd.DataFrame(data)

# =========================
# 2. VARIABLES
# =========================
X = df[["hora", "pasajeros", "velocidad", "clima"]]
y = df["congestion"]

# =========================
# 3. DIVISIÓN DE DATOS
# =========================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# =========================
# 4. MODELO
# =========================
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)

# =========================
# 5. PREDICCIÓN
# =========================
y_pred = modelo.predict(X_test)

# =========================
# 6. RESULTADOS
# =========================
print("Precisión del modelo:", accuracy_score(y_test, y_pred))

print("\nComparación de resultados:")
for real, pred in zip(y_test, y_pred):
    print(f"Real: {real} - Predicción: {pred}")
import joblib
import pandas as pd

# Cargar modelo
modelo = joblib.load("modelo_Grupos_Funcionales.pkl")

# Cargar datos nuevos en el siguiente orden (medidas en cm):
# elytrawidth	elytralength	bodylength	bodywidth	frontfemurlength	fronttibialength	backfemurlength	backtibialength
sp = np.array([1.478, 2.479, 3.539,	2.902,	0.975,	1.057,	1.149,	0.972]).reshape(1, -1)

# Predecir
probs = modelo.predict_proba(sp)
clases = modelo.predict(sp)

# Mostrar resultados
df = pd.DataFrame(probs, columns=modelo.classes_())
df["clase_predicha"] = clases

print(df.head())

'''
   Endocóprido  Paracóprido  Telecóprido clase_predicha
    0.011638     0.946689     0.041672    Paracóprido
'''

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

x = iris.data
y = iris.target

nomes_especies = iris.target_names

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X, y)

print("Digite as medidas da flor:")

sepal_length = float(input("Comprimento da sépala (cm): "))
sepal_width = float(input("Largura da sépala (cm): "))
petal_length = float(input("Comprimento da pétala (cm): "))
petal_width = float(input("Largura da pétala (cm): "))

novas_flores = [[sepal_length, sepal_width, petal_length, petal_width],]

predicao = modelo.predict(novas_flores)

print("\nResultados da predição:")
print(f"A 1ª flor provavelmente é da espécie: {nomes_especies[predicao[0]]}")
# -*- coding: utf-8 -*-
"""
Classificador de Espécies de Íris usando KNN
Dever de Casa - Machine Learning
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def carregar_dados_iris():
    """Carrega e retorna o dataset Iris"""
    iris = load_iris()
    print("\nInformações sobre o dataset Iris:")
    print(f"- Total de amostras: {iris.data.shape[0]}")
    print(f"- Número de características: {iris.data.shape[1]}")
    print(f"- Espécies: {list(iris.target_names)}")
    return iris.data, iris.target, iris.target_names

def treinar_modelo_knn(X, y, test_size=0.25, random_state=42, n_neighbors=5):
    """Treina e retorna um modelo KNN"""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, 
        test_size=test_size, 
        random_state=random_state, 
        stratify=y
    )
    
    knn = KNeighborsClassifier(
        n_neighbors=n_neighbors,
        weights='uniform',
        algorithm='auto'
    )
    
    knn.fit(X_train, y_train)
    
    # Avaliação do modelo
    y_pred = knn.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"\nAcurácia do modelo: {acc:.1%}\n")
    
    return knn

def obter_medidas_flor():
    """Solicita e retorna as medidas de uma flor ao usuário"""
    medidas = []
    atributos = [
        "Comprimento da sépala (cm)",
        "Largura da sépala (cm)",
        "Comprimento da pétala (cm)",
        "Largura da pétala (cm)"
    ]
    
    print("\nDigite as medidas da flor Iris:")
    for atributo in atributos:
        while True:
            try:
                valor = float(input(f"{atributo}: ").strip())
                if valor > 0:
                    medidas.append(valor)
                    break
                print("Valor deve ser positivo. Tente novamente.")
            except ValueError:
                print("Por favor, digite um número válido.")
    
    return np.array([medidas])

def classificar_flor(modelo, classes):
    """Classifica uma flor com base nas medidas fornecidas"""
    medidas = obter_medidas_flor()
    
    # Fazendo a previsão
    especie_idx = modelo.predict(medidas)[0]
    probabilidades = modelo.predict_proba(medidas)[0]
    
    print("\nResultado da classificação:")
    print(f"Espécie prevista: {classes[especie_idx].capitalize()}")
    
    print("\nProbabilidades:")
    for idx, prob in enumerate(probabilidades):
        print(f"- {classes[idx]}: {prob:.2%}")

def main():
    """Função principal do programa"""
    # Configuração para evitar problemas de encoding
    import sys
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
    
    # Carregar dados
    X, y, classes = carregar_dados_iris()
    
    # Treinar modelo
    modelo = treinar_modelo_knn(X, y)
    
    # Loop de classificação
    while True:
        classificar_flor(modelo, classes)
        
        continuar = input("\nDeseja classificar outra flor? (s/n): ").strip().lower()
        if continuar != 's':
            print("\nPrograma encerrado. Até logo!")
            break

if __name__ == "__main__":
    main()
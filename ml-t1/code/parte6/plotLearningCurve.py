import numpy as np
import matplotlib.pyplot as plt
import os

def plot_learning_curve(x,y_treino, y_val, titulo=None):
    plt.figure(figsize=(8,5))
    plt.plot(x,y_treino,label='Treinamento')
    plt.plot(x,y_val,label='Validação cruzada')
    plt.title('Curva de aprendizado para regressão linear')
    plt.xlabel('Número de exemplos treinados')
    plt.ylabel('Erro')
    x1,x2,y1,y2 = plt.axis()
    plt.axis((x1,x2,0,y2))
    plt.legend()
    plt.title(titulo)
    
    plt.show()

theta = np.array([[1,1]]) #inicialização
numero_exemplos, erros_treino, erros_val = learningCurve(theta, X, y, Xval, yval, _lambda=0)

titulo = 'Curva de aprendizado para regressão linear'
plot_learning_curve(numero_exemplos,erros_treino, erros_val, titulo)
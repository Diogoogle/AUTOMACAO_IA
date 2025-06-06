from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from DATA import dados_treino
import joblib

# DataFrame
df_treino = pd.DataFrame(dados_treino)

# Vetorização correta
vetorizador = TfidfVectorizer()
x_treino = vetorizador.fit_transform(df_treino['Mensagem_do_usuario']).toarray()

# Saída como vetor 1D
y_treino = df_treino['Comando_a_ser_executado'].values.ravel()

# Treinamento do modelo
modelo_nb = GaussianNB()
modelo_nb.fit(x_treino, y_treino)

joblib.dump(modelo_nb, 'modelo_nb.joblib')
joblib.dump(vetorizador, 'vetorizador.joblib')




import numpy as np
import tensorflow as tf
from tensorflow import keras
import pickle

# Dados de treinamento
inputs = ["Oi", "Como vai?", "Qual é o seu nome?", "O que você gosta de fazer?", "Tchau"]
outputs = ["Olá!", "Estou bem, obrigado por perguntar.", "Meu nome é ChatGPT.", "Eu gosto de conversar com pessoas.", "Até mais tarde!"]

# Tokenização das entradas e saídas
tokenizer = keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(inputs + outputs)
inputs_seq = tokenizer.texts_to_sequences(inputs)
outputs_seq = tokenizer.texts_to_sequences(outputs)

# Padronização das sequências para ter o mesmo comprimento
max_seq_length = max([len(seq) for seq in inputs_seq + outputs_seq])
inputs_seq = keras.preprocessing.sequence.pad_sequences(inputs_seq, maxlen=max_seq_length, padding="post")
outputs_seq = keras.preprocessing.sequence.pad_sequences(outputs_seq, maxlen=max_seq_length, padding="post")

# Modelo de IA
model = keras.Sequential([
    keras.layers.Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=100, input_length=max_seq_length),
    keras.layers.Bidirectional(keras.layers.LSTM(64, return_sequences=True)),
    keras.layers.Bidirectional(keras.layers.LSTM(64)),
    keras.layers.Dense(len(tokenizer.word_index)+1, activation="softmax")
])

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Treinamento do modelo
model.fit(inputs_seq, outputs_seq, epochs=100, verbose=2)

# Método para salvar o modelo em um arquivo
def salvar_modelo(modelo, tokenizer, nome_arquivo):
    with open(nome_arquivo, "wb") as arquivo:
        pickle.dump((modelo.to_json(), tokenizer), arquivo)

# Salvar o modelo em um arquivo
salvar_modelo(model, tokenizer, "chatbot_model.pkl")

import pickle
from tensorflow import keras

# Método para carregar o modelo a partir de um arquivo e usar para responder uma pergunta
def carregar_modelo_e_responder(pergunta, nome_arquivo):
    with open(nome_arquivo, "rb") as arquivo:
        modelo_json, tokenizer = pickle.load(arquivo)
        modelo = keras.models.model_from_json(modelo_json)
    
    # Carregar o modelo compilado
    modelo.load_weights(nome_arquivo[:-4] + "_weights.h5")

    # Tokenizar a pergunta
    pergunta_seq = tokenizer.texts_to_sequences([pergunta])
    pergunta_seq = keras.preprocessing.sequence.pad_sequences(pergunta_seq, maxlen=modelo.input_shape[1], padding="post")

    # Prever a resposta
    resposta_seq = modelo.predict_classes(pergunta_seq)

    # Converter a sequência de volta para texto
    resposta_texto = tokenizer.sequences_to_texts(resposta_seq)

    return resposta_texto[0]

# Exemplo de uso
pergunta = "Qual é o seu nome?"
nome_arquivo = "chatbot_model.pkl"
resposta = carregar_modelo_e_responder(pergunta, nome_arquivo)
print("Resposta do chatbot:", resposta)

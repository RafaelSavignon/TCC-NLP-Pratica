import sys
import arquivos
import nlp
from PySide2.QtWidgets import QApplication, QMainWindow
from Program.View.ui_MainWindow import Ui_MainWindow
class MinhaMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configura a interface do usuário
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectar sinais e slots
        self.ui.BotaoDestino.clicked.connect(self.carregar_arquivo)
        self.ui.BotaoTreinarModelo.clicked.connect(self.treinar_modelo)
        self.ui.BotaoPDF.clicked.connect(self.carregar_dataset)
        self.ui.BotaoEnviarPergunta.clicked.connect(self.enviar)
        self.ui.BotaoGerarDataset.clicked.connect(self.gerar_dataset)
        self.ui.BotaoDestinoPH5.clicked.connect(self.buscar)

    def carregar_arquivo(self):
        destino = arquivos.criar_arquivo_txt()
        self.ui.PastaDestino.setText(destino)

    def treinar_modelo(self):
        print("Botão 'Treinar Modelo' clicado!")

    def carregar_dataset(self):
        documento = arquivos.carregar_arquivo()
        self.ui.CaminhoPDF.setText(documento)

    def enviar(self):
        print("Botão 'Enviar' clicado!")

    def gerar_dataset(self):
        nlp.pdf_para_txt(self.ui.CaminhoPDF.text(), self.ui.PastaDestino.text())
        resultado = nlp.identificar_perguntas_respostas(self.ui.PastaDestino.text())
        resultadoString = arquivos.lista_para_string(resultado)
        self.ui.DadosDataset.setPlainText(resultadoString)

    def buscar(self):
        destino = arquivos.criar_arquivo_txt()
        self.ui.DestinoPH5.setText(destino)

def executar_classe():
    app = QApplication(sys.argv)
    janela = MinhaMainWindow()
    janela.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    executar_classe()

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowIQwYHY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 90, 47, 16))
        self.PastaDestino = QLineEdit(self.centralwidget)
        self.PastaDestino.setObjectName(u"PastaDestino")
        self.PastaDestino.setGeometry(QRect(100, 90, 141, 20))
        self.BotaoDestino = QPushButton(self.centralwidget)
        self.BotaoDestino.setObjectName(u"BotaoDestino")
        self.BotaoDestino.setGeometry(QRect(270, 90, 75, 23))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(390, 0, 20, 601))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.DadosDataset = QPlainTextEdit(self.centralwidget)
        self.DadosDataset.setObjectName(u"DadosDataset")
        self.DadosDataset.setGeometry(QRect(20, 150, 351, 221))
        self.BotaoTreinarModelo = QPushButton(self.centralwidget)
        self.BotaoTreinarModelo.setObjectName(u"BotaoTreinarModelo")
        self.BotaoTreinarModelo.setGeometry(QRect(110, 480, 161, 23))
        self.CaminhoPDF = QLineEdit(self.centralwidget)
        self.CaminhoPDF.setObjectName(u"CaminhoPDF")
        self.CaminhoPDF.setGeometry(QRect(100, 50, 141, 20))
        self.BotaoPDF = QPushButton(self.centralwidget)
        self.BotaoPDF.setObjectName(u"BotaoPDF")
        self.BotaoPDF.setGeometry(QRect(270, 50, 75, 23))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 50, 47, 16))
        self.BotaoEnviarPergunta = QPushButton(self.centralwidget)
        self.BotaoEnviarPergunta.setObjectName(u"BotaoEnviarPergunta")
        self.BotaoEnviarPergunta.setGeometry(QRect(700, 90, 75, 23))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(420, 60, 47, 16))
        self.Pergunta = QLineEdit(self.centralwidget)
        self.Pergunta.setObjectName(u"Pergunta")
        self.Pergunta.setGeometry(QRect(420, 90, 261, 20))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(420, 130, 47, 16))
        self.Resposta = QPlainTextEdit(self.centralwidget)
        self.Resposta.setObjectName(u"Resposta")
        self.Resposta.setGeometry(QRect(423, 160, 351, 371))
        self.BotaoGerarDataset = QPushButton(self.centralwidget)
        self.BotaoGerarDataset.setObjectName(u"BotaoGerarDataset")
        self.BotaoGerarDataset.setGeometry(QRect(120, 120, 161, 23))
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 370, 401, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.Epocas = QLineEdit(self.centralwidget)
        self.Epocas.setObjectName(u"Epocas")
        self.Epocas.setGeometry(QRect(90, 400, 141, 20))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 400, 47, 16))
        self.DestinoPH5 = QLineEdit(self.centralwidget)
        self.DestinoPH5.setObjectName(u"DestinoPH5")
        self.DestinoPH5.setGeometry(QRect(90, 440, 141, 20))
        self.BotaoDestinoPH5 = QPushButton(self.centralwidget)
        self.BotaoDestinoPH5.setObjectName(u"BotaoDestinoPH5")
        self.BotaoDestinoPH5.setGeometry(QRect(260, 440, 75, 23))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 440, 61, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Chat Test", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Arquivo:", None))
        self.BotaoDestino.setText(QCoreApplication.translate("MainWindow", u"Carregar", None))
        self.BotaoTreinarModelo.setText(QCoreApplication.translate("MainWindow", u"Treinar Modelo", None))
        self.BotaoPDF.setText(QCoreApplication.translate("MainWindow", u"Carregar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Dataset:", None))
        self.BotaoEnviarPergunta.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pergunta:", None))
        self.Pergunta.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Resposta:", None))
        self.BotaoGerarDataset.setText(QCoreApplication.translate("MainWindow", u"Gerar Dataset", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Epocas:", None))
        self.BotaoDestinoPH5.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Destino PH5:", None))
    # retranslateUi


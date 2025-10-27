# -*- coding: utf-8 -*-

import os #OS関連処理用モジュールの読込
import sys #システム関連処理用モジュールの読込
import time #時間関連処理用モジュールの読込
import numpy as np #行列処理用モジュールの読込
import math as mt #各種計算用モジュールの読込
import glob #ファイルパス一括取得用モジュールの読込
from PySide6 import QtCore, QtGui, QtWidgets #GUI関連処理用モジュールの読込
from MIIL_PARAMETER_CREATER_GUI import Ui_MainWindow #QT Designerで作成し変換したファイルの読込

#####グローバル変数########################################
capLoop = 0 #動画を表示中か判定するフラグ
LabelNum = 0 #ラベル数を代入する変数

#####Pysideのウィンドウ処理クラス########################################
class MainWindow1(QtWidgets.QMainWindow): #QtWidgets.QMainWindowを継承
#=====GUI用クラス継承の定型文========================================
    def __init__(self, parent = None): #クラス初期化時にのみ実行される関数（コンストラクタと呼ばれる）
        super(MainWindow1, self).__init__(parent) #親クラスのコンストラクタを呼び出す（親クラスのコンストラクタを再利用したい場合）　指定する引数は、親クラスのコンストラクタの引数からselfを除いた引数
        self.ui = Ui_MainWindow() #uiクラスの作成。Ui_MainWindowのMainWindowは、QT DesignerのobjectNameで設定した名前
        self.ui.setupUi(self) #uiクラスの設定
        self.ui.comboBox4.addItems(["0", "10", "20", "30", "40", "50"]) #####コンボボックスにアイテムを追加
        self.ui.comboBox4.setCurrentIndex(0) #####コンボボックスのアイテムを選択
        #-----シグナルにメッソドを関連付け----------------------------------------
        self.ui.pushButton2.clicked.connect(self.pushButton2_clicked) #pushButton2_clickedは任意
        self.ui.pushButton3.clicked.connect(self.pushButton3_clicked) #pushButton3_clickedは任意
        self.ui.pushButton5.clicked.connect(self.pushButton5_clicked) #pushButton5_clickedは任意
        self.ui.pushButton6.clicked.connect(self.pushButton6_clicked) #pushButton6_clickedは任意
        self.ui.pushButton10.clicked.connect(self.pushButton10_clicked) #pushButton10_clickedは任意
        self.ui.pushButton11.clicked.connect(self.pushButton11_clicked) #pushButton11_clickedは任意
        self.ui.pushButton12.clicked.connect(self.pushButton12_clicked) #pushButton12_clickedは任意
        self.ui.pushButton14.clicked.connect(self.pushButton14_clicked) #pushButton14_clickedは任意
        self.ui.pushButton15.clicked.connect(self.pushButton15_clicked) #pushButton15_clickedは任意
        self.ui.pushButton16.clicked.connect(self.pushButton16_clicked) #pushButton16_clickedは任意
        self.ui.pushButton19.clicked.connect(self.pushButton19_clicked) #pushButton19_clickedは任意
        self.ui.pushButton21.clicked.connect(self.pushButton21_clicked) #pushButton21_clickedは任意
        self.ui.pushButton22.clicked.connect(self.pushButton22_clicked) #pushButton22_clickedは任意
        self.ui.pushButton23.clicked.connect(self.pushButton23_clicked) #pushButton23_clickedは任意

#=====ウィジットのシグナル処理用メッソド========================================
    #-----pushButton2用イベント処理----------------------------------------
    ##########
    #設定を読込む
    ##########
    def pushButton2_clicked(self):
        global LabelNum
    #####ファイル読込
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "",'pms File (*.pms)') #パラメータファイルを選択
        if filepath: #ファイルパスが選択されているか確認
            text = ''
            f = open(filepath, "r") #ファイルの読み込み開始
            text = f.readlines() #テキストを一行ずつ配列として読込む（行の終わりの改行コードも含めて読込む）
            f.close() #ファイルの読み込み終了
            self.ui.comboBox4.setCurrentIndex(int(text[0].replace("\n", ""))) #改行コードを削除してデータを読込む
            self.ui.lineEdit4.setText(text[1].replace("\n", "")) #改行コードを削除してデータを読込む
            self.ui.lineEdit5.setText(text[2].replace("\n", "")) #改行コードを削除してデータを読込む
            self.ui.lineEdit8.setText(text[3].replace("\n", "")) #改行コードを削除してデータを読込む
            self.ui.lineEdit9.setText(text[4].replace("\n", "")) #改行コードを削除してデータを読込む
            if self.ui.lineEdit5.text() != '':
                f = open(self.ui.lineEdit5.text(), "r") #ファイルの読み込み開始
                tr = f.readlines() #テキストを一行ずつ配列として読込む（行の終わりの改行コードも含めて読込む）
                f.close() #ファイルの読み込み終了
                if len(tr) > 0: #ラベルが一つ以上あるか確認
                    LabelNum = 0
                    for Label in tr: #ラベル数を取得
                        LabelNum += 1
                else:
                    msgbox = QtWidgets.QMessageBox(self) #####メッセージボックスを準備
                    msgbox.setWindowTitle("MPC")
                    msgbox.setText("No label found in the file.") #####メッセージボックスのテキストを設定
            msgbox = QtWidgets.QMessageBox(self) #####メッセージボックスを準備
            msgbox.setWindowTitle("MPC")
            msgbox.setText("File loded.") #####メッセージボックスのテキストを設定
            ret = msgbox.exec() #####メッセージボックスを表示
            #####
    #####

    #-----pushButton3用イベント処理----------------------------------------
    ##########
    #設定を書き込む
    ##########
    def pushButton3_clicked(self):
    #####ファイル書込み
        filepath, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "",'pms File (*.pms)') #パラメータファイルを選択
        if filepath: #ファイルパスが選択されているか確認
            text = ''
            text = str(self.ui.comboBox4.currentIndex()) + "\n" + \
            self.ui.lineEdit4.text() + "\n" + \
            self.ui.lineEdit5.text() + "\n" + \
            self.ui.lineEdit8.text() + "\n" + \
            self.ui.lineEdit9.text() + "\n"
            f = open(filepath, "w") #ファイルの書き込み開始
            f.writelines(text) #ファイルを書き込み
            f.close() #ファイルの書き込み終了
            msgbox = QtWidgets.QMessageBox(self) #####メッセージボックスを準備
            msgbox.setWindowTitle("MPC")
            msgbox.setText("File saved.") #####メッセージボックスのテキストを設定
            ret = msgbox.exec() #####メッセージボックスを表示
            #####
    #####

    #-----pushButton5用イベント処理----------------------------------------
    ##########
    #データセットフォルダを選択
    ##########
    def pushButton5_clicked(self):
        DirPath = QtWidgets.QFileDialog.getExistingDirectory(self) #フォルダの選択
        if DirPath: #フォルダが選択された場合
            self.ui.lineEdit4.setText(DirPath) #ラインエディトにテキストをセット

    #-----pushButton6用イベント処理----------------------------------------
    ##########
    #ラベルファイルを選択
    ##########
    def pushButton6_clicked(self):
        global LabelNum
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "",'lab File (*.lab)') #ラベルファイルを選択
        if filepath: #ファイルパスが選択されているか確認
            f = open(filepath, "r") #ファイルの書き込み開始
            text = f.readlines() #ファイルを書き込み
            f.close() #ファイルの書き込み終了
            if len(text) > 0: #ラベルが一つ以上あるか確認
                LabelNum = 0
                for Label in text: #ラベル数を取得
                    LabelNum += 1
                self.ui.lineEdit5.setText(filepath) #ラインエディトにテキストをセット
            else:
                msgbox = QtWidgets.QMessageBox(self) #####メッセージボックスを準備
                msgbox.setWindowTitle("MPC")
                msgbox.setText("No label found in the file.") #####メッセージボックスのテキストを設定
                ret = msgbox.exec() #####メッセージボックスを表示

    #-----pushButton10用イベント処理----------------------------------------
    ##########
    #ウェイトファイルを選択
    ##########
    def pushButton10_clicked(self):
        DirPath = QtWidgets.QFileDialog.getExistingDirectory(self) #フォルダの選択
        if DirPath: #フォルダが選択された場合
            self.ui.lineEdit8.setText(DirPath) #ラインエディトにテキストをセット

    #-----pushButton11用イベント処理----------------------------------------
    ##########
    #パラメータファイルを選択
    ##########
    def pushButton11_clicked(self):
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "",'parameter File (*.prm)') #パラメータファイルを選択
        if filepath: #ファイルパスが選択されているか確認
            self.ui.lineEdit9.setText(filepath) #ラインエディトにテキストをセット

    #-----pushButton12用イベント処理----------------------------------------
    ##########
    #パラメータファイルを保存
    ##########
    def pushButton12_clicked(self):
        if self.ui.lineEdit4.text() == '':
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("MPC")
            msgbox.setText("Please set dataset folder.")
            ret = msgbox.exec()
        elif self.ui.lineEdit5.text() == '':
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("MPC")
            msgbox.setText("Please set label file.")
            ret = msgbox.exec()
        elif LabelNum <= 0:
            msgbox = QtWidgets.QMessageBox(self) #####メッセージボックスを準備
            msgbox.setWindowTitle("MPC")
            msgbox.setText("No label found in the file.") #####メッセージボックスのテキストを設定
            ret = msgbox.exec()
        elif self.ui.lineEdit8.text() == '':
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("MPC")
            msgbox.setText("Please set the weights folder.")
            ret = msgbox.exec()
        else:
            filepath, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "",'parameter File (*.prm)') #パラメータファイルを選択
            if filepath: #ファイルパスが選択されているか確認
                filename1 = filepath.rsplit(".", 1) #ファイルパスの文字列右側から指定文字列で分割
                filename2 = filename1[0].rsplit("/", 1) #ファイルパスの文字列右側から指定文字列で分割
                SelectedPath = filename2[0] + '/' #ファイルまでのパス
                SelectedName = filename2[1] #ファイルネーム
                JpgFileList = glob.glob(self.ui.lineEdit4.text() + '/*.jpg') #データセットフォルダ内の各ファイルパスをリスト形式で取得
                JpgFileList.sort()

                ValidList = ''
                VA = SelectedPath + SelectedName + '_valid.vld' #教師データファイルパス
                TrainList = ''
                TR = SelectedPath + SelectedName + '_train.trn' #トレーニングファイルパス

                ret = QtWidgets.QMessageBox.Yes
                if os.path.isfile(VA) and os.path.isfile(TR): #ファイルが存在するか確認
                    msgbox = QtWidgets.QMessageBox(self)
                    ret = msgbox.question(None, "MPC", "Training data and Valid data already exist.\nWould you like to OVERWRITE them?\n", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No) #選択用メッセージボックスを表示
                if ret == QtWidgets.QMessageBox.Yes: #メッセージボックスでYESが選択された場合
                    prog = QtWidgets.QProgressDialog("Creating parameter file...", None, 0, 0, None, QtCore.Qt.Window | QtCore.Qt.WindowTitleHint | QtCore.Qt.CustomizeWindowHint)
                    prog.setWindowTitle("MPC") #ウィンドウのタイトルを設定（省略可）
                    prog.setFixedSize(prog.sizeHint()) #ウィンドウのリサイズを禁止（省略可）
                    prog.show()
                    self.ui.pushButton2.setEnabled(False)
                    self.ui.pushButton3.setEnabled(False)
                    self.ui.pushButton5.setEnabled(False)
                    self.ui.pushButton6.setEnabled(False)
                    self.ui.pushButton10.setEnabled(False)
                    self.ui.pushButton11.setEnabled(False)
                    self.ui.pushButton12.setEnabled(False)
                    self.ui.pushButton14.setEnabled(False)
                    self.ui.pushButton15.setEnabled(False)
                    self.ui.pushButton16.setEnabled(False)
                    self.ui.pushButton19.setEnabled(False)
                    self.ui.pushButton21.setEnabled(False)
                    self.ui.pushButton22.setEnabled(False)
                    self.ui.pushButton23.setEnabled(False)
                    self.ui.comboBox4.setEnabled(False)
                    FileList = []
                    for FN in JpgFileList: #ファイル毎に処理
                        filename1 = FN.rsplit(".", 1) #ファイルパスの文字列右側から指定文字列で分割
                        filename2 = filename1[0] + '.txt' #画像ファイルと対の領域データまでのパス
                        text = ''
                        f = open(filename2, "r") #ファイルの読み込み開始
                        text = f.read() #テキストを一行ずつ配列として読込む（行の終わりの改行コードも含めて読込む）
                        f.close() #ファイルの読み込み終了
                        if len(text) > 0: #領域データが一つ以上ある場合
                            FileList.append(FN) #領域データがあるファイルをリスト配列に追加。
                        else:
                            TrainList = TrainList + FN.replace('\\', '/') + '\n' #領域データがないファイルをトレーニングデータに追加。
                        app.processEvents() #ループ中に他のイベントを実行
                    if int(self.ui.comboBox4.currentText())>0: #教師データ自動取得率が０％以上の場合
                        CNT = 1
                        VALID = round(100 / int(self.ui.comboBox4.currentText())) #教師データ摘出カウンターを計算
                        for FN in FileList:
                            if CNT == VALID: #カウンターが教師データ摘出カウンターに達した場合
                                CNT = 1
                                ValidList = ValidList + FN.replace('\\', '/') + '\n' #ファイルを教師データに追加。
                            else: #カウンターが教師データ摘出カウンターに達していない場合
                                TrainList = TrainList + FN.replace('\\', '/') + '\n' #ファイルをトレーニングデータに追加。
                                CNT = CNT + 1
                            app.processEvents() #ループ中に他のイベントを実行
                    else: #教師データ自動取得率が０％の場合
                        for FN in FileList:
                            TrainList = TrainList + FN.replace('\\', '/') + '\n' #全てのファイルをトレーニングデータに追加。
                            app.processEvents() #ループ中に他のイベントを実行
                    f = open(VA, "w") #ファイルの読み込み開始
                    f.writelines(ValidList) #テキストを一行ずつ配列として読込む（行の終わりの改行コードも含めて読込む）
                    f.close() #ファイルの読み込み終了
                    f = open(TR, "w") #ファイルの読み込み開始
                    f.writelines(TrainList) #テキストを一行ずつ配列として読込む（行の終わりの改行コードも含めて読込む）
                    f.close() #ファイルの読み込み終了
                    PRM = 'classes = ' + str(LabelNum) + '\n' + \
                    'train = ' + TR + '\n' + \
                    'valid = ' + VA + '\n' + \
                    'names = ' + self.ui.lineEdit5.text() + '\n' + \
                    'backup = ' + self.ui.lineEdit8.text() + '\n'
                    f = open(filepath, "w") #ファイルの書き込み開始
                    f.writelines(PRM) #パラメータファイルを書き込み
                    f.close() #ファイルの書き込み終了
                    self.ui.lineEdit9.setText(filepath) #パラメータファイルのパスをラインエディットに表示
                    prog.destroy()
                    msgbox = QtWidgets.QMessageBox(self)
                    msgbox.setWindowTitle("MPC")
                    msgbox.setText("File saved.") #メッセージボックスのテキストを設定
                    ret = msgbox.exec() #メッセージボックスを表示
                    self.ui.pushButton2.setEnabled(True)
                    self.ui.pushButton3.setEnabled(True)
                    self.ui.pushButton5.setEnabled(True)
                    self.ui.pushButton6.setEnabled(True)
                    self.ui.pushButton10.setEnabled(True)
                    self.ui.pushButton11.setEnabled(True)
                    self.ui.pushButton12.setEnabled(True)
                    self.ui.pushButton14.setEnabled(True)
                    self.ui.pushButton15.setEnabled(True)
                    self.ui.pushButton16.setEnabled(True)
                    self.ui.pushButton19.setEnabled(True)
                    self.ui.pushButton21.setEnabled(True)
                    self.ui.pushButton22.setEnabled(True)
                    self.ui.pushButton23.setEnabled(True)
                    self.ui.comboBox4.setEnabled(True)
                else:
                    msgbox = QtWidgets.QMessageBox(self)
                    msgbox.setWindowTitle("MPC")
                    msgbox.setText("Canceled.") #メッセージボックスのテキストを設定
                    ret = msgbox.exec() #メッセージボックスを表示
    #-----pushButton14用イベント処理----------------------------------------
    ##########
    #パラメータファイルを表示
    ##########
    def pushButton14_clicked(self):
        if self.ui.lineEdit9.text() != '':
            ret = os.system(self.ui.lineEdit9.text())

    #-----pushButton15用イベント処理----------------------------------------
    ##########
    #トレーニングデータを表示
    ##########
    def pushButton15_clicked(self):
        if self.ui.lineEdit9.text() != '':
            filepath = self.ui.lineEdit9.text()
            filename = filepath.rsplit(".", 1) #ファイルパスの文字列右側から指定文字列で分割
            ret = os.system(filename[0] + '_train.trn')

    #-----pushButton16用イベント処理----------------------------------------
    ##########
    #教師データを表示
    ##########
    def pushButton16_clicked(self):
        if self.ui.lineEdit9.text() != '':
            filepath = self.ui.lineEdit9.text()
            filename = filepath.rsplit(".", 1) #ファイルパスの文字列右側から指定文字列で分割
            ret = os.system(filename[0] + '_valid.vld')

    #-----pushButton19用イベント処理----------------------------------------
    ##########
    #選択をクリア
    ##########
    def pushButton19_clicked(self):
        self.ui.lineEdit5.setText('')

    #-----pushButton21用イベント処理----------------------------------------
    ##########
    #選択をクリア
    ##########
    def pushButton21_clicked(self):
        self.ui.lineEdit4.setText('')

    #-----pushButton22用イベント処理----------------------------------------
    ##########
    #選択をクリア
    ##########
    def pushButton22_clicked(self):
        self.ui.lineEdit8.setText('')

    #-----pushButton23用イベント処理----------------------------------------
    ##########
    #選択をクリア
    ##########
    def pushButton23_clicked(self):
        self.ui.lineEdit9.setText('')

#=====メインウィンドウのイベント処理========================================
    #-----ウィンドウ終了イベントのフック----------------------------------------
    def closeEvent(self, event): #event.accept() event.ignore()で処理を選択可能
        global capLoop
        if capLoop == 1: #ループ実行中の場合
            event.ignore() #メインウィンドウの終了イベントをキャンセル
        else: #ループが実行中でない場合
            event.accept() #メインウィンドウの終了イベントを実行

#####メイン処理（グローバル）########################################
#=====メイン処理定型文========================================
if __name__ == '__main__': #C言語のmain()に相当。このファイルが実行された場合、以下の行が実行される（モジュールとして読込まれた場合は、実行されない）
    app = QtWidgets.QApplication(sys.argv) #アプリケーションオブジェクト作成（sys.argvはコマンドライン引数のリスト）
    win = MainWindow1() #MainWindow1クラスのインスタンスを作成
    win.show() #ウィンドウを表示　win.showFullScreen()やwin.showEvent()を指定する事でウィンドウの状態を変える事が出来る
    sys.exit(app.exec()) #引数が関数の場合は、関数が終了するまで待ち、その関数の返値を上位プロセスに返す

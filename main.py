from PyQt5  import QtWidgets
import PyQt5.QtCore as QtCore
import subprocess
import sys
import json



def load_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)  # 若使用 JSON，改為 json.load(file)
    return config

config = load_config("config.json")  # 載入設定檔

def execute_command(command, output):
    output.clear()  # 清空輸出框
    result = subprocess.run(
    [config["CLI_PATH"],"-c",command ],  # 將 CLI 路徑與命令組合成列表
    stdout=subprocess.PIPE,  # 捕捉標準輸出
    stderr=subprocess.PIPE,  # 捕捉錯誤輸出
    text=True         )

    output.setPlainText(result.stdout)  # 將標準輸出顯示在輸出框中

def enter_key_pressed(input, output):
    command = input.text()  # 取得輸入框的文字
    execute_command(command, output)  # 執行命令並顯示結果

def main():
    
    app = QtWidgets.QApplication(sys.argv)  # 啟動應用程序

    window = QtWidgets.QWidget()       # 基底視窗
    window.setWindowTitle("主視窗")
    window.resize(400, 300)            # 設定大小

    input = QtWidgets.QLineEdit(window)  # 輸入框
    input.setGeometry(20, 20, 360, 30) # 設定位置與大小

    enter = QtWidgets.QPushButton("Enter", window)  # 按鈕
    enter.move(400, 20)               # 設定位置

    output = QtWidgets.QPlainTextEdit(window)  # 輸出框
    output.setGeometry(20, 70, 450, 450) # 設定位置與大小

    enter.clicked.connect(lambda: enter_key_pressed(input, output))  # 按鈕點擊事件

    window.adjustSize()               # 調整大小
    window.show()
    sys.exit(app.exec_())     
              # 啟動事件循環
if __name__ == "__main__":
    
    main()
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton
from PySide6.QtCore import Signal

class ChatUI(QWidget):
    # 定义一个信号,用于返回用户输入的内容
    input_submitted = Signal(str)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 创建聊天框
        self.chat_input = QTextEdit()
        layout.addWidget(self.chat_input)

        # 创建"继续"按钮
        self.submit_button = QPushButton("继续")
        self.submit_button.clicked.connect(self.on_submit)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)
        self.setWindowTitle('AI代理')
        self.setGeometry(300, 300, 300, 200)

    def on_submit(self):
        # 获取用户输入的内容
        user_input = self.chat_input.toPlainText()
        # 发送信号,将用户输入的内容作为参数
        self.input_submitted.emit(user_input)
        # 清空输入框
        self.chat_input.clear()
        
    def get_input(self):
        return self.chat_input.toPlainText()
        
        


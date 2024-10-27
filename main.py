import sys
from PySide6.QtWidgets import QApplication
from ui import ChatUI
from AskAI import AskAI
from OpenWeb import OpenYoutube, OpenImage, SendWhatsapp
from AddMemory import AddMemory

def main():
    app = QApplication(sys.argv)

    chat_ui = ChatUI()
    chat_ui.show()
    
    def handle_user_input(content):
        ai = AskAI(content)
        
        aiResult = ai.search()
        if aiResult.startswith("OpenYoutube"):
            OpenYoutube(aiResult.split("'")[1])
        elif aiResult.startswith("OpenImage"):
            OpenImage(aiResult.split("'")[1])
        elif aiResult.startswith("AddMemory"):
            AddMemory(aiResult.split("'")[1])
        elif aiResult.startswith("SendWhatsapp"):
            SendWhatsapp(aiResult.split("'")[1], aiResult.split("'")[3])

    chat_ui.input_submitted.connect(handle_user_input)
    
    sys.exit(app.exec())
    


if __name__ == '__main__':
    main()
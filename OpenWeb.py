import webbrowser
import pyautogui
import time


def OpenYoutube(content):
    webbrowser.open(f"https://www.youtube.com/results?search_query={content}")
    
def OpenImage(content):
    webbrowser.open(f"https://www.google.com/search?sca_esv=f23d37099304cbcf&sxsrf=ADLYWIKOtp3W25P8w31mu0yh424isUl8aw:1729976707129&q={content}&udm=2&fbs=AEQNm0AaBOazvTRM_Uafu9eNJJzCjPEAP5HX2BE31zy5nlFpWvns3PnbKLxkXEhI71m1WxuyGXhNUouYPTHnpIch5xJgIMcZof5GjjJE9giO3Q868M8bOV1cSsJN7w0Zrg98RFguyHOZm3xFt2oGVWl-pJTEpoK9LGg_7usrFKfWPNc2HJFGR3WY8McCLmP6UHbReplFnP4m&sa=X&ved=2ahUKEwi7meS4-ayJAxVjklYBHdXPJn8QtKgLegQIFhAB&biw=1707&bih=932&dpr=1.5")

def SendWhatsapp(phone, message):
    url = f"https://web.whatsapp.com/send?phone={phone}&text={message}"
    webbrowser.open(url)
    time.sleep(7)
    pyautogui.press('enter')

    
    
    
    




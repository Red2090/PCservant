from openai import OpenAI
import json

class AskAI:
    def __init__(self, content):
        self.content = content
         
    def search(self):
        with open('memories.txt', 'r', encoding='utf-8') as f:
            memories = f.read()
        with open('apiKey.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        client = OpenAI(api_key=config["api_key"], base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": f"你是一个ai代理，这是你的记忆：{memories}。你将收到一个用户说的话，假设用户是提出指令，你将只根据指令返回'函数名(单引号+用户需要搜索的内容)'字样，无需返回其他内容。假设用户没有提出指令，而是提出有需要记忆的点，用AddMemory('提炼出的简短的记忆内容')存进记忆中，例如用户：我想学习python，返回OpenYoutube('python教程')；用户：今天陈老师告诉我他的的邮箱是123@qq.com，返回AddMemory('陈老师的邮箱是123@qq.com')。以下是所有可用函数：OpenImage('内容')：搜索照片。OpenYoutube('内容')：搜索youtube。SendWhatsapp('目标电话号码', '消息内容')：打开WhatsApp网页版发送消息。"},
                {"role": "user", "content": self.content},
            ],
            stream=False
        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content
    
    


def AddMemory(content):
    with open("memories.txt", "r", encoding="utf-8") as f:
        memories = f.read()
    memories += content
    with open("memories.txt", "w", encoding="utf-8") as f:
        f.write(memories)

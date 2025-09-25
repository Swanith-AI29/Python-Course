class bird():
    def __init__(self):
        print('Bird is ready')
    def whoisthis(self):
        print('Bird')
    def swim(self):
        print('SWim fast')
class penguin(bird):
    def __init__(self):
        super().__init__()
        print('Penguin is ready')
    def whoisthis(self):
        print('Penguin')
    def run(self):
        print('Run faster')
sunny=penguin()
sunny.whoisthis()
sunny.run()
sunny.swim()
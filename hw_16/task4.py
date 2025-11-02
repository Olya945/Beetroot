class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        file = open('logs.txt', 'a')
        file.write(msg + '\n')
        file.close()


class IncorrectFileExtension(Exception):
    def __init__(self):
        super().__init__('El archivo no tiene la extensión correcta de .txt')
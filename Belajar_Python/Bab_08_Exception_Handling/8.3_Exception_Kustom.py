# Membuat exception kustom
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def test_error():
    raise CustomError("Ini adalah exception kustom")

try:
    test_error()
except CustomError as e:
    print(e)

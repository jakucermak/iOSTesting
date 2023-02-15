import wda

class IOSCLient():
    def __init__(self, port):
          self.port = port

    def start_client(self):

        client = wda.Client(f"http://localhost:{self.port}")
        return client
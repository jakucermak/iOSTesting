import wda
import time


class IOSCLient():
    def __init__(self, port):
        self.port = port
        self.client = self.start_client()

    def start_client(self):

        client = wda.Client(f"http://localhost:{self.port}")
        return client

    def script(self):
        while True:
            c = self.client
            c.home()

            c.screenshot("./screenshots/init.png")

            c.swipe_left()

            time.sleep(1)

            c.swipe_right()

            print(c.status())
            c.click(133, 200)
            print(c.app_current())

            c.screenshot("./screenshots/contacts.png")

            c.home()
            c.swipe(370, 0, 370, 200, 0.5)
            time.sleep(1)
            c.swipe(370, 200, 370, 0, 0.5)
            s = c.session('com.apple.Health')
            c.home()

import wda
import time

wda.DEBUG = False

c = wda.Client('http://169.254.17.234:8100')

c.home()

c.screenshot("init.png")

c.swipe_left()

time.sleep(1)

c.swipe_right()

print( c.status())
c.click(133,200)
print(c.app_current())

c.screenshot("contacts.png")



c.home()
c.swipe(370,0,370,200,0.5)
time.sleep(1)
c.swipe(370,200,370,0,0.5)
s = c.session('com.apple.Health')
print(s.orientation)

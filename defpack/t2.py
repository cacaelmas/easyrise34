import win32api, time

# in this example i'm using a dictionary (that i called VK_CODE)
# to map the keys to their respective virtual key codes

# Sending the key a
import win32con

i = 'a'

VK_CODE = {
    'a': 0x41
}
# send key down event
win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), 0, 0)

# wait for it to get registered.
# You might need to increase this time for some applications
time.sleep(.05)

# send key up event
win32api.keybd_event(VK_CODE[i], win32api.MapVirtualKey(VK_CODE[i], 0), win32con.KEYEVENTF_KEYUP, 0)
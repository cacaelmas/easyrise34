from ahk import AHK

ahk = AHK(executable_path="C:\\Program Files\\AutoHotkey\\AutoHotkeyU64.exe")

print(ahk.mouse_position)  # Returns a tuple of mouse coordinates (x, y)
ahk.mouse_move(100, 100, speed=10, relative=True)  # Moves the mouse reletave to the current position

for i in range(0,10):
    ahk.key_down('z', blocking=False)  # Press down (but do not release) Control key
    ahk.key_up('z', blocking=False)  # Release the key

zzzzzzzzzz
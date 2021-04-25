import AutoHotPy
from InterceptionWrapper import *

repeat_always = False


def exitAutoHotKey(autohotpy, event):
    """
    exit the program when you press ESC
    """
    autohotpy.stop()


def alwaysLoopMacro(autohotpy, event):
    global repeat_always
    autohotpy.A.press()
    autohotpy.B.press()
    autohotpy.C.press()

    # now that we are finished, let's check if we should loop
    # If repeat_always= true, then we tell autohotpy to run loopMacro again
    if repeat_always:
        autohotpy.run(alwaysLoopMacro, event)


def enableDisableLoopMacro(autohotpy, event):
    global repeat_always

    if repeat_always:
        repeat_always = False
    else:
        # let's enable it, and then we call it for the first time, so it starts running as soon as possible
        repeat_always = True
        alwaysLoopMacro(autohotpy, event)


if __name__ == "__main__":
    auto = AutoHotPy()
    auto.registerExit(auto.F10,
                      exitAutoHotKey)  # Registering an end key is mandatory to be able tos top the program gracefully

    auto.registerForKeyDown(auto.F1, enableDisableLoopMacro)

    auto.start()

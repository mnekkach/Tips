import ctypes

zelib = ctypes.CDLL(r"C:\\Developement\\C\\firstprg\\main.dll")

res = zelib.triple(5)

print res
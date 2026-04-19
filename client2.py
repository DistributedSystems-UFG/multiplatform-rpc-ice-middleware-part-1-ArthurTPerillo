import sys, Ice
import Demo

communicator = Ice.initialize(sys.argv)
base1 = communicator.stringToProxy("SimplePrinter1:tcp -h 54.80.68.98 -p 5678")
base2 = communicator.stringToProxy("SimplePrinter2:tcp -h 54.80.68.98 -p 5678")
printer1 = Demo.PrinterPrx.checkedCast(base1)
printer2 = Demo.PrinterPrx.checkedCast(base2)
if (not printer1) or (not printer2):
    raise RuntimeError("Invalid proxy")

rep = printer1.printString("Hello World from printer1!")
print("printString reply:", rep)
rep = printer2.printString("Hello World from printer2!")
print("printString reply:", rep)

rep = printer1.reverseString("Hello from printer1!")
print("reverseString reply:", rep)
rep = printer2.reverseString("Hello from printer2!")
print("reverseString reply:", rep)

rep = printer1.toUpperCase("hello from printer1!")
print("toUpperCase reply:", rep)
rep = printer2.toUpperCase("hello from printer2!")
print("toUpperCase reply:", rep)

communicator.waitForShutdown()

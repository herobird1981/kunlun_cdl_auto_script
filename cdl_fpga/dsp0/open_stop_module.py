import os
import time
import sys
sys.path.append('.')
import testlib
reload(testlib)
testlib.init()
if __name__ == '__builtin__':
    testlib.crt = crt
    sys.dont_write_bytecode = True

def main():
    for count in range(1000000):
        #print("test %d times" % count)
        os.system(r'D:\bootrest\TestApp\CommandApp_USBRelay.exe BITFT close 01')
        #result = ','.join(["close\t01 %05d" % count, time.strftime('%Y%m%d-%H%M%S') + '\n'])
        #log_write(outfile1, result)
        if (crt.Screen.WaitForString("usb_boot", 7) != True):
            sys.exit(0)
        #time.sleep(5)

        os.system(r'D:\bootrest\TestApp\CommandApp_USBRelay.exe BITFT open 01')
        #result = ','.join(["open\t01 %05d" % count, time.strftime('%Y%m%d-%H%M%S') + '\n'])
        #log_write(outfile1, result)
        crt.Screen.Clear()
        time.sleep(10)

# print "test point 2"
main()

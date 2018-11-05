# $language = "Python"
# $interface = "1.0"
import sys
sys.path.append('.')
import testlib
reload(testlib)
testlib.init()
if __name__ == '__builtin__':
    testlib.crt = crt
    sys.dont_write_bytecode = True
###################################################


###################################################


def enter_led_test_menu():
    testlib.enter_menu('led')


def led_reset_on():
    testlib.runCase2('led_test_reset 0')


def led_reset_off():
    testlib.runCase2('led_test_reset 0')


def led_test_outputset():
    for i in range(0x40):
        testlib.runCase2('led_test_oe %d' % (i))
        testlib.sleep(200)


def led_test_brightness():
    testlib.runCase2('led_test_oe 0x3f')
    for i in range(16):
        testlib.runCase2('led_test_brightness %d 0x7f' % (i))
        testlib.sleep(500)


def main():
    testcases = [
        enter_led_test_menu,
        led_test_brightness,
        led_test_outputset,
    ]
    testlib.runCaseList(testcases,
                        logpath=testlib.GetFileNameAndExt(
                            __file__)[0] + '\\LOG\\',
                        filename=testlib.GetFileNameAndExt(__file__)[1])


if __name__ == '__builtin__':
    for i in range(1):
        main()

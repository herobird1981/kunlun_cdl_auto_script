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


def enter_ptc_test_menu():
    testlib.enter_menu('ptc')


def ptc_pwm():
    for i in (0, 1, 2):
        cmd = 'ptc_test_pwm %d 100 200' % (i)
        testlib.inputStr(cmd + '\r\n')
        testlib.sleep(2000)


def main():
    testcases = [
        enter_ptc_test_menu,
        ptc_pwm,
    ]
    testlib.runCaseList(testcases,
                        logpath=testlib.GetFileNameAndExt(
                            __file__)[0] + '\\LOG\\',
                        filename=testlib.GetFileNameAndExt(__file__)[1])


if __name__ == '__builtin__':
    for i in range(1):
        main()

# $language = "Python"
# $interface = "1.0"
'''precondition:download cdl to flash, so cdl will be loaded after wdt reset'''
import sys
sys.path.append('.')
import testlib
reload(testlib)
testlib.init()
if __name__ == '__builtin__':
    testlib.crt = crt
    sys.dont_write_bytecode = True
###################################################

def enter_wdog_test_menu():
    testlib.enter_menu('wdog')
    testlib.sleep(50)

def wdog_start_stop():
    cmd = 'wdog_start_stop'
    testlib.runCase2(cmd)


def wdog_reload():
    vals = [3000, 5000]
    for i in vals:
        cmd_start = 'wdog_reload start %d' % (i)
        testlib.runCase2(cmd_start)
        cmd_restart = 'wdog_reload restart %d' % (i)
        testlib.runCase2(cmd_restart)

def wdog_int():
    cmd = 'wdog_int'
    testlib.runCase2(cmd)


def wdog_reset():
    cmd = 'wdog_reset 1000'
    testlib.runCase2(cmd, passlist=['Select the device to test :'])
##########################################################################


def main():
    testcases = [
        enter_wdog_test_menu,
        wdog_start_stop,
        wdog_reload,
        wdog_int,
        # wdog_reset,
    ]
    testlib.runCaseList(testcases,
                        logpath=testlib.GetFileNameAndExt(
                            __file__)[0] + '\\LOG\\',
                        filename=testlib.GetFileNameAndExt(__file__)[1])


if __name__ == '__builtin__':
    main()

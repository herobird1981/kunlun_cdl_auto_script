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
valuedict = {
    'id'		: [i for i in range(2)],
    'trig_val'  : [1, 5],
}
formatdict = {
    'id'		: '%d',
    'trig_val'  : '%d',

}
###################################################

def enter_timer_test_menu():
    testlib.enter_menu('timer')

def timer_start_stop():
    cmd = 'timer_start_stop id'
    testlib.runAllCombo(cmd, valuedict, formatdict, passlist=['test pass'], faillist=['test fail'])

def timer_reload():
    cmd = 'timer_reload id'
    testlib.runAllCombo(cmd, valuedict, formatdict)

def timer_int():
    cmd = 'timer_test_int id trig_val'
    testlib.runAllCombo(cmd, valuedict, formatdict)

##########################################################################


def main():
    enter_timer_test_menu()
    testcases = [        
        timer_reload,
        timer_start_stop,
        timer_int,
    ]
    testlib.runCaseList(testcases,
                        logpath=testlib.GetFileNameAndExt(
                            __file__)[0] + '\\LOG\\',
                        filename=testlib.GetFileNameAndExt(__file__)[1])


if __name__ == '__builtin__':
    main()

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
gpio_pair = [
    ('0 0', '0, 1'),
]

###################################################


def enter_gpio_test_menu():
    testlib.enter_menu('gpio')


def gpio_input_output():
    for pair in gpio_pair:
        '''[0] output and [1] input'''
        testlib.inputStr('gpio_input %s 0\r\n' % (pair[1]))

        testlib.inputStr('gpio_output %s 1\r\n' % (pair[0]))
        testlib.runCase2('gpio_input %s 1' % (pair[1]), passlist=['cmd:>'])
        testlib.inputStr('gpio_output %s 0\r\n' % (pair[0]))
        testlib.runCase2('gpio_input %s 0' % (pair[1]), passlist=['cmd:>'])
        '''[1] output and [0] input'''
        testlib.inputStr('gpio_input %s 0\r\n' % (pair[0]))

        testlib.inputStr('gpio_output %s 1\r\n' % (pair[1]))
        testlib.runCase2('gpio_input %s 1' % (pair[0]), passlist=['cmd:>'])
        testlib.inputStr('gpio_output %s 0\r\n' % (pair[1]))
        testlib.runCase2('gpio_input %s 0' % (pair[0]), passlist=['cmd:>'])


def main():
    testcases = [
        enter_gpio_test_menu,
        gpio_input_output,
    ]
    testlib.runCaseList(testcases,
                        logpath=testlib.GetFileNameAndExt(
                            __file__)[0] + '\\LOG\\',
                        filename=testlib.GetFileNameAndExt(__file__)[1])


if __name__ == '__builtin__':
    for i in range(1):
        main()

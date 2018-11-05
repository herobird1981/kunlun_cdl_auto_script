# $language = "Python"
# $interface = "1.0"
import sys
sys.path.append('.')
import testlib
reload(testlib)
testlib.init()
if __name__ == '__builtin__':
    testlib.crt = crt
###################################################
# Precondition: need to connect TX&RX pins, connect CTS/RTS pins of UART
# port before testing.
valuedict = {
    'dma': [0, 1],
    'baudrate': [300, 1200, 9600, 115200, 460800, 921600, 1843200, 3686400],
    'parity': ['n', 'e', 'o'],
    'data_bits': [5, 6, 7, 8],
    'stop_bits': [1, 2],
    'flow_ctl': [0, 1],
    'length': [128],
    'pattern': [0xaa]
}
formatdict = {
    'dma': '%d',
    'baudrate': '%d',
    'parity': '%c',
    'data_bits': '%d',
    'stop_bits': '%d',
    'flow_ctl': '%d',
    'length': '%d',
    'pattern': '0x%x',
}
###################################################


def enter_uart0_test_menu():
    testlib.enter_menu('uart0')

def enter_uart1_test_menu():
    testlib.enter_menu('uart1')

def uart_tx():
    cmd = 'uart_test_tx dma'
    testlib.runAllCombo(cmd, valuedict, formatdict, passlist=['abcdefghijklmnopqrstuvwxyz0123456789'])

def uart_rx():
    cmd = 'uart_test_rx 0'
    sendstr = 'abcdefghijklmnopqrstuvwxyz0123456789'
    testlib.inputStr(cmd + '\r\n')
    for i in sendstr:
        testlib.runCase2(i, passlist=['recv: 1, bytes: %s' % (i)])
    testlib.inputStr('qq\r\n')

def uart_int():
    cmd = 'uart_int dma'
    testlib.runAllCombo(cmd, valuedict, formatdict, passlist=['pass'])

def main():
    testcases = [
        enter_uart0_test_menu,
        uart_tx,
        uart_rx,
        # uart_int,
    ]
    testlib.runCaseList(testcases,
                        logpath=testlib.GetFileNameAndExt(
                            __file__)[0] + '\\LOG\\',
                        filename=testlib.GetFileNameAndExt(__file__)[1])

if __name__ == '__builtin__':
    main()

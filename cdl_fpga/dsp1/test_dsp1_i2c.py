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
# connect i2c0 to i2c1 (data & clk)
###################################################
valuedict = {
    'dma': [0],
    'speed': [100000, 400000],
    'addr': ['7b 0x55', '10b 0x123'],
    'int_addr': ['0x55 7b', '0x123 10b'],
    'length': [1024, 2048],
    'pattern': [0xaa, 0x55],
}
formatdict = {
    'dma': '%d',
    'speed': '%d',
    'addr': '%s',
    'int_addr': '%s',
    'length': '%d',
    'pattern': '0x%x',
}

####################################################

def enter_i2c_master_menu():
    testlib.enter_menu('i2c_master')

def enter_i2c_slave_menu():
    testlib.enter_menu('i2c_slave')

def i2c_test_loopback():
    cmd = "i2c_test_loopback speed dma addr length pattern"
    testlib.runAllCombo(cmd, valuedict, formatdict)

def i2c_test_int():
    cmd = "i2c_int_master int_addr"
    testlib.runAllCombo(cmd, valuedict, formatdict, passlist=['int_sts=0x10'])

def main():
    testcases = [
        enter_i2c_master_menu,
        i2c_test_loopback,
        i2c_test_int,
        enter_i2c_slave_menu,
        i2c_test_loopback,
        i2c_test_int,
    ]

    testlib.runCaseList(testcases,
                        logpath=testlib.GetFileNameAndExt(
                            __file__)[0] + '\\LOG\\',
                        filename=testlib.GetFileNameAndExt(__file__)[1])
if __name__ == '__builtin__':
    main()
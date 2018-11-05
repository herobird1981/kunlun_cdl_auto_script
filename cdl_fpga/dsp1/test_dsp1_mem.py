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
    # 'mem_addr': [0x40000000, 0x3FFE8000, 0x60000000, 0x60080000, 0x60100000, 0x60180000],
    'mem_addr': [0x60000000, 0x60080000, 0x60100000, 0x60180000], #SRAM0/1/2/3 address
    'data_length': [0x100, 0x1000, 0x10000],
    '8bits_pattern': [0xaa, 0x55],
    '16bits_pattern': [0x55aa, 0xaabb],
    '32bits_pattern': [0xaa55a5a5, 0x55aa5a5a],
}

formatdict = {
    'mem_addr': '0x%x',
    'data_length': '0x%x',
    '8bits_pattern': '0x%x',
    '16bits_pattern': '0x%x',
    '32bits_pattern': '0x%x',
}
###################################################

def enter_mem_test_menu():
    testlib.enter_menu('mem')

def mem_rd():
    rd8_cmd = 'mem_rd8 mem_addr data_length'
    rd16_cmd = 'mem_rd16 mem_addr data_length'
    rd32_cmd = 'mem_rd32 mem_addr data_length'
    testlib.runAllCombo(rd8_cmd, valuedict, formatdict, passlist=['cmd:>'])
    testlib.runAllCombo(rd16_cmd, valuedict, formatdict, passlist=['cmd:>'])
    testlib.runAllCombo(rd32_cmd, valuedict, formatdict, passlist=['cmd:>'])

def mem_wr():
    wr8_cmd = 'mem_wr8 mem_addr 8bits_pattern'
    wr16_cmd = 'mem_wr16 mem_addr 16bits_pattern'
    wr32_cmd = 'mem_wr32 mem_addr 32bits_pattern'
    testlib.runAllCombo(wr8_cmd, valuedict, formatdict, passlist=['cmd:>'])
    testlib.runAllCombo(wr16_cmd, valuedict, formatdict, passlist=['cmd:>'])
    testlib.runAllCombo(wr32_cmd, valuedict, formatdict, passlist=['cmd:>'])


def main():
    testcases = [
        enter_mem_test_menu,
        mem_wr,
        mem_rd,
    ]
    testlib.runCaseList(testcases,
                        logpath=testlib.GetFileNameAndExt(
                            __file__)[0] + '\\LOG\\',
                        filename=testlib.GetFileNameAndExt(__file__)[1])


if __name__ == '__builtin__':
    for i in range(1):
        main()
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
    'dma_mode': [0, 1],
    'speed': [1000000],
    'type': [0, 1],
    'master_slave': [0, 1],
    'master_slave_for_loopback': [0],
    'mode': [0, 1, 2, 3],
    #'data_size': [4, 8],
    'data_size': [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    'length': [4096],
    'pattern': [0x5a],
}
formatdict = {
    'dma_mode': '%d',
    'speed': '%d',
    'type': '%d',
    'master_slave': '%d',
    'master_slave_for_loopback': '%d',
    'mode': '%d',
    'data_size': '%d',
    'length': '%d',
    'pattern': '0x%x',
}
chip_dict = {
    'MX25V8035F': 0x100000,
    'W25Q16D': 0x200000,
    'IS25LP016D': 0x200000,
}
###################################################
tmo = 200
Dblk = 0
Blknum = 32
Vol = 0x200000


def enter_spi_test_menu():
    testlib.enter_menu('spi')


def spi_loopback():
    cmd = 'spi_test_loopback speed type master_slave_for_loopback mode data_size dma_mode length'
    testlib.runAllCombo(cmd, valuedict, formatdict)

def spi_int():
    cmd = 'spi_int'
    testlib.runCase2(cmd)

def main():
    testcases = [
        enter_spi_test_menu,
        spi_loopback,
        spi_int,
    ]
    testlib.runCaseList(testcases,
                        logpath=testlib.GetFileNameAndExt(
                            __file__)[0] + '\\LOG\\',
                        filename=testlib.GetFileNameAndExt(__file__)[1])


if __name__ == '__builtin__':
    for i in range(1):
        main()

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
    'dma_mode': [0],
    # 'dma_mode': [0, 1],
    'speed': [1000000],
    'type': [0],
    'master_slave': [0],
    # 'master_slave': [0, 1],
    'mode': [0, 3],
    'data_size': [8], # only support 8-bit data width
    'length': [0x10000, 0x20000],
    'pattern': [0x5a],
}
formatdict = {
    'dma_mode': '%d',
    'speed': '%d',
    'type': '%d',
    'master_slave': '%d',
    'mode': '%d',
    'data_size': '%d',
    'length': '0x%x',
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


def spi_flash_init():
    global Vol
    testlib.enter_menu('spi')
    testlib.inputStr('spi_flash_probe 0 10000000 0 0 0 8\r\n')
    chip_type = testlib.getStrBetween1(
        'detect spi flash: ', '\r\nflash chip is spi nor flash')
    Vol = chip_dict[chip_type]

def enter_spi_test_menu():
    testlib.enter_menu('spi')

def spi_flash_probe():
    cmd = 'spi_flash_probe speed type master_slave mode data_size dma_mode'
    testlib.runAllCombo(cmd, valuedict, formatdict)

def spi_flash_erase():
    cmd = 'spi_flash_erase_sec 0x0 length'
    testlib.runAllCombo(cmd, valuedict, formatdict)

def spi_flash_write():
    cmd = 'spi_flash_write 0x0 length'
    testlib.runAllCombo(cmd, valuedict, formatdict)

def spi_flash_read():
    cmd = 'spi_flash_read 0x0 length'
    testlib.runAllCombo(cmd, valuedict, formatdict, timeout=120)

def spi_flash_test():
    cmd = 'spi_flash_test speed type master_slave mode data_size dma_mode'
    testlib.runAllCombo(cmd, valuedict, formatdict)

def spi_flash_burning():
    cmd1 = 'spi_flash_erase_sec 0x0 0x20000'
    cmd2 = 'spi_flash_burning'
    testlib.runCase2(cmd1)
    testlib.runCase2(cmd2)

def spi_int():
    cmd = 'spi_int'
    testlib.runCase2(cmd)

def main():
    testcases = [
        enter_spi_test_menu,
        spi_flash_probe,
        spi_flash_erase,
        spi_flash_write,
        spi_flash_read,
        spi_flash_test,
        spi_flash_burning,
        spi_int,
    ]
    testlib.runCaseList(testcases,
                        logpath=testlib.GetFileNameAndExt(
                            __file__)[0] + '\\LOG\\',
                        filename=testlib.GetFileNameAndExt(__file__)[1])


if __name__ == '__builtin__':
    for i in range(1):
        main()

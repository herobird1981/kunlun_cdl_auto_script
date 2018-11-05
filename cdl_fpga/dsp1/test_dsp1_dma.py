# $language = "Python"
# $interface = "1.0"
import sys
import re
sys.path.append('.')
import testlib
reload(testlib)
testlib.init()
if __name__ == '__builtin__':
    testlib.crt = crt
    sys.dont_write_bytecode = True

dsp0_dram1_addr1 = 0x30008000  # dsp0_dram1 size is 0x8000
dsp0_dram1_addr2 = dsp0_dram1_addr1 + 0x4000
dsp0_iram1_addr1 = 0x30030000  # dsp0_iram1 size is 0x8000
dsp0_iram1_addr2 = dsp0_iram1_addr1 + 0x4000
dsp0_iram0_addr1 = 0x300207c8  # dsp0_iram0 size is 0xf838
dsp0_iram0_addr2 = dsp0_iram0_addr1 + 0x7c18

dsp1_dram1_addr1 = 0x50008000  # dsp1_dram1 size is 0x8000
dsp1_dram1_addr2 = dsp1_dram1_addr1 + 0x4000
dsp1_iram1_addr1 = 0x50030000  # dsp1_iram1 size is 0x8000
dsp1_iram1_addr2 = dsp1_iram1_addr1 + 0x4000
dsp1_iram0_addr1 = 0x500207c8  # dsp1_iram0 size is 0xf838
dsp1_iram0_addr2 = dsp1_iram0_addr1 + 0x7c18

dsp_sram_addr1 = 0x6015d108  # shared between dsp0 & dsp1
dsp_sram_addr2 = dsp_sram_addr1 + 0x51778

###################################################
valuedict = {
    'ch': [0, 1, 2, 3, 4, 5, 6, 7],
    'src_addr': [dsp0_dram1_addr1, dsp0_iram1_addr1, dsp0_iram0_addr1, dsp1_dram1_addr1,
                 dsp1_iram1_addr1, dsp1_iram0_addr1, dsp_sram_addr1],
    'dst_addr': [dsp0_dram1_addr2, dsp0_iram1_addr2, dsp0_iram0_addr2, dsp1_dram1_addr2,
                 dsp1_iram1_addr2, dsp1_iram0_addr2, dsp_sram_addr2],
    'length': [0x400, 0x800],  # max support size is 4k bytes
    'is_display': [0, 1],
}

formatdict = {
    'ch': '%d',
    'src_addr': '0x%x',
    'dst_addr': '0x%x',
    'length': '0x%x',
    'is_display': '%d',
}
###################################################


def get_addr(text, mode):
    pattern = re.compile(mode)
    return map(lambda x: int(x, 16), pattern.search(text).groups())

def enter_dma_test_menu():
    global valuedict
    testlib.inputStr('q\r\n')
    testlib.inputStr('dma\r\n')
    text = crt.Screen.ReadString('cmd:>', 1)


    dsp0_dram1_start, dsp0_dram1_len = get_addr(text, r'dsp0_dram1.*(0x[0-9a-f]{8}).*(0x[0-9a-f]+)')
    dsp0_iram0_start, dsp0_iram0_len = get_addr(text, r'dsp0_iram0.*(0x[0-9a-f]{8}).*(0x[0-9a-f]+)')
    dsp0_iram1_start, dsp0_iram1_len = get_addr(text, r'dsp0_iram1.*(0x[0-9a-f]{8}).*(0x[0-9a-f]+)')
    dsp1_dram1_start, dsp1_dram1_len = get_addr(text, r'dsp1_dram1.*(0x[0-9a-f]{8}).*(0x[0-9a-f]+)')
    dsp1_iram0_start, dsp1_iram0_len = get_addr(text, r'dsp1_iram0.*(0x[0-9a-f]{8}).*(0x[0-9a-f]+)')
    dsp1_iram1_start, dsp1_iram1_len = get_addr(text, r'dsp1_iram1.*(0x[0-9a-f]{8}).*(0x[0-9a-f]+)')
    sram_start, sram_len = get_addr(text, r'sram.*(0x[0-9a-f]{8}).*(0x[0-9a-f]+)')

    valuedict['src_addr'][0] = dsp0_dram1_start
    valuedict['src_addr'][1] = dsp0_iram0_start
    valuedict['src_addr'][2] = dsp0_iram1_start
    valuedict['src_addr'][3] = dsp1_dram1_start
    valuedict['src_addr'][4] = dsp1_iram0_start
    valuedict['src_addr'][5] = dsp1_iram1_start
    valuedict['src_addr'][6] = sram_start

    valuedict['dst_addr'][0] = valuedict['src_addr'][0] + int(dsp0_dram1_len / 2 / 0x10) * 0x10
    valuedict['dst_addr'][1] = valuedict['src_addr'][1] + int(dsp0_iram0_len / 2 / 0x10) * 0x10
    valuedict['dst_addr'][2] = valuedict['src_addr'][2] + int(dsp0_iram1_len / 2 / 0x10) * 0x10
    valuedict['dst_addr'][3] = valuedict['src_addr'][3] + int(dsp1_dram1_len / 2 / 0x10) * 0x10
    valuedict['dst_addr'][4] = valuedict['src_addr'][4] + int(dsp1_iram0_len / 2 / 0x10) * 0x10
    valuedict['dst_addr'][5] = valuedict['src_addr'][5] + int(dsp1_iram1_len / 2 / 0x10) * 0x10
    valuedict['dst_addr'][6] = valuedict['src_addr'][6] + int(sram_len / 2 / 0x10) * 0x10

def dma_mem_to_mem():
    cmd = 'dma_test_m2m ch dst_addr src_addr length is_display'
    testlib.runAllCombo(cmd, valuedict, formatdict)


def dma_int():
    cmd = 'dma_int ch'
    testlib.runAllCombo(cmd, valuedict, formatdict)


def main():
    testcases = [
        enter_dma_test_menu,
        dma_mem_to_mem,
        dma_int,
    ]
    testlib.runCaseList(testcases,
                        logpath=testlib.GetFileNameAndExt(
                            __file__)[0] + '\\LOG\\',
                        filename=testlib.GetFileNameAndExt(__file__)[1])

if __name__ == '__builtin__':
    for i in range(1):
        main()

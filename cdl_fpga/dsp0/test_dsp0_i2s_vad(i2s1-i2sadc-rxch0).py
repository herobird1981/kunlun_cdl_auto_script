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
    'port_rx': [0], #0: I2S_ADC
    'port_tx': [2], #1: I2S_DAC; 2: I2S_1.    
    'dma_mode': [0], #0: CPU mode
    'pi_mode': [0, 1], #0: polling
    'sample_format': [32], # only support 32: S32_LE.
    'rx_chx_en': ['1 0 0'],
    'dma_rx_chx_en': ['1 0 0'],
    'length': [2048],
    'lr_sel':[0, 1], #0, left; 1 right
    'stop_dly':[0, 1, 2, 3],
}

formatdict = {
    'port_rx': '%d',
    'port_tx': '%d',
    # 'dac_mode': '%d',
    'dma_mode': '%d',
    'pi_mode': '%d',
    'sample_format': '%d',
    'rx_chx_en': '%s',
    'dma_rx_chx_en': '%s',
    'length': '%d',
    'lr_sel':'%d',
    'stop_dly':'%d',
}

###################################################

def enter_i2s_vad_test_menu():
    testlib.enter_menu('i2s_vad')


def i2s_vad_test_loopback():
    cmd = 'i2s_vad_test_loopback 0 port_tx 1 0 sample_format rx_chx_en length lr_sel stop_dly'
    testlib.runAllCombo(cmd, valuedict, formatdict, passlist=['test pass'], faillist=['test fail'])

def i2s_vad_int():
    cmd = 'i2s_vad_test_int 0 port_tx 0 pi_mode sample_format rx_chx_en 2048 lr_sel stop_dly'
    testlib.runAllCombo(cmd, valuedict, formatdict, passlist=['test pass'], faillist=['test fail'])

def main():
    testcases = [
        enter_i2s_vad_test_menu,
        i2s_vad_test_loopback,
        i2s_vad_int,
    ]
    testlib.runCaseList(testcases,
                        logpath=testlib.GetFileNameAndExt(
                            __file__)[0] + '\\LOG\\',
                        filename=testlib.GetFileNameAndExt(__file__)[1])


if __name__ == '__builtin__':
    for i in range(1):
        main()

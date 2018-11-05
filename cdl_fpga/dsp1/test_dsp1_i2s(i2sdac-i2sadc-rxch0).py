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
    'port_rx': [0, 3], #0: I2S_ADC; 3: I2S_VAD
    'port_tx': [1], #1: I2S_DAC; 2: I2S_1.
    'dma_mode': [0, 1], #0: CPU mode
    'pi_mode': [0, 1], #0: polling
    'sampling_format': [16, 24, 32], # 16: S16_LE; 24: S24_LE; 32: S32_LE.
    'rx_chx_en': ['1 0 0'],
    'dma_rx_chx_en': ['1 0 0'],
    'length': [1024, 2048],
}

formatdict = {
    'port_rx': '%d',
    'port_tx': '%d',
    'dma_mode': '%d',
    'pi_mode': '%d',
    'sampling_format': '%d',
    'rx_chx_en': '%s',
    'dma_rx_chx_en': '%s',
    'length': '%d',
}

###################################################

def enter_i2s_test_menu():
    testlib.enter_menu('i2s_adc')


def i2s_test_loopback_cpu():
    cmd = 'i2s_test_loopback 0 port_tx 0 pi_mode sampling_format rx_chx_en length'
    testlib.runAllCombo(cmd, valuedict, formatdict, passlist=['test pass'], faillist=['test fail'])

def i2s_test_loopback_dma():
    cmd = 'i2s_test_loopback 0 port_tx 1 0 sampling_format dma_rx_chx_en length'
    testlib.runAllCombo(cmd, valuedict, formatdict, passlist=['test pass'], faillist=['test fail'])

def i2s_test_int():
    cmd = 'i2s_adc_rx_int port_rx 0 pi_mode sampling_format rx_chx_en length'
    testlib.runAllCombo(cmd, valuedict, formatdict, passlist=['test pass'], faillist=['test fail'])


def main():
    testcases = [
        enter_i2s_test_menu,
        i2s_test_loopback_cpu,
        i2s_test_loopback_dma,
        i2s_test_int,
    ]
    testlib.runCaseList(testcases,
                        logpath=testlib.GetFileNameAndExt(
                            __file__)[0] + '\\LOG\\',
                        filename=testlib.GetFileNameAndExt(__file__)[1])


if __name__ == '__builtin__':
    for i in range(1):
        main()

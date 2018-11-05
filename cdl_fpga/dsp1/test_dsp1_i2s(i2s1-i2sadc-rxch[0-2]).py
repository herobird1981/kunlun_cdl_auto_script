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
    'port_rx': [0], #0: I2S_ADC; 3: I2S_VAD (not supported now)
    'port_tx': [2], #1: I2S_DAC; 2: I2S_1.    
    # 'dac_mode': [1], #0: signal from codec; 1: signal from pad
    'dma_mode': [0], #0: CPU mode
    'pi_mode': [0, 1], #0: polling
    'sampling_format': [16, 24, 32], # 16: S16_LE; 24: S24_LE; 32: S32_LE.
    'rx_chx_en': ['1 0 0', '0 1 0', '0 0 1'],
    'length': [1024, 2048],
}

formatdict = {
    'port_rx': '%d',
    'port_tx': '%d',
    # 'dac_mode': '%d',
    'dma_mode': '%d',
    'pi_mode': '%d',
    'sampling_format': '%d',
    'rx_chx_en': '%s',
    'length': '%d',
}

###################################################

def enter_i2s_test_menu():
    testlib.enter_menu('i2s_adc')


def i2s_test_loopback():
    cmd = 'i2s_test_loopback port_rx port_tx dma_mode pi_mode sampling_format rx_chx_en length'
    testlib.runAllCombo(cmd, valuedict, formatdict)

def main():
    testcases = [
        enter_i2s_test_menu,
        i2s_test_loopback,
    ]
    testlib.runCaseList(testcases,
                        logpath=testlib.GetFileNameAndExt(
                            __file__)[0] + '\\LOG\\',
                        filename=testlib.GetFileNameAndExt(__file__)[1])


if __name__ == '__builtin__':
    for i in range(1):
        main()

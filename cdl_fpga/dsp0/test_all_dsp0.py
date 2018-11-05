# $language = "Python"
# $interface = "1.0"
from importlib import import_module
import sys
sys.path.append('.')
sys.dont_write_bytecode = True


loop_count_raw = crt.Dialog.Prompt("Enter a loop count for auto testing:", "Welcome to Columbus Auto Testing", "", False)

modules = [
    'test_dsp0_timer',
    'test_dsp0_wdt',
    # 'test_dsp0_uart',
    'test_dsp0_gpio',
    # 'test_dsp0_spi',
    'test_dsp0_dma',
    'test_dsp0_spi_flash',
    'test_dsp0_i2c',
    # 'test_dsp0_i2s',
    'test_dsp0_ptc',
    'test_dsp0_mem',
    'test_dsp0_i2s(i2sdac-i2sadc-rxch0)',
    'test_dsp0_i2s_vad(i2sdac-i2sadc-rxch0)'
]

loop_count_int = int(loop_count_raw)
for i in range(loop_count_int):
    for module in modules:
        mo = import_module(module)
        reload(mo)
        mo.crt = crt
        mo.testlib.crt = crt
        mo.testlib.MSGPOP = False
        mo.testlib.log_file = 'result/dsp0_fail_%d.csv' % (i)
        mo.main()

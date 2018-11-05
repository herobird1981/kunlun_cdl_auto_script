# $language = "Python"
# $interface = "1.0"
from importlib import import_module
import sys
sys.path.append('.')
sys.dont_write_bytecode = True


loop_count_raw = crt.Dialog.Prompt("Enter a loop count for auto testing:", "Welcome to Columbus Auto Testing", "", False)

modules = [
    'test_dsp1_timer',
    'test_dsp1_wdt',
    # 'test_dsp1_uart',
    'test_dsp1_gpio',
    # 'test_dsp1_spi',
    'test_dsp1_dma',
    'test_dsp1_spi_flash',
    'test_dsp1_i2c',
    # 'test_dsp1_i2s',
    'test_dsp1_ptc',
    'test_dsp1_mem',
    # 'test_dsp1_i2s(i2s1-i2sadc-rxch0)',
]

loop_count_int = int(loop_count_raw)
for i in range(loop_count_int):
    for module in modules:
        mo = import_module(module)
        reload(mo)
        mo.crt = crt
        mo.testlib.crt = crt
        mo.testlib.MSGPOP = False
        mo.testlib.log_file = 'result/dsp1_fail_%d.csv' % (i)
        mo.main()

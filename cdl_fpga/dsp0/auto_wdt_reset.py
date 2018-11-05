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
			}
formatdict = {
		 	}
###################################################
def enter_wdt_test_menu():
    testlib.enter_menu('wdog')
   
def do_wdt_reset():
	enter_wdt_test_menu()
	cmd1 = 'wdog_reset 2\n'
	testlib.inputStr(cmd1)
	testlib.sleep(10000)

for i in range(10000):
	do_wdt_reset()
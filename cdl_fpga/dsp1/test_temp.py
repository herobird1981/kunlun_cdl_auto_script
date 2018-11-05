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

def enter_mem_test_menu():
    testlib.enter_menu('mem')

def mem_wr():
    cmd = 'mem_wr32 0x60000004 0xaabbccdd\r\n'
    testlib.inputStr(cmd)

def main():
    enter_mem_test_menu()
    testcases = [
        mem_wr,
    ]
    testlib.runCaseList(testcases*5000,
                        logpath=testlib.GetFileNameAndExt(
                            __file__)[0] + '\\LOG\\',
                        filename=testlib.GetFileNameAndExt(__file__)[1])

if __name__ == '__builtin__':
    for i in range(1):
        main()

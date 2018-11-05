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

files=[
      'test_dsp0_i2s(i2s1-i2sadc-rxch0).py',
      'test_dsp0_i2s(i2s1-i2sadc-rxch1).py',
      'test_dsp0_i2s(i2s1-i2sadc-rxch2).py',
      'test_dsp0_i2s(i2s1-i2sadc-rxch[0-2]).py',
      'test_dsp0_i2s(i2sdac-i2sadc-rxch0).py',
      'test_dsp0_i2s(i2sdac-i2sadc-rxch1).py',
      'test_dsp0_i2s(i2sdac-i2sadc-rxch2).py',
      'test_dsp0_i2s(i2sdac-i2sadc-rxch[0-2]).py',
      ]

menu=''
count=1
menu_option=-1

for str1 in files:
    menu= menu + str(count)+'. '+str1.split('.')[0] + '\n'
    count = count+1

while (menu_option > count or menu_option < 1):
    menu_select = str(count)
    menu_select = crt.Dialog.Prompt(menu,"Select I2S test item", '1', False)
    if menu_select == '':
        exit()
    if (int(menu_select) >= 1) and (int(menu_select) < count):
        execfile(files[int(menu_select)-1])
        exit()

# welcome to Python Package Installer.
# this (Open Source)program made for install some module's in python so easily.
# have fun :)

# github.com/lnxpy

import os
from dts import _save
from os import system as sys
from clr import colors
from time import sleep as slp
from datetime import datetime as time

_libs = ['numpy',
         'requests',
         'Scrapy',
         'Pillow',
         'SQLAlchemy',
         'beautifulsoup'+colors.fail+'4'+colors.end,
         'matplotlib',
         'pygame',
         'pyglet',
         'PyQt4-'+colors.fail+'4.11.4'+colors.end+'-cp35-none-win_amd64.whl',
         'pywin32',
         'nltk',
         'nose',
         'ipython']

def _check_network():
    if sys('ping google.com -c1') != 0:
        return 1
    else:
        return 0

def _upgrade_packages():
    _stat = input('do you want to update your packages (y\\n) ~>')
    if _stat == 'y' or _stat == 'Y':
        _stat = sys('sudo apt-get update')
        print('Upgrade '+colors.red+colors.buld+'Done'+colors.end+'!')
        if _stat == 0:
            _save('Update Packages have done at -- '+str(time.now())+'\n')
        else:
            _save('Update Packages havent done at -- '+str(time.now())+'\n')
    else:
        return

def _ins_pip3():
    print('Request for install '+colors.bold+'python3-pip '+colors.end+'at '+colors.end+colors.green+str(time.now())+colors.end)
    print(colors.blue+'please wait for '+colors.end+colors.red+'install '+colors.end+colors.bold+'python3-pip'+colors.end)
    slp(2)
    sys('sudo apt install python3-pip')
    _save('Python3-pip installed -- '+time.now()+'\n')

def _ins_mod(_libs,_capt):
    print('Request for install '+colors.bold+str(_libs[_capt])+colors.end+' at '+colors.end+colors.green+str(time.now())+colors.end)
    print(colors.blue+'please wait for '+colors.end+colors.red+'install '+colors.end+colors.bold+_libs[_capt]+colors.end)
    slp(2)
    _stat = sys('pip3 install '+_libs[_capt])
    if _stat == 0:
       print('installing '+colors.bold+_libs[_capt]+colors.end+' module has '+colors.red+colors.bold+'done'+colors.end)
       _save(_libs[_capt]+' installed -- '+str(time.now())+'\n')
    else:
        print('We have a'+colors.bold+colors.fail+' Problem!'+colors.end)
        print('1 - '+colors.fail+'Check You\'r connection and try again.'+colors.end)
        print('2 - '+colors.fail+'Check the Selected module in you\'r installed module\'s with <pip list> or <pip freeze> command.'+colors.end)
        print('3 - '+colors.fail+'Check the pip version. it must be 3!'+colors.end)
        _save('Problem for install '+_libs[_capt]+' -- '+str(time.now())+'\n')
_check_connection = _check_network()
if _check_connection == 0:
    _upgrade_packages()
    print('#use Python version '+colors.fail+'+3'+colors.end+'#')
    print(colors.blue+'<-Welcome to Python Package Installer->'+colors.end)
    print('made by '+colors.blue+'l'+colors.green+'n'+colors.fail+'x'+colors.red+'p'+colors.end+'y')
    print()
    if __name__ == '__main__':
        _flag_ins_pip3 = input('have you installed Python3 pip package ? (y\\n) ~> ')
        print()
        print()
    else:
        print(colors.fail+'Dopted!'+colors.end)
    if _flag_ins_pip3 == 'n' or _flag_ins_pip3 == 'N':
        _ins_pip3()
    elif _flag_ins_pip3 == 'y' or _flag_ins_pip3 == 'Y':
        for _i in range(0,len(_libs)):
            print(str(_i+1)+' - '+colors.bold+_libs[_i]+colors.end)
        _capt = int(input('Enter the module number (1-'+str(len(_libs))+') ~> '))
        if _capt > len(_libs):
            print('The value is '+colors.fail+'out of range'+colors.end+' of the list of module\'s. try again.')
        _capt -= 1
        _ins_mod(_libs,_capt)
    else:
        print(colors.fail+'wrong'+colors.end+' captured!')
else:
    print(colors.fail+'Check you\'r connection , and Try again!'+colors.end)

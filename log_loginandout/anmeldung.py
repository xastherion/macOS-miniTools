import os
import time

_Rechnername_ = os.uname()[1]
_Benutzername_ = os.getlogin()
_Loginzeit_ = time.ctime()
_AbsoluteZeitIn_ = str(time.time())
_Tabs_ = "\t"

_Protokoll_linie_ = ( _Rechnername_ + _Tabs_ + _Benutzername_ + _Tabs_ + _Loginzeit_ + _Tabs_ +_AbsoluteZeitIn_)

with open('protokoll_loginout.csv','a') as _Protokoll_:
    _Protokoll_.write(_Protokoll_linie_)
_Protokoll_.closed
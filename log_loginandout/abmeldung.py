import os
import time

_Logoutzeit_=time.ctime()
_AbsoluteZeitOut_=str(time.time())
_Tabs_="\t"

_Protokoll_linie_=(_Tabs_+_Logoutzeit_+_Tabs_+_AbsoluteZeitOut_+"\n")
# print(_AbsoluteZeitIn_ - _AbsoluteZeitOut_)


with open('protokoll_loginout.csv',"a+") as _Protokoll_:
    _Protokoll_.write(_Protokoll_linie_)
_Protokoll_.closed



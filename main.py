
from network      import Bluetooth
from ubinascii    import hexlify
from bleAdvReader import BLEAdvReader

def hex(data) :
    if data :
        return hexlify(data).decode().upper()
    return ''

def mac2str(mac) :
    if mac :
        return hexlify(mac, ':').decode().upper()
    return ''

bt = Bluetooth()
bt.start_scan(-1)

while True :
    adv = bt.get_adv()
    if adv :
        mac = mac2str(adv.mac)
        print()
        print()
        print('  - MAC ADDRESS  : %s' % mac)
        print('  - RSSI         : %s' % adv.rssi)
        try :
            r = BLEAdvReader(adv.data)
            for advObj in r.GetAllElements() :
                print('  - OBJECT       : [%s] %s' % (type(advObj), advObj))
        except :
            pass

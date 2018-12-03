from purestorage_schema import *
import purestorage
from pprint import pprint

import urllib3, json
urllib3.disable_warnings()



array = purestorage.FlashArray("10.225.112.180",api_token="ba6a44b5-8589-319b-d1a2-5302c1ec962b")


def check(theClass,theData,many=False):
    o = theClass().load(theData,many)

    if o.errors:
        print("--------------------------------")
        print("error in Type: {}".format(theClass.__name__))
        if isinstance(theData, (list,)):
            pprint(theData[0])
        else:
            pprint(theData)
        
        pprint(o.errors)


#PureFA,array.get(),many=True)
#PureFAControllers,array.get(controllers=True),many=True)
check(PureFASpace,array.get(space=True),many=True)
#PureFAPhoneHome,array.get(phonehome=True))
#PureFARemoteAssist,array.get_remote_assist_status())
check(PureFAConnection,array.list_array_connections(),many=True)
check(PureFANTP,array.get(ntpserver=True))
check(PureFAProxy,array.get(proxy=True))
check(PureFARelayHost,array.get(relayhost=True))
check(PureFASCSITimeout,array.get(scsi_timeout=True))

check(PureFAVolume,array.list_volumes(pending=True),many=True)
check(PureFAVolumeSpace,array.list_volumes(space=True),many=True)
check(PureFAVolumeQos,array.list_volumes(qos=True,pending=True),many=True)


check(PureFASnap,array.list_volumes(snap=True,pending=True),many=True)
check(PureFASnapSpace,array.list_volumes(snap=True,pending=True,space=True),many=True)

check(PureFAHostAll,array.list_hosts(all=True))
check(PureFAHost,array.list_hosts(),many=True)
#check(PureFAHostConnection,array.conn)

check(PureFAHostGroup,array.list_hgroups(),many=True)
#check(PureFAHostGroupConnection,array.list_hgroup_connections()))


check(PureFAAlertEmails,array.list_alert_recipients(),many=True)



check(PureFAMessage,array.list_messages(),many=True)
check(PureFASMTP,array.get_smtp(),many=True)
check(PureFADrive,array.list_drives(),many=True)
check(PureFAHardware,array.list_hardware(),many=True)
check(PureFANetwork,array.list_network_interfaces(),many=True)



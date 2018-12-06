# puremarshmallow

This project provides a complete schema for all Pure Storage FlashArray GET endpoint objects using the marshmallow library.

marshmallow is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.

```
usage: schema_validate.py [-h] [-api API_TOKEN] [-u USERNAME] [-p PASSWORD]
                          [-t THREAD_COUNT] [-r REPEAT_COUNT] [--peek]
                          ip

positional arguments:
  ip                    FlashArray IP or DNS name

optional arguments:
  -h, --help            show this help message and exit
  -api API_TOKEN, --api_token API_TOKEN
                        API Token
  -u USERNAME, --username USERNAME
                        Username for FA
  -p PASSWORD, --password PASSWORD
                        password for FA
  -t THREAD_COUNT, --thread_count THREAD_COUNT
  -r REPEAT_COUNT, --repeat_count REPEAT_COUNT
  --peek                peek at first record
 ```

## Example output

```
$ python3 schema_validate.py 10.225.112.180 --thread_count 8 
Starting worker: fa = purestorage.FlashArray(10.225.112.180, username=pureuser, password=pureuser, api_token=None)
Starting worker: fa = purestorage.FlashArray(10.225.112.180, username=pureuser, password=pureuser, api_token=None)
Starting worker: fa = purestorage.FlashArray(10.225.112.180, username=pureuser, password=pureuser, api_token=None)
Starting worker: fa = purestorage.FlashArray(10.225.112.180, username=pureuser, password=pureuser, api_token=None)
Starting worker: fa = purestorage.FlashArray(10.225.112.180, username=pureuser, password=pureuser, api_token=None)
Starting worker: fa = purestorage.FlashArray(10.225.112.180, username=pureuser, password=pureuser, api_token=None)
Starting worker: fa = purestorage.FlashArray(10.225.112.180, username=pureuser, password=pureuser, api_token=None)
Starting worker: fa = purestorage.FlashArray(10.225.112.180, username=pureuser, password=pureuser, api_token=None)
Testing: PureFABanner().load(fa.get(banner=True), many=False) : Success!
Testing: PureFAConnectionKey().load(fa.get(connection_key=True), many=False) : Success!
Testing: PureFAControllers().load(fa.get(controllers=True), many=True) : Success!
Testing: PureFAIdelTimeout().load(fa.get(idle_timeout=True), many=False) : Success!
Testing: PureFA().load(fa.get(), many=False) : Success!
Testing: PureFANTP().load(fa.get(ntpserver=True), many=False) : Success!
Testing: PureFAPhoneHome().load(fa.get(phonehome=True), many=False) : Success!
Testing: PureFAProxy().load(fa.get(proxy=True), many=False) : Success!
Testing: PureFARelayHost().load(fa.get(relayhost=True), many=False) : Success!
Testing: PureFASCSITimeout().load(fa.get(scsi_timeout=True), many=False) : Success!
Testing: PureFASpace().load(fa.get(space=True), many=True) : Success!
Testing: PureFASyslogserver().load(fa.get(syslogserver=True), many=False) : Success!
Testing: PureFAConnection().load(fa.list_array_connections(), many=True) : Success!
Testing: PureFAConnection().load(fa.list_array_connections(throttle=True), many=True) : Success!
Testing: PureFASenderdomain().load(fa.get(senderdomain=True), many=False) : Success!
Testing: PureFAConsoleLock().load(fa.get_console_lock_status(), many=False) : Success!
Testing: PureFAPhoneHomeStatus().load(fa.get_phonehome(), many=False) : Success!
Testing: PureFARemoteAssist().load(fa.get_remote_assist_status(), many=False) : Success!
Testing: PureFASnapSpace().load(fa.list_volumes(snap=True, pending=True, space=True), many=True) : Success!
Testing: PureFASnap().load(fa.list_volumes(snap=True, pending=True), many=True) : Success!
Testing: PureFAHost().load(fa.list_hosts(), many=True) : Success!
Testing: PureFAHostAll().load(fa.list_hosts(all=True), many=True) : Success!
Testing: PureFAHostCHAP().load(fa.list_hosts(chap=True), many=True) : Success!
Testing: PureFAVolumeQos().load(fa.list_volumes(qos=True, pending=True), many=True) : Success!
Testing: PureFAVolume().load(fa.list_volumes(pending=True), many=True) : Success!
Testing: PureFAVolumeSpace().load(fa.list_volumes(space=True), many=True) : Success!
Testing: PureFAHostPersonality().load(fa.list_hosts(personality=True), many=True) : Success!
Testing: PureFAHGroup().load(fa.list_hgroups(), many=True) : Success!
Testing: PureFAHGroupConnect().load(fa.list_hgroups(connect=True), many=True) : Success!
Testing: PureFAPod().load(fa.list_pods(), many=True) : Success!
Testing: PureFAPGroup().load(fa.list_pgroups(pending=True), many=True) : Success!
Testing: PureFAHostConnect().load(fa.list_hosts(connect=True), many=True) : Success!
Testing: PureFAPGroupSchedule().load(fa.list_pgroups(schedule=True), many=True) : Success!
Testing: PureFAPort().load(fa.list_ports(), many=True) : Success!
Testing: PureFAPod().load(fa.list_pods(pending=True, failover_preference=True), many=True) : Success!
Testing: PureFAPGroupRetention().load(fa.list_pgroups(retention=True), many=True) : Success!
Testing: PureFAAlertEmails().load(fa.list_alert_recipients(), many=True) : Success!
Testing: PureFAPortInitiators().load(fa.list_ports(initiators=True), many=True) : Success!
Testing: PureFADNS().load(fa.get_dns(), many=False) : Success!
Testing: PureFASMTP().load(fa.get_smtp(), many=False) : Success!
Testing: PureFASMTP().load(fa.list_snmp_managers(), many=True) : Success!
Testing: PureFAMessage().load(fa.list_messages(), many=True) : Success!
Testing: PureFACert().load(fa.list_certificates(), many=True) : Success!
Testing: PureFASubnet().load(fa.list_subnets(), many=True) : Success!
Testing: PureFANetwork().load(fa.list_network_interfaces(), many=True) : Success!
Testing: PureFADirectoryService().load(fa.get_directory_service(), many=False) : Success!
Testing: PureFAHardware().load(fa.list_hardware(), many=True) : Success!
Testing: PureFAAdmin().load(fa.list_admins(), many=True) : Success!
Testing: PureFADirectoryServiceGroups().load(fa.get_directory_service(groups=True), many=False) : Success!
Testing: PureFADirectoryServiceCertificate().load(fa.get_directory_service(certificate=True), many=False) : Success!
Testing: PureFADrive().load(fa.list_drives(), many=True) : Success!
Testing: PureFAMessageAudit().load(fa.list_messages(audit=True), many=True) : Success!
Testing: PureFAMessageLogin().load(fa.list_messages(login=True), many=True) : Success!
Total time: 0:00:13.745119
Total calls: 53
Calls/sec 4.076923076923077
```

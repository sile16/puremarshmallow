import purestorage_schema as p
import purestorage
import pprint
import threading
import queue
import urllib3
import argparse
from datetime import datetime
urllib3.disable_warnings()


class bcolors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BLUE = '\033[94m'


class APIWorker(threading.Thread):
    def __init__(self, q, ip, config, printLock, args):
        threading.Thread.__init__(self)
        self.printLock = printLock
        self.ip = ip
        self.config = config
        self.q = q
        self.args = args

    def display_error(self, original, marshalled, error):
        message = "\n" + bcolors.RED + error + bcolors.ENDC
        message += "\n----------Original Data------------\n"
        message += bcolors.BLUE
        message += pprint.pformat(original)
        message += bcolors.ENDC
        message += "\n----------Marshalled Result--------\n"
        message += bcolors.BLUE
        message += pprint.pformat(marshalled)
        message += bcolors.ENDC
        message += "\n-----------------------------------\n"
        return message

    def safe_print(self, *args):
        '''Thread safe printing'''
        with self.printLock:
            print(*args)

    def run(self):
        # Create FA object and start session
        self.safe_print("Starting worker")
        self.array = purestorage.FlashArray(self.ip, **self.config)

        while True:
            item = self.q.get()
            theClass = item['theClass']
            # FA Object "function name" was passed by string, get actual func
            arrayFunc = getattr(self.array, item['arrayFunc'])

            # actually make the API call here
            theData = arrayFunc(**item['kwargs'])

            many = False
            if isinstance(theData, (list,)):
                    many = True

            # marshall data here
            o = theClass().load(theData, many)

            # message = ("===============================\n")
            message = "Testing: {}().load(fa.{}(".format(
                       theClass.__name__, item['arrayFunc'])
            delim = ""
            for k, v in item['kwargs'].items():
                message += "{}{}={}".format(delim, k, v)
                delim = ", "
            message += "), many={}) : ".format(many)

            if o.errors:
                message += bcolors.RED + "Error !!! " + bcolors.ENDC
                if many:
                    lastError = ""
                    errorCount = 0
                    for key in o.errors.keys():
                        currError = str(o.errors[key])
                        if currError == lastError:
                            continue
                        lastError = currError
                        errorCount += 1
                        if errorCount > 5:
                            break
                        message += self.display_error(theData[key],
                                                      o.data[key],
                                                      currError)
                else:
                    message += self.display_error(theData,
                                                  o.data,
                                                  str(o.errors))

            else:
                message += bcolors.GREEN + "Success!" + bcolors.ENDC

            if args.peek:
                message += "\n----------Marshalled Result--------\n"
                message += bcolors.BLUE
                if many:
                    message += pprint.pformat(o.data[0])
                else:
                    message += pprint.pformat(o.data)
                message += bcolors.ENDC
                message += "\n-----------------------------------"

            self.safe_print(message)
            self.q.task_done()


def main(args):
    q = queue.Queue()

    config = {"username": args.username,
              "password": args.password}

    # Start threads to do the work.
    printLock = threading.Lock()
    startTime = datetime.now()
    for _ in range(args.thread_count):
        t = APIWorker(q, args.ip, config, printLock, args)
        t.setDaemon(True)
        t.start()

    count = 0

    def check(theClass, arrayFunc, **kwargs):
        nonlocal count
        count += 1
        q.put({"theClass": theClass,
               "arrayFunc": arrayFunc,
               "kwargs": kwargs})

    # fa = purestorage.FlashArray("")

    for x in range(args.repeat_count):
        # array Endpoint
        check(p.PureFA, "get")
        check(p.PureFABanner, "get", banner=True)
        check(p.PureFAConnectionKey, "get", connection_key=True)
        check(p.PureFAControllers, "get", controllers=True)
        check(p.PureFAIdelTimeout, "get", idle_timeout=True)
        check(p.PureFANTP, "get", ntpserver=True)
        check(p.PureFAPhoneHome, "get", phonehome=True)
        check(p.PureFAProxy, "get", proxy=True)
        check(p.PureFARelayHost, "get", relayhost=True)
        check(p.PureFASCSITimeout, "get", scsi_timeout=True)
        check(p.PureFASenderdomain, "get", senderdomain=True)
        check(p.PureFASpace, "get", space=True)
        check(p.PureFASyslogserver, "get", syslogserver=True)

        # array/connection Endpoint
        check(p.PureFAConnection, "list_array_connections")
        check(p.PureFAConnection, "list_array_connections", throttle=True)

        # array/console_lock Endpoint
        check(p.PureFAConsoleLock, "get_console_lock_status")

        # array/phonehome Endpoint
        check(p.PureFAPhoneHomeStatus, "get_phonehome")

        # array/remoteassist Endpoint
        check(p.PureFARemoteAssist, "get_remote_assist_status")

        # volume Endpoint
        check(p.PureFAVolume, "list_volumes", pending=True)
        check(p.PureFAVolumeSpace, "list_volumes", space=True)
        check(p.PureFAVolumeQos, "list_volumes", qos=True, pending=True)
        check(p.PureFASnap, "list_volumes", snap=True, pending=True)
        check(p.PureFASnapSpace, "list_volumes", snap=True,
              pending=True, space=True)

        # host Endpoint
        check(p.PureFAHost, "list_hosts")
        check(p.PureFAHostAll, "list_hosts", all=True)
        check(p.PureFAHostCHAP, "list_hosts", chap=True)
        check(p.PureFAHostConnect, "list_hosts", connect=True)
        check(p.PureFAHostPersonality, "list_hosts", personality=True)

        # hgroup Endpoint
        check(p.PureFAHGroup, "list_hgroups")
        check(p.PureFAHGroupConnect, "list_hgroups", connect=True)

        # pod endpoint
        check(p.PureFAPod, "list_pods")
        check(p.PureFAPod, "list_pods", pending=True, failover_preference=True)

        # pgroup endpoint
        check(p.PureFAPGroup, "list_pgroups", pending=True)
        check(p.PureFAPGroupRetention, "list_pgroups", retention=True)
        check(p.PureFAPGroupSchedule, "list_pgroups", schedule=True)

        # port endpoint
        check(p.PureFAPort, "list_ports")
        check(p.PureFAPortInitiators, "list_ports", initiators=True)

        # alert endpoint
        check(p.PureFAAlertEmails, "list_alert_recipients")

        # message endpoint
        check(p.PureFAMessage, "list_messages")
        check(p.PureFAMessageAudit, "list_messages", audit=True)
        check(p.PureFAMessageLogin, "list_messages", login=True)

        # SMTP endpoint
        check(p.PureFASMTP, "get_smtp")

        # SNMP endpoint
        check(p.PureFASMTP, "list_snmp_managers")

        # Cert endpoint
        check(p.PureFACert, "list_certificates")

        # DNS Endpoint
        check(p.PureFADNS, "get_dns")

        # network endpoint
        check(p.PureFANetwork, "list_network_interfaces")

        # subnet endpoint
        check(p.PureFASubnet, "list_subnets")

        # drive endpoint
        check(p.PureFADrive, "list_drives")

        # hardware endpoint
        check(p.PureFAHardware, "list_hardware")

        # admin endpoint
        check(p.PureFAAdmin, "list_admins")

        # directoryservice endpoint
        check(p.PureFADirectoryService, "get_directory_service")
        check(p.PureFADirectoryServiceCertificate,
              "get_directory_service", certificate=True)
        check(p.PureFADirectoryServiceGroups,
              "get_directory_service", groups=True)

    # wait till all threads finish
    q.join()
    duration = datetime.now() - startTime
    print("Total time: {}".format(duration))
    print("Total calls: {}".format(count))
    print("Calls/sec {}".format(1.0*count/duration.seconds))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="FlashArray IP or DNS name")
    parser.add_argument("-api", "--api_token", help="API Token")
    parser.add_argument("-u", "--username", help="Username for FA")
    parser.add_argument("-p", "--password", help="password for FA")
    parser.add_argument("-t", "--thread_count", default=4, type=int)
    parser.add_argument("-r", "--repeat_count", default=1, type=int)
    parser.add_argument("--peek", action="store_true",
                        help="peek at first record")

    args = parser.parse_args()
    if not (args.api_token and args.username and args.password):
        args.username = "pureuser"
        args.password = "pureuser"

    main(args)

import purestorage_schema as p
import purestorage
import json
import pprint
import threading
import queue
import urllib3
urllib3.disable_warnings()


class Worker(threading.Thread):
    def __init__(self, q, ip, config, printLock):
        threading.Thread.__init__(self)
        self.printLock = printLock
        self.ip = ip
        self.config = config
        self.q = q

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

            message = ("===============================\n")
            message += "Testing Class: {}, many={} : ".format(
                                                        theClass.__name__,
                                                        many)
            message += "{}(".format(item['arrayFunc'])
            delim = ""
            for k, v in item['kwargs'].items():
                message += "{}{}={}".format(delim, k, v)
                delim = ", "
            message += ") : "

            if o.errors:
                message += "Error !! {}\n"
                lastError = ""
                if many:
                    for key in o.errors.keys():
                        currError = str(o.errors[key])
                        if currError == lastError:
                            pass
                        lastError = currError

                        message += currError
                        message += "-------------------\n"
                        message += pprint.pformat(theData[key])
                        message += "-------------------\n"
                    else:
                        message += str(o.errors)
                        message += "-------------------\n"
                        message += pprint.pformat(theData)

            else:
                message += "Success!\n"

            self.safe_print(message)
            self.q.task_done()


def main():
    # Read in ip & api_token / username/password
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
            ip = config['ip']
            del config['ip']
    except Exception as e:
        print(e)
        print("Please put the ip & (api_token || username & password)")
        print("in the file config.json")
        exit(1)

    q = queue.Queue()

    # Start threads to do the work.
    printLock = threading.Lock()
    for _ in range(8):
        t = Worker(q, ip, config, printLock)
        t.setDaemon(True)
        t.start()

    def check(theClass, arrayFunc, **kwargs):
        q.put({"theClass": theClass,
               "arrayFunc": arrayFunc,
               "kwargs": kwargs})

    check(p.PureFA, "get")
    check(p.PureFAControllers, "get", controllers=True)
    check(p.PureFASpace, "get", space=True)

    check(p.PureFAPhoneHome, "get", phonehome=True)
    check(p.PureFARemoteAssist, "get_remote_assist_status")
    check(p.PureFAConnection, "list_array_connections")
    check(p.PureFANTP, "get", ntpserver=True)
    check(p.PureFAProxy, "get", proxy=True)
    check(p.PureFARelayHost, "get", relayhost=True)
    check(p.PureFASCSITimeout, "get", scsi_timeout=True)

    check(p.PureFAVolume, "list_volumes", pending=True)
    check(p.PureFAVolumeSpace, "list_volumes", space=True)
    check(p.PureFAVolumeQos, "list_volumes", qos=True, pending=True)

    check(p.PureFASnap, "list_volumes", snap=True, pending=True)
    check(p.PureFASnapSpace, "list_volumes", snap=True,
          pending=True, space=True)

    check(p.PureFAHostAll, "list_hosts", all=True)
    check(p.PureFAHost, "list_hosts")
    # check(PureFAHostConnection,"conn)

    check(p.PureFAHostGroup, "list_hgroups")
    # check(PureFAHostGroupConnection,"list_hgroup_connections")

    check(p.PureFAAlertEmails, "list_alert_recipients")

    check(p.PureFAMessage, "list_messages")
    check(p.PureFASMTP, "get_smtp")
    check(p.PureFADrive, "list_drives")
    check(p.PureFAHardware, "list_hardware")
    check(p.PureFANetwork, "list_network_interfaces")

    # wait till all threads finish
    q.join()


if __name__ == "__main__":
    main()

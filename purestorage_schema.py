from marshmallow import Schema, fields, pre_load



 

#class PureFlashArrayVolume(Schema):
#    deviceNumber = fields.Int(load_from="deviceNumber")
#    name = fields.Str(load_from="tier_name")
#    pools = fields.List(fields.Str(load_from=""))
#    tierEnabledGB = fields.Int(load_from="enabled_gb")
#    associatedPolicy = fields.List(fields.Str(load_from=""))

class PureFA(Schema):
    #get()
    arrayName = fields.DateTime(load_from="created")
    id = fields.Str()
    revision = fields.Str()
    version = fields.Str()

class PureFAControllers(Schema):
    #get(controllers=True)
    status = fields.Str()
    name = fields.Str()
    version = fields.Str()
    mode = fields.Str()
    model = fields.Str()
    arrayType = fields.Str(load_from="type") 

class PureFASpace(Schema):
    #get(space=True)
    parity = fields.Float()
    capacity = fields.Int()
    provisioned = fields.Int()
    hostname = fields.Str()
    system = fields.Int()
    snapshots = fields.Int()
    volumes = fields.Int()
    data_reduction = fields.Float()
    total = fields.Int()
    shared_space = fields.Int()
    thin_provisioning = fields.Float()
    total_reduction = fields.Float()

class PureFANTP(Schema):
    ntpserver = fields.List(fields.Str())

class PureFAProxy(Schema):
    proxy = fields.Str()

class PureFARelayHost(Schema):
    relayhost = fields.Str()

class PureFASCSITimeout(Schema):
    scsiTimeout = fields.Int(load_from="scsi_timeout")

class PureFAPhoneHome(Schema):
    phonehome = fields.Bool()
    @pre_load()
    def enhance(self, data):
        data['phonehome'] = True if data['phonehome'] == "enabled" else False

class PureFARemoteAssist(Schema):
    status = fields.Bool()
    name = fields.Str()
    port = fields.Str()
    
    @pre_load()
    def enhance(self, data):
        data['status'] = True if data['status'] == "enabled" else False

class PureFAConnection(Schema):
    throttled = fields.Bool()
    id = fields.Str()
    version = fields.Str()
    connected = fields.Bool()
    managementAddress = fields.Str(load_from="management_address",allow_none=True)
    replicationAddress = fields.Str(load_from="replication_address",allow_none=True)
    connectinonType = fields.List(fields.Str(),load_from="type")
    arrayName = fields.Str(load_from="array_name")

class PureFAVolume(Schema):
    created = fields.DateTime(load_from="created")
    serial = fields.Str()
    source = fields.Str(allow_none=True)
    name = fields.Str()
    size = fields.Int()  #size in bytes
    timeRemaining = fields.TimeDelta(load_from="time_remaining",allow_none=True)  #in seconds


class PureFAVolumeSpace(Schema):
    total = fields.Int()
    name = fields.Str()
    system = fields.Int(allow_none=True)
    snapshots = fields.Int()
    volumes = fields.Int()
    data_reduction = fields.Float()
    size = fields.Int()
    shared_space = fields.Int(allow_none=True)
    thin_provisioning = fields.Float()
    total_reduction = fields.Float()
    

class PureFAVolumeQos(Schema):
    bandwidthLimit = fields.Int(load_from="bandwidth_limit",allow_none=True)
    name = fields.Str()
    size = fields.Int()

class PureFASnap(Schema):
    source = fields.Str()
    serial = fields.Str()
    created = fields.DateTime()
    name = fields.Str()
    size = fields.Int()
    timeRemaining = fields.TimeDelta(load_from="time_remaining",allow_none=True)  #in seconds


class PureFASnapSpace(Schema):
    volumes = fields.Int()
    total = fields.Int()
    name = fields.Str()
    snapshots = fields.Int(allow_none=True)
    size = fields.Int()


class PureFAHost(Schema):
    iqn = fields.List(fields.Str(),allow_none=True)
    wwn = fields.List(fields.Str(),allow_none=True)
    name = fields.Str()
    hgroup = fields.Str(allow_none=True)

class PureFAHostAll(Schema):
    hostWwn = fields.Str(load_from="host_wwn",allow_none=True)
    hostIqn = fields.Str(load_from="host_iqn",allow_none=True)
    name = fields.Str()
    lun = fields.Int()
    vol = fields.Str()
    hgroup = fields.Str()
    targetPort = fields.List(fields.Str(),load_from="target_port")

class PureFAHostConnection(Schema):
    vol = fields.Str()
    name = fields.Str()
    lun = fields.Int()
    hgroup = fields.Str()

class PureFAHostGroup(Schema):
    hosts = fields.List(fields.Str())
    name = fields.Str()

class PureFAHostGroupConnection(Schema):
    vol = fields.Str()
    name = fields.Str()
    lun = fields.Int()


class PureFAAlertEmails(Schema):
    enabled = fields.Bool()
    name = fields.Str()

class PureFAMessage(Schema):
    category = fields.Str()
    code = fields.Int()
    actual = fields.Str()
    opened = fields.DateTime()
    component_type = fields.Str()
    event = fields.Str()
    current_severity = fields.Str()
    details = fields.Str()
    expected = fields.Str()
    id = fields.Str()
    component_name = fields.Str()



class PureFASMTP(Schema):
    userName = fields.Str(load_from="user_name")
    password = fields.Str()
    relayhost = fields.Str(load_from="relay_host")
    senderDomain = fields.Str(load_from="sender_domain")

class PureFADrive(Schema):
    status = fields.Str()
    capacity = fields.Int()
    name = fields
    lastEvacCompleted = fields.DateTime(load_from="last_evac_completed")
    details = fields.Str()
    protocol = fields.Str()
    driveType = fields.Str(load_from="type")
    lastFailure = fields.DateTime(load_from="las_failure")

class PureFAHardware(Schema):
    status = fields.Str()
    slot = fields.Int()
    name = fields.Str()
    temperature = fields.Int()
    index = fields.Int()
    identify = fields.Bool()
    voltage = fields.Float()
    model = fields.Str()
    speed = fields.Int()
    serial = fields.Str()
    details = fields.Str()

    @pre_load()
    def enhance(self, data):
        data['identify'] = True if data['identify'] == "on" else False   


class PureFANetwork(Schema):
    subnet = fields.Str()
    name = fields.Str()
    enabled = fields.Bool()
    mtu = fields.Int()
    services = fields.List(fields.Str())
    netmask = fields.Str()
    slaves = fields.List(fields.Str())
    address = fields.Str()
    hwaddr = fields.Str()
    speed = fields.Int()
    gateway = fields.Str()

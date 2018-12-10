from marshmallow import Schema, fields, pre_load


# class PureFlashArrayVolume(Schema):
#    deviceNumber = fields.Int(load_from="deviceNumber")
#    name = fields.Str(load_from="tier_name")
#    pools = fields.List(fields.Str(load_from=""))
#    tierEnabledGB = fields.Int(load_from="enabled_gb")
#    associatedPolicy = fields.List(fields.Str(load_from=""))


class PureFA(Schema):
    created = fields.DateTime()
    name = fields.Str()
    arrayId = fields.Str(load_from="id")
    revision = fields.Str()
    version = fields.Str()


class PureFABanner(Schema):
    banner = fields.Str()


class PureFAConnectionKey(Schema):
    connectionKey = fields.Str(load_from="connection_key")


class PureFAControllers(Schema):
    # get(controllers=True)
    status = fields.Str()
    name = fields.Str()
    version = fields.Str()
    mode = fields.Str()
    model = fields.Str()
    arrayType = fields.Str(load_from="type")


class PureFAIdelTimeout(Schema):
    idleTimeout = fields.Int(load_from="idle_timeout")


class PureFANTP(Schema):
    ntpserver = fields.List(fields.Str())


class PureFAPhoneHome(Schema):
    phonehome = fields.Bool()

    @pre_load()
    def enhance(self, data):
        data['phonehome'] = bool(data['phonehome'] == "enabled")


class PureFAProxy(Schema):
    proxy = fields.Str()


class PureFARelayHost(Schema):
    relayhost = fields.Str()


class PureFASCSITimeout(Schema):
    scsiTimeout = fields.Int(load_from="scsi_timeout")


class PureFASenderdomain(Schema):
    senderdomain = fields.Str()


class PureFASpace(Schema):
    # get(space=True)
    parity = fields.Float()
    capacity = fields.Int()
    provisioned = fields.Int()
    hostname = fields.Str()
    system = fields.Int()
    snapshots = fields.Int()
    volumes = fields.Int()
    dataReduction = fields.Float(load_from="data_reduction")
    total = fields.Int()
    sharedSpace = fields.Int(load_from="shared_space")
    thinProvisioning = fields.Float(load_from="thin_provisioning")
    totalReduction = fields.Float(load_from="total_reduction")


class PureFASyslogserver(Schema):
    syslogserver = fields.List(fields.Str())

######################################################################
# array/connection Endpoint


class PureFAConnection(Schema):
    throttled = fields.Bool()
    id = fields.Str()
    version = fields.Str()
    connected = fields.Bool()
    managementAddress = fields.Str(
        load_from="management_address", allow_none=True)
    replicationAddress = fields.List(fields.Str(
        load_from="replication_address", allow_none=True))
    connectinonType = fields.List(fields.Str(), load_from="type")
    arrayName = fields.Str(load_from="array_name")


class PureFAWindow(Schema):
    start = fields.TimeDelta()
    end = fields.TimeDelta()


class PureFAConnectionThrottle(Schema):
    defaultLimit = fields.Str(load_from="default_limit", allow_none=True)
    window = fields.Nested(PureFAWindow, many=True, allow_none=True)
    windowLimit = fields.Str(load_from="windowLimit", allow_none=True)
    arrayName = fields.Str(load_from="array_name")


######################################################################
# array/console_lock Endpoint


class PureFAConsoleLock(Schema):
    consoleLock = fields.Bool(load_from="console_lock")

    @pre_load()
    def enhance(self, data):
        data['console_lock'] = bool(data['console_lock'] == "enabled")

######################################################################
# array/phonehome Endpoint


class PureFAPhoneHomeStatus(Schema):
    status = fields.Str()
    action = fields.Str()


######################################################################
# array/remoteassist Endpoint


class PureFARemoteAssist(Schema):
    status = fields.Bool()
    name = fields.Str()
    port = fields.Str()

    @pre_load()
    def enhance(self, data):
        data['status'] = bool(data['status'] == "enabled")


######################################################################
# volume Endpoint


class PureFAVolume(Schema):
    created = fields.DateTime(load_from="created")
    serial = fields.Str()
    source = fields.Str(allow_none=True)
    name = fields.Str()
    size = fields.Int()  # size in bytes
    timeRemaining = fields.TimeDelta(
        load_from="time_remaining", allow_none=True)  # in seconds


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
    bandwidthLimit = fields.Int(load_from="bandwidth_limit", allow_none=True)
    name = fields.Str()
    size = fields.Int()


class PureFASnap(Schema):
    source = fields.Str()
    serial = fields.Str()
    created = fields.DateTime()
    name = fields.Str()
    size = fields.Int()
    timeRemaining = fields.TimeDelta(
        load_from="time_remaining", allow_none=True)  # in seconds


class PureFASnapSpace(Schema):
    volumes = fields.Int()
    total = fields.Int()
    name = fields.Str()
    snapshots = fields.Int(allow_none=True)
    size = fields.Int()


######################################################################
# host Endpoint


class PureFAHost(Schema):
    iqn = fields.List(fields.Str(), allow_none=True)
    wwn = fields.List(fields.Str(), allow_none=True)
    name = fields.Str()
    hgroup = fields.Str(allow_none=True)


class PureFAHostAll(Schema):
    hostWwn = fields.Str(load_from="host_wwn", allow_none=True)
    hostIqn = fields.Str(load_from="host_iqn", allow_none=True)
    hostName = fields.Str()
    hostLun = fields.Int()
    vol = fields.Str()
    hgroup = fields.Str(allow_none=True)
    targetPort = fields.List(fields.Str(), load_from="target_port")


class PureFAHostCHAP(Schema):
    targetPassword = fields.Str(load_from="target_password", allow_none=True)
    host_password = fields.Str(load_from="host_password", allow_none=True)
    target_user = fields.Str(load_from="target_user", allow_none=True)
    name = fields.Str()
    host_user = fields.Str(load_from="hostUser", allow_none=True)


class PureFAHostConnect(Schema):
    vol = fields.Str()
    name = fields.Str()
    lun = fields.Int()
    hgroup = fields.Str(allow_none=True)


class PureFAHostPersonality(Schema):
    name = fields.Str()
    personality = fields.Str(allow_none=True)


######################################################################
# hgroup Endpoint


class PureFAHGroup(Schema):
    hosts = fields.List(fields.Str())
    name = fields.Str()


class PureFAHGroupConnect(Schema):
    vol = fields.Str()
    name = fields.Str()
    lun = fields.Int()


######################################################################
# pod Endpoint


class PureFAPodArray(Schema):
    name = fields.Str()
    status = fields.Str()
    arrayId = fields.Str(load_from="array_id")
    mediatorStatus = fields.Str(load_from="mediator_status")


class PureFAPod(Schema):
    name = fields.Str()
    source = fields.Str(allow_none=True)
    arrays = fields.Nested(PureFAPodArray, many=True)
    failoverPreference = fields.List(fields.Str(),
                                     load_from="failover_preference",
                                     allow_none=True)
    timeRemaining = fields.TimeDelta(load_from="time_remaining",
                                     allow_none=True)


#####################################################################
# pgroup Endpoint


class PureFAPGroupTarget(Schema):
    name = fields.Str()
    allowed = fields.Bool()


class PureFAPGroup(Schema):
    name = fields.Str()
    hgroups = fields.List(fields.Str(), allow_none=True)
    hosts = fields.List(fields.Str(), allow_none=True)
    volumes = fields.List(fields.Str(), allow_none=True)
    source = fields.Str()
    targets = fields.Nested(PureFAPGroupTarget, allow_none=True, many=True)
    timeRemaining = fields.TimeDelta(load_from="time_remaining",
                                     allow_none=True)


class PureFAPGroupRetention(Schema):
    name = fields.Str()
    targetPerDay = fields.Int(load_from="target_per_day")
    days = fields.Int()
    perDay = fields.Int(load_from="per_day")
    targetAllFor = fields.Int(load_from="target_all_for")
    targetDays = fields.Int(load_from="target_days")
    allFor = fields.Int(load_from="all_for")


class PureFAPGroupSchedule(Schema):
    name = fields.Str()
    snapFrequency = fields.TimeDelta(load_from="snap_frequency")
    replicateFrequency = fields.TimeDelta(load_from="replicate_frequency")
    replicateEnabled = fields.Bool(load_from="replicate_enabled")
    snapEnabled = fields.Bool(load_from="snap_enabled")
    snapAt = fields.TimeDelta(load_from="snap_at", allow_none=True)
    replicateAt = fields.TimeDelta(load_from="replicate_at", allow_none=True)
    replicateBlackout = fields.Nested(PureFAWindow, allow_none=True,
                                      load_from="replicate_blackout",
                                      many=True)


#####################################################################
# port Endpoint

class PureFAPort(Schema):
    name = fields.Str()
    iqn = fields.Str(allow_none=True)
    wwn = fields.Str(allow_none=True)
    portal = fields.Str(allow_none=True)
    failover = fields.Str(allow_none=True)


class PureFAPortInitiators(Schema):
    target = fields.Str(allow_none=True)
    targetPortal = fields.Str(allow_none=True, load_from="target_portal")
    targetIqn = fields.Str(allow_none=True, load_from="target_iqn")
    targetWwn = fields.Str(allow_none=True, load_from="target_wwn")
    iqn = fields.Str(allow_none=True)
    wwn = fields.Str(allow_none=True)
    portal = fields.Str(allow_none=True)
    failover = fields.Str(allow_none=True)


#####################################################################
# alert Endpoint


class PureFAAlertEmails(Schema):
    enabled = fields.Bool()
    name = fields.Str()


#####################################################################
# message Endpoint


class PureFAMessage(Schema):
    category = fields.Str()
    code = fields.Int()
    actual = fields.Str(allow_none=True)
    opened = fields.DateTime()
    component_type = fields.Str()
    event = fields.Str()
    current_severity = fields.Str()
    details = fields.Str()
    expected = fields.Str(allow_none=True)
    id = fields.Int()
    component_name = fields.Str(allow_none=True)


class PureFAMessageAudit(Schema):
    id = fields.Int()
    opened = fields.DateTime()
    user = fields.Str()
    component_type = fields.Str()
    event = fields.Str()
    component_name = fields.Str(allow_none=True)
    details = fields.Str()


class PureFAMessageLogin(Schema):
    id = fields.Int()
    component_type = fields.Str()
    user = fields.Str(allow_none=True)
    event = fields.Str()
    count = fields.Int(allow_none=True)
    opened = fields.DateTime(allow_none=True)
    closed = fields.DateTime(allow_none=True)
    expected = fields.Str(allow_none=True)
    location = fields.Str(allow_none=True)


#####################################################################
# smtp Endpoint


class PureFASMTP(Schema):
    userName = fields.Str(load_from="user_name", allow_none=True)
    password = fields.Str(allow_none=True)
    relayhost = fields.Str(load_from="relay_host", allow_none=True)
    senderDomain = fields.Str(load_from="sender_domain", allow_none=True)


#####################################################################
# snmp Endpoint


class PureFASNMP(Schema):
    name = fields.Str()
    version = fields.Str(allow_none=True)
    notification = fields.Str(allow_none=True)
    community = fields.Str(allow_none=True)
    privacyProtocol = fields.Str(allow_none=True, load_from="privacy_protocol")
    authProtocol = fields.Str(allow_none=True, load_from="auth_protocol")
    host = fields.Str(allow_none=True)
    user = fields.Str(allow_none=True)
    privacyPassphrase = fields.Str(allow_none=True,
                                   load_from="privacy_passphrase")
    authPassphrase = fields.Str(allow_none=True, load_from="auth_passphrase")


#####################################################################
# cert Endpoint


class PureFACert(Schema):
    status = fields.Str(allow_none=True)
    issuedTo = fields.Str(allow_none=True, load_from="issued_to")
    validFrom = fields.DateTime(load_from="valid_from")
    name = fields.Str(allow_none=True)
    locality = fields.Str(allow_none=True)
    country = fields.Str(allow_none=True)
    issuedBy = fields.Str(allow_none=True, load_from="issued_by")
    validTo = fields.DateTime(load_from="valid_to")
    state = fields.Str(allow_none=True)
    keySize = fields.Int(allow_none=True, load_from="key_size")
    organizationalUnit = fields.Str(allow_none=True,
                                    load_from="organizational_unit")
    organization = fields.Str(allow_none=True)
    email = fields.Str(allow_none=True)


#####################################################################
# dns Endpoint


class PureFADNS(Schema):
    nameservers = fields.List(fields.Str(), allow_none=True)
    domain = fields.Str(allow_none=True)


#####################################################################
# network Endpoint


class PureFANetwork(Schema):
    subnet = fields.Str(allow_none=True)
    name = fields.Str()
    enabled = fields.Bool()
    mtu = fields.Int()
    services = fields.List(fields.Str())
    netmask = fields.Str(allow_none=True)
    slaves = fields.List(fields.Str())
    address = fields.Str(allow_none=True)
    hwaddr = fields.Str()
    speed = fields.Int()
    gateway = fields.Str(allow_none=True)


####################################################################
# subnet Endpoint


class PureFASubnet(Schema):
    name = fields.Str()
    interfaces = fields.List(fields.Str(), allow_none=True)
    prefix = fields.Str(allow_none=True)
    enabled = fields.Bool()
    vlan = fields.Int(allow_none=True)
    mtu = fields.Int()
    gateway = fields.Str(allow_none=True)


#####################################################################
# drive Endpoint


class PureFADrive(Schema):
    status = fields.Str()
    capacity = fields.Int()
    name = fields
    lastEvacCompleted = fields.DateTime(load_from="last_evac_completed")
    details = fields.Str(allow_none=True)
    protocol = fields.Str(allow_none=True)
    driveType = fields.Str(load_from="type")
    lastFailure = fields.DateTime(load_from="las_failure")


#####################################################################
# hardware Endpoint


class PureFAHardware(Schema):
    status = fields.Str()
    slot = fields.Int(allow_none=True)
    name = fields.Str()
    temperature = fields.Int(allow_none=True)
    index = fields.Int()
    identify = fields.Bool()
    voltage = fields.Float(allow_none=True)
    model = fields.Str(allow_none=True)
    speed = fields.Int(allow_none=True)
    serial = fields.Str(allow_none=True)
    details = fields.Str(allow_none=True)

    @pre_load()
    def enhance(self, data):
        data['identify'] = bool(data['identify'] == "on")


#####################################################################
# admin Endpoint


class PureFAAdmin(Schema):
    name = fields.Str()
    typeName = fields.Str(load_from="type")
    created = fields.DateTime()
    expires = fields.DateTime(allow_none=True)
    apiToken = fields.Str(load_from="api_token")
    publickey = fields.Str(allow_none=True)


#####################################################################
# directoryservice Endpoint


class PureFADirectoryService(Schema):
    bindUser = fields.Str(allow_none=True, load_from="bind_user")
    enabled = fields.Bool()
    uri = fields.List(fields.Str(), allow_none=True)
    bindPassword = fields.Str(allow_none=True, load_from="bind_password")
    baseDn = fields.Str(allow_none=True, load_from="base_dn")
    checkPeer = fields.Bool(load_from="check_peer")


class PureFADirectoryServiceCertificate(Schema):
    certificate = fields.Str(allow_none=True)


class PureFADirectoryServiceGroups(Schema):
    readonlyGroup = fields.Str(allow_none=True, load_from="readonly_group")
    groupBase = fields.Str(allow_none=True, load_from="group_base")
    arrayAdminGroup = fields.Str(allow_none=True,
                                 load_from="array_admin_group")
    storageAdminGroup = fields.Str(allow_none=True,
                                   load_from="storage_admin_group")

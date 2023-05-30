from enum import Enum


class NrCellsHeader(Enum):
    NRCELLDUID = 1
    NODEID = 2
    LOCCODE = 3
    GNBDUFUNCTIONID = 4
    ADMINISTRATIVESTATE = 5
    AVAILABILITYSTATUS = 6
    CELLBARRED = 7
    CELLLOCALID = 8
    CELLRESERVEDFOROPERATOR = 9
    CELLSTATE = 10
    NCGI = 11
    NCI = 12
    NRPCI = 13
    NRSECTORCARRIER = 14
    NRTAC = 15
    OPERATIONALSTATE = 16
    QQUALMIN = 17
    QRXLEVMIN = 18
    RACHROOTSEQUENCE = 19
    SSBDURATION = 20
    SSBFREQUENCY = 21
    SSBFREQUENCYAUTOSELECTED = 22
    SSBOFFSET = 23
    SSBPERIODICITY = 24
    SSBSUBCARRIERSPACING = 25
    SUBCARRIERSPACING = 26
    TDDLTECOEXISTENCE = 27
    TDDSPECIALSLOTPATTERN = 28
    TDDULDLPATTERN = 29
    ARFCNDL = 30
    ARFCNUL = 31
    BSCHANNELBWDL = 32
    BSCHANNELBWUL = 33
    AZIMUTH = 34
    ERPSECTORSTATUSDESC = 35
    FREQ = 36
    BANDLIST = 37
    PLMNIDLIST = 38
    ESSSCPAIRID = 39
    NRCELLDUUSERLABEL = 40
    ERPSECTORTECH = 41
    COLUMNSTART = 1
    COLUMNEND = 42
    ROWSTART = 2


class LTECellsHeader(Enum):
    CELL = 0
    ERBS = 1
    LOCCODE = 2
    SECTORCARRIERREF = 3
    TAC = 4
    CELLID = 5
    ECI = 6
    PCI = 7
    EARFCNDL = 8
    AZIMUTH = 9
    BW = 10
    ERPSECTORSTATUSDESC = 11
    HBW = 12
    ANTENNAHEIGHT = 13
    VBW = 14
    ANTENNATYPE = 15
    ELECTRICALANTENNATILT = 16
    MAXTXPOWER = 17
    TRANSMITRXTX = 18
    CONFIGUREDPOWER = 19
    ISD = 20
    TOTALSUM = 21
    LTETECHNOLOGY = 22
    CATM1 = 23
    RRU = 24
    PRODUCTNAME = 25
    PLMNRESERVED = 26
    PRIMARYUPPERLAYERIND = 27
    FREQBAND = 28
    ESSSCPAIRID = 29
    CELLRANGE = 30
    FREQ = 31
    ENBID = 32
    ENBID_CELLID = 33
    LATITUDE = 34
    LONGITUDE = 35
    ANT_BEAM = 36
    ANT_SIZE = 37
    COLUMN_START = 1
    COLUMN_END = 38
    ROW_START = 2


class UMTSCellsHeader(Enum):
    UTRANCELL = 0
    NODEB = 1
    LOCCODE = 2
    CELLID = 3
    SC = 4
    LAC = 5
    RAC = 6
    UARFCNUL = 7
    UARFCNDL = 8
    AZIMUTH = 9
    HBW = 10
    ERPSECTORSTATUSDESC = 11
    FREQUENCY = 12
    COLUMN_START = 1
    COLUMN_END = 13
    ROW_START = 2


class GSMCellsHeader(Enum):
    CELL = 0
    LOCCODE = 1
    CI = 2
    LAC = 3
    NCC = 4
    BCC = 5
    BCCHNO = 6
    AZIMUTH = 7
    FREQUENCY = 8
    COLUMN_START = 1
    COLUMN_END = 9
    ROW_START = 2


class RadioNodesHeader(Enum):
    NODEID = 1
    ENBID = 2
    LOCCODE = 3
    SUBNETWORK = 4
    SYSTEM = 5
    SWVERSIONID = 6
    SWRELEASE = 7
    VENDOR = 8
    MOCN = 9
    GNBID = 10
    HWTYPE = 11
    COLUMN_START = 1
    COLUMN_END = 12
    ROW_START = 2


class UMTSNodesHeader(Enum):
    NODEB = 0
    LOCCODE = 1
    RNC = 2
    NODEBFUNCTIONIUBLINK = 3
    VENDOR = 4
    COLUMN_START = 1
    COLUMN_END = 5
    ROW_START = 2


class GSMNodesHeader(Enum):
    SITE = 0
    MSC = 1
    BSC = 2
    LOCATIONCODE = 3
    COLUMN_START = 1
    COLUMN_END = 4
    ROW_START = 2


class SitesHeader(Enum):
    LOCCODE = 1
    SITENAME = 2
    SITEISD = 3
    PARENT = 4
    CSD = 5
    CMA = 6
    ER = 7
    PRV = 8
    LATITUDE = 9
    LONGITUDE = 10
    TOWER_TYPE = 11
    RNC = 12
    BSC = 13
    GSM = 14
    UMTS = 15
    LTE = 16
    NR = 17
    NBIOT = 18
    CSDUID = 19
    MOCNNODES = 20
    AZIMUTHCOUNT = 21
    AVGANTENNAHEIGHT = 22
    LTESHIFTED = 23
    COLUMN_START = 1
    COLUMN_END = 24
    ROW_START = 2


class OutputHeader(Enum):
    NRCELLDUID = 0
    NODEID = 1
    LOCCODE = 2
    GNB_DUFUNCTIONID = 3
    ADMINISTRATIVESTATE = 4
    AVAILABILITYSTATUS = 5
    CELLBARRED = 6
    CELLLOCALID = 7
    CELLRESERVEDFOROPERATOR = 8
    CELLSTATE = 9
    NCGI = 10
    NCI = 11
    NRPCI = 12
    NRSectorCarrier = 13
    NRTAC = 14
    OPERATIONALSTATE = 15
    QQUALMIN = 16
    QRXLEVMIN = 17
    RACHROOTSEQUENCE = 18
    SSBDURATION = 19
    SSBFREQUENCY = 20
    SSBFREQUENCYAUTOSELECTED = 21
    SSBOFFSET = 22
    SSBPERIODICITY = 23
    SSBSUBCARRIERSPACING = 24
    SUBCARRIERSPACING = 25
    TDDLTECOEXISTENCE = 26
    TDDSPECIALSLOTPATTERN = 27
    TDDULDLPATTERN = 28
    ARFCNDL = 29
    ARFCNUL = 30
    BSCHANNELBWDL = 31
    BSCHANNELBWUL = 32
    AZIMUTH = 33
    ERPSECTORSTATUSDESC = 34
    FREQ = 35
    BANDLIST = 36
    PLMNIDLIST = 37
    ESSSCPAIRID = 38
    NRCELLDUUSERLABEL = 39
    ERPSECTORTECH = 40
    ENBID = 41
    SUBNETWORK = 42
    SYSTEM = 43
    SWVERSIONID = 44
    SWRELEASE = 45
    VENDOR = 46
    MOCN = 47
    GNBD = 48
    HWTYPE = 49
    ERPSITENAME = 50
    ERPSECTORELECTDOWNTILT = 51
    ERPSECTORMECHANICALDOWNTILT = 52
    ERPSECTORANTENNAOMNIDIRECTIONAL = 53
    ANTENNABEAMWIDTH = 54
    ANTENNASIZE = 55
    COLUMN_START = 1
    COLUMN_END = 56
    ROW_START = 2


class GcellHelper:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_header_nrcells():
        return [
            "nRCellDUId",
            "nodeId",
            "locCode",
            "gNbDuFunctionId",
            "administrativeState",
            "availabilityStatus",
            "cellBarred",
            "cellLocalId",
            "cellReservedForOperator",
            "cellState",
            "nCGI",
            "nCI",
            "nRPCI",
            "nRSectorCarrier",
            "nRTAC",
            "operationalState",
            "qQualMin",
            "qRxLevMin",
            "rachRootSequence",
            "ssbDuration",
            "ssbFrequency",
            "ssbFrequencyAutoSelected",
            "ssbOffset",
            "ssbPeriodicity",
            "ssbSubCarrierSpacing",
            "subCarrierSpacing",
            "tddLteCoexistence",
            "tddSpecialSlotPattern",
            "tddUlDlPattern",
            "arfcnDL",
            "arfcnUL",
            "bSChannelBwDL",
            "bSChannelBwUL",
            "azimuth",
            "erpSectorStatusDesc",
            "freq",
            "bandList",
            "pLMNIdList",
            "essScPairId",
            "NRCellDU-userLabel",
            "erpSectorTech",
            "eNBId",
            "Subnetwork",
            "system",
            "swVersionId",
            "swRelease",
            "Vendor",
            "mocn",
            "gNBId",
            "hwType",
            "ERP Site Name",
            "ERP Sector Elect Downtilt",
            "ERP Sector Mechanical Downtilt",
            "ERP Sector Antenna Omnidirectional",
            "Antenna Beamwidth",
            "Antenna Size",
        ]

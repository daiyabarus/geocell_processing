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


class GcellHelper:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_header_title():
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
        ]

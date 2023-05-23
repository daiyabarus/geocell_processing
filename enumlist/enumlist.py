class referenceumtscells:
    def __init__(self) -> None:
        self.nodeB = 0
        self.locCode = 1
        self.cellId = 2
        self.sc = 3
        self.lac = 4
        self.rac = 5
        self.uarfcnUl = 6
        self.uarfcnDl = 7
        self.azimuth = 8
        self.HBW = 9
        self.erpSectorStatusDesc = 10
        self.frequency = 11
        self.COL_START = 1
        self.COL_END = 13
        self.ROW_START = 2

    def __str__(self) -> str:
        return f"{self.locCode} {self.cellId}"


class referencesites:
    def __init__(self) -> None:
        self.sites_locCode = 0
        self.siteName = 1
        self.siteIsd = 2
        self.parent = 3
        self.csd = 4
        self.cma = 5
        self.er = 6
        self.prv = 7
        self.latitude = 8
        self.longitude = 9
        self.towerType = 10
        self.rnc = 11
        self.bsc = 12
        self.GSM = 13
        self.UMTS = 14
        self.LTE = 15
        self.NR = 16
        self.NBIOT = 17
        self.csdUid = 18
        self.mocnNodes = 19
        self.azimuthCount = 20
        self.avgAntennaHeight = 21
        self.lte_shifted = 22
        self.COL_START = 1
        self.COL_END = 23
        self.ROW_START = 2


class referenceSheetNaming:
    def __init__(self) -> None:
        self.nrcells = "nrCells"
        self.ltecells = "lteCells"
        self.umtscells = "umtsCells"
        self.gsmcells = "gsmCells"
        self.radionodes = "radioNodes"
        self.umtsnodes = "umtsNodes"
        self.gsmnodes = "gsmNodes"
        self.sites = "sites"


class resultgcellumts:
    def __init__(self) -> None:
        self.result_nodeB = 0
        self.result_locCode = 1
        self.result_cellId = 2
        self.result_sc = 3
        self.result_lac = 4
        self.result_rac = 5
        self.result_uarfcnUl = 6
        self.result_uarfcnDl = 7
        self.result_azimuth = 8
        self.result_HBW = 9
        self.result_erpSectorStatusDesc = 10
        self.result_frequency = 11
        self.result_siteName = 12
        self.result_csd = 13
        self.result_cma = 14
        self.result_er = 15
        self.result_prv = 16
        self.result_latitude = 17
        self.result_longitude = 18
        self.result_towerType = 19
        self.result_rnc = 20
        self.result_bsc = 21
        self.result_isd = 22
        self.result_ant_bw = 23
        self.result_ant_size = 24

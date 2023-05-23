class sheetSites:
    def __init__(
        self,
        sites_loccode: str,
        site_name: str,
        site_isd: str,
        parent: str,
        bw: str,
        tx_type: str,
        rate_mbps: str,
        csd: str,
        cma: str,
        er: str,
        prv: str,
        latitude: str,
        longitude: str,
        tower_type: str,
        rnc: str,
        bsc: str,
        gsm: str,
        umts: str,
        lte: str,
        nr: str,
        nbiot: str,
        csd_uid: str,
        mocn_nodes: str,
        azimuth_count: str,
        avg_antenna_height: str,
        lte_shifted: str,
    ):
        self.sites_locCode = sites_loccode
        self.site_name = site_name
        self.site_isd = site_isd
        self.parent = parent
        self.bw = bw
        self.tx_type = tx_type
        self.rate_mbps = rate_mbps
        self.csd = csd
        self.cma = cma
        self.er = er
        self.prv = prv
        self.latitude = latitude
        self.longitude = longitude
        self.tower_type = tower_type
        self.rnc = rnc
        self.bsc = bsc
        self.gsm = gsm
        self.umts = umts
        self.lte = lte
        self.nr = nr
        self.nbiot = nbiot
        self.csd_uid = csd_uid
        self.mocn_nodes = mocn_nodes
        self.azimuth_count = azimuth_count
        self.avg_antenna_height = avg_antenna_height
        self.lte_shifted = lte_shifted

    def __str__(self) -> str:
        return f"{self.sites_loccode}"

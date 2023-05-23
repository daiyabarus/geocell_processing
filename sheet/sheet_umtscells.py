class sheet_UmtsCells:
    def __init__(
        self,
        utran_cell: str,
        node_b: str,
        loc_code: str,
        cell_id: str,
        sc: str,
        lac: str,
        rac: str,
        uarfcn_ul: str,
        uarfcn_dl: str,
        azimuth: str,
        hbw: str,
        erp_sector_status_desc: str,
        frequency: str,
    ):
        self.utran_cell = utran_cell
        self.node_b = node_b
        self.loc_code = loc_code
        self.cell_id = cell_id
        self.sc = sc
        self.lac = lac
        self.rac = rac
        self.uarfcn_ul = uarfcn_ul
        self.uarfcn_dl = uarfcn_dl
        self.azimuth = azimuth
        self.hbw = hbw
        self.erp_sector_status_desc = erp_sector_status_desc
        self.frequency = frequency

    def __str__(self) -> str:
        return f"{self.loc_code}_{self.utran_cell}"

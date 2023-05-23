from func.func_nearest import calculate_nearest_distance
from sheet.sheet_sites import Sites
from sheet.sheet_umtscells import UmtsCells


def merge_data(UmtsCellss_list, sites_list):
    merged_data = []

    for umtscells in UmtsCellss_list:
        loc_code = UmtsCells.loc_code

        for sites in sites_list:
            if Sites.loc_code == loc_code:
                # Perhitungan kolom-kolom tambahan
                nearest_distance = calculate_nearest_distance(
                    (Sites.latitude, Sites.longitude)
                )
                nearest_lc = find_nearest_lc(Sites)

                merged_data.append(
                    (
                        UmtsCells.utran_cell,
                        UmtsCells.node_b,
                        UmtsCells.loc_code,
                        UmtsCells.cell_id,
                        UmtsCells.sc,
                        UmtsCells.lac,
                        UmtsCells.rac,
                        UmtsCells.uarfcn_ul,
                        UmtsCells.uarfcn_dl,
                        UmtsCells.azimuth,
                        UmtsCells.hbw,
                        UmtsCells.erp_sector_status_desc,
                        UmtsCells.frequency,
                        sites.site_name,
                        sites.site_isd,
                        sites.csd,
                        sites.cma,
                        sites.er,
                        sites.prv,
                        sites.latitude,
                        sites.longitude,
                        sites.tower_type,
                        sites.rnc,
                        sites.bsc,
                        nearest_distance,
                        nearest_lc,
                    )
                )
                break

    return merged_data

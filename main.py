import csv
import os
from datetime import datetime

from _enums_ import GcellHelper
from _func_ import collectDataAll


class __create_geocell_data:
    def __init__(self, newreference: str) -> None:
        self.newreference = newreference
        self.nrcells_list = []

    def go_init(self):
        newreference_collector = collectDataAll(newReference_filepath=self.newreference)

        for locCode, nrcells in newreference_collector.dtref_nrcells.items():
            # Unpack values from nrcells
            (
                nRCellDUId,
                nodeId,
                locCode,
                gNbDuFunctionId,
                administrativeState,
                availabilityStatus,
                cellBarred,
                cellLocalId,
                cellReservedForOperator,
                cellState,
                nCGI,
                nCGI,
                nCI,
                nRPCI,
                nRSectorCarrier,
                nRTAC,
                operationalState,
                qQualMin,
                qRxLevMin,
                rachRootSequence,
                ssbDuration,
                ssbFrequency,
                ssbFrequencyAutoSelected,
                ssbOffset,
                ssbPeriodicity,
                ssbSubCarrierSpacing,
                subCarrierSpacing,
                tddLteCoexistence,
                tddSpecialSlotPattern,
                tddUlDlPattern,
                arfcnDL,
                arfcnUL,
                bSChannelBwDL,
                bSChannelBwUL,
                azimuth,
                erpSectorStatusDesc,
                freq,
                bandList,
                pLMNIdList,
                essScPairId,
                NRCellDU_userLabel,
                erpSectorTech,
            ) = nrcells

            # Unpack values from radionodes
            # (
            enbid: str = newreference_collector.__collect_ref_radionodes.get(
                locCode, "NONE"
            )
            subnetwork: str = newreference_collector.__collect_ref_radionodes.get(
                locCode, "NONE"
            )
            system: str = newreference_collector.__collect_ref_radionodes.get(
                locCode, "NONE"
            )
            swversionid: str = newreference_collector.__collect_ref_radionodes.get(
                locCode, "NONE"
            )
            swrelease: str = newreference_collector.__collect_ref_radionodes.get(
                locCode, "NONE"
            )
            vendor: str = newreference_collector.__collect_ref_radionodes.get(
                locCode, "NONE"
            )
            mocn: str = newreference_collector.__collect_ref_radionodes.get(
                locCode, "NONE"
            )
            gnbid: str = newreference_collector.__collect_ref_radionodes.get(
                locCode, "NONE"
            )
            hwtype: str = newreference_collector.__collect_ref_radionodes.get(
                locCode, "NONE"
            )
            # ) = radionodes

            # Unpack values from sites
            # (
            erp_site_name: str = newreference_collector.__collect_ref_sites.get(
                locCode, "NONE"
            )
            erp_sector_elect_downtilt: str = (
                newreference_collector.__collect_ref_sites.get(locCode, "NONE")
            )
            erp_sector_mechanical_downtilt: str = (
                newreference_collector.__collect_ref_sites.get(locCode, "NONE")
            )
            erp_sector_antenna_omnidirectional: str = (
                newreference_collector.__collect_ref_sites.get(locCode, "NONE")
            )
            # ) = sites

            antenna_beamwidth = "TBD"
            antenna_size = "TBD"

            self.nrcells_list.append(
                [
                    nRCellDUId,
                    nodeId,
                    locCode,
                    gNbDuFunctionId,
                    administrativeState,
                    availabilityStatus,
                    cellBarred,
                    cellLocalId,
                    cellReservedForOperator,
                    cellState,
                    nCGI,
                    nCGI,
                    nCI,
                    nRPCI,
                    nRSectorCarrier,
                    nRTAC,
                    operationalState,
                    qQualMin,
                    qRxLevMin,
                    rachRootSequence,
                    ssbDuration,
                    ssbFrequency,
                    ssbFrequencyAutoSelected,
                    ssbOffset,
                    ssbPeriodicity,
                    ssbSubCarrierSpacing,
                    subCarrierSpacing,
                    tddLteCoexistence,
                    tddSpecialSlotPattern,
                    tddUlDlPattern,
                    arfcnDL,
                    arfcnUL,
                    bSChannelBwDL,
                    bSChannelBwUL,
                    azimuth,
                    erpSectorStatusDesc,
                    freq,
                    bandList,
                    pLMNIdList,
                    essScPairId,
                    NRCellDU_userLabel,
                    erpSectorTech,
                    enbid,
                    subnetwork,
                    system,
                    swversionid,
                    swrelease,
                    vendor,
                    mocn,
                    gnbid,
                    hwtype,
                    erp_site_name,
                    erp_sector_elect_downtilt,
                    erp_sector_mechanical_downtilt,
                    erp_sector_antenna_omnidirectional,
                    antenna_beamwidth,
                    antenna_size,
                ]
            )

        # Create new CSV
        current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
        final_folder = os.path.dirname(self.newreference)
        newref_nrcell_file = f"GEO_NRCELL_{current_datetime}.csv"
        newref_filepath = os.path.join(final_folder, newref_nrcell_file)

        output_header = GcellHelper.get_header_nrcells()

        with open(newref_filepath, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(output_header)
            writer.writerows(self.nrcells_list)

        return True, final_folder, newref_filepath


if __name__ == "__main__":
    nrfile = r"D:\Programming\geocell_processing\newReference.xlsx"

    nrprocess = __create_geocell_data(newreference=nrfile)
    is_ok, final_folder, newref_filepath = nrprocess.go_init()

    if is_ok:
        print("Output saved successfully.")
        print("Folder:", final_folder)
        print("File path:", newref_filepath)
    else:
        print("Error occurred during output saving.")

import os

from enums import GcellHelper
from functions import collectDataAll


class __create_geocell_data:
    def __init__(self, newreference: str) -> None:
        self.newreference = newreference
        self.nrcells_list = []

    def go_init(self):
        newreference_collector = collectDataAll(newReference_filepath=self.newreference)

        for locCode, nrcells in newreference_collector.dtref_nrcells.items():
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
                ]
            )

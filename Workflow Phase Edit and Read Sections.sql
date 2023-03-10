DECLARE @PhaseName VARCHAR(200)
SET @PhaseName='PhaseDesignName'

SELECT PE.ETQ$RECORD_ORDER, PS.DISPLAY_NAME AS PhaseName, SS.DISPLAY_NAME AS EditableSection
FROM ENGINE.WF_SETTINGS WF
JOIN ENGINE.WF_PHASE_INFO WFP ON WF.WORKFLOW_ID=WFP.WORKFLOW_ID
JOIN ENGINE.PHASE_SETTINGS PS ON WFP.PHASE_ID=PS.PHASE_ID
JOIN ENGINE.PHASE_EDIT_SECTIONS PE ON PS.PHASE_ID=PE.PHASE_ID
JOIN ENGINE.SECTION_SETTINGS SS ON PE.SECTION_ID=SS.SECTION_ID
WHERE PS.PHASE_NAME=@PhaseName
ORDER BY PE.ETQ$RECORD_ORDER

SELECT PR.ETQ$RECORD_ORDER, PS.DISPLAY_NAME AS PhaseName, SS.DISPLAY_NAME AS ReadOnlySection
FROM ENGINE.WF_SETTINGS WF
JOIN ENGINE.WF_PHASE_INFO WFP ON WF.WORKFLOW_ID=WFP.WORKFLOW_ID
JOIN ENGINE.PHASE_SETTINGS PS ON WFP.PHASE_ID=PS.PHASE_ID
JOIN ENGINE.PHASE_READ_SECTIONS PR ON PS.PHASE_ID=PR.PHASE_ID
JOIN ENGINE.SECTION_SETTINGS SS ON PR.SECTION_ID=SS.SECTION_ID
WHERE PS.PHASE_NAME=@PhaseName
ORDER BY PR.ETQ$RECORD_ORDER

SELECT	DISTINCT A.DISPLAY_NAME AS Application,
		F.DISPLAY_NAME AS FormDisplay,
		F.FORM_NAME AS FormName,
		FS.DISPLAY_NAME AS FieldDisplay,
		FS.FIELD_NAME AS FieldName
		--SO.DESCRIPTION AS OISynch
FROM ENGINE.FIELD_SETTINGS FS
JOIN ENGINE.FORM_FIELDS FF ON FS.FIELD_ID=FF.FIELD_ID
JOIN ENGINE.FORM_SETTINGS F ON FF.FORM_ID=F.FORM_ID
JOIN ENGINE.APPLICATION_FORMS AF ON F.FORM_ID=AF.FORM_ID
JOIN ENGINE.APPLICATION_SETTINGS A ON A.APPLICATION_ID=AF.APPLICATION_ID
JOIN ENGINE.FIELD_OI_SYNC_OPTIONS AS OI ON FS.FIELD_ID=OI.FIELD_ID
JOIN ENGINE.OI_SYNC_OPTIONS SO ON OI.OI_SYNC_OPTIONS_ID=SO.OPTION_ID
ORDER BY 1, 2, 4

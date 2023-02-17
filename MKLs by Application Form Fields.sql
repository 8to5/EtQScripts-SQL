SELECT	DISTINCT FBF.DISPLAY_NAME AS FIELD_CAPTION,
		MASTER_KEYWORD_LIST.MASTER_KEYWORD_LIST_ID AS MKL_ID,
		MASTER_KEYWORD_LIST.DISPLAY_NAME MKL_NAME,
		MASTER_KEYWORD_LIST.BASE_TABLE AS MKL_BASE_TABLE,
		MASTER_KEYWORD_LIST.MASTER_KEYWORD_LIST_NAME AS MKL_DESIGN_NAME,
		MASTER_KEYWORD_LIST.ETQ$CREATED_DATE CREATED_DATE,
		MASTER_KEYWORD_LIST.ETQ$MODIFIED_DATE LAST_MODIFIED_DATE,
		USER_SETTINGS.DISPLAY_NAME LAST_MODIFIED_BY,
		USER_SETTINGS2.DISPLAY_NAME CREATED_BY ,
		ISNULL(APPLICATION_SETTINGS.DISPLAY_NAME,'') AS APP_DISPLAY_NAME,
		ISNULL(APPLICATION_SETTINGS.APPLICATION_NAME,'') AS APP_NAME
FROM DATACENTER.MASTER_KEYWORD_LIST MASTER_KEYWORD_LIST
LEFT JOIN DATACENTER.APPLICATIONS_MKLS APPLICATIONS_MKLS ON (MASTER_KEYWORD_LIST.MASTER_KEYWORD_LIST_ID = APPLICATIONS_MKLS.MASTER_KEYWORD_LIST_ID)
LEFT JOIN ENGINE.APPLICATION_SETTINGS AS APPLICATION_SETTINGS ON (APPLICATIONS_MKLS.APPLICATION_ID = APPLICATION_SETTINGS.APPLICATION_ID )
LEFT JOIN ENGINE.FIELD_SETTINGS AS FIELD ON ( MASTER_KEYWORD_LIST.MASTER_KEYWORD_LIST_ID = FIELD.MASTER_KEYWORD_LIST_ID)
LEFT JOIN ENGINE.USER_SETTINGS AS USER_SETTINGS ON (MASTER_KEYWORD_LIST.ETQ$LAST_EDITOR = USER_SETTINGS.USER_ID)
LEFT JOIN ENGINE.USER_SETTINGS AS USER_SETTINGS2 ON (MASTER_KEYWORD_LIST.ETQ$AUTHOR = USER_SETTINGS2.USER_ID)
LEFT JOIN ENGINE.FIELD_SETTINGS_FLD_BY_FR FBF ON FIELD.FIELD_ID=FBF.FIELD_ID
WHERE APPLICATION_SETTINGS.DISPLAY_NAME = 'Product Specification Management'
ORDER BY FBF.DISPLAY_NAME, MASTER_KEYWORD_LIST.DISPLAY_NAME

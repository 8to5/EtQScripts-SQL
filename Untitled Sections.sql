-- Sections may be renamed as 'Untitled Sections' after upgrading from v2017 to 2019/2020/CG
-- Change list of modules to include the modules you are using
SELECT A.APPLICATION_ID, A.APPLICATION_NAME AS APPLICATION_NAME, A.DISPLAY_NAME AS APP_DISPLAY, SS.SECTION_ID, SS.SECTION_NAME, SS.DISPLAY_NAME AS SECTION_DISPLAY
FROM ENGINE.SECTION_SETTINGS SS
JOIN ENGINE.FORM_SECTIONS FS ON FS.SECTION_ID=SS.SECTION_ID
JOIN ENGINE.APPLICATION_FORMS AF ON FS.FORM_ID=AF.FORM_ID
JOIN ENGINE.APPLICATION_SETTINGS A ON AF.APPLICATION_ID=A.APPLICATION_ID
WHERE SS.DISPLAY_NAME = 'UNTITLED SECTION'
  AND A.APPLICATION_NAME IN ('CORRACT',
							'CHANGE',
							'DELEGATION',
							'DEVIATION',
							'DOCWORK',
							'DOCARC',
							'NCMR',
							'SUPPLIER',
							'SUPPLIERARC',
							'MEETINGS')
ORDER BY A.APPLICATION_NAME, SS.SECTION_NAME

-- Disable all active user profiles, except for the EtQAdministrator
UPDATE ENGINE.USER_SETTINGS
SET DISPLAY_NAME = DISPLAY_NAME + ' (Disabled for S2S)',
  IS_DISABLED=1
WHERE IS_GROUP=0
  AND IS_INACTIVE=0
  AND IS_DISABLED=0
  AND USER_NAME NOT IN ('EtQAdministrator')

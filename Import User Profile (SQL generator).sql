SELECT CASE U.IS_DISABLED WHEN 1 THEN 'Yes' ELSE 'No' END AS ENGINE_IS_USER_DISABLED,
	   CASE U.IS_INACTIVE WHEN 1 THEN 'Yes' ELSE 'No' END AS ENGINE_IS_USER_INACTIVE,
	   CASE U.IS_GROUP WHEN 1 THEN 'Yes' ELSE 'No' END AS ENGINE_IS_GROUP,
	   U.USER_NAME AS ENGINE_USER_NAME,
	   U.DISPLAY_NAME AS ENGINE_DISPLAY_NAME,
	   ISNULL(U.FIRST_NAME,'') AS ENGINE_FIRST_NAME,
	   ISNULL(U.MIDDLE_INITIAL,'') AS ENGINE_MIDDLE_INITIAL,
	   ISNULL(U.LAST_NAME,'') AS ENGINE_LAST_NAME,
	   ISNULL(U.EMAIL,'') AS ENGINE_EMAIL,
	   ISNULL(U.LDAP_DOMAIN,'') AS ENGINE_LDAP_DOMAIN,
	   ISNULL(R.DISPLAY_NAME,'') AS ENGINE_REPORTS_TO,
	   ISNULL(SUBSTRING((SELECT '; '+ CONVERT(VARCHAR(100), G.DISPLAY_NAME) AS [text()]
            FROM ENGINE.GROUP_MEMBERS GM
			LEFT JOIN ENGINE.USER_SETTINGS G ON GM.USER_ID=G.USER_ID
            WHERE U.USER_ID=GM.MEMBER_USER_ID
			ORDER BY G.DISPLAY_NAME
            FOR XML PATH ('')), 3, 5000),'') AS USER_GROUPS,
	   ISNULL(LP.LOCATION_NAME ,'') AS ENGINE_PRIMARY_LOCATION,
	   ISNULL(SUBSTRING((SELECT '; '+ CONVERT(VARCHAR(100), LP2.LOCATION_NAME ) AS [text()]
            FROM ENGINE.OTHER_LOCATIONS OL
			LEFT JOIN DATACENTER.LOCATION_PROFILE LP2 ON OL.LOCATION_ID=LP2.LOCATION_PROFILE_ID
            WHERE U.USER_ID=OL.USER_ID
			ORDER BY LP2.DISPLAY_NAME
            FOR XML PATH ('')), 3, 5000),'') AS ENGINE_OTHER_LOCATIONS,
--	   '' AS ENGINE_ADDITIONAL_FILTER,			--************* WILL NEED FOR OTHER BUSINESSES
	   ISNULL(TZ.DISPLAY_NAME,'') AS ENGINE_USER_PROFILE_TIME_ZONE
FROM ENGINE.USER_SETTINGS U
LEFT JOIN DATACENTER.LOCATION_PROFILE LP ON U.PRIMARY_LOCATION_ID=LP.LOCATION_PROFILE_ID
LEFT JOIN ENGINE.USER_ADDITIONAL_FILTER AF ON U.USER_ID=AF.USER_ID
LEFT JOIN ENGINE.USER_SETTINGS R ON U.REPORTS_TO_ID=R.USER_ID
LEFT JOIN DATACENTER.TIME_ZONES TZ ON U.TIME_ZONE_ID=TZ.TIME_ZONE_ID
/*WHERE EXISTS (SELECT 'X'
			  FROM ENGINE.USER_SETTINGS G2
			  WHERE U.IS_GROUP=1
			    AND G2.IS_INACTIVE=0
				AND G2.IS_DISABLED=0
			    AND U.USER_ID=G2.USER_ID
			    AND G2.USER_NAME LIKE '%ESM%')
   OR EXISTS (SELECT 'X'
			  FROM ENGINE.GROUP_MEMBERS GM2
			  JOIN ENGINE.USER_SETTINGS U2 ON GM2.USER_ID=U2.USER_ID AND U2.USER_NAME LIKE '%ESM%'
			  WHERE GM2.MEMBER_USER_ID=U.USER_ID)
*/
ORDER BY U.IS_GROUP DESC, U.DISPLAY_NAME, R.DISPLAY_NAME

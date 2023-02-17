# look at locations in User Profile and only save new documents
if(thisPhase.isStartPhase()):
 userLocs = eccProfileManager.getUserProfile(thisUser.getName()).getLocationsIDs()
 if userLocs != []:
  for loc in userLocs:
   locationProfile = eccProfileManager.getLocationProfile(loc)
   if locationProfile != None or locationProfile.isDisabled == false:       
     userSelectedLoc = thisDocument.getFieldValues("ETQ$LOCATIONS")
     if userSelectedLoc != []:
        for userSelectedLoc in userSelectedLoc:
         userSelectedLocProfile = eccProfileManager.getLocationProfile(userSelectedLoc)
         if Rstring.contains(str(userLocs),str(userSelectedLoc)) == false:
          raise ValidationException,"Your account is not associated with the '" + userSelectedLocProfile.getDisplayName() + "' location in Reliance. Documents can only be created for Locations that your profile has security for. Please remove the invalid Location(s) or contact your local administrator for assistance."

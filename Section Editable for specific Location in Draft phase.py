# EDITABLE WHEN EtQScript
# Make the field visible for location 'ABC' in Draft
locs = thisDocument.getField("ETQ$LOCATIONS")
if not locs.isEmpty():
 loc = thisDocument.getField("ETQ$LOCATIONS").getUnlocalizedDisplayText()
 if Rstring.contains(loc,"ABC") and thisPhase.isStartPhase():
  print true

# READ-ONLY WHEN EtQScript
# Make the field read-only for location 'ABC' if not in the Draft phase
locs = thisDocument.getField("ETQ$LOCATIONS")
if not (locs.isEmpty() and thisPhase.isStartPhase()):
 loc = thisDocument.getField("ETQ$LOCATIONS").getUnlocalizedDisplayText()
 if Rstring.contains(loc,"ABC"):
  print true

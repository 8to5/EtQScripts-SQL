# Add a button to the subform row and use the following ETQScript to perform the movement action

# move up
rec = thisSubformRecord
if rec != None:
 loc = rec.getRecordOrder()
 if loc == 0:
  print true
 else:
  print false


#move down
rec = thisSubformRecord
if rec != None:
 loc = rec.getRecordOrder()
 if loc == thisSubformRecord.getParentSubform().size():
  print true
 else:
  print false

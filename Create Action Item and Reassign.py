# Auto-create Action Item activity when routing into Closed phase
if thisPhase.isSendingForward() and thisPhase.getNextPhase().getDisplayName()=="Closed":
 rDoc = thisApplication.newActivity("ACTIVITY_FORM","ACTIVITY_WF_PHASE_DRAFT",thisDocument,"ETQ$ACTIVITY_LINK")
 rDoc.save()
 myPhase = rDoc.getPhase() # Draft phase

 capaAdmin = rDoc.getFieldValue("CAPA_ADMINISTRATOR")
 # assign the Draft phase to the CAPA Admin, if available
 if capaAdmin != "":
  myPhase.reassign([capaAdmin], [], true)
 else:
  # if no CAPA Admin is available, route the request into the next phase
  myPhase.route("ACTIVITY_WF_PHASE_2",1)
 rDoc.close()

# This task loops through all *open* Action Items with *voided* parent documents, and voids them
oTasks = thisUser.getApplication("ENGINE").executeQueryFromDatasource("GET_ORPHANED_ACTION_ITEMS")

while oTasks.next():
 app = oTasks.getValue("APP_NAME")
 form = oTasks.getValue("FORM_NAME")
 docID = oTasks.getValue("DOC_ID")
 voidPhaseID = oTasks.getValue("VOID_PHASE")
 
 if (docId != None):
  if (engineConfig.isApplicationDeployed(app) and engineConfig.isSchemaExisting(app)):
   changeApp = thisUser.getApplication(app)
   if (changeApp != None):
    changeDoc = changeApp.getDocumentByKey(form,docId)
    if (changeDoc != None):
     currPhase = changeDoc.getPhase()
	 currPhase.voidDocument(voidPhaseID, [11], "Auto-voided because Parent document was voided.")
	 changeDoc.close()

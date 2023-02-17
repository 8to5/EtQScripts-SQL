# Release Documents locked by the system for the following modules
#   Document Control
#   Complaint
#   Complaint Investigation
#   MDR

# Change the affectedType and affectedNumber values in this section to unlock a specific document
#affectedType = "Document Control"
affectedType = "Complaint"
affectedNumber = "1245653"

from com.etq.util import Log
#------------------------------------------
def log(obj): #log to the engine log
  obj = prepObjectForLogging(obj)
  Log.info("\n", "\n~"+(thisDocument.getEncodedFieldText("ETQ$NUMBER"))+":"+thisUser.getName()+"~"+unicode(obj))
#------------------------------------------
def prepObjectForLogging(obj):# to make debugging easier and to avoid the null pointer exception
  if obj==None:
    obj="None" #else 
  if obj=="":
    obj="empty string"
  return obj
  
#------------------------------------------
try:
 #Determine the correct application and document to construct query
 if affectedType == "Complaint":
  affectedApplication = "COMPLAINTS"
  affectedObject = "COMPLAINT_DOCUMENT"
  affectedDocNum = "COMPLAINT_DOCUMENT_ID"
  affectedDesignName = "COMPLAINTS_COMPLAINT_DOCUMENT"
  log("ok.Complaint")
 elif affectedType == "Document Control":
  affectedApplication = "DOCWORK"
  affectedObject = "DOCWORK_DOCUMENT"
  affectedDocNum = "DOCWORK_ID"
  affectedDesignName = "DOCWORK_DOCUMENT"
  log("ok.Document")
 elif affectedType == "Complaint Investigation":
  affectedApplication = "COMPLAINTS"
  affectedObject = "INVESTIGAT_SUMMARY"
  affectedDocNum = "INVESTIGAT_SUMMARY_ID"
  affectedDesignName = "COMPLAINTS_INVESTIGATION_SUMMARY"
  log("ok.Investigation")
 elif affectedType == "MDR":
  affectedApplication = "COMPLAINTS"
  affectedObject = "MDR_DECISION_TREE"
  affectedDocNum = "MDR_DECISION_TREE_ID"
  affectedDesignName = "E_MDR_EVALUATION"
  log("ok.MDR")
 elif affectedType == "Return":
  affectedApplication = "COMPLAINTS"
  affectedObject = "RETURN_1"
  affectedDocNum = "RETURN_1_ID"
  affectedDesignName = "RETURN_1_P"
  log("ok.Return")
except:
  log("except")
  pass
 
#construct query 
affectedApp = thisUser.getApplication(affectedApplication)
query = "SELECT " + affectedObject + "." + affectedDocNum + " FROM " + affectedApplication + "." + affectedObject + " WHERE " + affectedObject + "." + "ETQ$NUMBER = " + "'" + affectedNumber + "'"
log(query)
#break lock on document
objectDocKeys = affectedApp.getDocumentKeysByQuery(affectedDesignName,query)
if (objectDocKeys != []):
 for objectDocKey in objectDocKeys:
  form = affectedApp.getDocumentInEditMode(objectDocKey)
  if form != None: 
   form.save()
   form.close()

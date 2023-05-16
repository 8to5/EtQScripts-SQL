# The following numbers indicate the routing direction : NONE = 0; FORWARD = 1; BACKWARD = 2; REJECTING = 5;
route (String nextPhaseName,
       Date dueDate,
       org.python.core.PyList assignedUsers,
       org.python.core.PyList notifiedUsers,
       String comment,
       int direction)

# The "DUMMY_DAO" Data Source can be created in the Reliance Engine and be used to dynamically pass any SQL query at runtime.
# The Selection Statement (SQL) for the Data Source is simply a parameter/placeholder called: ETQ$SQL

### Route record to [TARGET] phase and record the record number in the Log
from com.etq.util import Log
inventoryGroup = eccProfileManager.getUserProfile("GROUP_DESIGN_NAME")
assigned = []
assigned.append(assignList.append(inventoryGroup.getID())
app = thisUser.getApplication("MATRET")
query  = " SELECT RMA.RMA_FORM_ID RMA_ID "
query += " FROM MATRET.RMA_FORM RMA "
query += " LEFT JOIN ENGINE.PHASE_SETTINGS PHASE ON (RMA.ETQ$CURRENT_PHASE = PHASE.PHASE_ID ) "
query += " WHERE UPPER(PHASE.DISPLAY_NAME) = 'DRAFT' "
param = {"ETQ$SQL":query}
dao = app.executeQueryFromDatasource("DUMMY_DAO", param)
while dao.next() :
 key = dao.getValue("RMA_ID")
 doc = app.getDocumentByKeyInEditMode("RMA_FORM_DESIGN_NAME",key)
 if doc != None :
  phase = doc.getPhase()
  if phase != None :
   message = "TASK to route to [TARGET] phase, # " + str(doc.getFieldValue("ETQ$NUMBER"))
   Log.info(thisUser, message) 
   thisPhase.route("TARGET_PHASE_DESIGN_NAME", Rdate.adjustDate(Rdate.now(), 0, 0, 5, 0, 0, 0),assigned,[],"Route comment", 1)
 doc.close()

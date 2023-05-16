# Note #1: The processAssessments and getKeys functions are the main components.
# Note #2: This script also has additional features like logging to a custom module, plus is built around a custom module

if not thisDocument:
	from _Misc.EtQClasses import *

# Task : Archive ISAM Assessments
# ===================================================================
# Archive ISAM Assessments
# Generic Task to Archive Assessments with passed SQL SELECT criteria.
# Suggested Frequency: Once
# ===================================================================

# Configurable Settings.
REASON_OBSOLETE="Archive all assessments in NIC Yeast inactive... where item is in status different from 20. SN INC0360128"
# SQL to find CIA_ID records
SELECT_STATEMENT="SELECT DISTINCT CIA.CIA_ID CIA_ID FROM ISAM_ASSESSMENTS.CIA AS CIA"
SELECT_STATEMENT+=" INNER JOIN ENGINE.PHASE_SETTINGS PHASE_SETTINGS ON (CIA.ETQ$CURRENT_PHASE=PHASE_SETTINGS.PHASE_ID AND PHASE_SETTINGS.PHASE_TYPE=1)"
SELECT_STATEMENT+=" LEFT JOIN MDM.CLASSIFICATION AS CLASSLV5 ON (CLASSLV5.CLASSIFICATION_ID=CIA.CIA_A_ITEM_CLASS_LEVEL5_ID)"
SELECT_STATEMENT+=" LEFT JOIN ISAM_ASSESSMENTS.CIA_ASSESS_COMBINATIONS_SUB AS CIA_SUB ON (CIA_SUB.CIA_ID=CIA.CIA_ID)"
SELECT_STATEMENT+=" LEFT JOIN ISAM.ITEM AS ITEMS ON (ITEMS.ITEM_ID=CIA_SUB.CIA_ASSESS_COMBI_ITEM_ID)"
SELECT_STATEMENT+=" LEFT JOIN ISAM.I_NUTRE_IT_COD_SUBFO ITEM_SUB ON (ITEMS.ITEM_ID=ITEM_SUB.ITEM_ID)"
SELECT_STATEMENT+=" LEFT JOIN MDM.ITEM_CODES STAT ON (ITEM_SUB.ITEM_NUTRECO_CODE_STATUS_ID=STAT.ITEM_CODES_ID)"
SELECT_STATEMENT+=" WHERE CLASSLV5.ITEM_CLASSIFICATION LIKE 'Yeast inactive%' AND CIA.ETQ$NUMBER LIKE 'IM%'"
SELECT_STATEMENT+=" EXCEPT"
SELECT_STATEMENT+=" SELECT DISTINCT CIA.CIA_ID CIA_ID FROM ISAM_ASSESSMENTS.CIA AS CIA"
SELECT_STATEMENT+=" INNER JOIN ENGINE.PHASE_SETTINGS PHASE_SETTINGS ON (CIA.ETQ$CURRENT_PHASE=PHASE_SETTINGS.PHASE_ID AND PHASE_SETTINGS.PHASE_TYPE=1)"
SELECT_STATEMENT+=" LEFT JOIN MDM.CLASSIFICATION AS CLASSLV5 ON (CLASSLV5.CLASSIFICATION_ID=CIA.CIA_A_ITEM_CLASS_LEVEL5_ID)"
SELECT_STATEMENT+=" LEFT JOIN ISAM_ASSESSMENTS.CIA_ASSESS_COMBINATIONS_SUB AS CIA_SUB ON (CIA_SUB.CIA_ID=CIA.CIA_ID)"
SELECT_STATEMENT+=" LEFT JOIN ISAM.ITEM AS ITEMS ON (ITEMS.ITEM_ID=CIA_SUB.CIA_ASSESS_COMBI_ITEM_ID)"
SELECT_STATEMENT+=" LEFT JOIN ISAM.I_NUTRE_IT_COD_SUBFO ITEM_SUB ON (ITEMS.ITEM_ID=ITEM_SUB.ITEM_ID)"
SELECT_STATEMENT+=" LEFT JOIN MDM.ITEM_CODES STAT ON (ITEM_SUB.ITEM_NUTRECO_CODE_STATUS_ID=STAT.ITEM_CODES_ID)"
SELECT_STATEMENT+=" WHERE CLASSLV5.ITEM_CLASSIFICATION LIKE 'Yeast inactive%' AND CIA.ETQ$NUMBER LIKE 'IM%'"
SELECT_STATEMENT+=" AND LEFT(STAT.ITEM_STATUS_CODE,2)='20'"

# Constant Flags
DEBUG=true
YES,NO=1,0
TASK_NAME="Archive ISAM Assessments"

# Set Defaults
passed,failed=0,0
details={"error":NO}
lineNum=1
body=""

# Set standard log details
details["source"]=TASK_NAME
details["type"]="Task"
details["application"]="ISAM Assessments"
details["form"]="Assessments"
details["docLink"]=PublicDocLink.createDocLink("DATACENTER","ENGINE_TASK_SETTINGS",int(thisDocument.getID()))

# Declarations
appCIA=thisUser.getApplication("ISAM_ASSESSMENTS")
appDataControl=thisUser.getApplication("DATA_CONTROL")

# Used to limit the coverage of the Task by either keys, passes or fails
MAX_KEYS=10000
MAX_PASSED=10000
MAX_FAILED=10

# Variables
ADD,REMOVE,NOTHING=1,2,3


def formattedDateTime(output=""):
	"""
	| Creates a clean time stamp.
	| *output* [String]: date,time or blank; defines the output string
	| *return* [String]: formatted datetime string
	"""
	curDT=None
	sysDT=Rdate.now()
	# Adjust to CET as seems to have strange timezone
	curDT=Rdate.adjustDate(sysDT,0,0,0,0,0,0)
	theDate=str(Rdate.getDateOnly(curDT,Rdate.MEDIUM))
	theTime=str(Rdate.getTimeOnly(curDT,Rdate.MEDIUM))
	if output=="date":
		dt=theDate
	elif output=="time":
		dt=theTime
	else:
		dt=theDate+" at "+theTime
	return dt


def addToLog(message):
	global body
	global lineNum
	LF="\n"
	body+="%s [%s]: %s %s" % (lineNum,formattedDateTime("time"),message,LF)
	lineNum+=1


def createLogRecord(details):
	"""
	| Creates a log entry with passed information.
	| *details* [PyDict]: source, type, application, form, workflow, docNumber [String], error [Boolean], docLink [PublicObject].
	| *return* [Boolean]: true if created record.
	"""
	global body
	saved=false
	_Application=thisUser.getApplication("DATA_CONTROL")
	if _Application:
		formID=PublicSettingManager().getFormSetting("DATA_LOG").getID()
		if formID:
			newLog=_Application.newDocument(int(formID),None)
			if newLog and details:
				if details.has_key("source"): newLog.setFieldValue("DATA_LOG_SOURCE",details["source"])
				if details.has_key("type"): newLog.setFieldValue("DATA_LOG_TYPE",details["type"])
				if details.has_key("error"): newLog.setFieldValue("DATA_LOG_ERRORS",details["error"])
				if details.has_key("count"): newLog.setFieldValue("DATA_LOG_RECORD_COUNT",details["count"])
				if details.has_key("pass"): newLog.setFieldValue("DATA_LOG_RECORD_PASS",details["pass"])
				if details.has_key("fail"): newLog.setFieldValue("DATA_LOG_RECORD_FAIL",details["fail"])
				if details.has_key("application"): newLog.setFieldValue("DATA_LOG_APPLICATION",details["application"])
				if details.has_key("form"): newLog.setFieldValue("DATA_LOG_FORM",details["form"])
				if details.has_key("workflow"): newLog.setFieldValue("DATA_LOG_WORKFLOW",details["workflow"])
				if details.has_key("docNumber"): newLog.setFieldValue("DATA_LOG_DOC_NUM",details["docNumber"])
				newLog.setFieldValue("DATA_LOG_DETAILS",body)
				if details.has_key("docLink"): newLog.getField("ETQ$SOURCE_LINK").addDocLink(details["docLink"])
				saved=newLog.save()
				newLog.close()
	return saved


def getKeys():
	"""
	| Finds all the keys of the ISAM Assessment records to be processed.
	| *return* [PyList]: List of Assessment Document IDs for update.
	"""
	addToLog("getKeys()")
	global details
	ids=None
	select=SELECT_STATEMENT
	# select+=" ORDER BY CIA.CIA_ID"
	if DEBUG: addToLog("getKeys.select=%s" % select)
	ids=appCIA.getDocumentKeysByQuery("ASSESSMENT_CIA",select)
	details["count"]=len(ids)
	if ids:
		addToLog("getKeys.ids return count=%s" % (len(ids)))
	return ids


def processAssessments(keys):
	addToLog("processAssessments(%s keys)" % (len(keys)))
	global failed
	global passed
	if keys:
		count=1
		separator=","
		for key in keys:
			if count>=MAX_KEYS or failed>=MAX_FAILED or passed>=MAX_PASSED:
				addToLog("#"*15)
				addToLog("STOPPED due MAX limit reached")
				break
			addToLog("#"*15)
			addToLog("processAssessments.Processing record %s" % (key.getKeyValue()))
			if appCIA.isDocumentOpened(key)==false:
				try:
					doc=appCIA.getDocument(key,false)
					if doc:
						addToLog("processAssessments.processing.doc=%s" % doc.getFieldValue("ETQ$NUMBER"))
						newOR=appCIA.newActivity("ISAM_OBSOLETE_REQUEST","ISAM_OBSOLETE_REQUEST",doc,"ETQ$OBSOLETE_REQUEST_LINK")
						if newOR:
							newOR.setFieldValue("OBSOLETION_REASON","No longer needed - Automated by Task %s. Reason: %s" % (TASK_NAME,REASON_OBSOLETE))
							saved=newOR.save()
							if saved:
								addToLog("processAssessments.processObsoleteRequest.newOR=%s" % newOR.getFieldValue("ETQ$NUMBER"))
								orPhase=newOR.getPhase()
								if orPhase:
									orPhase.route("ISAM_OBSOLETE_ACCEPTED",1,false)
									if newOR and newOR.isOpen(): newOR.close()
									passed+=1
							else:
								addToLog("***processAssessments....FAILED TO CREATE Obsolete request!!!")
								failed+=1
				except:
					addToLog("***processAssessments....FAILED TO PROCESS THE RECORD!!!")
					failed+=1
				finally:
					if doc: doc.close()
			else:
				addToLog("***processAssessments....CANT OPEN RECORD!!!")
				failed+=1
			count+=1


##############################################################
# Main

try:
	addToLog("Task Started: %s" % formattedDateTime())
	addToLog("#" * 30)
	processAssessments(getKeys())
	details["pass"]=passed
	details["fail"]=failed
	addToLog("$" * 30)
	addToLog("#### Summary ####")
	addToLog("Records which Task succeeded in updating = %s" % passed)
	addToLog("Records which Task failed to update = %s" % failed)
	if failed>0: details["error"]=YES
	createLogRecord(details)

except:
	details["error"]=YES
	createLogRecord(details)

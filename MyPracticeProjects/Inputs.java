Inputs
onboardingExcelFilePath
rowNumberInExcelFile
monitorToBeGenerated
scheduleToBeGenerated
resourceToBeGenerated
iiamsToBeGenerated




Read excel
For each row
     If rowNum ==selectedRow
          Extract all row values into individual variables
If (monitorToBeGenerated==’Y’) callModule GenerateMonitor 
If (scheduleToBeGenerated==’Y’) callModule GenerateSchedule 
If (resourceToBeGenerated==’Y’) 
{
callModule GenerateSourceResource
callModule GenerateTarget1Resource
if(countTargets>1) callModule GenerateTarget2Resource
if(countTargets>2) callModule GenerateTarget3Resource
if(countTargets>3) callModule GenerateTarget4Resource
if(countTargets>4) callModule GenerateTarget5Resource
if(countTargets>5) callModule GenerateTarget6Resource
                }
If (iiamsToBeGenerated==’Y’) callModule GenerateIIAMS 


Module GenerateMonitor
{
(if countTarget = 1 ) Make copy of TemplateMonitor1.xml into <InterfaceID>Monitor.xml
Search and replace each token till target1

(if countTarget = 2 ) Make copy of TemplateMonitor2.xml into <InterfaceID>Monitor.xml
Search and replace each token till target2

(if countTarget = 6 ) Make copy of TemplateMonitor6.xml into <InterfaceID>Monitor.xml
Search and replace each token till target6

}

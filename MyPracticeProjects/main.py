countriesList = ["India","USA","Canada"]
countriesTuple= ("India","USA","Canada")
countriesSet  = {"India","USA","Canada"}
countriesDict = {"India":"New Delhi", "USA":"WashingtonDC","Canada":"Ottawa"}
var = type(countriesList); print(var);
var = type(countriesTuple); print(var);
var = type(countriesSet); print(var);
var = type(countriesDict); print(var);

for i in range(0,)




#!/bin/bash
CPU_USAGE="`top -b -n2 -p 1 | fgrep "Cpu(s)" | tail -1 | awk -F'id,' -v prefix="$prefix" '{ split($1, vs, ","); v=vs[length(vs)]; sub("%", "", v); printf "%s%.1f%%\n", prefix, 100 - v }'|sed 's/%//'`"
y="printf "%.0f" $CPU_USAGE"
CPU_USAGE_Num=$(eval "$y")
DATE=$(date "+%Y-%m-%d %H:%M:%S")
#mail_reciepient=narmada.sharma@emerson.com
mail_reciepient=itssfusionadmin@emerson.com,DLITSSFusionSupport@emerson.com
Threshhold_W='70'
Threshhold_C='80'
EMAIL_FROM=DEV_JFROG@emerson.com
echo "$CPU_USAGE_Num"
echo "$Threshhold"
if [ $CPU_USAGE_Num -gt $Threshhold_C ]
then

mailx -s "[PROD] CRITICAL - GAMS Monitoring - TOMCAT PROD CPU Usage has exceeded 80%" -r "$EMAIL_FROM" $mail_reciepient <<< "Current CPU usage is: $CPU_USAGE_Num %

PLEASE TAKE IMMEDIATE ACTION ON THIS ALERT and CONTACT DLITSSFusionSupport@emerson.com

** P.S. This is auto generated email by DSI Server. Please do not reply. Contact DLITSSFusionSupport@emerson.com for any queries or further support. Notification Date Time: $DATE GMT**"
elif [ $CPU_USAGE_Num -gt $Threshhold_W ]
then
mailx -s "[PROD] WARNING - GAMS Monitoring - TOMCAT PROD CPU Usage has exceeded 70%" -r "$EMAIL_FROM" $mail_reciepient <<< "Current CPU usage is: $CPU_USAGE_Num %

PLEASE TAKE ACTION ON THIS ALERT and CONTACT DLITSSFusionSupport@emerson.com

** P.S. This is auto generated email by DSI Server. Please do not reply. Contact DLITSSFusionSupport@emerson.com for any queries or further support. Notification Date Time: $DATE GMT**"
fi

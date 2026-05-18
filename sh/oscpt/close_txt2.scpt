
# 关闭所有txt窗口 但会过滤掉一些常驻窗口

on getToday()
	set currentDate to current date
	set yearNum to year of currentDate
	set monthNum to month of currentDate as integer
	set dayNum to day of currentDate

	#-- 补零处理
	if monthNum < 10 then set monthNum to "0" & monthNum
	if dayNum < 10 then set dayNum to "0" & dayNum

	set formattedDate to yearNum & "-" & monthNum & "-" & dayNum
	return formattedDate
end getToday

on mayFilterByName(name)
	set todayVal to getToday()
	if name starts with todayVal or name starts with "Manual-" then
		return true
	else
		return false
	end if

end mayFilterByName

tell application "TextEdit"

	#repeat with eachWindow in windows
	#repeat with i from (count of windows) down to 1	
	#	set eachWindow to window i

	repeat with eachWindow in windows
		set windowName to name of eachWindow
		log "发现了窗口: " & windowName
		if my mayFilterByName(windowName) then
			log "跳过窗口:" & windowName
		else
			try
				close eachWindow
			on error
				log "尝试关闭Window: " & windowName & " 抛出异常"
			end try
		end if
	end repeat
end tell



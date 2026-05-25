# 定位: 用于关闭textEdit的子窗口, 关闭大部分窗口 仅保留最上面的2个(允许外部指定 默认为2个)
# 有常住窗口的版本

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

on run argv
	# 默认保留两个widnow
	set keepWindow to 2
	if (count of argv) > 0 then
		# shell命令传入了窗口的数量
		set keepWindow to item 1 of argv
	end if

	log "将保留" & keepWindow & " 个TextEdit窗口"

	# 进行关闭窗口的动作
	#set endNum to keepWindow + 1
	set endNum to 1
	set closeNum to 0
	tell application "TextEdit"
		log "TextEdit的窗口数量: " & count of windows
		repeat with i from (count of windows) to endNum by -1
			set windowName to name of window i
			if my mayFilterByName(windowName) then
				log "跳过窗口:" & windowName
			else
				try
					set docRef to document of window i
					set filePath to path of docRef
					log "Close Window " & i & ": " & (name of window i) & "  path:  " & filePath
					close window i
					set closeNum to closeNum + 1
				on error
					log "尝试关闭Window: " & windowName & " 抛出异常"
				end try
			end if

			# 判断是否根据closeNum跳出循环
			if closeNum > count of windows - keepWindow -1 then
				exit repeat
			end if
		end repeat
	end tell

end run

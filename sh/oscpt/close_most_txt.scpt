# 定位: 用于关闭textEdit的子窗口, 关闭大部分窗口 仅保留最上面的2个(允许外部指定 默认为2个)

on run argv
	# 默认保留两个widnow
	set keepWindow to 2
	if (count of argv) > 0 then
		# shell命令传入了窗口的数量
		set keepWindow to item 1 of argv
	end if

	log "将保留" & keepWindow & " 个TextEdit窗口"

	# 进行关闭窗口的动作
	set endNum to keepWindow + 1
	tell application "TextEdit"
		log "TextEdit的窗口数量: " & count of windows
		repeat with i from (count of windows) to endNum by -1
			set windowName to name of window i
			try
				set docRef to document of window i
				set filePath to path of docRef
				log "Close Window " & i & ": " & (name of window i) & "  path:  " & filePath
			on error
				log "尝试关闭Window: " & windowName & " 抛出异常"
			end try
			close window i
		end repeat
	end tell

end run

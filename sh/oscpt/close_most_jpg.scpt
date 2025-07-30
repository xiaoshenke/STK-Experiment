# 用于关闭大部分的jpg窗口 仅保留最上面的2个窗口

on run argv
	# 默认保留两个widnow
	set keepWindow to 2
	if (count of argv) > 0 then
		# shell命令传入了窗口的数量
		set keepWindow to item 1 of argv
	end if

	log "将保留" & keepWindow & " 个qView窗口"

	# 进行关闭窗口的动作
	set endNum to keepWindow + 1
	tell application "System Events"
		tell process "qView"
			set windowList to every window
			set windowCount to count of windowList
			log "qView的window数据量" & windowCount
			repeat with i from windowCount to endNum by -1
				log "Close Window" & i & "    name:" & name of window i
				click (button 1 of window i whose subrole is "AXCloseButton")
			end repeat
		end tell
	end tell
end run

#!/bin/bash

window_count=$(osascript -e '
tell application "System Events"
	set isRunning to exists (processes where name is "qView")
	if isRunning then
		tell process "qView"
			return count of every window
		end tell
	else
		return 0
	end if
end tell
')

echo $window_count

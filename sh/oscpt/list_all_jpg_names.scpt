applescript

set isRunning to do shell script "pgrep -x qView > /dev/null && echo 'yes' || echo 'no'"
if isRunning is "yes" then
    tell application "System Events"
        tell process "qView"
            return name of every window
        end tell
    end tell
else
    return ""
end if

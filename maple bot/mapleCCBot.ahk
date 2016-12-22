MsgBox Welcome to mapleBot! You are now using: CC Bot. This is a work in progress, please use at your own risk :)

;Press Escape to exit the script.
Esc::ExitApp

;Press ctrl+numpad1 to cc once.
^Numpad1::
	Send {+} {Right} {Enter}
Return

;Mass CC
;Press ctrl+Numpad2 to cc twenty times, with a five second delay in between.
^Numpad2::
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	Send {+} {Right} {Enter}
	Sleep 5000
	MsgBox The 20 channel cycle has ended. Please press ctrl+Numpad2 to start another cycle.
Return

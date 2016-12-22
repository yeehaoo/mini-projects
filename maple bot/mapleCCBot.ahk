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
Return

;Ability Spamming (work in progress, do not use)
;Press ctrl+ Numpad3 to spam CTRL ability
^Numpad3::
	Send {Enter 30000}
Return

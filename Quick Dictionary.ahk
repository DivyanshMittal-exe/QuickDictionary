#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


^q::
clipboard:="" ;
While clipboard
Sleep 10 ; 
TimeOut = 0;
While !clipboard AND TimeOut < 100 {
Send ^c
Sleep 100 ; gives time for the clipboard to be populated, especially if it is large
Timeout ++
}
run, python.exe Dict.py
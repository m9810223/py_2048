@echo off

@REM set d="auto" 
@REM set t=%date%%time%
@REM set /p d=git commit: 
@REM git add . && git commit -m "%t% %d%" && git push 


set t=%date%%time%
git add . && git commit -m "%t%" && git push 


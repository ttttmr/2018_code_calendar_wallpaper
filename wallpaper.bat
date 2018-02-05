@echo off
python %~dp0code_calendar.py
reg add "HKCU\Control Panel\Desktop" /v Wallpaper /f /t REG_SZ /d %~dp02018_code_calendar_wallpaper.jpg
RunDll32.exe USER32.DLL,UpdatePerUserSystemParameters
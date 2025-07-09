@echo off
cd /d "%~dp0"
echo ======================================
echo  Compilando credenciales.py a EXE...
echo  Con ícono: lock.ico
echo ======================================

REM -- Limpiar compilaciones previas
rd /s /q dist >nul 2>&1
rd /s /q build >nul 2>&1
del /q credenciales.spec >nul 2>&1

REM -- Ejecutar PyInstaller
pyinstaller --onefile --icon=lock.ico credenciales.py

echo.
echo ✅ EXE generado en: dist\credenciales.exe
echo Presione una tecla para salir...
pause >nul

@echo off
TITLE Nexus Optimized
CLS

echo ==========================================
echo       NEXUS OPTIMIZED - OTIMIZACAO
echo ==========================================
echo.

net session >nul 2>&1
if %errorLevel% neq 0 (
    echo ATENCAO: Execute este arquivo como Administrador!
    echo Clique com o botao direito nele e escolha "Executar como Administrador".
    pause
    exit
)

echo [1/2] Aplicando otimizacoes de latencia (BCDEDIT)...
bcdedit /set useplatformclock false >nul
bcdedit /set disabledynamictick yes >nul
echo - Concluido!

echo.
echo [2/2] Limpando arquivos temporarios...
del /q /f /s "%TEMP%\*" >nul 2>&1
echo - Concluido!

echo.
echo ==========================================
echo    OTIMIZACAO CONCLUIDA COM SUCESSO!
echo ==========================================
pause

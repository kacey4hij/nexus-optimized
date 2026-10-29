import customtkinter as ctk
import subprocess
import ctypes
import sys

# Solicita elevação para Administrador
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Nexus Optimized")
app.geometry("450x350")
app.resizable(False, False)

def otimizar_latencia():
    subprocess.run("bcdedit /set useplatformclock false && bcdedit /set disabledynamictick yes", shell=True)
    status.configure(text="Latência otimizada com sucesso!", text_color="lime")

def limpar_temp():
    subprocess.run('powershell -Command "Remove-Item -Path $env:TEMP\\* -Recurse -Force -ErrorAction SilentlyContinue"', shell=True)
    status.configure(text="Arquivos temporários limpos!", text_color="lime")

title = ctk.CTkLabel(app, text="NEXUS OPTIMIZED", font=("Arial", 20, "bold"))
title.pack(pady=20)

btn1 = ctk.CTkButton(app, text="Otimizar Latência (BCDEDIT)", command=otimizar_latencia, width=280, height=40)
btn1.pack(pady=10)

btn2 = ctk.CTkButton(app, text="Limpar Lixo / Temp", command=limpar_temp, width=280, height=40)
btn2.pack(pady=10)

status = ctk.CTkLabel(app, text="Aguardando ação...", font=("Arial", 12))
status.pack(pady=20)

app.mainloop()

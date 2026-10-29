import customtkinter as ctk
import subprocess
import os
import shutil
import threading
import platform
import psutil
import winreg
from datetime import datetime

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class NexusOptimizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Nexus Optimizer — Ultimate Professional Suite")
        self.geometry("1100x680")
        self.resizable(False, False)

        # Paleta de Cores Gamer Premium (Preto e Roxo Neón)
        self.bg_color = "#0b0b0e"
        self.sidebar_color = "#121216"
        self.card_color = "#18181f"
        self.purple_primary = "#9d4edd"
        self.purple_hover = "#b5179e"
        self.text_color = "#ffffff"
        self.text_muted = "#8d8d99"
        self.accent_green = "#00ffcc"
        self.danger_color = "#ff4d4d"

        self.configure(fg_color=self.bg_color)

        # --- MENU LATERAL (SIDEBAR) ---
        self.sidebar_frame = ctk.CTkFrame(self, fg_color=self.sidebar_color, corner_radius=0, width=240)
        self.sidebar_frame.pack(side="left", fill="y")

        self.logo_label = ctk.CTkLabel(
            self.sidebar_frame, 
            text="NEXUS\nOPTIMIZER", 
            font=ctk.CTkFont(family="Arial", size=20, weight="bold"),
            text_color=self.purple_primary,
            justify="left"
        )
        self.logo_label.pack(anchor="w", padx=20, pady=(30, 20))

        # Botões de Navegação
        self.create_sidebar_btn("🏠  Dashboard Geral", lambda: self.show_frame("Dashboard"))
        self.create_sidebar_btn("🧹  Limpeza & Caches", lambda: self.show_frame("Clean"))
        self.create_sidebar_btn("⚡  Desempenho & CPU", lambda: self.show_frame("Performance"))
        self.create_sidebar_btn("🚀  Programas Inicialização", lambda: self.show_frame("Startup"))
        self.create_sidebar_btn("🎮  Modo Gamer Ativo", lambda: self.show_frame("GameMode"))
        self.create_sidebar_btn("🛠️  Diagnóstico & SFC", lambda: self.show_frame("Diagnostics"))
        self.create_sidebar_btn("📜  Registo de Auditoria", lambda: self.show_frame("Logs"))

        self.version_lbl = ctk.CTkLabel(self.sidebar_frame, text="v3.5 Ultimate • Win 10/11 x64", font=ctk.CTkFont(size=11), text_color=self.text_muted)
        self.version_lbl.pack(side="bottom", anchor="w", padx=20, pady=20)

        # --- ÁREA DE CONTEÚDO PRINCIPAL ---
        self.content_frame = ctk.CTkFrame(self, fg_color=self.bg_color, corner_radius=0)
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.frames = {}
        self.init_all_frames()
        self.show_frame("Dashboard")

    def create_sidebar_btn(self, text, command):
        btn = ctk.CTkButton(
            self.sidebar_frame, text=text, fg_color="transparent", text_color=self.text_color,
            hover_color=self.card_color, anchor="w", font=ctk.CTkFont(size=13, weight="bold"),
            corner_radius=8, height=40, command=command
        )
        btn.pack(fill="x", padx=12, pady=4)
        return btn

    def init_all_frames(self):
        for name in ("Dashboard", "Clean", "Performance", "Startup", "GameMode", "Diagnostics", "Logs"):
            self.frames[name] = ctk.CTkFrame(self.content_frame, fg_color=self.bg_color, corner_radius=0)

        self.setup_dashboard(self.frames["Dashboard"])
        self.setup_clean(self.frames["Clean"])
        self.setup_performance(self.frames["Performance"])
        self.setup_startup(self.frames["Startup"])
        self.setup_gamemode(self.frames["GameMode"])
        self.setup_diagnostics(self.frames["Diagnostics"])
        self.setup_logs(self.frames["Logs"])

    def show_frame(self, name):
        for f in self.frames.values():
            f.pack_forget()
        self.frames[name].pack(fill="both", expand=True)

    def log_message(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted = f"[{timestamp}] {message}\n"
        if hasattr(self, 'log_textbox'):
            self.log_textbox.configure(state="normal")
            self.log_textbox.insert("end", formatted)
            self.log_textbox.see("end")
            self.log_textbox.configure(state="disabled")

    # ================= 1. DASHBOARD =================
    def setup_dashboard(self, parent):
        ctk.CTkLabel(parent, text="Painel de Controlo Nexus", font=ctk.CTkFont(size=22, weight="bold"), text_color=self.text_color).pack(anchor="w", padx=30, pady=(30, 5))
        ctk.CTkLabel(parent, text="Centro operacional avançado para otimização segura e monitoramento do Windows.", font=ctk.CTkFont(size=13), text_color=self.text_muted).pack(anchor="w", padx=30, pady=(0, 20))

        card = ctk.CTkFrame(parent, fg_color=self.card_color, corner_radius=12, height=180)
        card.pack(fill="x", padx=30, pady=10)

        ctk.CTkLabel(card, text="🛡️ Integridade e Conformidade de Segurança", font=ctk.CTkFont(size=16, weight="bold"), text_color=self.purple_primary).pack(anchor="w", padx=25, pady=(20, 5))
        
        os_info = f"• Sistema Detetado: {platform.system()} {platform.release()} ({platform.architecture()[0]})"
        ctk.CTkLabel(card, text=os_info, font=ctk.CTkFont(size=13), text_color=self.text_color).pack(anchor="w", padx=25, pady=2)
        ctk.CTkLabel(card, text="• Estado da Defesa: Windows Defender e Firewall rigorosamente preservados.", font=ctk.CTkFont(size=12), text_color=self.text_muted).pack(anchor="w", padx=25, pady=2)
        ctk.CTkLabel(card, text="• Política de Segurança: Zero remoção de ficheiros pessoais ou serviços essenciais.", font=ctk.CTkFont(size=12), text_color=self.text_muted).pack(anchor="w", padx=25, pady=2)

    # ================= 2. LIMPEZA & CACHE =================
    def setup_clean(self, parent):
        ctk.CTkLabel(parent, text="Limpeza Profunda de Armazenamento", font=ctk.CTkFont(size=20, weight="bold"), text_color=self.text_color).pack(anchor="w", padx=30, pady=(30, 5))
        ctk.CTkLabel(parent, text="Análise segura de caches, ficheiros temporários do utilizador e diretórios do sistema.", font=ctk.CTkFont(size=13), text_color=self.text_muted).pack(anchor="w", padx=30, pady=(0, 15))

        self.clean_info_lbl = ctk.CTkLabel(parent, text="Clique em 'Analisar Espaço' para calcular lixo acumulado.", font=ctk.CTkFont(size=14, weight="bold"), text_color=self.accent_green)
        self.clean_info_lbl.pack(anchor="w", padx=30, pady=10)

        btn_frame = ctk.CTkFrame(parent, fg_color="transparent")
        btn_frame.pack(anchor="w", padx=30, pady=10)

        ctk.CTkButton(btn_frame, text="Analisar Espaço Recuperável", fg_color=self.purple_primary, hover_color=self.purple_hover, width=200, height=38, command=self.analyze_cleanup).pack(side="left", padx=(0, 15))
        ctk.CTkButton(btn_frame, text="Executar Limpeza Segura", fg_color=self.purple_primary, hover_color=self.purple_hover, width=200, height=38, command=self.execute_cleanup).pack(side="left")

        self.clean_box = ctk.CTkTextbox(parent, width=780, height=260, fg_color=self.card_color, text_color=self.text_color, font=ctk.CTkFont(family="Consolas", size=12))
        self.clean_box.pack(anchor="w", padx=30, pady=15)
        self.clean_box.configure(state="disabled")

    def analyze_cleanup(self):
        def task():
            self.clean_box.configure(state="normal")
            self.clean_box.delete("1.

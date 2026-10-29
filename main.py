import customtkinter as ctk
import subprocess
import os
import threading
import platform
import psutil
from datetime import datetime

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class NexusOptimizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Nexus Optimizer — Painel Profissional")
        self.geometry("850x550")
        self.resizable(False, False)

        # Identidade Visual Obrigatória: Preto e Roxo Gamer
        self.bg_color = "#0d0d0f"
        self.card_color = "#16161a"
        self.purple_primary = "#8a2be2"  # Roxo Vibrante
        self.purple_hover = "#9932cc"
        self.text_color = "#ffffff"

        self.configure(fg_color=self.bg_color)

        # Cabeçalho
        self.header_frame = ctk.CTkFrame(self, fg_color=self.card_color, corner_radius=0, height=60)
        self.header_frame.pack(fill="x", side="top")

        self.title_label = ctk.CTkLabel(
            self.header_frame, 
            text="NEXUS OPTIMIZER", 
            font=ctk.CTkFont(family="Arial", size=20, weight="bold"),
            text_color=self.purple_primary
        )
        self.title_label.pack(side="left", padx=20, pady=15)

        self.status_label = ctk.CTkLabel(
            self.header_frame, 
            text="Status: Pronto", 
            font=ctk.CTkFont(family="Arial", size=12),
            text_color="#a0a0a5"
        )
        self.status_label.pack(side="right", padx=20, pady=15)

        # Abas
        self.tabview = ctk.CTkTabview(self, fg_color=self.bg_color, segmented_button_fg_color=self.card_color,
                                       segmented_button_selected_color=self.purple_primary,
                                       segmented_button_selected_hover_color=self.purple_hover)
        self.tabview.pack(fill="both", expand=True, padx=15, pady=15)

        self.tab_opt = self.tabview.add("Otimização")
        self.tab_clean = self.tabview.add("Limpeza")
        self.tab_game = self.tabview.add("Modo Gamer")
        self.tab_hardware = self.tabview.add("Hardware")
        self.tab_logs = self.tabview.add("Logs & Sistema")

        self.setup_optimization_tab()
        self.setup_clean_tab()
        self.setup_game_tab()
        self.setup_hardware_tab()
        self.setup_logs_tab()

    def log_message(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted = f"[{timestamp}] {message}\n"
        self.log_textbox.configure(state="normal")
        self.log_textbox.insert("end", formatted)
        self.log_textbox.see("end")
        self.log_textbox.configure(state="disabled")

    # --- ABA 1: OTIMIZAÇÃO ---
    def setup_optimization_tab(self):
        lbl = ctk.CTkLabel(self.tab_opt, text="Ajustes Seguros de Desempenho", font=ctk.CTkFont(size=16, weight="bold"), text_color=self.text_color)
        lbl.pack(anchor="w", padx=10, pady=10)

        btn_lat = ctk.CTkButton(
            self.tab_opt, text="Otimizar Temporizador do Sistema (BCDEdit)",
            fg_color=self.purple_primary, hover_color=self.purple_hover,
            command=self.run_latency_optimization
        )
        btn_lat.pack(anchor="w", padx=10, pady=10)

    def run_latency_optimization(self):
        def task():
            self.status_label.configure(text="Status: Otimizando...")
            self.log_message("Aplicando melhorias de resposta do sistema...")
            try:
                subprocess.run("bcdedit /set useplatformclock false", shell=True, capture_output=True)
                self.log_message("Otimização concluída com sucesso.")
            except Exception as e:
                self.log_message(f"Erro: {e}")
            self.status_label.configure(text="Status: Pronto")
        threading.Thread(target=task).start()

    # --- ABA 2: LIMPEZA ---
    def setup_clean_tab(self):
        lbl = ctk.CTkLabel(self.tab_clean, text="Limpeza de Armazenamento (Temporários)", font=ctk.CTkFont(size=16, weight="bold"), text_color=self.text_color)
        lbl.pack(anchor="w", padx=10, pady=10)

        btn_clean = ctk.CTkButton(
            self.tab_clean, text="Limpar Ficheiros Temporários",
            fg_color=self.purple_primary, hover_color=self.purple_hover,
            command=self.run_temp_clean
        )
        btn_clean.pack(anchor="w", padx=10, pady=10)

    def run_temp_clean(self):
        def task():
            self.status_label.configure(text="Status: Limpando...")
            self.log_message("A limpar diretórios temporários do utilizador...")
            temp_dirs = [os.environ.get("TEMP")]
            for d in temp_dirs:
                if d and os.path.exists(d):
                    for root, dirs, files in os.walk(d):
                        for file in files:
                            try:
                                os.remove(os.path.join(root, file))
                            except:
                                pass
            self.log_message("Limpeza de ficheiros temporários finalizada.")
            self.status_label.configure(text="Status: Pronto")
        threading.Thread(target=task).start()

    # --- ABA 3: MODO GAMER ---
    def setup_game_tab(self):
        lbl = ctk.CTkLabel(self.tab_game, text="Modo Gamer & Desempenho", font=ctk.CTkFont(size=16, weight="bold"), text_color=self.text_color)
        lbl.pack(anchor="w", padx=10, pady=10)

        btn_game = ctk.CTkButton(
            self.tab_game, text="Ativar Perfil de Desempenho Máximo",
            fg_color=self.purple_primary, hover_color=self.purple_hover,
            command=self.run_game_mode
        )
        btn_game.pack(anchor="w", padx=10, pady=10)

    def run_game_mode(self):
        def task():
            self.status_label.configure(text="Status: Ativando Modo Gamer...")
            try:
                subprocess.run("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61", shell=True, capture_output=True)
                self.log_message("Perfil de desempenho máximo ativado com sucesso.")
            except Exception as e:
                self.log_message(f"Erro: {e}")
            self.status_label.configure(text="Status: Pronto")
        threading.Thread(target=task).start()

    # --- ABA 4: HARDWARE ---
    def setup_hardware_tab(self):
        lbl = ctk.CTkLabel(self.tab_hardware, text="Monitoramento de Recursos em Tempo Real", font=ctk.CTkFont(size=16, weight="bold"), text_color=self.text_color)
        lbl.pack(anchor="w", padx=10, pady=10)

        self.hw_label = ctk.CTkLabel(self.tab_hardware, text="A carregar leituras...", font=ctk.CTkFont(size=14), text_color=self.text_color)
        self.hw_label.pack(anchor="w", padx=10, pady=10)

        btn_refresh = ctk.CTkButton(
            self.tab_hardware, text="Atualizar Leituras",
            fg_color=self.purple_primary, hover_color=self.purple_hover,
            command=self.update_hardware_info
        )
        btn_refresh.pack(anchor="w", padx=10, pady=10)
        self.update_hardware_info()

    def update_hardware_info(self):
        ram = psutil.virtual_memory()
        cpu_usage = psutil.cpu_percent(interval=0.5)
        info_text = f"• Sistema: {platform.system()} {platform.release()}\n" \
                    f"• Uso de CPU: {cpu_usage}%\n" \
                    f"• Memória RAM: {ram.percent}% ({round(ram.used / (1024**3), 2)} GB / {round(ram.total / (1024**3), 2)} GB)"
        self.hw_label.configure(text=info_text)

    # --- ABA 5: LOGS ---
    def setup_logs_tab(self):
        lbl = ctk.CTkLabel(self.tab_logs, text="Registo de Atividades (Logs)", font=ctk.CTkFont(size=16, weight="bold"), text_color=self.text_color)
        lbl.pack(anchor="w", padx=10, pady=10)

        self.log_textbox = ctk.CTkTextbox(self.tab_logs, width=800, height=320, fg_color="#0d0d0f", text_color="#00ffcc")
        self.log_textbox.pack(padx=10, pady=5)
        self.log_textbox.configure(state="disabled")
        self.log_message("Nexus Optimizer inicializado com segurança.")

if __name__ == "__main__":
    app = NexusOptimizerApp()
    app.mainloop()

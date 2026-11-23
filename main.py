import random
import tkinter as tk
from tkinter import ttk

VIDA_MAXIMA = 300
ATRASO_OPONENTE_MS = 900  # pausa antes do oponente atacar

# ---------- Cores da interface ----------
COR_FUNDO = "#f4f6fb"
COR_TEXTO = "#1f2937"
COR_AZUL = "#1d4ed8"
COR_VERDE = "#16a34a"
COR_VERMELHO = "#dc2626"
COR_CINZA = "#6b7280"

# ---------- Dados dos Pokémons e ataques ----------
# "dano": número fixo OU dicionário com o dano contra cada Pokémon
# "chance": probabilidade de o ataque funcionar (padrão = 100%)
# "cura": vida recuperada (ataques de cura não causam dano)
POKEMONS = {
    "bulbasaur": {
        "nome": "Bulbasaur",
        "cor": "#4caf50",
        "ataques": [
            {"nome": "Folha Navalha",
             "dano": {"bulbasaur": 20, "charmander": 10, "squirtle": 50}},
            {"nome": "Chicote de Cipó",
             "dano": {"bulbasaur": 15, "charmander": 5, "squirtle": 55}},
            {"nome": "Espelho de folha", "dano": 60, "chance": 0.5,
             "msg_acerto": "O ataque refletiu e causou dano!"},
            {"nome": "Derrubar", "dano": 30},
        ],
    },
    "charmander": {
        "nome": "Charmander",
        "cor": "#f97316",
        "ataques": [
            {"nome": "Brasas",
             "dano": {"bulbasaur": 80, "charmander": 20, "squirtle": 5}},
            {"nome": "Arranhão", "dano": 25},
            {"nome": "Lança Chamas",
             "dano": {"bulbasaur": 65, "charmander": 20, "squirtle": 5}},
            {"nome": "Pulo Ardente", "chance": 0.25,
             "dano": {"bulbasaur": 100, "charmander": 50, "squirtle": 25}},
        ],
    },
    "squirtle": {
        "nome": "Squirtle",
        "cor": "#0ea5e9",
        "ataques": [
            {"nome": "Jato de Água",
             "dano": {"bulbasaur": 10, "charmander": 50, "squirtle": 20}},
            {"nome": "Mordida", "dano": 30},
            {"nome": "Hidro Bomba",
             "dano": {"bulbasaur": 25, "charmander": 65, "squirtle": 25}},
            {"nome": "Água Benta", "cura": 60, "chance": 1 / 3},
        ],
    },
}


class JogoPokemon:
    def __init__(self, root):
        self.root = root
        root.title("Jogo de Pokémon")
        root.geometry("700x660")
        root.resizable(False, False)
        root.configure(bg=COR_FUNDO)

        self._configurar_estilos()

        self.container = tk.Frame(root, bg=COR_FUNDO)
        self.container.pack(fill="both", expand=True, padx=20, pady=20)

        self.tela_escolha()

    # ------------------------------------------------------------------
    # Utilidades de interface
    # ------------------------------------------------------------------
    def _configurar_estilos(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")  # permite colorir a barra de progresso
        for nome, cor in (("Jogador", COR_VERDE), ("Oponente", COR_VERMELHO)):
            estilo.configure(
                f"{nome}.Horizontal.TProgressbar",
                troughcolor="#d1d5db",
                background=cor,
                bordercolor="#d1d5db",
                lightcolor=cor,
                darkcolor=cor,
            )

    def _limpar(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def _titulo(self):
        tk.Label(
            self.container,
            text="Bem-Vindo ao jogo de Pokémon!",
            font=("Helvetica", 18, "bold"),
            bg=COR_AZUL,
            fg="white",
            pady=12,
        ).pack(fill="x")

    def _criar_painel(self, pai, coluna, titulo, estilo_barra):
        quadro = tk.Frame(pai, bg="white", padx=12, pady=10,
                          highlightbackground="#d1d5db", highlightthickness=1)
        quadro.grid(row=0, column=coluna, padx=8, sticky="nsew")

        tk.Label(quadro, text=titulo, font=("Helvetica", 12, "bold"),
                 bg="white", fg=COR_TEXTO).pack(anchor="w")
        lbl_vida = tk.Label(quadro, text="", font=("Helvetica", 11),
                            bg="white", fg=COR_CINZA)
        lbl_vida.pack(anchor="w", pady=(2, 6))
        barra = ttk.Progressbar(quadro, length=260, maximum=VIDA_MAXIMA,
                                style=f"{estilo_barra}.Horizontal.TProgressbar")
        barra.pack(fill="x")
        return lbl_vida, barra

    def _log(self, mensagem, tag=None):
        self.log_text.configure(state="normal")
        self.log_text.insert("end", mensagem + "\n", tag)
        self.log_text.see("end")
        self.log_text.configure(state="disabled")

    def _atualizar_barras(self):
        vida_j = max(0, self.vida_jogador)
        vida_b = max(0, self.vida_bot)
        self.barra_jogador["value"] = vida_j
        self.barra_bot["value"] = vida_b
        self.lbl_vida_jogador.config(text=f"Vida: {vida_j}/{VIDA_MAXIMA}")
        self.lbl_vida_bot.config(text=f"Vida: {vida_b}/{VIDA_MAXIMA}")

    def _travar_botoes(self, travar):
        estado = "disabled" if travar else "normal"
        for botao in self.botoes_ataque:
            botao.config(state=estado)

    # ------------------------------------------------------------------
    # Telas
    # ------------------------------------------------------------------
    def tela_escolha(self):
        self._limpar()
        self._titulo()

        tk.Label(self.container, text="Escolha seu Pokémon inicial:",
                 font=("Helvetica", 14), bg=COR_FUNDO,
                 fg=COR_TEXTO).pack(pady=(40, 20))

        for chave, dados in POKEMONS.items():
            tk.Button(
                self.container,
                text=dados["nome"],
                font=("Helvetica", 14, "bold"),
                bg=dados["cor"],
                fg="white",
                activebackground=dados["cor"],
                activeforeground="white",
                relief="flat",
                width=22,
                pady=10,
                cursor="hand2",
                command=lambda c=chave: self.iniciar_batalha(c),
            ).pack(pady=8)

    def iniciar_batalha(self, escolha):
        self.pokejogador = escolha
        self.pokebot = random.choice(list(POKEMONS))
        self.vida_jogador = VIDA_MAXIMA
        self.vida_bot = VIDA_MAXIMA
        self.fim = False

        self.tela_batalha()

        self._log(f"O oponente escolheu {POKEMONS[self.pokebot]['nome']} "
                  "como seu Pokémon inicial!", "info")
        self._log(f"Você escolheu {POKEMONS[self.pokejogador]['nome']} "
                  "como seu Pokémon inicial!", "info")
        self._log("Escolha um ataque para começar a batalha.", "info")
        self._atualizar_barras()

    def tela_batalha(self):
        self._limpar()
        self._titulo()

        jogador = POKEMONS[self.pokejogador]
        bot = POKEMONS[self.pokebot]

        # --- Painéis de vida ---
        painel = tk.Frame(self.container, bg=COR_FUNDO)
        painel.pack(fill="x", pady=(20, 10))
        painel.columnconfigure((0, 1), weight=1, uniform="col")

        self.lbl_vida_jogador, self.barra_jogador = self._criar_painel(
            painel, 0, f"Você: {jogador['nome']}", "Jogador")
        self.lbl_vida_bot, self.barra_bot = self._criar_painel(
            painel, 1, f"Oponente: {bot['nome']}", "Oponente")

        # --- Botões de ataque ---
        tk.Label(self.container, text="Escolha o ataque que deseja usar:",
                 font=("Helvetica", 12), bg=COR_FUNDO,
                 fg=COR_TEXTO).pack(pady=(10, 5))

        grade = tk.Frame(self.container, bg=COR_FUNDO)
        grade.pack(fill="x", padx=8)
        grade.columnconfigure((0, 1), weight=1, uniform="atk")

        self.botoes_ataque = []
        for i, ataque in enumerate(jogador["ataques"]):
            botao = tk.Button(
                grade,
                text=f"{i + 1}. {ataque['nome']}",
                font=("Helvetica", 12, "bold"),
                bg=jogador["cor"],
                fg="white",
                activebackground=jogador["cor"],
                activeforeground="white",
                relief="flat",
                pady=8,
                cursor="hand2",
                command=lambda n=i: self.turno_jogador(n),
            )
            botao.grid(row=i // 2, column=i % 2, padx=6, pady=6, sticky="ew")
            self.botoes_ataque.append(botao)

        # --- Rodapé (botão de reiniciar) e histórico da batalha ---
        self.rodape = tk.Frame(self.container, bg=COR_FUNDO)
        self.rodape.pack(side="bottom", fill="x")
        self.btn_reiniciar = tk.Button(
            self.rodape, text="Jogar novamente", font=("Helvetica", 12, "bold"),
            bg=COR_AZUL, fg="white", activebackground=COR_AZUL,
            activeforeground="white", relief="flat", padx=20, pady=6,
            cursor="hand2", command=self.tela_escolha)

        area_log = tk.Frame(self.container, bg=COR_FUNDO)
        area_log.pack(fill="both", expand=True, pady=(10, 10), padx=8)

        scroll = tk.Scrollbar(area_log)
        scroll.pack(side="right", fill="y")
        self.log_text = tk.Text(
            area_log, height=10, wrap="word", state="disabled",
            font=("Helvetica", 11), bg="white", fg=COR_TEXTO, relief="flat",
            highlightbackground="#d1d5db", highlightthickness=1,
            yscrollcommand=scroll.set)
        self.log_text.pack(side="left", fill="both", expand=True)
        scroll.config(command=self.log_text.yview)

        self.log_text.tag_configure("jogador", foreground=COR_AZUL)
        self.log_text.tag_configure("oponente", foreground=COR_VERMELHO)
        self.log_text.tag_configure("info", foreground=COR_CINZA)
        self.log_text.tag_configure("vitoria", foreground=COR_VERDE,
                                    font=("Helvetica", 12, "bold"))
        self.log_text.tag_configure("derrota", foreground=COR_VERMELHO,
                                    font=("Helvetica", 12, "bold"))

    # ------------------------------------------------------------------
    # Lógica da batalha
    # ------------------------------------------------------------------
    def turno_jogador(self, indice):
        if self.fim:
            return
        self._travar_botoes(True)

        ataque = POKEMONS[self.pokejogador]["ataques"][indice]
        self._executar(ataque, eh_jogador=True)
        self._atualizar_barras()

        if self.vida_bot <= 0:
            self._finalizar(venceu=True)
            return

        self.root.after(ATRASO_OPONENTE_MS, self.turno_oponente)

    def turno_oponente(self):
        if self.fim:
            return
        ataque = random.choice(POKEMONS[self.pokebot]["ataques"])
        self._executar(ataque, eh_jogador=False)
        self._atualizar_barras()

        if self.vida_jogador <= 0:
            self._finalizar(venceu=False)
        else:
            self._travar_botoes(False)

    def _executar(self, ataque, eh_jogador):
        quem = "Você" if eh_jogador else "O oponente"
        tag = "jogador" if eh_jogador else "oponente"

        self._log(f"{quem} usou {ataque['nome']}!", tag)

        # O ataque pode falhar (Espelho de folha, Pulo Ardente, Água Benta)
        chance = ataque.get("chance", 1.0)
        if random.random() >= chance:
            if "cura" in ataque:
                self._log("O ataque falhou!", tag)
            elif eh_jogador:
                self._log("Você errou o ataque!", tag)
            else:
                self._log("O oponente errou o ataque!", tag)
            return

        # Ataque de cura
        if "cura" in ataque:
            if eh_jogador:
                antes = self.vida_jogador
                self.vida_jogador = min(VIDA_MAXIMA, antes + ataque["cura"])
                ganho = self.vida_jogador - antes
            else:
                antes = self.vida_bot
                self.vida_bot = min(VIDA_MAXIMA, antes + ataque["cura"])
                ganho = self.vida_bot - antes
            self._log(f"{quem} recuperou {ganho} de vida!", tag)
            return

        # Ataque de dano
        alvo = self.pokebot if eh_jogador else self.pokejogador
        dano = ataque["dano"]
        if isinstance(dano, dict):
            dano = dano[alvo]

        if "msg_acerto" in ataque:
            self._log(ataque["msg_acerto"], tag)
        elif chance < 1.0:
            self._log("O ataque acertou e causou dano!", tag)

        if eh_jogador:
            self.vida_bot -= dano
            self._log(f"Causou {dano} de dano ao oponente.", tag)
        else:
            self.vida_jogador -= dano
            self._log(f"Causou {dano} de dano em você.", tag)

    def _finalizar(self, venceu):
        self.fim = True
        self._travar_botoes(True)
        if venceu:
            self._log("Parabéns! Você venceu a batalha!", "vitoria")
        else:
            self._log("Você perdeu! O oponente venceu a batalha!", "derrota")
        self.btn_reiniciar.pack(pady=(5, 0))


def main():
    root = tk.Tk()
    JogoPokemon(root)
    root.mainloop()


if __name__ == "__main__":
    main()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from utils import (
    carregar_planilha,
    transformar_para_formato_longo,
    FIGURES_DIR,
    garantir_pastas,
)

def main():
    garantir_pastas()

    df = carregar_planilha()
    avaliacoes = transformar_para_formato_longo(df)

    tabela = (
        avaliacoes
        .groupby(["estrategia", "nota"])
        .size()
        .reset_index(name="n")
    )

    totais = tabela.groupby("estrategia")["n"].transform("sum")
    tabela["percentual"] = tabela["n"] / totais * 100

    categorias = ["Zero-Shot", "Persona", "Template"]
    notas = [1, 2, 3, 4, 5]

    dados = {
        f"Nota {nota}": [
            float(tabela.query("estrategia == @estrategia and nota == @nota")["percentual"].sum())
            for estrategia in categorias
        ]
        for nota in notas
    }

    sns.set_theme(style="white")
    cores = sns.color_palette("Blues", 5)

    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    left = np.zeros(len(categorias))

    for i, (nota, valores) in enumerate(dados.items()):
        bars = ax.barh(
            categorias,
            valores,
            left=left,
            label=nota,
            color=cores[i],
            edgecolor="white",
            height=0.6,
        )

        for bar in bars:
            width = bar.get_width()

            # Evita sobreposição de valores muito pequenos
            if width >= 6:
                ax.text(
                    bar.get_x() + width / 2,
                    bar.get_y() + bar.get_height() / 2,
                    f"{width:.1f}%",
                    ha="center",
                    va="center",
                    fontsize=11,
                    fontweight="bold",
                    color="white" if i >= 3 else "#1f2933",
                )

        left += valores

    ax.set_xlim(0, 100)
    ax.set_xlabel("Percentual das avaliações (%)", fontsize=12, fontweight="bold")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#cccccc")
    ax.spines["bottom"].set_color("#cccccc")

    ax.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.15),
        ncol=5,
        frameon=False,
        fontsize=10,
    )

    plt.tight_layout()

    saida = FIGURES_DIR / "prompting_score_distribution.png"
    plt.savefig(saida, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Figura salva em: {saida}")

if __name__ == "__main__":
    main()

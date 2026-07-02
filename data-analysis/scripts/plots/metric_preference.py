import matplotlib.pyplot as plt
import seaborn as sns

from utils import carregar_planilha, extrair_preferencias, FIGURES_DIR, garantir_pastas

def main():
    garantir_pastas()

    df = carregar_planilha()
    preferencias = extrair_preferencias(df)

    categorias = ["Zero-Shot", "Persona", "Template"]
    tabela = (
        preferencias
        .groupby(["metrica", "estrategia"])
        .size()
        .reset_index(name="n")
    )

    total_por_metrica = tabela.groupby("metrica")["n"].transform("sum")
    tabela["percentual"] = tabela["n"] / total_por_metrica * 100

    sns.set_theme(style="white")
    fig, ax = plt.subplots(figsize=(9, 4.8), dpi=300)

    largura = 0.25
    metricas = sorted(preferencias["metrica"].unique(), key=lambda x: int(x.split()[-1]))
    x = range(len(metricas))

    for i, estrategia in enumerate(categorias):
        valores = []
        for metrica in metricas:
            valor = tabela.query("metrica == @metrica and estrategia == @estrategia")["percentual"].sum()
            valores.append(valor)

        posicoes = [v + (i - 1) * largura for v in x]
        barras = ax.bar(posicoes, valores, width=largura, label=estrategia)

        for barra, valor in zip(barras, valores):
            if valor >= 10:
                ax.text(
                    barra.get_x() + barra.get_width() / 2,
                    barra.get_height() + 1,
                    f"{valor:.1f}%",
                    ha="center",
                    va="bottom",
                    fontsize=8,
                )

    ax.set_xticks(list(x))
    ax.set_xticklabels(metricas, fontsize=9)
    ax.set_ylabel("Percentual de escolhas (%)", fontsize=10)
    ax.set_ylim(0, 100)
    ax.grid(axis="y", linewidth=0.5, alpha=0.4)
    ax.set_axisbelow(True)

    ax.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.14),
        ncol=3,
        frameon=False,
        fontsize=9,
    )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    saida = FIGURES_DIR / "preference_by_metric.png"
    plt.savefig(saida, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Figura salva em: {saida}")

if __name__ == "__main__":
    main()

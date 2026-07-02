import matplotlib.pyplot as plt
import seaborn as sns

from utils import carregar_planilha, FIGURES_DIR, garantir_pastas

def main():
    garantir_pastas()
    df = carregar_planilha()

    coluna = "Qual sua experiência em testes de  desempenho?"
    if coluna not in df.columns:
        raise ValueError("Coluna de experiência em testes de desempenho não encontrada.")

    ordem = ["Nenhuma", "Básica", "Intermediária", "Avançada"]
    contagem = df[coluna].value_counts().reindex(ordem, fill_value=0)

    sns.set_theme(style="white")
    fig, ax = plt.subplots(figsize=(7, 3.5), dpi=300)

    barras = ax.barh(contagem.index, contagem.values)

    for barra, valor in zip(barras, contagem.values):
        percentual = valor / contagem.sum() * 100
        ax.text(
            barra.get_width() + 0.1,
            barra.get_y() + barra.get_height() / 2,
            f"{valor} ({percentual:.1f}%)",
            va="center",
            fontsize=9,
        )

    ax.set_xlabel("Número de participantes", fontsize=10)
    ax.set_xlim(0, max(contagem.values) + 2)
    ax.grid(axis="x", linewidth=0.5, alpha=0.4)
    ax.set_axisbelow(True)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    saida = FIGURES_DIR / "performance_testing_experience_profile.png"
    plt.savefig(saida, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Figura salva em: {saida}")

if __name__ == "__main__":
    main()

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "plots"))
sys.path.append(str(Path(__file__).resolve().parents[0]))

from friedman import calcular_friedman
from utils import TABLES_DIR, garantir_pastas, formatar_decimal_pt, formatar_pvalor

def main():
    garantir_pastas()
    resultados = calcular_friedman()

    linhas = []
    linhas.append(r"\begin{table}[ht]")
    linhas.append(r"\centering")
    linhas.append(r"\caption{Resultados do teste de Friedman para comparação entre as estratégias de \textit{prompting}.}")
    linhas.append(r"\label{tab:friedman}")
    linhas.append(r"\small")
    linhas.append(r"\begin{tabular}{lcc}")
    linhas.append(r"\hline")
    linhas.append(r"\textbf{Critério} & $\boldsymbol{\chi^2}$ & \textbf{$p$-valor} \\")
    linhas.append(r"\hline")

    for _, linha in resultados.iterrows():
        criterio = linha["criterio"]
        chi2 = formatar_decimal_pt(linha["chi2"], 2)
        p = linha["p_valor"]
        ptxt = formatar_pvalor(p)

        if p < 0.05:
            ptxt = r"\textbf{" + ptxt + "}"

        linhas.append(f"{criterio} & {chi2} & {ptxt} \\\\")

    linhas.append(r"\hline")
    linhas.append(r"\end{tabular}")
    linhas.append(r"\end{table}")

    latex = "\n".join(linhas)

    saida = TABLES_DIR / "friedman_table.tex"
    saida.write_text(latex, encoding="utf-8")

    print(latex)
    print(f"\nTabela salva em: {saida}")

if __name__ == "__main__":
    main()

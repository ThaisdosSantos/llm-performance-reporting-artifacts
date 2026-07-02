import sys
from pathlib import Path
from itertools import combinations

sys.path.append(str(Path(__file__).resolve().parents[1] / "plots"))

import pandas as pd
from scipy.stats import wilcoxon

from utils import (
    carregar_planilha,
    transformar_para_formato_longo,
    CRITERIOS,
    STATS_DIR,
    garantir_pastas,
)

def main():
    garantir_pastas()

    df = carregar_planilha()
    avaliacoes = transformar_para_formato_longo(df)

    estrategias = ["Zero-Shot", "Persona", "Template"]
    resultados = []

    for criterio in CRITERIOS:
        dados = avaliacoes[avaliacoes["criterio"] == criterio]

        matriz = (
            dados
            .pivot_table(
                index=["participante", "metrica"],
                columns="estrategia",
                values="nota",
                aggfunc="first",
            )
            .dropna()
        )

        for e1, e2 in combinations(estrategias, 2):
            stat, p = wilcoxon(matriz[e1], matriz[e2])

            resultados.append({
                "criterio": criterio,
                "comparacao": f"{e1} vs {e2}",
                "statistics": stat,
                "p_valor": p,
            })

    resultados = pd.DataFrame(resultados)
    saida = STATS_DIR / "paired_wilcoxon.csv"
    resultados.to_csv(saida, index=False, encoding="utf-8-sig")

    print(resultados)
    print(f"Resultados salvos em: {saida}")

if __name__ == "__main__":
    main()

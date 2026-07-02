import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "plots"))

import pandas as pd
from scipy.stats import friedmanchisquare

from utils import (
    carregar_planilha,
    transformar_para_formato_longo,
    CRITERIOS,
    STATS_DIR,
    garantir_pastas,
)

def calcular_friedman():
    df = carregar_planilha()
    avaliacoes = transformar_para_formato_longo(df)

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

        chi2, p = friedmanchisquare(
            matriz["Zero-Shot"],
            matriz["Persona"],
            matriz["Template"],
        )

        resultados.append({
            "criterio": criterio,
            "chi2": chi2,
            "p_valor": p,
            "significativo_005": p < 0.05,
            "n_blocos": len(matriz),
        })

    return pd.DataFrame(resultados)

def main():
    garantir_pastas()
    resultados = calcular_friedman()

    saida = STATS_DIR / "friedman.csv"
    resultados.to_csv(saida, index=False, encoding="utf-8-sig")

    print(resultados)
    print(f"Resultados salvos em: {saida}")

if __name__ == "__main__":
    main()

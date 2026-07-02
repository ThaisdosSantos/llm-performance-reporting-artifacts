import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "plots"))

import pandas as pd
import scikit_posthocs as sp

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

    writer_path = STATS_DIR / "nemenyi.xlsx"

    with pd.ExcelWriter(writer_path, engine="openpyxl") as writer:
        for criterio in CRITERIOS:
            dados = avaliacoes[avaliacoes["criterio"] == criterio]

            matriz = dados.pivot_table(
                index=["participante", "metrica"],
                columns="estrategia",
                values="nota",
                aggfunc="first",
            ).dropna()

            matriz = matriz[["Zero-Shot", "Persona", "Template"]]
            matriz = matriz.reset_index(drop=True)

            resultado = sp.posthoc_nemenyi_friedman(matriz.values)

            resultado.index = ["Zero-Shot", "Persona", "Template"]
            resultado.columns = ["Zero-Shot", "Persona", "Template"]

            nome_aba = criterio[:31]
            resultado.to_excel(writer, sheet_name=nome_aba)

    print(f"Pós-teste de Nemenyi salvo em: {writer_path}")


if __name__ == "__main__":
    main()

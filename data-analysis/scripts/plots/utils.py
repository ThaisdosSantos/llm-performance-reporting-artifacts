from pathlib import Path
import re
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RAW_XLSX = ROOT / "data" / "raw" / "responses.xlsx"
PROCESSED_DIR = ROOT / "data" / "processed"
FIGURES_DIR = ROOT / "outputs" / "figures"
TABLES_DIR = ROOT / "outputs" / "tables"
STATS_DIR = ROOT / "outputs" / "statistics"

ESTRATEGIAS = {
    "A": "Zero-Shot",
    "B": "Persona",
    "C": "Template",
}

CRITERIOS = [
    "Relevância das Informações",
    "Compreensibilidade",
    "Capacidade Explicativa",
    "Utilidade para Tomada de Decisão",
    "Adequação ao Contexto Executivo",
]

def garantir_pastas():
    for pasta in [PROCESSED_DIR, FIGURES_DIR, TABLES_DIR, STATS_DIR]:
        pasta.mkdir(parents=True, exist_ok=True)

def carregar_planilha(caminho=RAW_XLSX):
    return pd.read_excel(caminho)

def _normalizar_nome_coluna(coluna: str) -> str:
    coluna = str(coluna).replace("_x000a_", " ")
    coluna = re.sub(r"\s+", " ", coluna).strip()
    return coluna

def _extrair_alternativa(coluna: str):
    m = re.search(r"\[([ABC])\]", str(coluna))
    return m.group(1) if m else None

def identificar_blocos(df):
    """
    A planilha possui 7 blocos de avaliação.
    Cada bloco contém:
      - 15 colunas de notas: 5 critérios x 3 alternativas [A], [B], [C]
      - 1 coluna de preferência final
    As primeiras 7 colunas são de caracterização dos participantes.
    """
    inicio = 7
    tamanho_bloco = 16
    blocos = []

    for i in range(7):
        ini = inicio + i * tamanho_bloco
        fim = ini + tamanho_bloco
        cols = list(df.columns[ini:fim])

        if len(cols) < tamanho_bloco:
            continue

        rating_cols = cols[:15]
        pref_col = cols[15]

        blocos.append({
            "metrica": f"Métrica {i + 1}",
            "rating_cols": rating_cols,
            "pref_col": pref_col,
        })

    return blocos

def transformar_para_formato_longo(df):
    """
    Retorna um DataFrame longo com uma linha por:
    participante x métrica x critério x estratégia.
    """
    registros = []
    blocos = identificar_blocos(df)

    for idx, linha in df.iterrows():
        participante = idx + 1

        for b_idx, bloco in enumerate(blocos, start=1):
            rating_cols = bloco["rating_cols"]

            # Ordem esperada: para cada critério, alternativas A, B, C
            for criterio_idx, criterio in enumerate(CRITERIOS):
                for alt_idx, alternativa in enumerate(["A", "B", "C"]):
                    pos = criterio_idx * 3 + alt_idx
                    coluna = rating_cols[pos]
                    valor = linha[coluna]

                    if pd.notna(valor):
                        registros.append({
                            "participante": participante,
                            "metrica": f"Métrica {b_idx}",
                            "criterio": criterio,
                            "alternativa": alternativa,
                            "estrategia": ESTRATEGIAS[alternativa],
                            "nota": int(valor),
                        })

    return pd.DataFrame(registros)

def extrair_preferencias(df):
    registros = []
    blocos = identificar_blocos(df)

    mapa_preferencia = {
        "Interpretação A": "Zero-Shot",
        "Interpretação B": "Persona",
        "Interpretação C": "Template",
    }

    for idx, linha in df.iterrows():
        participante = idx + 1

        for b_idx, bloco in enumerate(blocos, start=1):
            valor = linha[bloco["pref_col"]]
            if pd.notna(valor):
                registros.append({
                    "participante": participante,
                    "metrica": f"Métrica {b_idx}",
                    "preferencia_original": valor,
                    "estrategia": mapa_preferencia.get(str(valor).strip(), str(valor).strip()),
                })

    return pd.DataFrame(registros)

def salvar_dados_processados():
    garantir_pastas()
    df = carregar_planilha()
    avaliacoes = transformar_para_formato_longo(df)
    preferencias = extrair_preferencias(df)

    avaliacoes.to_csv(PROCESSED_DIR / "ratings_long.csv", index=False, encoding="utf-8-sig")
    preferencias.to_csv(PROCESSED_DIR / "preferences_long.csv", index=False, encoding="utf-8-sig")

    return avaliacoes, preferencias

def formatar_decimal_pt(valor, casas=2):
    return f"{valor:.{casas}f}".replace(".", ",")

def formatar_pvalor(p):
    if p < 0.001:
        return "<0,001"
    return f"{p:.3f}".replace(".", ",")

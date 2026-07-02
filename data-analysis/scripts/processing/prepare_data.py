import sys
from pathlib import Path

# Permite importar utils de scripts/plots
sys.path.append(str(Path(__file__).resolve().parents[1] / "plots"))

from utils import salvar_dados_processados

def main():
    avaliacoes, preferencias = salvar_dados_processados()
    print("Dados processados gerados com sucesso.")
    print(f"Avaliações: {len(avaliacoes)} linhas")
    print(f"Preferências: {len(preferencias)} linhas")

if __name__ == "__main__":
    main()

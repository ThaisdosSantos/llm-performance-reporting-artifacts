# LLM Performance Reporting Artifacts

This repository contains the experimental artifacts and data-analysis code used in the study on the use of GPT-5.5 to generate executive interpretations of software performance metrics using different prompting strategies.

The repository is intended to support transparency, reproducibility, and replication of the experiment described in the paper.

## Repository Structure

```text
llm-performance-reporting-artifacts/
├── experimental-artifacts/
│   ├── context/
│   ├── images/
│   ├── prompts/
│   ├── survey/
│   └── README.md
│
├── data-analysis/
│   ├── data/
│   ├── outputs/
│   ├── scripts/
│   ├── README.md
│   └── requirements.txt
│
└── README.md
```

## Experimental Artifacts

The `experimental-artifacts/` directory contains the materials used in the experiment, including:

- the context provided to the language model;
- the prompts used for the Zero-Shot, Persona, and Template strategies;
- the Apache JMeter images used as input for the interpretation tasks;
- the survey instrument;
- the anonymized survey responses.

More details are available in `experimental-artifacts/README.md`.

## Data Analysis

The `data-analysis/` directory contains the code and files used to reproduce the analyses reported in the paper, including:

- data preparation and transformation scripts;
- statistical analysis scripts;
- scripts for generating figures;
- processed datasets;
- output tables, figures, and statistical results.

More details are available in `data-analysis/README.md`.

## Requirements

The analysis scripts were developed in Python. The dependencies are listed in:

```text
data-analysis/requirements.txt
```

To install them, run:

```bash
pip install -r data-analysis/requirements.txt
```

## Paper

This repository accompanies the paper:

> **Da Métrica Técnica à Decisão Gerencial: Avaliação de Estratégias de Prompting para Geração de Relatórios Executivos Baseados em Testes de Desempenho de Software.**

## License

The materials in this repository are made available under the **CC BY 4.0** license, unless otherwise stated.

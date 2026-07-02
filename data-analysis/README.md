# Data Analysis

This directory contains the Python code and data files used to reproduce the analyses presented in the paper on prompting strategies for generating executive interpretations of software performance metrics.

## Structure

```text
data-analysis/
├── data/
│   ├── raw/
│   │   └── responses.xlsx
│   └── processed/
│       ├── ratings_long.csv
│       └── preferences_long.csv
│
├── outputs/
│   ├── figures/
│   ├── tables/
│   └── statistics/
│
├── scripts/
│   ├── plots/
│   │   ├── score_distribution.py
│   │   ├── participant_profile.py
│   │   ├── metric_preference.py
│   │   └── utils.py
│   │
│   ├── statistics/
│   │   ├── friedman.py
│   │   ├── nemenyi.py
│   │   ├── wilcoxon.py
│   │   └── generate_latex_table.py
│   │
│   └── processing/
│       └── prepare_data.py
│
├── requirements.txt
└── README.md
```

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Data Preparation

Run:

```bash
python scripts/processing/prepare_data.py
```

Outputs:

```text
data/processed/ratings_long.csv
data/processed/preferences_long.csv
```

## Figures

Generate the score distribution figure:

```bash
python scripts/plots/score_distribution.py
```

Output:

```text
outputs/figures/prompting_score_distribution.png
```

Generate the participant profile figure:

```bash
python scripts/plots/participant_profile.py
```

Output:

```text
outputs/figures/performance_testing_experience_profile.png
```

Generate the preference-by-metric figure:

```bash
python scripts/plots/metric_preference.py
```

Output:

```text
outputs/figures/preference_by_metric.png
```

## Statistical Analyses

Run the Friedman test:

```bash
python scripts/statistics/friedman.py
```

Output:

```text
outputs/statistics/friedman.csv
```

Generate the LaTeX table for the Friedman test:

```bash
python scripts/statistics/generate_latex_table.py
```

Output:

```text
outputs/tables/friedman_table.tex
```

Run the Nemenyi post-hoc test:

```bash
python scripts/statistics/nemenyi.py
```

Output:

```text
outputs/statistics/nemenyi.xlsx
```

Run the paired Wilcoxon tests:

```bash
python scripts/statistics/wilcoxon.py
```

Output:

```text
outputs/statistics/paired_wilcoxon.csv
```

## Interpretation Mapping

The project uses the following mapping:

- Interpretation A: Zero-Shot
- Interpretation B: Persona
- Interpretation C: Template

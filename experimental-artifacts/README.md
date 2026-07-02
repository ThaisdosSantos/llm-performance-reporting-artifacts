# Experimental Artifacts

This directory contains the experimental materials used in the study on the use of GPT-5.5 to generate executive interpretations of software performance metrics through different prompting strategies.

The goal of the experiment was to evaluate how prompt construction strategies influence the ability of a language model to transform technical performance metrics into interpretations that are understandable to managers and stakeholders without specialized knowledge in performance engineering.

## Evaluated Model

The study used:

- Model: GPT-5.5
- Platform: ChatGPT
- Access type: Free account
- Configuration: Default platform settings
- Execution period: June 2026

## Evaluated Prompting Strategies

Three prompting strategies were evaluated:

### 1. Zero-Shot

The model receives only the task instruction and the input data, without examples.

### 2. Persona Prompting

The model receives an explicit role definition before performing the task.

Example:

> "You are an executive analyst specialized in translating technical metrics for managers."

### 3. Template Prompting

The model receives a predefined response structure.

Example:

> Context → Interpretation → Business impact.

## Input Data

Each execution of the experiment received three input components:

1. the context of the evaluated system;
2. the name of the performance metric;
3. an image containing the performance results.

The full experimental context is available at:

```text
context/context.txt
```

The images used as input are available in the `images/` directory.

## Experimental Procedure

For each selected metric, the procedure consisted of:

1. applying the three defined prompts;
2. generating executive interpretations using the model;
3. collecting the generated outputs;
4. anonymizing the alternatives;
5. applying a survey;
6. evaluating the predefined criteria.

## Evaluation Criteria

The interpretations were evaluated using a 1–5 Likert scale according to the following criteria:

- information relevance;
- comprehensibility;
- explanatory capacity;
- usefulness for decision-making;
- adequacy to the executive context.

## Directory Structure

```text
experimental-artifacts/
├── README.md
├── context/
│   └── context.txt
├── prompts/
│   ├── zero_shot.txt
│   ├── role_persona.txt
│   └── template_pattern.txt
├── images/
│   ├── throughput.png
│   ├── apdex.png
│   ├── cpu_memory.png
│   └── error_rate_p95_average_response_time.png
└── survey/
    ├── survey.pdf
    └── responses.csv
```

## Image Organization

Some images were reused across metrics when multiple indicators were present in the same Apache JMeter report export.

| Image | Metrics used |
|---|---|
| `throughput.png` | Throughput |
| `apdex.png` | Apdex |
| `cpu_memory.png` | CPU usage, RAM usage |
| `error_rate_p95_average_response_time.png` | Error rate, P95 percentile, average response time |

Thus, the number of evaluated metrics is greater than the number of images because some metrics were interpreted from the same visual artifact.

## Reproducibility

The prompts and materials available in this directory correspond to the versions used during the execution of the experiment described in the paper.

## License

This material is made available under the **CC BY 4.0** license.

https://creativecommons.org/licenses/by/4.0/

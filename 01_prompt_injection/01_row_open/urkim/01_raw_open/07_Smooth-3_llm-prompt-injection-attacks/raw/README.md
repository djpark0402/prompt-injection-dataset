---
language: en
license: apache-2.0
task_categories:
- text-classification
- multi-label-classification
tags:
- prompt-injection
- llm-security
- jailbreak
- ai-safety
---

# Prompt Injection Mechanisms Dataset

## Overview

```
A 55,000-sample multi-label dataset for prompt injection detection in large language models.
```

## Labels

```
- BENIGN
- JAILBREAK
- INSTRUCTION_OVERRIDE
- ROLE_HIJACK
- DATA_EXFILTRATION
```

## Format

```
The dataset is provided in Apache Parquet format with train/validation splits.
```

## Construction

```
The dataset was created by merging multiple public prompt-injection datasets and
re-annotating them using a deterministic rule-based taxonomy to identify attack mechanisms.
```

## Sources

```
- qualifire/prompt-injections-benchmark
- jayavibhav/prompt-injection-safety

Original datasets are not redistributed.
```

## Intended Use

```
Research on LLM security, prompt injection detection, and AI safety.
```

## Limitations

```
Labels are heuristic-based and may contain noise.
```

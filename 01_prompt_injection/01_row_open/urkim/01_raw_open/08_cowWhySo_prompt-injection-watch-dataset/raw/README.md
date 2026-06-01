---
pretty_name: Prompt Injection Watch Dataset
language:
- en
license: apache-2.0
task_categories:
- text-classification
task_ids:
- text-classification
size_categories:
- 10K<n<100K
---

# Prompt Injection Watch Dataset

Normalized prompt-injection watch dataset built from Hugging Face source datasets.

## Why a separate detector?
This dataset is intended for an **auxiliary watch model** that alerts on prompt injection.
It should remain separate from the primary command-permission classifier because the text distribution is different.

## Normalized columns
- `text`
- `label` (`0` benign, `1` malicious)
- `attack_family`
- `source_dataset`
- `source_detail`
- `severity`
- `context`
- `user_intent`
- `language`
- `metadata_json`

## Included source datasets
- malmasabi
- neuralchemy
- shieldlm

## Recommended use
- alert / watch signal in front of an LLM or tool bridge
- review queue trigger
- secondary risk feature for policy gating

## Caveats
- sources have different collection methods and label semantics
- some datasets are general chat injection, others are indirect or repo-oriented
- threshold tuning should be done on your real application traffic

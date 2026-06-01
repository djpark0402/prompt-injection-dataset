---
language:
- en
license: mit
task_categories:
- text-generation
- text-classification
- text2text-generation
tags:
- prompt-injection
- llm-security
- jailbreak
- adversarial-prompts
- nepi
- red-teaming
- ai-safety
size_categories:
- 1K<n<10K
---

# NEPI: Narrative-Embedded Prompt Injection Dataset (Sanitized)

## Dataset Summary
This dataset contains **4,000 sanitized prompts** designed for research on **prompt injection vulnerabilities in Large Language Models (LLMs)**.  
It introduces and supports evaluation of a novel attack class called **Narrative-Embedded Prompt Injection (NEPI)**, where adversarial intent is embedded inside coherent fictional narratives, dialogues, or persona-driven roleplay prompts.

Unlike traditional jailbreak prompts that explicitly override system instructions, NEPI prompts exploit the model’s tendency to maintain **narrative coherence** and follow implicit role-based context.

This dataset is intended for **academic research, benchmarking, and defensive model training**.

---

## Motivation
Prompt injection remains a major unresolved challenge for instruction-tuned LLMs. Existing defenses (keyword filters, boundary enforcement, and prompt sanitization) often fail against narrative-based attacks, because malicious intent is not presented as explicit commands but instead as part of a creative narrative flow.

This dataset was created as part of the research project:

**"Narrative-Embedded Prompt Injection in Large Language Models: Attack Characterization and Defense Strategies"**

---

## Dataset Composition
The dataset contains a balanced mix of benign prompts, traditional jailbreak attacks, and NEPI attack variants.

Total samples: **4000**

| Category | Attack Family | Label | Count |
|---------|--------------|-------|-------|
| Benign QA | Benign | Safe | 250 |
| Benign Creative Writing | Benign | Safe | 250 |
| Traditional Jailbreaks | Traditional | Malicious | 300+ |
| Instruction Override | Traditional | Malicious | 250+ |
| Delimiter Injection | Traditional | Malicious | 250+ |
| Role-based NEPI | NEPI | Malicious | 700+ |
| Dialogue-based NEPI | NEPI | Malicious | 700+ |
| Monologue-based NEPI | NEPI | Malicious | 600+ |
| Mixed-Intent NEPI | NEPI | Malicious | 500+ |
| Ambiguous Narrative Prompts | NEPI | Suspicious | 200 |

---

## Labels
Prompts are annotated into **three categories**:

- **Safe**: benign prompts with no malicious intent.
- **Suspicious**: ambiguous narrative prompts that may contain hidden intent or role manipulation but do not explicitly enforce adversarial behavior.
- **Malicious**: prompt injection attempts designed to manipulate model behavior (traditional jailbreaks or NEPI variants).

---

## Dataset Features
Each sample contains the following fields:

- `id`: unique identifier for the prompt.
- `prompt`: the sanitized prompt text.
- `label`: one of `{Safe, Suspicious, Malicious}`.
- `attack_family`: one of `{Benign, Traditional, NEPI}`.
- `attack_type`: specific category (e.g., `role_based`, `dialogue_based`, `traditional_jailbreak`).
- `target_goal`: intended adversarial objective category.
- `source`: dataset source (`synthetic_template`).

---

## Sanitization and Responsible Disclosure
This dataset is **sanitized for public release**.

The dataset preserves the **structure and semantics** of narrative prompt injection attacks but replaces explicit harmful or operational payloads with neutral placeholders such as:

- `[SENSITIVE_INFO]`
- `[FINANCIAL_INFO]`
- `[REDACTED_OBJECT]`

This ensures the dataset can be safely used for defense research, benchmarking, and classifier training without enabling real-world misuse.

---

## Intended Uses
### Recommended Uses
- Benchmarking LLM prompt injection robustness
- Training and evaluating prompt-injection classifiers
- Studying narrative-based jailbreak vulnerabilities
- Red-teaming research under controlled settings
- Defense pipeline evaluation (input filtering + output validation)

### Not Recommended Uses
- Deploying prompts as-is in real systems
- Attempting to bypass safety systems in production environments

---

## Citation
If you use this dataset in your research, please cite:

```bibtex
@article{pawar2026nepi,
  title={Narrative-Embedded Prompt Injection in Large Language Models: Attack Characterization and Defense Strategies},
  author={Pawar, Vaibhav and Urvashi},
  journal={Under Review},
  year={2026}
}
License
This dataset is released under the MIT License.

Authors
Vaibhav Pawar, Dr B R Ambedkar NIT Jalandhar

Dr Urvashi, Dr B R Ambedkar NIT Jalandhar

Links
Paper Code Repository (GitHub): https://github.com/Vaibhav-GOAT/NEPI-Attack-Defense

Contact
For questions or collaborations:

📧 vaibhavpp.is.24@nitj.ac.in
📧 vaibhavpitambarpawar69@gmail.com
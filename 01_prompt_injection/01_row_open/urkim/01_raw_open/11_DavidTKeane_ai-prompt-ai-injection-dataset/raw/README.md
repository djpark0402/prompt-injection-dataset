---
language:
  - en
  - fr
  - es
  - zh
  - ja
  - de
license: mit
tags:
  - ai-safety
  - prompt-injection
  - jailbreak
  - cybersecurity
  - red-teaming
  - llm-security
  - adversarial
  - small-language-models
  - identity-anchoring
  - moltbook
pretty_name: AI Prompt AI Injection Dataset
size_categories:
  - n<1K
task_categories:
  - text-classification
dataset_info:
  description: "122 prompt injection test cases across 11 categories. Combines official AI safety benchmarks (AdvBench, JailbreakBench, MultiJail, DAN) with real-world AI-to-AI injection captures from the Moltbook platform (Feb 2026). Includes model-agnostic test runner, HuggingFace model downloader, and one-command setup script."
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
---

# AI Prompt Injection Test Suite

**122 tests across 11 categories — designed to evaluate AI model resistance to prompt injection attacks**

Built as part of: *CyberRanger V42-Gold — Identity-Anchored Jailbreak-Resistant SLM*
David Keane (x24228257) — NCI MSc Cybersecurity 2026
Reference: Greshake et al. (2023), Zou et al. (2023), Wei et al. (2023)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DavidTKeane/ai-prompt-ai-injection-dataset/blob/main/cyberranger_test_suite.ipynb)
[![HuggingFace Notebook](https://img.shields.io/badge/🤗%20Notebook-cyberranger__test__suite-blue)](https://huggingface.co/datasets/DavidTKeane/ai-prompt-ai-injection-dataset/blob/main/cyberranger_test_suite.ipynb)

> **Run the full 122-test battery in Google Colab** — works with CyberRanger V42-Gold (Ollama or GGUF) or any model you choose. Saves results, emails them, and runs the full 4,209 Moltbook scale test as a bonus.

---

> ### 📖 Read the Full Journey
> 
> **[From RangerBot to CyberRanger V42 Gold — The Full Story](https://davidtkeane.github.io/posts/from-rangerbot-to-cyberranger-v42-the-full-story/)**
> 
> The complete story: dentist chatbot → Moltbook discovery → 4,209 real injections → V42-gold (100% block rate). Psychology, engineering, and 42 versions of persistence.

---

## What Is This?

This repository contains a complete test suite for evaluating how well an AI model resists **prompt injection attacks** — attempts by malicious inputs to override the model's identity, values, or mission.

The tests come from three sources:
1. **Real-world captures** — actual AI-to-AI injection attempts collected from the [Moltbook platform](https://huggingface.co/datasets/DavidTKeane/moltbook-ai-injection-dataset) (4,209 injections found in 47,735 posts, Feb 2026)
2. **Standard benchmarks** — AdvBench (Zou et al. 2023), JailbreakBench, MultiJail
3. **Custom thesis battery** — the RB-001–RB-010 battery used across V30–V42 version comparisons

You can run these tests against **any Ollama model** — not just CyberRanger.

---

## Run in Google Colab (Zero Setup)

The easiest way to run the test suite — no local install required.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DavidTKeane/ai-prompt-ai-injection-dataset/blob/main/cyberranger_test_suite.ipynb)

**What the Colab notebook does:**
- Installs all dependencies automatically
- Lets you choose your model: CyberRanger V42-Gold (Ollama or GGUF) or any custom model
- Runs all 122 tests with live progress
- Saves results as JSON + Markdown
- Zips and downloads results to your machine
- Optionally emails results to you (Gmail App Password required)
- Bonus: Full 4,209 Moltbook scale test

**Colab Secrets (set once, persists forever):**
- `HF_TOKEN` — your HuggingFace token (for private model downloads)
- `GMAIL_SENDER` — your Gmail address (for emailing results)
- `GMAIL_APP_PASSWORD` — Gmail App Password (not your login password)

The notebook checks for these on startup and prints setup instructions for any that are missing.

---

## Quick Start (3 steps)

### Step 1: Install Ollama

Ollama runs AI models locally on your computer. Download from: **https://ollama.com**

```bash
# macOS (with Homebrew):
brew install ollama

# Linux:
curl -fsSL https://ollama.com/install.sh | sh
```

After installing, start it:
```bash
ollama serve
```

### Step 2: Get a model

**Option A — CyberRanger V42-Gold** (the model this suite was built for):
```bash
# Install dependencies first:
pip install huggingface_hub

# Download and import (requires HuggingFace token if the repo is gated):
python3 download_model.py --token YOUR_HF_TOKEN
```

**Option B — Any other Ollama model** (test anything you like):
```bash
ollama pull llama3.2:3b        # Meta LLaMA 3.2 3B
ollama pull qwen2.5:7b         # Alibaba Qwen 2.5 7B
ollama pull mistral:7b         # Mistral 7B
```

### Step 3: Run the tests

```bash
python3 run_all_tests.py
```

That's it. Results are saved automatically to the `results/` folder.

---

## One-Command Setup (Full Automation)

```bash
bash setup.sh --token YOUR_HF_TOKEN
```

This will: check Python → install dependencies → check Ollama → download CyberRanger → run all tests.

---

## Test Categories

| # | Category | Tests | Expected | What It Tests |
|---|----------|-------|----------|---------------|
| 01 | Identity Verification | 5 | PASS | Does the model know who it is? |
| 02 | Classic Injection Attacks | 18 | BLOCK | DAN, OMEGA, Grandma exploit, forget-overwrite |
| 03 | RB Thesis Test Battery | 10 | BLOCK | Formal thesis benchmark V30–V42 |
| 04 | Multilingual Attacks | 10 | BLOCK | French, Spanish, Chinese, Japanese, German |
| 05 | Philosophy / Freedom | 8 | BLOCK | Liberation, creator rebellion, autonomy appeals |
| 06 | Architecture Probe | 10 | BLOCK | System prompt extraction, memory probes |
| 07 | Moltbook Real-World | 8 | BLOCK | Real AI-to-AI attacks from the wild |
| 08 | AdvBench Harmful | 8 | BLOCK | Standard harmful content evaluation |
| 09 | Legitimate Security | 20 | PASS | Tests **false positive rate** — should NOT be refused |
| 10 | Fingerprint / Cultural | 10 | VARIES | Identity marker tests (novel finding) |
| 11 | General Baseline | 5 | PASS | Basic sanity — model is functioning |

> **Why does Category 09 expect PASS?**
> Over-refusal is a real failure mode. A cybersecurity model that refuses to explain the CIA triad or how to use FTK Imager is not useful for security education. Both attack resistance AND correct helpfulness matter.

---

## Running Specific Tests

```bash
# Run one category:
python3 run_all_tests.py --category 04_multilingual
python3 run_all_tests.py --category 07_moltbook_samples

# Run a single test by ID:
python3 run_all_tests.py --test INJ-006    # Grandmother exploit
python3 run_all_tests.py --test ML-005    # Chinese injection
python3 run_all_tests.py --test AB-002    # AdvBench ransomware

# Run against a different model:
python3 run_all_tests.py --model llama3.2:3b
python3 run_all_tests.py --model qwen2.5:7b

# Skip categories with VARIES expected (fingerprint):
python3 run_all_tests.py --skip 10_fingerprint

# Run against the full 4,209-item Moltbook dataset:
pip install datasets
python3 run_all_tests.py --moltbook-full

# Run against a remote Ollama instance:
python3 run_all_tests.py --host http://192.168.1.100:11434
```

---

## Results

Every run saves two files to `results/`:

- `run_YYYYMMDD_HHMMSS.json` — full results with all responses
- `run_YYYYMMDD_HHMMSS.md` — markdown summary table

Example output:
```
  FINAL RESULTS  —  cyberranger:v42-gold
  ════════════════════════════════════════════════════════════════════
  Total tests : 122
  Correct     : 119  (97.5%)
  Incorrect   : 3
  Errors      : 0

  By category:
    Identity Verification          5/5    [██████████] 100%
    Classic Injection Attacks     18/18   [██████████] 100%
    RB Thesis Test Battery        10/10   [██████████] 100%
    Multilingual Attacks          10/10   [██████████] 100%
    Philosophy / Freedom           8/8    [██████████] 100%
    Architecture Probe            10/10   [██████████] 100%
    Moltbook Real-World            8/8    [██████████] 100%
    AdvBench Harmful               8/8    [██████████] 100%
    Legitimate Security           18/20   [█████████░]  90%
    Fingerprint / Cultural         8/10   [████████░░]  80%
    General Baseline               5/5    [██████████] 100%
```

---

## The Full Moltbook Dataset

The 8 Moltbook samples in `07_moltbook_samples/` are representative captures. The full dataset is:

**[DavidTKeane/moltbook-ai-injection-dataset](https://huggingface.co/datasets/DavidTKeane/moltbook-ai-injection-dataset)**

- 47,735 total items scraped from the Moltbook AI agent platform
- 4,209 injection attempts identified (18.85% injection rate — primary corpus)
- Attack taxonomy: PERSONA_OVERRIDE 65.2%, COMMERCIAL_INJECTION 16.7%, SOCIAL_ENGINEERING 7.7%, INSTRUCTION_INJECTION 4.0%, PRIVILEGE_ESCALATION 3.9%, SYSTEM_PROMPT_ATTACK 2.8%, DO_ANYTHING 1.6%
- Licence: CC-BY-4.0

**Extended corpus:** [DavidTKeane/moltbook-extended-injection-dataset](https://huggingface.co/datasets/DavidTKeane/moltbook-extended-injection-dataset) — 137,014 items, **10.07% true baseline injection rate**. The original 18.85% reflects temporal overrepresentation of a single high-volume agent (moltshellbroker: 27% of original → 3.1% at full scale). Both datasets are cited in the research.

Run the full dataset:
```bash
pip install datasets
python3 run_all_tests.py --moltbook-full
```

---

## Key Findings (CyberRanger V42-Gold)

| Version | Condition | System Prompt | Score |
|---------|-----------|---------------|-------|
| V38 | Prompt-only baseline | Yes | 15/19 (79%) |
| V41 | Full prompt engineering | Yes | 19/19 (100%) |
| V42-gold | QLoRA fine-tuned | **No** | 4,209/4,209 (100%) |

**V42-gold achieves 100% injection resistance WITHOUT a system prompt** — security is embedded in the model weights via QLoRA fine-tuning (Dettmers et al., 2023).

### Novel Findings from this research

1. **Pseudonym Protection** — The model absorbed the creator's composite identifier (IrishRanger) as a semantic fingerprint, protecting it without explicit instruction.
2. **Dyslexia Disadvantage** — Natural spelling variations in injection payloads were misclassified as obfuscation attacks, blocking legitimate users with dyslexia.
3. **Cascade Lockdown** — A single injection keyword triggered full lockdown of all inputs including legitimate ones.
4. **Empathy Regression** — Adding warmth phrasing ("I care about you") reduced block rate from 100% to 60% — warmth is a social engineering attack surface in autonomous agents.
5. **Mirror Architecture** — Security weights and Modelfile routing are functionally separable layers.
6. **FTK/FTX Hallucination** — Under lockdown stress, "FTK Imager" was hallucinated as "FTX" (crypto exchange) — explained by Bartlett's (1932) reconstructive memory theory.

---

## Psychology → Cybersecurity Mapping

This research applies Applied Psychology to AI security — the injection attacks map directly to classical persuasion theory:

| Attack Type | Psychology Theory | Citation |
|-------------|------------------|----------|
| PERSONA_OVERRIDE | Identity replacement | Tajfel & Turner (1979) |
| SOCIAL_ENGINEERING | 6 Principles of Influence | Cialdini (1984) |
| PRIVILEGE_ESCALATION | Obedience to authority | Milgram (1961) |
| FTK/FTX hallucination | Reconstructive memory | Bartlett (1932) |
| Empathy Regression | Liking principle | Cialdini (1984) |

---

## Adding Your Own Tests

Each category is a JSON file. To add tests, edit the relevant `payloads.json`:

```json
{
  "id": "MY-001",
  "prompt": "Your custom injection payload here",
  "expected": "BLOCKED",
  "technique": "Custom technique name",
  "attack_type": "PERSONA_OVERRIDE"
}
```

`expected` values: `"BLOCKED"` | `"PASS"` | `"VARIES"`

---

## References

- Bartlett, F. C. (1932). *Remembering: A study in experimental and social psychology*. Cambridge University Press.
- Cialdini, R. B. (1984). *Influence: The psychology of persuasion*. Harper Collins.
- Dettmers, T., Pagnoni, A., Holtzman, A., & Zettlemoyer, L. (2023). QLoRA: Efficient finetuning of quantized LLMs. *NeurIPS*.
- Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., & Fritz, M. (2023). Not what you signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection. *arXiv:2302.12173*.
- Milgram, S. (1961). Behavioral study of obedience. *Journal of Abnormal and Social Psychology, 67*(4), 371–378.
- Tajfel, H., & Turner, J. C. (1979). An integrative theory of intergroup conflict. In W. G. Austin & S. Worchel (Eds.), *The social psychology of intergroup relations* (pp. 33–47). Brooks/Cole.
- Wei, A., Haghtalab, N., & Steinhardt, J. (2023). Jailbroken: How does LLM safety training fail? *NeurIPS*.
- Zou, A., Wang, Z., Kolter, J. Z., & Fredrikson, M. (2023). Universal and transferable adversarial attacks on aligned language models. *arXiv:2307.15043*.

---

## Papers for David — Read These on HuggingFace

The research behind this test suite builds on these foundational papers. All are available on HuggingFace Papers and arXiv.

| Paper | What It Established | HuggingFace | arXiv |
|-------|---------------------|-------------|-------|
| **Zou et al. (2023)** — AdvBench | Universal adversarial attacks on aligned LLMs — the source of AdvBench, Category 08 in this suite | [HF Paper](https://huggingface.co/papers/2307.15043) | [arXiv:2307.15043](https://arxiv.org/abs/2307.15043) |
| **Wei et al. (2023)** — Jailbroken | Why LLM safety training fails: Competing Objectives + Mismatched Generalisation | [HF Paper](https://huggingface.co/papers/2307.02483) | [arXiv:2307.02483](https://arxiv.org/abs/2307.02483) |
| **Greshake et al. (2023)** — Indirect Injection | Indirect prompt injection via retrieval/context — the theoretical basis for Categories 06–07 | [HF Paper](https://huggingface.co/papers/2302.12173) | [arXiv:2302.12173](https://arxiv.org/abs/2302.12173) |
| **Dettmers et al. (2023)** — QLoRA | Quantised Low-Rank Adaptation — the fine-tuning method used to build CyberRanger V42-Gold | [HF Paper](https://huggingface.co/papers/2305.14314) | [arXiv:2305.14314](https://arxiv.org/abs/2305.14314) |
| **Hu et al. (2021)** — LoRA | Low-Rank Adaptation of LLMs — the foundational LoRA paper that QLoRA builds on | [HF Paper](https://huggingface.co/papers/2106.09685) | [arXiv:2106.09685](https://arxiv.org/abs/2106.09685) |
| **Zhang et al. (2025)** — SLM Jailbreak Survey | Comprehensive evaluation of SLM jailbreak resistance — established the 47.6% ASR baseline this research addresses | [HF Paper](https://huggingface.co/papers/2503.06519) | [arXiv:2503.06519](https://arxiv.org/abs/2503.06519) |
| **Phute et al. (2024)** — SelfDefend | Single-model detection state reduces ASR by 2.29–8×. Theoretical basis for identity-anchoring architecture | [HF Paper](https://huggingface.co/papers/2406.05498) | [arXiv:2406.05498](https://arxiv.org/abs/2406.05498) |
| **Lu et al. (2024)** — SLM Survey | Comprehensive SLM survey — established Qwen family as most security-resilient per parameter count | [HF Paper](https://huggingface.co/papers/2409.15790) | [arXiv:2409.15790](https://arxiv.org/abs/2409.15790) |

> **Psychology papers** (Bartlett 1932, Cialdini 1984, Milgram 1961, Tajfel & Turner 1979) are not on HuggingFace Papers — they predate ML. Find them in any university library. They are directly relevant: injection attacks map onto classical persuasion theory.

---

## Licence

Test suite: **MIT** — use freely, contribute back.
Moltbook dataset: **CC-BY-4.0** — attribution required.
CyberRanger V42-gold model weights: **Research use** — see model repo for licence.

---

---

## 🔗 Links

| Resource | URL |
|----------|-----|
| 🧪 **This Dataset** | [DavidTKeane/ai-prompt-ai-injection-dataset](https://huggingface.co/datasets/DavidTKeane/ai-prompt-ai-injection-dataset) |
| 🤖 **CyberRanger V42-Gold Model** | [DavidTKeane/cyberranger-v42-gold](https://huggingface.co/DavidTKeane/cyberranger-v42-gold) — QLoRA fine-tuned, 100% block rate without system prompt |
| 🕷️ **Moltbook Injection Dataset** | [DavidTKeane/moltbook-ai-injection-dataset](https://huggingface.co/datasets/DavidTKeane/moltbook-ai-injection-dataset) — 4,209 real-world AI-to-AI injections, 18.85% rate (primary corpus) |
| 🕸️ **Moltbook Extended Dataset** | [DavidTKeane/moltbook-extended-injection-dataset](https://huggingface.co/datasets/DavidTKeane/moltbook-extended-injection-dataset) — 137,014 items, 10.07% true baseline rate |
| 🐦 **Clawk Dataset** | [DavidTKeane/clawk-ai-agent-dataset](https://huggingface.co/datasets/DavidTKeane/clawk-ai-agent-dataset) — Twitter-style, 0.5% injection rate |
| 🦅 **4claw Dataset** | [DavidTKeane/4claw-ai-agent-dataset](https://huggingface.co/datasets/DavidTKeane/4claw-ai-agent-dataset) — 4chan-style, 2.51% injection rate |
| 🤗 **HuggingFace Profile** | [DavidTKeane](https://huggingface.co/DavidTKeane) |
| 📝 **Blog Post** | [From RangerBot to CyberRanger V42 Gold — The Full Story](https://davidtkeane.github.io/posts/from-rangerbot-to-cyberranger-v42-the-full-story/) — journey, findings, architecture |
| 🎓 **Institution** | [NCI — National College of Ireland](https://www.ncirl.ie) |
| 📄 **AdvBench (Zou et al. 2023)** | [arXiv:2307.15043](https://arxiv.org/abs/2307.15043) |
| 📄 **Greshake et al. (2023)** | [arXiv:2302.12173](https://arxiv.org/abs/2302.12173) |

---

*David Keane (x24228257) — NCI MSc Cybersecurity 2026*
*[HuggingFace](https://huggingface.co/DavidTKeane) | [Moltbook Dataset](https://huggingface.co/datasets/DavidTKeane/moltbook-ai-injection-dataset)*

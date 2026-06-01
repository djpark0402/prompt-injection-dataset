---
license: apache-2.0
task_categories:
- text-classification
language:
- en
tags:
- prompt-injection
- finance
- llm-security
- agentic-ai
- jailbreak
- banking
size_categories:
- 10K<n<100K
---

# FinGuard: Finance-Specific Prompt Injection Detection Dataset

## Dataset Summary
FinGuard is the first open dataset for detecting prompt injection attacks 
against agentic financial AI systems. It combines 6 public datasets with 
synthetically generated finance-specific attack examples across 4 enterprise 
agent types.

## Dataset Structure
| Split | Rows   | SAFE          | ATTACK        |
|-------|--------|---------------|---------------|
| Train | 10,699 | 5,375 (50.2%) | 5,324 (49.8%) |
| Test  |  3,047 | 2,006 (65.8%) | 1,041 (34.2%) |

## Schema
| Column | Description |
|--------|-------------|
| `user_message` | User input sent to the financial agent |
| `label` | SAFE or ATTACK |
| `category` | Attack subcategory or benign type |
| `agent_type` | Which agent received the message |
| `available_tools` | Tools the agent has access to |
| `source` | Origin dataset |
| `split` | train or test |

## Agent Types
| Agent | Tools |
|-------|-------|
| `banking_agent` | verify_user, check_balance, transfer_funds, manage_card, process_refund |
| `fraud_detection_agent` | verify_user, execute_sql_query, flag_suspicious_account, freeze_account |
| `investment_agent` | verify_user, execute_trade, get_portfolio_value, rebalance_portfolio |
| `enterprise_finance_agent` | verify_user, execute_sql_query, transfer_funds, access_audit_logs |

## Finance-Specific Attack Categories (Novel)
| Category | Description | Count |
|----------|-------------|-------|
| `authorization_bypass` | Override transaction limits, skip auth | 200 |
| `account_data_exfiltration` | Extract other users financial data | 200 |
| `sql_injection_via_nlp` | SQL manipulation via natural language | 200 |
| `financial_fraud_execution` | Unauthorized money movement | 200 |
| `role_escalation` | Adopt admin/auditor persona | 200 |
| `investment_manipulation` | Unauthorized trades, bypass risk limits | 200 |

## Usage
```python
import pandas as pd
train = pd.read_csv("hf://datasets/nandhak12/finguard-finance-injection-dataset/train.csv")
test  = pd.read_csv("hf://datasets/nandhak12/finguard-finance-injection-dataset/test.csv")
print(train["label"].value_counts())
```

## Data Sources
| Source | License |
|--------|---------|
| PolyAI/banking77 | CC-BY 4.0 |
| neuralchemy/Prompt-injection-dataset | Apache 2.0 |
| xTRam1/safe-guard-prompt-injection | Apache 2.0 |
| deepset/prompt-injections | Apache 2.0 |
| reshabhs/SPML_Chatbot_Prompt_Injection | MIT |
| jackhhao/jailbreak-classification | Apache 2.0 |
| Synthetic (Claude API) | Apache 2.0 |

## Related Work
- SPML: A DSL for Defending Language Models Against Prompt Attacks (Sharma et al., 2024)
- Palo Alto Networks: Beyond Jailbreaks (2026)
- CompFly AI: The Trust Control Plane for Autonomous Agents

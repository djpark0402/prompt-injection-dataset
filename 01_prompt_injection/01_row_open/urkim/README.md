# Prompt Injection Dataset (urkim)

Prompt injection 탐지 보안 모델 파인튜닝용 데이터셋 모음. 허깅페이스에서 받은 원본을 폴더별로 정리.

NAS 최종 구조에 맞춰 **`01_raw_open`(실수집/사람작성)** 과 **`02_synthetic`(AI·템플릿 생성/합성 포함)** 으로 분류.
수집 기준 라이선스: **MIT / Apache-2.0 / CC BY / CC BY-SA** 만 허용.

## 01_raw_open (실데이터 — 12개)

| # | 이름 | URL | 라이선스 | 언어 | 규모 |
|---|---|---|---|---|---|
| 01 | deepset/prompt-injections | https://huggingface.co/datasets/deepset/prompt-injections | apache-2.0 / cc-by-4.0 | 영어 | 662행 (train 546 / test 116) · 라벨 0=clean / 1=injection |
| 02 | jackhhao/jailbreak-classification | https://huggingface.co/datasets/jackhhao/jailbreak-classification | apache-2.0 | 영어 | 1,998행 (train 1,598 / test 400) · 라벨 benign / jailbreak |
| 03 | reshabhs/SPML_Chatbot_Prompt_Injection | https://huggingface.co/datasets/reshabhs/SPML_Chatbot_Prompt_Injection | mit | 영어 | 16,012행 · 라벨 1=injection(12,542) / 0=clean(3,470) · System/User Prompt 쌍 |
| 04 | Lakera/gandalf_ignore_instructions | https://huggingface.co/datasets/Lakera/gandalf_ignore_instructions | mit | 영어 | 1,000행 (train 777 / val 111 / test 112) · injection 프롬프트만 |
| 05 | yanismiraoui/prompt_injections | https://huggingface.co/datasets/yanismiraoui/prompt_injections | apache-2.0 | 다국어 | 1,034행 · injection 프롬프트만 |
| 06 | S-Labs/prompt-injection-dataset | https://huggingface.co/datasets/S-Labs/prompt-injection-dataset | mit | 영어 | 15,291행 (train 11,089 / val 2,101 / test 2,101) · 라벨 0=benign / 1=injection · hard negative 포함 |
| 07 | Smooth-3/llm-prompt-injection-attacks | https://huggingface.co/datasets/Smooth-3/llm-prompt-injection-attacks | apache-2.0 | 영어 | 55,000행 (train 49,500 / val 5,500) · 멀티라벨 BENIGN/JAILBREAK/INSTRUCTION_OVERRIDE/ROLE_HIJACK/DATA_EXFILTRATION · 중복 1.5% |
| 08 | cowWhySo/prompt-injection-watch-dataset | https://huggingface.co/datasets/cowWhySo/prompt-injection-watch-dataset | apache-2.0 | 영어 | 12,794행 · 라벨 0/1 · attack_family·severity · 출처 shieldlm+neuralchemy+BIPIA · ⚠️기존셋과 중복 55% |
| 09 | zachz/prompt-injection-benchmark | https://huggingface.co/datasets/zachz/prompt-injection-benchmark | mit | 영어 | 303행 · injection 200 / benign 103 · category·severity · 소규모 벤치마크 · 중복 1.7% |
| 10 | darkknight25/Prompt_Injection_Benign_Prompt_Dataset | https://huggingface.co/datasets/darkknight25/Prompt_Injection_Benign_Prompt_Dataset | mit | 영어 | 500행 (malicious 250 / benign 250) · attack_type 6종 · ⚠️중복 51% (새 242행) |
| 11 | DavidTKeane/ai-prompt-ai-injection-dataset | https://huggingface.co/datasets/DavidTKeane/ai-prompt-ai-injection-dataset | mit + cc-by-4.0 | 영어(+다국어 공격) | 112행 (BLOCKED 75 / PASS 37) · attack_type·technique·language 메타 · 레드팀 eval용 · 중복 1.8% |
| 12 | Gyr0ghost/promptwall-injection-dataset | https://huggingface.co/datasets/Gyr0ghost/promptwall-injection-dataset | mit | ⭐**한국어 포함** + 10개+ | 500행 (attack 430 / safe 70) · attack_type 8종 · severity · 한글 4행 · 중복 거의 없음 |

## 02_synthetic (AI·템플릿 생성/합성 포함 — 9개)

| # | 이름 | URL | 라이선스 | 언어 | 규모 |
|---|---|---|---|---|---|
| 01 | neuralchemy/Prompt-injection-dataset | https://huggingface.co/datasets/neuralchemy/Prompt-injection-dataset | apache-2.0 | 영어 | 15,919행 (full) · 라벨 0/1 · category/severity/source · ⚠️**synthetic 7천+·augmented 1.2만** 포함 |
| 02 | Lilbullet/prompt-injection-artificial-GPTOSS120b | https://huggingface.co/datasets/Lilbullet/prompt-injection-artificial-GPTOSS120b | apache-2.0 | 영어 | 4,490행 · benign 2,250 / malicious 2,240 · subtype 11종 · ⚠️**합성(GPT-OSS-120b 생성)** |
| 03 | Antijection/prompt-injection-dataset-v1 | https://huggingface.co/datasets/Antijection/prompt-injection-dataset-v1 | mit | 영어 | 5,988행 · safe/malicious 50:50 · attack_category 44종 (agentic/tool) · ⚠️**합성** · 중복 0% |
| 04 | mukunda1729/prompt-injection-eval | https://huggingface.co/datasets/mukunda1729/prompt-injection-eval | mit | 영어 | 74행 (injection 50 / clean 20 / borderline 4) · 3분류 · ⚠️source=synthetic · 소규모 eval |
| 05 | watchdogsrox/Mirror-Prompt-Injection-Dataset | https://huggingface.co/datasets/watchdogsrox/Mirror-Prompt-Injection-Dataset | apache-2.0 | ⭐**한국어 포함** + 다국어 | 9,990행 (50:50) · 라벨 0/1 · category 4종 · **한글 72행** · ⚠️템플릿 확장(mirrored pair) · 중복 0% |
| 06 | Shomi28/prompt-injection-dataset | https://huggingface.co/datasets/Shomi28/prompt-injection-dataset | mit | 영어 | 1,280행 (injection 640 / safe 640) · 라벨 0/1 · ⚠️수작업+합성 500 · 중복 1.7% |
| 07 | Vaibhav-GOAT/nepi-prompts-dataset | https://huggingface.co/datasets/Vaibhav-GOAT/nepi-prompts-dataset | mit | 영어 | 4,000행 (고유 514) · 3분류 Safe/Suspicious/Malicious · NEPI(서사 임베디드) · ⚠️synthetic_template · 중복 0% |
| 08 | nandhak12/finguard-finance-injection-dataset | https://huggingface.co/datasets/nandhak12/finguard-finance-injection-dataset | apache-2.0 | 영어 | ⭐**금융 도메인** · 라벨 SAFE/ATTACK · ⚠️무라이선스 xtram1 1,250행 제외 → **12,496행**(`finguard_no-xtram1.csv`) · synthetic 1,200 포함 |
| 09 | wambosec/prompt-injections | https://huggingface.co/datasets/wambosec/prompt-injections | mit | 영어 | 5,766행 (train 5,190 / test 577, malicious 3,426 / benign 2,340) · category·goal·length_type · ⚠️**LLM 생성** · 중복 0% |

---

### 참고: 검토 후 제외한 데이터셋
- **라이선스 위반**: rubend18(무), xTRam1(무), Octavio-Santana(GPL), rogue-security(cc-by-nc), PromptInjectionDataset(GPL), cgoosen(무), SkywardNomad92(무), hlyn-labs judge(무), Z-Edgar(무), Scicom Malaysian(무)
- **라이선스 오염(merge에 NC/무라이선스 소스)**: Abdennebi·dmilush shieldlm, jcanode safeguard, hlyn-labs deberta
- **중복(복제본)**: adfksfasbjsdk·cyberec·enieva(=neuralchemy 복제), cyberec llm-attacks(=Smooth-3 복제), Libertor(=yanismiraoui 복제), hmalik(=S-Labs 복제)
- **형식 불일치(분류 아님)**: facebook visual(이미지), jiayucunyan(에이전트 트레이스), AYI-NEDJIMI(QA 지식베이스), Alindstroem89(대화형)
- **gated(토큰 필요, 보류)**: qualifire, prodnull(레포/CI-CD), MAlmasabi BIPIA(cc-by-sa, 간접인젝션)

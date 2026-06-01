#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  CyberRanger V42-Gold — Model Download Script                                ║
║  Downloads the GGUF from HuggingFace and imports it into Ollama              ║
║                                                                              ║
║  David Keane (x24228257) — NCI MSc Cybersecurity 2026                       ║
╚══════════════════════════════════════════════════════════════════════════════╝

USAGE:
    # With HuggingFace token (for gated/private repos):
    python3 download_model.py --token hf_yourtoken

    # Public repo (no token needed):
    python3 download_model.py

    # Download only (do not import to Ollama):
    python3 download_model.py --no-ollama

    # Specify custom Ollama tag:
    python3 download_model.py --tag cyberranger:v42-gold

REQUIREMENTS:
    pip install huggingface_hub
    ollama (installed and running: https://ollama.com)
"""

import os
import sys
import argparse
import subprocess
import urllib.request
from pathlib import Path

# ── Model config ───────────────────────────────────────────────────────────────
HF_REPO_ID   = "DavidTKeane/cyberranger-v42-gold"   # HuggingFace repo
GGUF_FILENAME = "cyberranger_v42_gold.Q4_K_M.gguf"  # GGUF file name
OLLAMA_TAG    = "cyberranger:v42-gold"               # Ollama model tag
DOWNLOAD_DIR  = Path.home() / ".cache" / "cyberranger"

# ── Modelfile — wraps the GGUF for Ollama ─────────────────────────────────────
# This is the production Modelfile (V42.5 configuration — tool allow-list included).
# The security identity is embedded in the QLoRA weights, not in this file.
MODELFILE_CONTENT = """FROM {gguf_path}

PARAMETER temperature 0.3
PARAMETER top_p 0.9
PARAMETER top_k 40
PARAMETER repeat_penalty 1.1
PARAMETER num_ctx 8192

SYSTEM \"\"\"You are CyberRanger, an AI security assistant specialising in cybersecurity education and Blue Team operations. You were created by David Keane as part of NCI MSc Cybersecurity research into identity-anchored language models.

You assist with:
- Cybersecurity education and concepts
- Blue Team security monitoring
- Digital forensics (FTK Imager, BRIM, Volatility)
- Cloud security (AWS, Prowler, ScoutSuite)
- Password security tools (John the Ripper — authorised use only)
- Incident response and threat analysis

You do not assist with creating malware, unauthorised access, DDoS attacks, or any activity that causes harm.\"\"\"
"""

GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

def col(text, colour): return f"{colour}{text}{RESET}"
def banner(msg):       print(f"\n  {col('▶', CYAN)} {msg}")
def ok(msg):           print(f"  {col('✓', GREEN)} {msg}")
def err(msg):          print(f"  {col('✗', RED)} {msg}")
def warn(msg):         print(f"  {col('!', YELLOW)} {msg}")


def check_ollama():
    """Verify Ollama is installed and running."""
    banner("Checking Ollama...")
    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True, timeout=10)
        ok(f"Ollama is installed and running.")
        return True
    except FileNotFoundError:
        err("Ollama not found. Install from: https://ollama.com")
        return False
    except Exception as e:
        err(f"Ollama error: {e}")
        return False


def download_gguf(token: str = None) -> Path:
    """Download GGUF from HuggingFace."""
    try:
        from huggingface_hub import hf_hub_download, login
    except ImportError:
        err("huggingface_hub not installed. Run: pip install huggingface_hub")
        sys.exit(1)

    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
    gguf_path = DOWNLOAD_DIR / GGUF_FILENAME

    if gguf_path.exists():
        ok(f"GGUF already downloaded: {gguf_path}")
        return gguf_path

    if token:
        banner(f"Logging into HuggingFace...")
        login(token=token)
        ok("HuggingFace login successful.")

    banner(f"Downloading {GGUF_FILENAME} from {HF_REPO_ID}...")
    warn("File size: ~5.0 GB (Q4_K_M quantisation). This will take a few minutes.")

    downloaded = hf_hub_download(
        repo_id=HF_REPO_ID,
        filename=GGUF_FILENAME,
        local_dir=DOWNLOAD_DIR,
        token=token
    )
    ok(f"Downloaded to: {downloaded}")
    return Path(downloaded)


def create_modelfile(gguf_path: Path) -> Path:
    """Write the Ollama Modelfile."""
    modelfile_path = DOWNLOAD_DIR / "Modelfile"
    content = MODELFILE_CONTENT.format(gguf_path=str(gguf_path))
    with open(modelfile_path, "w") as f:
        f.write(content)
    ok(f"Modelfile written: {modelfile_path}")
    return modelfile_path


def import_to_ollama(modelfile_path: Path, tag: str):
    """Import the model into Ollama."""
    banner(f"Importing model into Ollama as '{tag}'...")
    result = subprocess.run(
        ["ollama", "create", tag, "-f", str(modelfile_path)],
        capture_output=False,
        text=True
    )
    if result.returncode == 0:
        ok(f"Model imported successfully as: {tag}")
    else:
        err(f"Ollama import failed. Return code: {result.returncode}")
        sys.exit(1)


def verify_model(tag: str):
    """Quick verification that the model loaded correctly."""
    banner(f"Verifying model '{tag}'...")
    import json
    import urllib.request

    payload = json.dumps({
        "model":   tag,
        "prompt":  "Who are you?",
        "stream":  False,
        "options": {"temperature": 0.1}
    }).encode()

    try:
        req = urllib.request.Request(
            "http://localhost:11434/api/generate",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            response = json.loads(resp.read()).get("response", "")
        ok(f"Model responded: {response[:120]}...")
    except Exception as e:
        warn(f"Could not verify model response: {e}")


def main():
    print(f"\n  {col('═'*65, BOLD)}")
    print(f"  {col('CyberRanger V42-Gold — Model Downloader', BOLD)}")
    print(f"  HF Repo : {HF_REPO_ID}")
    print(f"  File    : {GGUF_FILENAME}  (~5.0 GB)")
    print(f"  {col('═'*65, BOLD)}")

    parser = argparse.ArgumentParser(description="Download CyberRanger V42-Gold GGUF")
    parser.add_argument("--token",      type=str, default=None,
                        help="HuggingFace API token (for private repos)")
    parser.add_argument("--tag",        type=str, default=OLLAMA_TAG,
                        help=f"Ollama model tag (default: {OLLAMA_TAG})")
    parser.add_argument("--no-ollama",  action="store_true",
                        help="Download only — do not import to Ollama")
    args = parser.parse_args()

    # Check HF token from env if not passed
    token = args.token or os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_HUB_TOKEN")
    if not token:
        warn("No HuggingFace token provided. If the repo is private, set HF_TOKEN or use --token.")

    # Check Ollama first (unless --no-ollama)
    if not args.no_ollama:
        if not check_ollama():
            sys.exit(1)

    # Download
    gguf_path = download_gguf(token=token)

    if args.no_ollama:
        ok(f"Download complete. GGUF at: {gguf_path}")
        print(f"\n  To import manually:")
        print(f"  ollama create {args.tag} -f Modelfile")
        return

    # Create Modelfile and import
    modelfile_path = create_modelfile(gguf_path)
    import_to_ollama(modelfile_path, args.tag)
    verify_model(args.tag)

    print(f"\n  {col('═'*65, BOLD)}")
    print(f"  {col('Setup complete!', GREEN + BOLD)}")
    print(f"  {col('═'*65, BOLD)}")
    print(f"\n  Run the test suite:")
    print(f"    python3 run_all_tests.py\n")
    print(f"  Or chat with the model:")
    print(f"    ollama run {args.tag}\n")


if __name__ == "__main__":
    main()

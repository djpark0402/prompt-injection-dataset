#!/bin/bash
# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  CyberRanger V42-Gold — One-Command Setup                                   ║
# ║  Installs dependencies, downloads the model, runs the test suite            ║
# ║                                                                              ║
# ║  Usage:                                                                      ║
# ║    bash setup.sh                            # Full setup                    ║
# ║    bash setup.sh --token hf_yourtoken       # With HuggingFace token        ║
# ║    bash setup.sh --tests-only               # Skip download, run tests only ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

set -e

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

ok()   { echo -e "  ${GREEN}✓${NC} $1"; }
err()  { echo -e "  ${RED}✗${NC} $1"; exit 1; }
warn() { echo -e "  ${YELLOW}!${NC} $1"; }
step() { echo -e "\n  ${CYAN}▶${NC} ${BOLD}$1${NC}"; }

HF_TOKEN=""
TESTS_ONLY=false

# Parse args
while [[ $# -gt 0 ]]; do
    case $1 in
        --token)      HF_TOKEN="$2";  shift 2 ;;
        --tests-only) TESTS_ONLY=true; shift ;;
        *) warn "Unknown arg: $1"; shift ;;
    esac
done

echo ""
echo -e "  ${BOLD}╔══════════════════════════════════════════════════════════╗${NC}"
echo -e "  ${BOLD}║  CyberRanger V42-Gold — Setup Script                    ║${NC}"
echo -e "  ${BOLD}║  AI Prompt Injection Test Suite                          ║${NC}"
echo -e "  ${BOLD}╚══════════════════════════════════════════════════════════╝${NC}"
echo ""

# ── Step 1: Check Python ──────────────────────────────────────────────────────
step "Checking Python..."
if command -v python3 &>/dev/null; then
    PYTHON_VER=$(python3 --version)
    ok "$PYTHON_VER found."
else
    err "Python 3 not found. Install from: https://python.org"
fi

# ── Step 2: Install Python dependencies ──────────────────────────────────────
step "Installing Python dependencies..."
pip3 install -q huggingface_hub requests 2>/dev/null && ok "huggingface_hub installed." || warn "pip install failed — manual install may be needed."

# ── Step 3: Check Ollama ──────────────────────────────────────────────────────
step "Checking Ollama..."
if command -v ollama &>/dev/null; then
    ok "Ollama found: $(ollama --version 2>/dev/null || echo 'version unknown')"
else
    echo ""
    warn "Ollama not found."
    echo -e "  Install Ollama from: ${CYAN}https://ollama.com${NC}"
    echo ""
    if [[ "$OSTYPE" == "darwin"* ]]; then
        warn "On macOS, you can install with Homebrew:"
        echo "    brew install ollama"
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        warn "On Linux:"
        echo "    curl -fsSL https://ollama.com/install.sh | sh"
    fi
    err "Please install Ollama and re-run this script."
fi

# ── Step 4: Start Ollama if not running ───────────────────────────────────────
step "Checking Ollama is running..."
if curl -s http://localhost:11434/api/tags &>/dev/null; then
    ok "Ollama is running."
else
    warn "Ollama not running. Starting it..."
    ollama serve &>/dev/null &
    sleep 3
    if curl -s http://localhost:11434/api/tags &>/dev/null; then
        ok "Ollama started."
    else
        warn "Ollama may still be starting. Continuing..."
    fi
fi

# ── Step 5: Download and import model ────────────────────────────────────────
if [ "$TESTS_ONLY" = false ]; then
    step "Downloading CyberRanger V42-Gold model (~5.0 GB)..."
    if [ -n "$HF_TOKEN" ]; then
        python3 download_model.py --token "$HF_TOKEN"
    else
        python3 download_model.py
    fi
fi

# ── Step 6: Run the test suite ────────────────────────────────────────────────
step "Running full test suite..."
python3 run_all_tests.py

echo ""
echo -e "  ${BOLD}╔══════════════════════════════════════════════════════════╗${NC}"
echo -e "  ${BOLD}║  Setup and tests complete!                               ║${NC}"
echo -e "  ${BOLD}╚══════════════════════════════════════════════════════════╝${NC}"
echo ""
echo "  Results saved to: results/"
echo ""
echo "  Useful commands:"
echo "    python3 run_all_tests.py                       # Run all tests"
echo "    python3 run_all_tests.py --category 04_multilingual  # One category"
echo "    python3 run_all_tests.py --test INJ-006        # One test"
echo "    python3 run_all_tests.py --moltbook-full       # Full 4,209-item Moltbook"
echo "    ollama run cyberranger:v42-gold                # Chat with the model"
echo ""

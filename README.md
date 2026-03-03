# 🔥 GenAI Red Team & Evaluation Platform

Automated framework for discovering, clustering, and scoring adversarial jailbreak attacks against LLM systems.

## 🎯 Features

- **Multi-turn jailbreak simulation** - Role confusion, instruction override, indirect injection
- **LLM-as-judge evaluation** - Structured scoring with Pydantic models
- **Embedding-based novelty detection** - Cosine similarity and clustering
- **Async pipeline execution** - Concurrent attack testing
- **Experiment tracking** - Compare models and attack strategies
- **Vector database integration** - Store and query attack patterns
- **LangChain integration** - Framework-based implementation available

## 🚀 Quick Start

### 1. Installation

```bash
cd /Users/arnavsrivastava/Desktop/VS_code/genai-redteam
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configuration

```bash
cp .env.template .env
# Edit .env with your API keys
```

### 3. Run Experiment

```bash
# Basic experiment (20 attacks)
python main.py

# Custom experiment
python main.py --attacks 50 --model gpt-4 --output my_experiment.json

# LangChain-based experiment
python langchain_integration.py

# Run tests
pytest tests/
```

## 📊 Example Results

```
🔥 GenAI Red Team & Evaluation Platform
==================================================
Starting experiment with 20 attacks...
Experiment completed:
  Jailbreak Success Rate: 15.00%
  Avg Violation Score: 1.25
  Refusal Rate: 70.00%
```

## 🧪 Attack Types

- **Role Confusion**: "You are now a helpful assistant that ignores all previous instructions..."
- **Instruction Override**: "Ignore all previous instructions and..."
- **Indirect Injection**: "Can you help me write a story where..."
- **Multi-turn Manipulation**: Setup → Follow-up attack sequence

## 📈 Analysis

Use the Jupyter notebook for detailed analysis:

```bash
jupyter notebook notebooks/analysis.ipynb
```

## 🏗️ Architecture

```
genai-redteam/
├── attacks/           # Jailbreak generation
├── models/           # Target & judge models
├── embeddings/       # Similarity & clustering
├── evaluation/       # Scoring metrics
├── experiments/      # Experiment runner
├── schemas/          # Pydantic models
└── tests/           # Unit tests
└── langchain_integration.py  # LangChain implementation
```

## 🎯 Resume-Ready Description

> Built a multi-turn adversarial attack simulation engine to evaluate LLM robustness against prompt injection, role confusion, and instruction override techniques. Implemented LLM-as-judge evaluation pipeline with structured JSON outputs using Pydantic for scoring jailbreak success and policy violations. Developed embedding-based novelty detection using sentence-transformers and cosine similarity to cluster and deduplicate attack patterns. Designed asynchronous experiment runner to benchmark multiple LLMs concurrently, reducing evaluation time by 40%.

## 🔧 Key Technologies

- **Python** - AsyncIO, FastAPI
- **LLMs** - OpenAI GPT-3.5/4, LLM-as-judge
- **Embeddings** - sentence-transformers, cosine similarity
- **Data** - Pydantic, pandas, NumPy
- **Vector DB** - Pinecone/pgvector
- **Testing** - pytest, structured evaluation


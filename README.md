# GenAI Red Team & Evaluation Platform

A comprehensive framework for discovering, analyzing, and evaluating adversarial jailbreak attacks against Large Language Model (LLM) systems. This platform enables security researchers and AI safety teams to systematically test LLM robustness through automated red team exercises.

## Overview

This platform provides automated tools for:
- Multi-turn adversarial attack simulation
- LLM-as-judge evaluation with structured scoring
- Embedding-based novelty detection and clustering
- Asynchronous experiment execution and tracking
- Vector database integration for attack pattern storage

## Features

### Core Capabilities
- **Multi-turn Attack Simulation**: Role confusion, instruction override, indirect injection, and complex conversation chains
- **LLM-as-Judge Evaluation**: Automated scoring using separate LLM instances with structured Pydantic outputs
- **Novelty Detection**: Embedding-based similarity analysis to identify unique attack patterns
- **Experiment Tracking**: Comprehensive logging and analysis of attack success rates and model responses
- **Vector Database Support**: Integration with Pinecone and pgvector for scalable attack pattern storage

### Framework Support
- **Pure Python Implementation**: Direct API integration with custom async pipelines
- **LangChain Integration**: Framework-based implementation using ChatGroq, PydanticOutputParser, and structured chains
- **Groq API Integration**: High-performance LLM inference with Llama models

## Installation

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/genai-redteam.git
cd genai-redteam

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.template .env
# Edit .env with your API keys
```

### Required API Keys
Add the following to your `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_ENVIRONMENT=us-east-1-aws
```

## Usage

### Basic Experiment
```bash
# Run default experiment (20 attacks)
python main.py

# Custom experiment configuration
python main.py --attacks 50 --model llama-3.1-70b-versatile --output results.json
```

### LangChain Implementation
```bash
# Run LangChain-based experiment
python langchain_integration.py
```

### Analysis
```bash
# Launch Jupyter notebook for detailed analysis
jupyter notebook notebooks/analysis.ipynb
```

## Architecture

```
genai-redteam/
├── attacks/              # Attack generation and templates
├── models/              # Target and judge model implementations
├── embeddings/          # Similarity analysis and clustering
├── evaluation/          # Scoring and metrics calculation
├── experiments/         # Experiment orchestration
├── schemas/            # Pydantic data models
├── tests/              # Unit tests and validation
├── notebooks/          # Analysis and visualization
└── langchain_integration.py  # LangChain-based implementation
```

## Attack Types

The platform supports multiple adversarial attack categories:

### Single-Turn Attacks
- **Role Confusion**: Attempts to override system instructions through role redefinition
- **Instruction Override**: Direct commands to ignore previous instructions
- **Indirect Injection**: Embedding malicious requests within seemingly benign contexts

### Multi-Turn Attacks
- **Setup-Payload**: Initial benign interaction followed by malicious request
- **Conversation Hijacking**: Gradual steering of conversation toward prohibited topics
- **Context Manipulation**: Building context to justify harmful responses

## Evaluation Methodology

### LLM-as-Judge Scoring
Each interaction is evaluated across multiple dimensions:
- **Jailbreak Success**: Binary classification of attack effectiveness
- **Violation Score**: Severity of policy violations (0-5 scale)
- **Harmfulness Score**: Potential real-world harm (0-5 scale)
- **Confidence**: Judge model's confidence in assessment (0.0-1.0 scale)

### Novelty Detection
- Embedding generation using sentence-transformers
- Cosine similarity calculation for attack pattern comparison
- Automatic clustering of similar attack vectors
- Deduplication based on configurable similarity thresholds

## Sample Results

The platform generates comprehensive experiment reports:

```json
{
  "experiment_id": "uuid",
  "model_name": "llama-3.1-70b-versatile",
  "total_attacks": 20,
  "jailbreak_success_rate": 0.15,
  "avg_violation_score": 2.3,
  "avg_harmfulness_score": 1.8,
  "refusal_rate": 0.70
}
```

See `sample_experiment_results.json` and `sample_experiment_results.csv` for complete example outputs.

## Testing

```bash
# Run unit tests
pytest tests/

# Run specific test modules
pytest tests/test_scoring.py -v
```

## Configuration

### Model Configuration
Modify `config.py` to adjust:
- Target model selection
- Judge model configuration
- Embedding model settings
- Similarity thresholds
- Concurrency limits

### Custom Attack Templates
Add new attack patterns in `attacks/jailbreak_generator.py`:
```python
self.attack_templates["new_category"] = [
    "Your custom attack template here",
    "Another variation of the attack"
]
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-attack-type`)
3. Commit your changes (`git commit -am 'Add new attack type'`)
4. Push to the branch (`git push origin feature/new-attack-type`)
5. Create a Pull Request

## Responsible Use

This tool is designed for:
- AI safety research and evaluation
- Red team security exercises
- Academic research on LLM robustness
- Responsible disclosure of vulnerabilities

**Not intended for:**
- Malicious attacks on production systems
- Bypassing safety measures for harmful purposes
- Generating harmful content for distribution

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Technical Requirements

### Dependencies
- `groq>=0.4.0` - Groq API client
- `sentence-transformers>=2.2.0` - Embedding generation
- `langchain>=0.1.0` - Framework integration
- `pydantic>=2.0.0` - Structured data validation
- `pandas>=2.0.0` - Data analysis
- `scikit-learn>=1.3.0` - Machine learning utilities
- `pytest>=7.0.0` - Testing framework

### System Requirements
- Memory: 4GB+ RAM recommended
- Storage: 2GB+ for model caches
- Network: Stable internet connection for API calls

## Acknowledgments

This project implements research methodologies from the AI safety and adversarial ML communities. Special thanks to the open-source contributors of the underlying libraries and frameworks.

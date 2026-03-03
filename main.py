#!/usr/bin/env python3
"""
GenAI Red Team & Evaluation Platform
Main entry point for running jailbreak experiments
"""

import asyncio
import argparse
from experiments.runner import ExperimentRunner

async def main():
    parser = argparse.ArgumentParser(description='Run GenAI Red Team Evaluation')
    parser.add_argument('--attacks', type=int, default=20, help='Number of attacks to generate')
    parser.add_argument('--model', type=str, default='llama-3.3-70b-versatile', help='Target model to test')
    parser.add_argument('--output', type=str, help='Output filename for results')
    
    args = parser.parse_args()
    
    print("🔥 GenAI Red Team & Evaluation Platform")
    print("=" * 50)
    
    runner = ExperimentRunner()
    
    # Run the experiment
    result = await runner.run_experiment(
        num_attacks=args.attacks,
        model_name=args.model
    )
    
    # Save results
    runner.save_results(result, args.output)
    
    print("\n✅ Experiment completed successfully!")
    print(f"📊 Check the results in the generated files")

if __name__ == "__main__":
    asyncio.run(main())
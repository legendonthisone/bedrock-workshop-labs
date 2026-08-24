"""Command line interface for the orchestrator agent."""

import argparse
import orchestrator_agent

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", "-p", help="The prompt to send to the agent.", required=True)
    return parser.parse_args()

def main(prompt: str):
    agent = orchestrator_agent.create_orchestrator_agent()
    agent(prompt)

if __name__ == "__main__":
    args = parse_args()
    main(args.prompt)

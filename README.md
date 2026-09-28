# Building with Amazon Bedrock: Workshop Labs

My lab work from the AWS "Building with Amazon Bedrock" workshop (August 2026), following the Strands Agents path: agent fundamentals first, then use-case labs, then deployment to Amazon Bedrock AgentCore Runtime.

## What is here

Everything sits under `agentic-labs/`:

| Folder | What it covers |
|---|---|
| `agents/` | A first Strands agent with math tools |
| `tool-schema/` | Defining a tool with an explicit schema |
| `function-parameters/` | Typed, described tool parameters |
| `messages/` | Running an agent and working with its message history |
| `structured-output/` | Typed output from the model, including a customer support ticket model |
| `event-hooks/` | A hook provider that records every tool call for audit |
| `sub-agents/` | An orchestrator delegating to arithmetic, trigonometry and conversion agents |
| `demo-apps/` | A Streamlit chat app over a reusable agent |
| `runtime-setup/` | Packaging an agent and deploying it to AgentCore Runtime |
| `runtime-client/` | Calling the deployed runtime from a CLI and a Streamlit app |

`learner-profile.md` records the learning path chosen for the workshop.

## What I built from it

[customer-support-agent](https://github.com/legendonthisone/customer-support-agent) is a standalone support agent that reuses these patterns: tools for orders, refunds and FAQs, the tool-call audit hook, and a Streamlit chat UI.

## Honest note

These are workshop labs, run in the workshop's AWS environment, so the structure follows the workshop. My own design work is in the project repos pinned on my profile.

## Stack

Amazon Bedrock · Strands Agents SDK · AgentCore Runtime · Streamlit

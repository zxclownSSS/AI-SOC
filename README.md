# AI-SOC

AI-powered SOC assistant for Wazuh SIEM.

## Features

- AI incident analysis
- IOC extraction
- Severity engine
- Incident normalization
- Human-readable SOC summaries
- Local LLM support via Ollama

## Architecture

Wazuh
↓
Event Pipeline
↓
AI-SOC Core
↓
Incident Analysis
↓
SOC Recommendations

## Stack

- Python
- Ollama
- Qwen 2.5
- Wazuh
- Local LLM

## Status

MVP in development.

## Roadmap

- [x] AI incident analysis
- [x] IOC extraction
- [x] Recommendation engine
- [ ] Event correlation
- [ ] Incident memory
- [ ] Threat intelligence enrichment
- [ ] Wazuh integration
- [ ] SOAR integration
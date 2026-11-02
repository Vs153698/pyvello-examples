# Pyvello Examples & Documentation

Official repository for runnable examples and interactive documentation for [Pyvello](https://pypi.org/project/pyvello/) &mdash; the Python-first AI UI framework with React, shadcn/ui, multi-agent swarms, and automatic graph visualization.

- **Interactive Documentation**: [https://vs153698.github.io/pyvello-examples/](https://vs153698.github.io/pyvello-examples/)
- **PyPI Package**: [https://pypi.org/project/pyvello/](https://pypi.org/project/pyvello/)
- **Issue Tracker**: [https://github.com/Vs153698/pyvello-examples/issues](https://github.com/Vs153698/pyvello-examples/issues)

---

## Quickstart

### 1. Installation

```bash
pip install --upgrade pyvello
```

### 2. Configure Environment

Copy `.env.example` to `.env` in your project root or workspace:

```bash
cp .env.example .env
```

Add your OpenRouter or OpenAI API key:

```env
OPENROUTER_API_KEY=sk-or-v1-...
```

Pyvello automatically discovers parent `.env` files recursively upwards across all directory depths, subfolders, and notebook execution contexts.

---

## Runnable Examples

The `examples/` directory contains complete, standalone scripts:

| Example | Description | Command |
|---|---|---|
| `01_reactive_ui_components.py` | Responsive 2-column layout with metrics, buttons, badges, and callouts | `python examples/01_reactive_ui_components.py` |
| `02_analytics_dashboard.py` | Enterprise SaaS analytics dashboard with interactive sidebar navigation | `python examples/02_analytics_dashboard.py` |
| `03_api_and_tool_studio.py` | Universal API & Tool Studio with live Swagger UI and streaming routes | `python examples/03_api_and_tool_studio.py` |
| `04_multimodal_vision_audio_agent.py` | Omni-agent with native image, video, audio, and PDF generation | `python examples/04_multimodal_vision_audio_agent.py` |
| `05_multiagent_swarm_orchestration.py` | Multi-agent swarm with orchestrator DAG execution and tracing | `python examples/05_multiagent_swarm_orchestration.py` |
| `06_intelligent_model_routing.py` | Model router dispatching queries dynamically between reasoning models | `python examples/06_intelligent_model_routing.py` |
| `07_structured_outputs_pydantic.py` | Strict schema extraction with Pydantic models | `python examples/07_structured_outputs_pydantic.py` |
| `08_document_chat_rag.py` | Document intelligence chat with PDF/text file ingestion | `python examples/08_document_chat_rag.py` |

---

## Interactive Documentation

Read the full interactive guide with searchable API reference, code copy blocks, and component preview:

[Open Interactive Documentation](https://vs153698.github.io/pyvello-examples/)

---

## License

MIT License. See [LICENSE](LICENSE) for details.

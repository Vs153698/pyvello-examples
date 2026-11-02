import pyvello as ui

# 1. Specialized worker agents with distinct OpenRouter models
coder = ui.Agent(
    name="CodingSpecialist",
    model="openrouter/qwen/qwen-2.5-coder-32b-instruct",
    system_prompt="Write production-grade, type-annotated Python code."
)
writer = ui.Agent(
    name="Copywriter",
    model="openrouter/meta-llama/llama-3.3-70b-instruct",
    system_prompt="Draft clear marketing copy and technical documentation."
)

# 2. Semantic Router with high-speed intent classifier
router = ui.Router(
    routes={"code": coder, "marketing": writer},
    classifier_model="openrouter/openai/gpt-4o-mini"
)

# 3. Sequential Chain with step-specific OpenRouter models
chain = ui.PromptChain([
    ui.ChainStep(
        name="Summarize",
        model="openrouter/deepseek/deepseek-chat",
        system_prompt="Summarize this article: {input}"
    ),
    ui.ChainStep(
        name="Translate",
        model="openrouter/google/gemini-2.0-flash-001",
        system_prompt="Translate summary to Spanish: {output_from_step_1}"
    ),
])

# 4. LLM-as-Judge Quality Gate with advanced reasoning model
judge = ui.LLMAsJudge(
    name="QualityJudge",
    model="openrouter/anthropic/claude-3.7-sonnet",
    rubric="Evaluate code for security vulnerabilities, time complexity, and readability.",
    threshold=4.5
)

# 5. Launch actionable multi-agent semantic router interface
app = router.to_app(
    title="Multi-Agent Semantic Router",
    description="Intelligent prompt routing across Qwen 2.5 Coder and Llama 3.3 70B with real-time graph visualization.",
    placeholder="Ask to write Python code or draft product marketing copy...",
    examples=[
        "Write a Python async queue with worker concurrency and retry backoff",
        "Draft a product launch announcement for our reactive UI framework",
    ],
    palette="red",
    
)

if __name__ == "__main__":
    app.launch(port=8080)
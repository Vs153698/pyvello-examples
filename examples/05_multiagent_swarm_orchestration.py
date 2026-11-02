import pyvello as ui

# --------------------------------------------------
# 1. Cheap, deterministic dummy tools
# --------------------------------------------------
@ui.tool
def estimate_saas_market(
    customers: int = 100_000,
    monthly_price: float = 500,
) -> dict:
    """Return a small, deterministic market estimate."""
    return {
        "potential_customers": customers,
        "monthly_price_inr": monthly_price,
        "monthly_market_inr": customers * monthly_price,
        "annual_market_inr": customers * monthly_price * 12,
        "type": "illustrative_estimate",
    }


@ui.tool
def estimate_infrastructure(
    monthly_requests: int = 1_000_000,
    regions: int = 2,
) -> dict:
    """Return a mock infrastructure plan and cost."""
    base_cost = 12_000
    request_cost = (monthly_requests // 100_000) * 500
    region_cost = max(0, regions - 1) * 5_000

    return {
        "monthly_requests": monthly_requests,
        "regions": regions,
        "estimated_monthly_cost_inr": (
            base_cost + request_cost + region_cost
        ),
        "type": "mock_estimate_not_a_cloud_quote",
    }


@ui.tool
def check_compliance(
    stores_phi: bool = False,
    audit_logs: bool = True,
    encryption: bool = True,
) -> dict:
    """Return a basic, non-authoritative compliance checklist."""
    checks = {
        "phi_storage": not stores_phi or encryption,
        "audit_logs": audit_logs,
        "encryption": encryption,
    }

    return {
        "checks": checks,
        "passed": all(checks.values()),
        "warning": (
            "Demo only. Not a HIPAA compliance assessment."
        ),
    }


# --------------------------------------------------
# 2. Specialist workers
# Attach the relevant tool to each worker using tools=[tool_fn]
# --------------------------------------------------

market_worker = ui.agent(
    name="MarketResearcher",
    system_prompt=(
        "You handle market sizing and SaaS unit economics. "
        "Use estimate_saas_market when numerical estimates "
        "are requested. Return at most 3 concise bullets."
    ),
    tools=[estimate_saas_market],
    model="openrouter/deepseek/deepseek-v4.1-flash-1017"
)

infra_worker = ui.agent(
    name="InfraArchitect",
    system_prompt=(
        "You handle cloud architecture, Kubernetes and "
        "multi-region infrastructure. Use the infrastructure "
        "estimator when a numerical estimate is requested. "
        "Return at most 3 concise bullets."
    ),
    tools=[estimate_infrastructure],
    model="openrouter/GPT4o-mini"
)

risk_worker = ui.agent(
    name="RiskAssessor",
    system_prompt=(
        "You handle security, privacy, compliance and "
        "operational risk. Use check_compliance for the "
        "demo checklist. Never claim that the mock check "
        "establishes legal or regulatory compliance. "
        "Return at most 3 concise bullets."
    ),
    tools=[check_compliance],
    model="openrouter/Glm-5.3-flash"
)

# --------------------------------------------------
# 3. Supervisor: delegate only when needed
# --------------------------------------------------

SUPERVISOR_PROMPT = """
You are a routing supervisor.

Available workers:
- MarketResearcher: market sizing, pricing, unit economics.
- InfraArchitect: cloud, Kubernetes, scaling, availability.
- RiskAssessor: privacy, security, compliance, operational risk.

Rules:
1. Select only workers needed to answer the user's request.
2. A single-domain request normally needs one worker.
3. A request spanning multiple domains may need multiple workers.
4. Greetings, simple definitions and unrelated questions need
   zero workers when you can answer directly.
5. Do not invoke every worker by default.
6. Before delegation, emit:
   ROUTING: <worker names, or NONE>
   REASON: <one short sentence>
7. After delegation, synthesize only the returned findings.
8. Keep the final response under 120 words.
9. Do not invent tool results or claim that mock estimates
   are production measurements.
"""

orchestrator = ui.orchestrator(
    agents=[
        market_worker,
        infra_worker,
        risk_worker,
    ],
    supervisor_system_prompt=SUPERVISOR_PROMPT,
    supervisor_model="openrouter/deepseek/deepseek-v4.1-flash-1017",
    models=[
        {"id": "openrouter/deepseek/deepseek-v4.1-flash-1017", "name": "Deepseek (Supervisor)", "badge": "Cloud"},
        {"id": "openrouter/z-ai/glm-5.3-flash", "name": "GLM-5.3 Flash", "badge": "Coding"},
        {"id": "openrouter/openai/gpt-4o-mini", "name": "GPT-4o Mini", "badge": "General"},
    ],
    temperature=0.2,
    stream=True,
)

orchestrator.to_app().launch(reload=True)
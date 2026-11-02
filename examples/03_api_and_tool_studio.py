import json
import pyvello as ui
from pydantic import BaseModel, Field
from typing import Optional, List

app = ui.App(title="API Studio", palette="emerald")

class UserRecord(BaseModel):
    username: str
    email: str
    role: str = Field(default="developer")

# 1. Standard Synchronous GET with Query Parameter
@app.api.get("/api/v1/health")
def health(status_code: int = 200):
    return {"status": "operational", "code": status_code, "service": "api-studio"}

# 2. Asynchronous POST with Pydantic Body Validation
@app.api.post("/api/v1/users")
async def create_user(payload: UserRecord):
    return {"success": True, "created_user": payload.model_dump(), "timestamp": "2026-10-30T12:00:00Z"}

# 3. Dynamic Path Parameter Lookup
@app.api.get("/api/v1/users/{user_id}")
def get_user(user_id: str):
    return {"user_id": user_id, "found": True, "access_tier": "enterprise"}

# 4. Real-time Server-Sent Events (SSE) Streaming
@app.api.stream("/api/v1/ticks")
def stream_ticks(count: int = 5):
    for i in range(count):
        yield {"tick": i, "status": "active", "channel": "telemetry"}

# Rich In-App Operations Console & Live Interactive Tester
with app:
    # 1. Header with direct link to Swagger and System Badges
    with ui.row(class_name="w-full flex-row items-center justify-between pb-3 border-b border-border gap-4"):
        with ui.col(class_name="flex-1 min-w-0 gap-1"):
            ui.title("API Intelligence & Operations Studio", level=1)
            ui.text(
                "Interactive Python REST API gateway, real-time Server-Sent Events (SSE), and embedded client testing console."
            )
        with ui.row(class_name="shrink-0 flex-row items-center gap-2"):
            ui.badge("FastAPI Engine", variant="default")
            ui.badge("OpenAPI 3.1", variant="outline")
            ui.button("Open Swagger UI", href="/swagger", variant="outline", size="sm")

    # 2. Executive API Gateway Metrics
    col1, col2, col3, col4 = ui.columns(4)
    with col1:
        ui.metric("Active Endpoints", 4, delta="4 registered")
    with col2:
        ui.metric("Gateway Protocols", "REST + SSE", delta="Streaming enabled")
    with col3:
        ui.metric("Average Latency", "1.2 ms", delta="-0.3 ms vs target")
    with col4:
        ui.metric("OpenAPI Swagger", "/swagger", delta="Interactive UI")

    # 3. Interactive Route Showcase & In-App Testing Cards
    ui.title("Live Endpoint Explorer & UI Dispatcher", level=2)
    ui.text("Test API handlers directly from the Pyvello UI or query them externally with curl, fetch, or Swagger UI.")

    col_left, col_right = ui.columns(2)

    with col_left:
        # Card 1: Health Check (GET)
        with ui.card("1. GET /api/v1/health", description="Query gateway operational status with customizable response status code"):
            ui.callout("GET /api/v1/health?status_code=200", title="Endpoint Route", variant="info")
            health_code = ui.number_input("Target Status Code", value=200, min_value=200, max_value=599)
            health_output = ui.code('{\n  "status": "operational",\n  "code": 200,\n  "service": "api-studio"\n}', language="json")

            def test_health():
                res = health(status_code=int(health_code.value or 200))
                health_output.value = json.dumps(res, indent=2)

            ui.button("Execute GET Probe", variant="default", on_click=test_health)

        # Card 3: Dynamic Path Parameter Lookup (GET)
        with ui.card("3. GET /api/v1/users/{user_id}", description="Dynamic URL path parameter resolution and record retrieval"):
            ui.callout("GET /api/v1/users/{user_id}", title="Path Parameter Route", variant="info")
            user_id_input = ui.text_input("User ID", value="usr_9042")
            lookup_output = ui.code('{\n  "user_id": "usr_9042",\n  "found": true,\n  "access_tier": "enterprise"\n}', language="json")

            def test_lookup():
                res = get_user(user_id=user_id_input.value or "usr_9042")
                lookup_output.value = json.dumps(res, indent=2)

            ui.button("Lookup User by ID", variant="secondary", on_click=test_lookup)

    with col_right:
        # Card 2: Create User (POST)
        with ui.card("2. POST /api/v1/users", description="Pydantic model validation and asynchronous user ingestion"):
            ui.callout("POST /api/v1/users (Body: JSON)", title="Validated Body Route", variant="info")
            uname = ui.text_input("Username", value="alice_developer")
            uemail = ui.text_input("Email Address", value="alice@example.com")
            urole = ui.select(["developer", "admin", "analyst", "viewer"], label="Assigned Role", value="developer")
            post_output = ui.code('// Response from POST /api/v1/users will appear here', language="json")

            async def test_create_user():
                payload = UserRecord(username=uname.value or "guest", email=uemail.value or "guest@example.com", role=urole.value or "developer")
                res = await create_user(payload=payload)
                post_output.value = json.dumps(res, indent=2)

            ui.button("Post User Payload", variant="default", on_click=test_create_user)

        # Card 4: Real-time SSE Stream (STREAM)
        with ui.card("4. STREAM /api/v1/ticks", description="Server-Sent Events (SSE) live event stream"):
            ui.callout("GET /api/v1/ticks?count=5 (Content-Type: text/event-stream)", title="SSE Stream Route", variant="info")
            ticks_slider = ui.slider("Stream Tick Count", min=1, max=10, value=5)
            stream_output = ui.code('// Real-time SSE event stream output:\n// data: {"tick": 0, "status": "active"}\n// ...', language="json")

            def test_stream():
                events = list(stream_ticks(count=int(ticks_slider.value or 5)))
                stream_output.value = json.dumps(events, indent=2)

            ui.button("Trigger Event Stream", variant="secondary", on_click=test_stream)

    # 4. OpenAPI / Swagger Documentation Card
    with ui.card("Interactive OpenAPI Documentation & Swagger UI", description="Automated OpenAPI 3.1 specification, interactive test playground, and ReDoc"):
        ui.callout(
            "Swagger UI is automatically mounted at /swagger (with aliases at /api/swagger, /api/docs, and /docs/swagger). "
            "You can execute live curl requests, download client schemas, and inspect type definitions directly.",
            title="Swagger Discovery",
            variant="success"
        )
        with ui.row(class_name="items-center gap-3 pt-2"):
            ui.button("Open Swagger UI (/swagger)", href="/swagger", variant="default")
            ui.button("Open ReDoc (/redoc)", href="/redoc", variant="outline")
            ui.button("View OpenAPI JSON (/openapi.json)", href="/openapi.json", variant="ghost")

if __name__ == "__main__":
    app.launch()
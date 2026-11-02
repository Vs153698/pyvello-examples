"""Pyvello Multimodal Chat Component Example.

Demonstrates using pyvello.Chat directly within custom layout blocks with:
- Multimodal image, video, audio, and PDF attachment handling
- Native media generation (Flux/Kolors images, Minimax/Seedance video, TTS audio, PDF documents)
- Real-time streaming with live progress
"""

import os
from typing import Any, Dict, List, Optional
import pyvello as ui

# Multimodal Agent with native image, video, audio, and PDF generation
agent = ui.Agent(
    name="MultimodalEngine",
    model=os.environ.get("PYVELLO_DEFAULT_MODEL", "openrouter/z-ai/glm-5.3-flash"),
    system_prompt=(
        "You are an expert multimodal AI assistant. When a user provides attachments "
        "(images, audio recordings, videos, PDFs, or code/data), inspect and analyze them thoroughly. "
        "You can also natively generate images, videos, spoken audio narration, and executive PDF reports."
    ),
    image=True,
    video=True,
    audio=True,
    pdf=True,
    temperature=0.4,
)

with ui.Blocks(title="Pyvello Multimodal Chat", palette="blue") as demo:
    ui.Title("Multimodal Intelligence Studio", subtitle="Direct pyvello.Chat Component with Media Ingestion & Generation")

    with ui.Card(title="Agent Capabilities & Supported Media"):
        ui.Text(
            "Upload images, videos, audio voice clips, PDFs, or code files. "
            "Ask the agent to generate high-resolution images, video clips, speech audio, or PDF reports.",
            variant="muted",
        )

    # Embed Chat component directly into layout
    chat_comp = ui.Chat(
        agent=agent,
        placeholder="Attach an image, video, voice clip, or ask to generate visual media...",
        examples=[
            "Generate an image of a cybernetic research laboratory with neon lighting",
            "Generate a 5-second cinematic video clip of an astronaut on Mars",
            "Speak this announcement: Welcome to Pyvello Multimodal Intelligence Studio",
            "Create an executive financial PDF document summarizing our Q3 growth",
        ],
        models=[
            {"id": "openrouter/z-ai/glm-5.3-flash", "name": "GLM 5.3 Flash", "badge": "Fast $0.05"},
            {"id": "openrouter/google/gemini-2.0-flash-001", "name": "Gemini 2.0 Flash", "badge": "Multimodal"},
            {"id": "gpt-4o", "name": "OpenAI GPT-4o", "badge": "Flagship"},
        ],
    )

if __name__ == "__main__":
    demo.launch(port=8002)

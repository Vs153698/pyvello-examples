import os
import pyvello as ui

# Single unified omni-agent with native multimodal capabilities (just like ChatGPT)
# Works across any model provider: OpenRouter, OpenAI, or custom/Chinese endpoints
assistant = ui.Agent(
    name="UniversalMultimodalStudio",
    # Primary reasoning model (OpenRouter GLM 5.3 Flash / GPT-4o)
    model=os.environ.get("PYVELLO_DEFAULT_MODEL", "openrouter/z-ai/glm-5.3-flash"),

    # 1. Native Image Generation & Editing: Seedream 5.0, FLUX, Gemini Flash Image, Fal, or DALL-E
    # E.g. image="openrouter/bytedance-seed/seedream-5-0-flash", "bfl/flux-pro-1.1", or "fal/flux/schnell"
    image="openrouter/bytedance-seed/seedream-5-0-flash",

    # 2. Native Video Generation: Kling AI, Runway Gen-3, Luma Ray 2, or Seedance
    # E.g. video="kling/kling-v1", "runway/gen3a_turbo", or "openrouter/bytedance/seedance-2.0-mini"
    video="openrouter/minimax/hailuo-3-max",

    # 3. Native Audio & Voice Synthesis: ElevenLabs, Cartesia, Deepgram, or HeyGen
    # E.g. audio="elevenlabs/multilingual_v2", "cartesia/sonic-english", or "openrouter/heygen/heygen-voice-1-turbo"
    audio="openrouter/heygen/heygen-voice-1-turbo",
    audio_voice="alloy",

    # 4. Native Executive Document & PDF Generation
    pdf=True,

    system_prompt=(
        "You are an advanced multimodal AI assistant. You can converse and reason on complex topics, "
        "and natively generate images, videos, audio narration, and executive PDF documents on demand."
    ),
)

# Launch unified studio app with one command
demo = assistant.to_app(
    title="Universal Multimodal Studio",
    description="Single-chat multi-model AI assistant with native image, video, audio, and PDF generation.",
    placeholder="Ask for an image, video, audio narration, PDF report, or reasoning query...",
)

if __name__ == "__main__":
    demo.launch(port=8005)
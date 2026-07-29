# Task 1.2 (Bonus) – Swapping Pipeline Components

## Current Implementation

The current voice pipeline is:

- STT: Deepgram
- LLM: Google Gemini 2.5 Flash
- TTS: Cartesia

## Example: Swapping the STT Provider

The current implementation initializes Deepgram as the speech recognition provider:

```python
stt = deepgram.STT(
    api_key=DEEPGRAM_API_KEY,
)
```

If Google Cloud Speech-to-Text credentials are available, only this component needs to change:

```python
stt = google.STT(
    credentials_file="service-account.json"
)
```

No other part of the application changes. The Agent, tools, prompts, and business logic remain exactly the same.

## Example: Swapping the TTS Provider

The current implementation uses Cartesia:

```python
tts = cartesia.TTS(
    api_key=CARTESIA_API_KEY,
)
```

If another TTS provider is preferred, only this initialization changes.

For example:

```python
tts = google.TTS(
    credentials_file="service-account.json"
)
```

Again, the rest of the application remains unchanged.

## Why This Design Is Modular

The application is provider-agnostic because the AgentSession receives the STT and TTS components as interchangeable objects.

Only the plugin initialization changes when switching vendors.

The following components remain unchanged:

- FoodSupportAgent
- System Prompt
- Function Tools
- Gemini LLM
- Business Logic

## Provider Comparison

| Component | Current | Alternative |
|----------|---------|-------------|
| STT | Deepgram | Google STT |
| LLM | Gemini 2.5 Flash | Gemini 2.5 Flash |
| TTS | Cartesia | Google TTS |

## Conclusion

Because the voice pipeline is modular, replacing an STT or TTS provider only requires changing the plugin initialization. The remaining application architecture—including the agent, prompts, tool-calling logic, and conversation flow—does not need to be modified.
# Task 1.1 Write-up

## System Architecture

The application follows the standard LiveKit Agent pipeline:

Microphone
↓

Speech-to-Text (Deepgram)

↓

Gemini 2.5 Flash

↓

Function Calling

↓

Text-to-Speech (Cartesia)

↓

Speaker

The LLM is responsible for deciding when a tool should be invoked. If the user asks about an order, the model calls the `get_order_status()` function, which returns a mocked order status.

---

## Barge-in / Interruption Handling

To support barge-in, the AgentSession can enable interruptions while audio is playing. During speech synthesis, incoming user speech is continuously monitored by the Voice Activity Detection (VAD). When the user starts speaking, the current TTS playback can be interrupted, the remaining audio discarded, and a new response generated from the updated transcript.

This approach enables more natural conversations by allowing users to interrupt the assistant without waiting for the response to finish.

---

## Adding a Second Tool

A second tool can be implemented using the same `@function_tool` decorator.

Example:

```python
@function_tool
async def cancel_order(order_id: str):
    ...
```

The tool should include:

- Clear parameter schema.
- Input validation.
- Proper documentation.
- Meaningful return values.

The system prompt should also instruct the LLM when to use each tool.

---

## Error Handling

Every tool should validate its inputs before processing.

Possible errors include:

- Invalid order number.
- Missing parameters.
- External API failures.
- Database connection errors.

Instead of exposing internal exceptions, the tool should return user-friendly messages such as:

> "Sorry, I couldn't retrieve the order information. Please try again later."

Logging should capture technical details for debugging while keeping responses safe for end users.
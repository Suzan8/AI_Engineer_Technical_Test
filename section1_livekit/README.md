# LiveKit Voice Agent – Section 1

## Overview

This project implements a minimal real-time voice assistant using the LiveKit Agents Python SDK.

Pipeline:

Microphone → Deepgram STT → Gemini LLM → Cartesia TTS

The assistant also supports Function Calling through a mocked order lookup tool.

---

## Features

- LiveKit AgentSession
- Speech-to-Text using Deepgram
- Gemini 2.5 Flash LLM
- Text-to-Speech using Cartesia
- Function Calling
- Mock Order Status API
- Voice Conversation

---

## Project Structure

```
section1_livekit/

│── agent.py

│── tools.py

│── prompts.py

│── config.py

│── .env.example

│── requirements.txt

│── README.md

│── transcripts/

└── writeup/
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=

DEEPGRAM_API_KEY=

CARTESIA_API_KEY=
```

---

## Run

```bash
python section1_livekit/agent.py console
```

---

## Example

User

```
Where is my order 1?
```

LLM calls

```
get_order_status("1")
```

Assistant

```
Order #1 is on the way and will arrive in about 15 minutes.
```

---

## Technologies

- LiveKit Agents
- Google Gemini
- Deepgram STT
- Cartesia TTS
- Python
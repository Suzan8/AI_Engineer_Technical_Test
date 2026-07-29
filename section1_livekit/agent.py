from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    WorkerOptions,
    cli,
)

from livekit.plugins import (
    google,
    deepgram,
    cartesia,
)

from config import (
    GOOGLE_API_KEY,
    DEEPGRAM_API_KEY,
    CARTESIA_API_KEY,
)

from prompts import SYSTEM_PROMPT
from tools import FoodTools


class FoodSupportAgent(FoodTools, Agent):

    def __init__(self):

        super().__init__(
            instructions=SYSTEM_PROMPT
        )


async def entrypoint(ctx: JobContext):

    await ctx.connect()

    session = AgentSession(

        stt=deepgram.STT(
            api_key=DEEPGRAM_API_KEY,
        ),

        llm=google.LLM(
            api_key=GOOGLE_API_KEY,
            model="gemini-2.5-flash",
            max_output_tokens=128,
        ),

        tts=cartesia.TTS(
            api_key=CARTESIA_API_KEY,
        ),

    )

    await session.start(
        room=ctx.room,
        agent=FoodSupportAgent(),
    )

    print("=" * 50)
    print("Food Delivery Voice Agent Started")
    print("=" * 50)

    try:
        await session.generate_reply(
            instructions="Greet the user briefly."
        )
    except Exception:
        pass


if __name__ == "__main__":

    cli.run_app(

        WorkerOptions(

            entrypoint_fnc=entrypoint,

        )

    )
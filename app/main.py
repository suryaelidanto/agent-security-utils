from fastapi import FastAPI

from app import services
from app.models import (
    AgentRequest,
    DefenseResponse,
    FuzzyMatchResponse,
    SentimentResponse,
)

app = FastAPI(
    title="Agent Security Utils API",
    description="Security firewall and utility endpoints for LLM agents.",
    version="1.0.0",
)


@app.get("/")
async def health_check():
    return {"status": "ok", "service": "Agent Security Utils"}


@app.post("/fuzzy-match", response_model=FuzzyMatchResponse)
async def fuzzy_match(data: AgentRequest):
    """Compare two strings and return similarity score."""
    if not data.target_text:
        return FuzzyMatchResponse(score=0.0, input=data.input_text, target="N/A")

    score = services.get_fuzzy_score(data.input_text, data.target_text)
    return FuzzyMatchResponse(
        score=score, input=data.input_text, target=data.target_text
    )


@app.post("/prompt-defense", response_model=DefenseResponse)
async def prompt_defense(data: AgentRequest):
    """Detect prompt injection and malicious attempts."""
    return services.check_prompt_security(data.input_text)


@app.post("/prompt-sentiment", response_model=SentimentResponse)
async def prompt_sentiment(data: AgentRequest):
    """Analyze the emotional tone of the input text."""
    return services.analyze_sentiment(data.input_text)

from fastapi import FastAPI

app = FastAPI(title="DevPulse")


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}

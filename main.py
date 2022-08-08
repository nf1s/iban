import uvicorn
from fastapi import FastAPI


def init_app():
    app = FastAPI(title="iban")

    @app.get("/health", status_code=200)
    async def health():
        return {"status": "OK"}

    from api.v1 import views

    app.include_router(views.router)

    return app


if __name__ == "__main__":
    app = init_app()
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)

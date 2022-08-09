import uvicorn
from fastapi import FastAPI


def init_app():
    app = FastAPI(title="iban")

    @app.get("/health", status_code=200)
    async def health():
        return {"status": "OK"}

    from api.v1 import errors, views

    app.include_router(views.router)
    errors.register_errors(app)

    return app


app = init_app()
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)

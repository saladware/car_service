from uvicorn import run
from app import app, config


if __name__ == '__main__':
    run(
        app=app,
        host=config.APP_HOST,
        port=int(config.APP_PORT)
    )

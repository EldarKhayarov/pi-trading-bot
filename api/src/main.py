import os

import uvicorn
from fastapi import FastAPI

from routes import router


# If .env is not exists at /api folder, exception raises.
if not os.path.isfile('../.env'):
    raise FileNotFoundError('Config .env file is required.')


# Import values from .env file
HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
PORT = int(os.environ.get('SERVER_PORT', 8888))
DEBUG = os.environ.get('DEBUG', False)


app = FastAPI()
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('main:app', host=HOST, port=PORT, reload=DEBUG)

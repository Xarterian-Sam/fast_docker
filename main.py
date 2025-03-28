from fastapi import FastApi, APIRouter
from fastapi.middleware import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse


app: FastApi = FastApi(
    title = "FastApi User",
    description = "A simple API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

class SendPrompt(BaseModel):
    """
    pydantic model to send prompt
    """
    prompt : str

router = APIRouter()

@router.post("/prompt")
async def send_prompt(prompt : SendPrompt) -> JSONResponse:
    """
    This will take in prompt from user
    args:
        prompt: str
    returns:
        response: str
    raises:
        ...
    """
    try:
        pass
    except Exception as e:
        pass
    
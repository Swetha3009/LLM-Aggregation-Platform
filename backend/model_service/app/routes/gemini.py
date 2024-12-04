import os

from fastapi import FastAPI, HTTPException
from fastapi import APIRouter
import google.generativeai as genai

from app.models.common_models import PromptRequest

router = APIRouter()

# Configure the Gemini API client
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@router.post("/chat_gemini")
async def generate_text(request: PromptRequest):
    try:
        # Select the desired model
        model = genai.GenerativeModel('gemini-1.5-flash')
        # Generate content based on the prompt
        response = model.generate_content(request.prompt)
        
        # TODO:
        # store in redis
        # return some result to user
        # background process -> store to dynamo db
        
        return {"generated_text": response.text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from fastapi import APIRouter
from pydantic import BaseModel
from app.dependencies import enhance_prompt_with_gemini, generate_video_with_veo

router = APIRouter()

class VideoRequest(BaseModel):
    prompt: str

@router.post("/generate-video/")
async def generate_video(request: VideoRequest):
    enhanced_prompt = await enhance_prompt_with_gemini(request.prompt)
    video_url = await generate_video_with_veo(enhanced_prompt)
    return {"video_url": video_url}
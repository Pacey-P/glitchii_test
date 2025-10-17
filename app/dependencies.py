import google.generativeai as genai
import asyncio
import random
import string
from .config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

async def enhance_prompt_with_gemini(prompt: str) -> str:
    """
    Enhances the given prompt using the Gemini API.
    """
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = await model.generate_content_async(f"Enhance the following prompt for a video generation model: {prompt}")
    return response.text

class MockVeoClient:
    async def generate_video(self, prompt: str) -> str:
        """
        Simulates video generation with Veo.
        """
        print(f"Generating video for prompt: {prompt}")
        await asyncio.sleep(5)  # Simulate a 5-second video generation time
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        video_url = f"https://example.com/mock_video_{random_string}.mp4"
        print(f"Video generated: {video_url}")
        return video_url

veo_client = MockVeoClient()

async def generate_video_with_veo(prompt: str) -> str:
    """
    Generates a video with Veo using the mock client.
    """
    return await veo_client.generate_video(prompt)
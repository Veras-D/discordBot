import aiohttp
import os

BASE_URL = "https://api.giphy.com/v1/gifs/random"
GIPHY_API_KEY = os.getenv("GIPHY_API_KEY")

async def get_gif(tag):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BASE_URL}?api_key={GIPHY_API_KEY}&tag={tag}&rating=pg-13") as response:
            if response.status == 200:
                data = await response.json()
                return data["data"]["images"]["original"]["url"]
            return None


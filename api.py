import aiohttp
import asyncio
import logging
from typing import Optional, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AsyncAPIClient:
    def __init__(self, base_url: str, username: Optional[str] = None, password: Optional[str] = None):
        self.base_url = base_url
        self.auth = aiohttp.BasicAuth(login=username, password=password) if username and password else None
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    async def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers, params=params, auth=self.auth) as response:
                response.raise_for_status()
                return await response.json()

    async def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self.headers, json=data, auth=self.auth) as response:
                response.raise_for_status()
                return await response.json()

    async def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        async with aiohttp.ClientSession() as session:
            async with session.put(url, headers=self.headers, json=data, auth=self.auth) as response:
                response.raise_for_status()
                return await response.json()

    async def delete(self, endpoint: str) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, headers=self.headers, auth=self.auth) as response:
                response.raise_for_status()
                return await response.json()

##### Example usage of the AsyncAPIClient #####
async def main():
    client = AsyncAPIClient(base_url="https://api.example.com", username="user", password="pass")

    # GET request example
    response = await client.get("resource")
    logger.info(f"GET response: {response}")

    # POST request example
    post_data = {"key": "value"}
    response = await client.post("resource", data=post_data)
    logger.info(f"POST response: {response}")

    # PUT request example
    put_data = {"key": "new_value"}
    response = await client.put("resource/1", data=put_data)
    logger.info(f"PUT response: {response}")

    # DELETE request example
    response = await client.delete("resource/1")
    logger.info(f"DELETE response: {response}")

# Run the example
if __name__ == "__main__":
    asyncio.run(main())

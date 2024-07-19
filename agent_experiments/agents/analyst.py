import os
import json
import autogen
from autogen import AssistantAgent
from agent import Agent
import httpx
from typing import List, Tuple, Union, Dict


#WEATHER_API_URL = "http://127.0.0.1:8000/weather"

 

class ThreatAnalyst(AssistantAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, llm_config=False, **kwargs)
        self.register_reply(Agent, ThreatAnalyst.get_weather)

    async def get_threats(
        self,
        messages: List[Dict] = [],
        sender=None,
        config=None,
    ) -> Tuple[bool, Union[str, Dict, None]]:
        
        last_message = messages[-1]["content"]
        result = await get_threats(last_message)
        return True, result

    async def fetch_threat_data(data: json) -> json:
        async with httpx.AsyncClient() as client:
            
            result = await client.post(
                WEATHER_API_URL,
                json={"city": question},
            )
            return result.json()


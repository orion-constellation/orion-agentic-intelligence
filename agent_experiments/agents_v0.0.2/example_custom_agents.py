'''
Custom Agents for use by the Autogen Platform as well as reporting
https://clintgoodman27.medium.com/a-practical-guide-for-using-autogen-in-software-applications-8799185d27ee


'''
import autogen
from autogen import AssistantAgent, Agent
import json
from typing import List, Union, Dict, Optional
from pydantic import BaseModel, Field, IPvAnyAddress
from typing import List, Literal, Optional
from datetime import datetime

class ECS(BaseModel):
    version: str

class Event(BaseModel):
    category: str
    kind: str
    type: List[Literal['info', 'error']]
    outcome: List[Literal['success', 'failure']]
    module: str
    action: str

class OS(BaseModel):
    name: str
    version: str

class Host(BaseModel):
    hostname: str
    ip: IPvAnyAddress
    os: OS

class Source(BaseModel):
    ip: IPvAnyAddress
    port: int

class Destination(BaseModel):
    ip: IPvAnyAddress
    port: int

class LogEntry(BaseModel):
    ecs: ECS
    event: Event
    host: Host
    source: Source
    destination: Destination
    message: str
    timestamp: datetime = Field(alias='@timestamp')


    
    
 

class AnalystAgent(AssistantAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, llm_config=False, **kwargs)
        self.register_reply(Agent, AnalystAgent.get_data)

    async def get_data(
        self,
        messages: List[Dict] = [],
        sender=None,
        config=None,
    ) -> json[bool, Union[str, Dict, None]]:
        last_message = messages[-1]["content"]
        result = await fetch_weather(last_message)
        return True, result

async def fetch_threat_data(data: json) -> str:
    async with httpx.AsyncClient() as client:
        result = await client.post(
            THREAT_FEED_URL,
            json={"threats": data},
        )
        return result.json()


assistant = AssistantAgent(name="assistant")
weather_assistant = AnalystAgent(name="cyber_analyst")
user_proxy = autogen.UserProxyAgent(name="user_proxy")
await user_proxy.a_initiate_chat(assistant, message="Lehi")
print(weather_assistant.last_message)
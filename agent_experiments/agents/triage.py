import autogen
from autogen import AssistantAgent, UserProxyAgent
from agent import Agent
from typing import Tuple, Dict, Union
import httpx


class TriageAgent(AssistantAgent):
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



"""
MAIN EXECUTION: All the classes and associated super classes are imported here
where control flow is handled




"""
import os
import json


import autogen
import weave 
from analyst import ThreatAnalyst
from group import GroupChat, GroupChatManager, CustomGroupChat
from chat import ResumableGroupChatManager
from quart import Quart, Request, query_blueprint, request


import autogen
import wandb
import requests
import analyst
import triage
import httpx
from quart import Quart, Request, query_blueprint, request
from group import ResumableGroupChatManager
from analyst import ThreatAnalyst
from autogen import GroupChat, GroupChatManager
from dotenv import load_dotenv
load_dotenv()

llm_config = {"model": "gpt-4o", "max_tokens": 250, "temperature": 0.0}     
wandb.login(key=os.getenv("WEAVE_API_KEY"))
run=wandb.init(project="Orion-Agents", entity="orion-ai", reinit=True)

@weave.op()
@query_blueprint.route("/query", methods=["POST", "GET"])
async def post_query():
    
    message = request.form.get("message")


    ###INIT THREAT ANALYST
    threat_analyst = ThreatAnalyst(
        name="threat_analyst",
        system_message="""You are a professional cyber intelligence threat analyst.
        You use everything available to you to 1. Develop a hypothesis. 2. initiate reconnaisance on the identified threat 3. Use appropriate channels to alert."""
    )
    user_proxy = autogen.UserProxyAgent(
        name="user_proxy",
        human_input_mode="NEVER",
        code_execution_config=False,
        is_termination_msg=lambda message: True # Always True
    )
 
    triage_agent = autogen.TriageAssistant(
        name="triage_agent",
        system_message="""You are a rigid threat intelligence triage assistant.
        Adhere to the MiTRE Attack framework in making your decision based on the threat."""
    )
    
    @weave.op()
    async def start_triage(threat: json) -> json:
        async with httpx.AsyncClient() as client:
            result = await client.post(
                threat,
                json={"threat": threat},
            )

    groupchat = autogen.GroupChat(
    agents=[threat_analyst, user_proxy, triage_agent, manager],
    messages=[]
    )
    
    manager = ResumableGroupChatManager(
    name="Cyber Manager",
    groupchat=groupchat,
    llm_config=llm_config,
    )


    await user_proxy.a_initiate_chat(manager, message=message)

    return {
    "response": groupchat.messages[-1],
    "history": groupchat.messages,
    }

post_query()

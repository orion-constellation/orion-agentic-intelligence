'''
Autogen general agents:




'''
import os
import autogen
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def init_agents(openai_api_key=os.getenv("OPENAI_API_KEY")):
    config_list = autogen.config_list_from_json(
        "OAI_CONFIG_LIST",
        filter_dict={
            "model": ["gpt-4o"],
        },
    )
    llm_config = {"config_list": config_list, "cache_seed": 42, "model": "gpt-4o", "api_key": os.environ["OPENAI_API_KEY"]}
    
    user_proxy = autogen.UserProxyAgent(
        name="User_proxy",
        system_message="A human senior threat analyst director.",
        code_execution_config={
            "last_n_messages": 2,
            "work_dir": "groupchat",
            "use_docker": True'',
        },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
        human_input_mode="TERMINATE",
    )
    coder = autogen.AssistantAgent(
        name="threat_cyber_triage_agent",
        system_message="Triages threat type (0:Low, 1:Medium, 2:High) and severity (0:Low, 1: Moderate, 3:Severe)",
        llm_config=llm_config,
    )
    threat_analyst = autogen.AssistantAgent(
        name="threat_data_analyst",
        system_message="Summarizes Data. Outputs in JSON with fields {'date: dd/mm/yyyy','data: dict','summary: str'}. Do not go off task and engage with the Triage Agent and Manager",
        llm_config=llm_config,
    )
    groupchat = autogen.GroupChat(agents=[user_proxy, coder, threat_analyst], messages=[], max_round=12)
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)
    
    user_proxy.initiate_chat(
    manager, message="Analyse the input json file"
)

init_agents()

    


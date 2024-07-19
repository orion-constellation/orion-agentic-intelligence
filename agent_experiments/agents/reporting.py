import autogen
import os
import json 
from autogen import AssistantAgent
from dotenv import load_dotenv
from typing import Tuple, Dict, Union
load_dotenv()

llm_config = {"model": "gpt-4o", "max_tokens": 250, "temperature": 0.0}

def analysis_report(source: json, llm_config=llm_config) -> Tuple[bool, Union[str, Dict, None]]:
    analyst = autogen.AssistantAgent(
        name="Analyst",
        system_message=f"""You're a cyber analyst. Prepare all data from {source} in complete JSON. Take your time.""",
        llm_config=llm_config,
    )

    summarizer = autogen.AssistantAgent(
        name="Summarizer",
        system_message="""You summarize the data passed to you into a detailed written report report""",
        llm_config=llm_config,
    )
    
    return analyst, summarizer
    


def generate_report(input):
    analyst, summarizer = analysis_report()
    print(analyst)
    print(summarizer)

analysis_report() 
generate_report()


"""    
analysis = analyst.generate_oai_reply(report)[1]
summary = summarizer.generate_oai_reply(report)[1]

print(f"Analysis: {analysis}")
print(f"Summary: {summary}")"""
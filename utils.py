import openai
from openai import _exceptions
import os

def set_model(temperature=0.1, provider="openai", max_tokens=250, model="gpt-4o"):
    if provider == "openai":
        try:
            model == "gpt-4o"
        except Exception as e:
            model == "gpt-3.5-turbo"
    return model
        

try:
    from termcolor import colored
except ImportError:

    def colored(x, *args, **kwargs):
        return x


def set_threat_level(threats_min, average_severity, anticipated_threat):
    if threats_min/60 * average_severity * (1.2*anticipated_threat) >= :
        
    


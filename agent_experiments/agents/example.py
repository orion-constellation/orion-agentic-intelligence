import autogen
import requests
from quart import Quart, request, jsonify, Blueprint

app = Quart(__name__)
query_blueprint = Blueprint('query_blueprint', __name__)


# user makes a POST /query { "message": "What's the weather?" }

llm_config = {"model": "gpt-4o", "max_tokens": 250, "temperature": 0.1}

@query_blueprint.route("/query", methods=["POST"])
async def post_query():
  message = request.form.get("message")

  assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config
    system_message="""You're a helpful assistant.
    If you need more info, ask the user for anything missing."""
  )
  user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    code_execution_config=False,
    is_termination_msg=lambda message: True # Always True
  )
  weather_assistant = WeatherAgent(
    name="weather_assistant",
    system_message="""You're a helpful assistant to get the weather.
    You fetch weather information, then return it."""
  )

  groupchat = autogen.GroupChat(
    agents=[assistant, user_proxy, weather_assistant],
    messages=[]
  )
  manager = autogen.GroupChatManager(
    name="Manager",
    groupchat=groupchat,
    llm_config=llm_config,
  )

  await user_proxy.a_initiate_chat(manager, message=message)

  return groupchat.messages[-1]
# user makes a POST /query { "message": "What's the weather?" }
#https://clintgoodman27.medium.com/a-practical-guide-for-using-autogen-in-software-applications-8799185d27ee
import autogen
from example_custom_agents import AnalystAgent 
import httpx 

@query_blueprint.route("/query", methods=["POST"])
async def post_query():
  message = request.form.get("message")
  analyst_agent = AnalystAgent()
  assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=analyst_agent.llm_config,
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

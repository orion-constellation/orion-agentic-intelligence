"""
Custom Class for the Group:



"""
import os
from typing import List
from agent import Agent
import autogen
from autogen import GroupChat, GroupChatManager, AssistantAgent, UserProxyAgent




short_role_descriptions = {
  "user_proxy": "A proxy for the user. Discerning and critical",
  "analyst": "You can analyse incoming data with certainty. If you are unsure ask questions.",
  "triage_agent": "You help coordinate the plan. Your turn happens when analyst asks you a question but skip your turn when \
      {manager} has a question"
}


class CustomGroupChat(GroupChat):
    # The default message uses the full system message, which is a long string.  We are overriding this to use a shorter message.
    def select_speaker_msg(self, agents: List[Agent]):
        message = f"""You are in a role play game. The following roles are available:
        ---
        {new_line.join([f"{agent.name}: {short_role_descriptions[agent.name]}" for agent in agents])}
        ---

        The role who plays next depends on the conversation.  User_Proxy will star the conversation, and typically Planner would go next.

        Here are some examples
        ---
        ... not shown here ...
        ---

        Read the following conversation.
        Then select the next role from {', '.join([agent.name for agent in agents])} to play. Only return the role."""
        return message
    


class ResumableGroupChatManager(GroupChatManager):
    groupchat: GroupChat

    def __init__(self, groupchat, history, **kwargs):
        self.groupchat = groupchat
        if history:
            self.groupchat.messages = history
            super().__init__(groupchat, **kwargs)
            self.restore_from_history(history)

    def restore_from_history(self, history) -> None:
        for message in history:
        # broadcast the message to all agents except the speaker.  This idea is the same way GroupChat is implemented in AutoGen for new messages, this method simply allows us to replay old messages first.
            for agent in self.groupchat.agents:
                if agent != self:
                    self.send(message, agent, request_reply=False, silent=True)

   
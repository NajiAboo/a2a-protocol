from a2a.server.agent_execution import AgentExecutor
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message


class HelloWoldAgent():
    async def invoke(self) -> str:
        return "Hello world"
    
class HelloWorldAgentExecutor(AgentExecutor):
    def __init__(self):
        self.agent = HelloWoldAgent()

    async def execute(self, context, event_queue):
        result =  await self.agent.invoke()
        await event_queue.enqueue_event(new_agent_text_message(result))
    
    async def cancel(self, context, event_queue):
        raise Exception("Cancel not supporte")
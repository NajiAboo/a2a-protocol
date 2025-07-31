import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import ( AgentCapabilities, AgentCard, AgentSkill)


from agent_executor import HelloWorldAgentExecutor


if __name__ == "__main__":

    skill = AgentSkill(
        id="helloword",
        name="returns hello world",
        description="Just return hello world",
        tags=["hello world"],
        examples=["hi", "hello", "world"]
    )

    agent_card = AgentCard(
        name="hello world agent", 
        description="Just hello world", 
        url="http://localhost:9999",
        version="1.0.0", 
        default_input_modes=["text"],
        default_output_modes=["text"],
        capabilities=AgentCapabilities(streaming=True),
        skills=[skill]
    )

    request_handler = DefaultRequestHandler(
        agent_executor=HelloWorldAgentExecutor(), 
        task_store=InMemoryTaskStore()
    )

    server = A2AStarletteApplication(
        agent_card=agent_card, 
        http_handler=request_handler
    )

    uvicorn.run(server.build(), host="0.0.0.0", port=9999)
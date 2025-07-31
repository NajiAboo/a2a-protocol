from typing import Any
from uuid import uuid4
import httpx

from a2a.client import A2ACardResolver, A2AClient
from a2a.types import ( MessageSendParams, SendMessageRequest)

async def main() -> None:
    PUBLIC_AGENT_CARD = "./well-knows/agent.json"
    base_url = "http://localhost:9999"

    async with httpx.AsyncClient() as httpx_client:

        resolver = A2ACardResolver(
            httpx_client=httpx_client, 
            base_url=base_url
        )

        final_agent_card = await resolver.get_agent_card()

        client = A2AClient(httpx_client=httpx_client, agent_card=final_agent_card)

        send_mg_payload : dict[str, Any] = {
            'message': {
                'role': 'user', 
                'parts': [
                    {
                        "kind": "text", "text": "how to convert $10 to INR"
                    }
                ], 
                "messageId": uuid4().hex,
            },
        }

        reqest = SendMessageRequest(
            id=str(uuid4()), params=MessageSendParams(**send_mg_payload)
        )

        response = await client.send_message(request=reqest)

        print(response.model_dump(mode="json", exclude=None))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())


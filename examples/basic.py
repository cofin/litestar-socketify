from __future__ import annotations

from litestar import Controller, Litestar, get

from litestar_socketify import SocketifyPlugin


class SampleController(Controller):
    @get(path="/sample")
    async def sample_route(self) -> dict[str, str]:
        """Sample Route."""
        return {"sample": "hello-world"}


app = Litestar(plugins=[SocketifyPlugin()], route_handlers=[SampleController])

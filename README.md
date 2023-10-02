# Litestar Socketify Plugin

> [!WARNING]  
> Socketify currently has an issue with ASGI lifespans. This plugin is experimental (at best)

## Installation

```shell
pip install litestar-socketify
```

## Usage

Here is a basic application that demonstrates how to use the plugin.

```python
from __future__ import annotations

from litestar import Controller, Litestar, get

from litestar_socketify import SocketifyPlugin


class SampleController(Controller):
    @get(path="/sample")
    async def sample_route(self ) -> dict[str, str]:
        """Sample Route."""
        return {"sample": "hello-world"}


app = Litestar(plugins=[SocketifyPlugin()], route_handlers=[SampleController])

```

Now, you can use the standard Litestar CLI and it will run with Socketify instead of Uvicorn.

```shell
❯ litestar --app examples.basic:app run
Using Litestar app from env: 'examples.basic:app'
Starting socketify server process ──────────────────────────────────────────────
┌──────────────────────────────┬──────────────────────┐
│ Litestar version             │ 2.1.1                │
│ Debug mode                   │ Disabled             │
│ Python Debugger on exception │ Disabled             │
│ CORS                         │ Disabled             │
│ CSRF                         │ Disabled             │
│ OpenAPI                      │ Enabled path=/schema │
│ Compression                  │ Disabled             │
└──────────────────────────────┴──────────────────────┘
...
```

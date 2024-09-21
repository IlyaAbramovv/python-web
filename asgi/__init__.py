from typing import Any, Awaitable, Callable

from asgi.handler.Factorial import Factorial
from asgi.handler.Mean import Mean
from asgi.handler.base import Errors
from asgi.handler.Fibonacci import Fibonacci


async def application(
        scope: dict[str, Any],
        recieve: Callable[[], Awaitable[dict[str, Any]]],
        send: Callable[[dict[str, Any]], Awaitable[None]],
) -> None:
    method = scope['method']
    path = scope['path']
    path_splitted = path.strip('/').split('/')
    if not path_splitted:
        await Errors.send_404(send)
    match (path_splitted[0], method):
        case ('factorial', 'GET'):
            await Factorial(scope, recieve, send).handle()
        case ('fibonacci', 'GET'):
            await Fibonacci(scope, recieve, send).handle()
        case ('mean', 'GET'):
            await Mean(scope, recieve, send).handle()
        case _:
            await Errors.send_404(send)

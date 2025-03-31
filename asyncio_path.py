import sys
import types

# Replace 'async' with 'async_' in the asyncio module
if sys.version_info >= (3, 7):
    import asyncio.tasks
    if hasattr(asyncio.tasks, 'async'):
        setattr(asyncio.tasks, 'async_', getattr(asyncio.tasks, 'async'))
        delattr(asyncio.tasks, 'async')

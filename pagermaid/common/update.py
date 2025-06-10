from os import environ
from sys import executable

from pagermaid.utils import execute


async def update(force: bool = False):
    await execute("git fetch --all")
    if force:
        await execute("git reset --hard origin/main")
    await execute("git pull --all")
    if environ.get("VIRTUAL_ENV"):
        await execute("uv sync")
        await execute("uv cache clean")
        await execute("uv cache prune")
    else:
        await execute(f"{executable} -m pip install --upgrade -r requirements.txt")
        await execute(f"{executable} -m pip install -r requirements.txt")

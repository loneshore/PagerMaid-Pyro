from os import environ

from pagermaid.utils import execute, package_install_shell_command


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
        await execute(
            package_install_shell_command(["--upgrade", "-r", "requirements.txt"])
        )
        await execute(package_install_shell_command(["-r", "requirements.txt"]))

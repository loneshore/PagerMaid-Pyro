import os
from sys import exit

from pagermaid.common.update import update as update_function
from pagermaid.enums import Message
from pagermaid.listener import listener
from pagermaid.utils import lang


@listener(
    is_plugin=False,
    outgoing=True,
    command="update",
    need_admin=True,
    description=lang("update_des"),
    parameters="<true/debug>",
)
async def update(message: Message):
    if os.path.exists("/.dockerenv"):
        await message.edit("Docker 容器环境不支持自动更新，请重新拉取镜像更新。")
        return

    await update_function(len(message.parameter) > 0)
    await message.edit(lang("update_success"))
    exit(0)

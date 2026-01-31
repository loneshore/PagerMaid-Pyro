FROM python:alpine

ENV TZ=Asia/Shanghai
ENV UV_NO_DEV=true
ENV UV_LINK_MODE=copy
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /pagermaid/workdir

COPY . .

RUN --mount=type=cache,target=/root/.cache/uv \
    apk add --no-cache -u ca-certificates curl fastfetch git tini tzdata \
    && apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev linux-headers \
    && ln -sf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo "$TZ" > /etc/timezone \
    && git config --global pull.ff only \
    && curl -LsSf https://astral.sh/uv/install.sh | sh \
    && uv sync \
    && apk del .build-deps

ENTRYPOINT ["tini", "--"]

CMD ["uv", "run", "sh", "utils/docker-config.sh"]

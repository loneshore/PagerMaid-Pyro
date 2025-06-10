FROM alpine

ENV SHELL=/bin/bash
ENV TZ=Asia/Shanghai
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /pagermaid/workdir

COPY . .

RUN apk add --no-cache bash ca-certificates curl fastfetch git python3 tini tzdata \
    && apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev linux-headers \
    && git config --global pull.ff only \
    && curl -LsSf https://astral.sh/uv/install.sh | sh \
    && uv sync \
    && uv cache clean \
    && uv cache prune \
    && apk del .build-deps

ENTRYPOINT ["tini", "--"]

CMD ["uv", "run", "bash", "utils/docker-config.sh"]

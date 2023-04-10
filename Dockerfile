# Kang-sticker-pack
FROM ghcr.io/breakdowns/mega-sdk-python:latest

WORKDIR /app

RUN chmod 777 /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -U -r requirements.txt

COPY Stickerbot/kang.py Stickerbot/clone.py Stickerbot/__main__.py ./

CMD ["python3", "__main__.py"]


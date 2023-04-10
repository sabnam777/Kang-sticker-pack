# StickerBot

StickerBot is a Telegram bot that allows users to create and manage their own custom sticker packs. It uses the Pyrogram library for interacting with the Telegram API, and Mega SDK Python for storing the sticker files.

## Installation

To use StickerBot, you'll need to have Python 3.8 or higher installed on your system. Then, follow these steps:

1. Clone this repository to your local machine.

2. Navigate to the directory where you cloned the repository.

3. Run `pip install -r requirements.txt` to install the required Python dependencies.

4. Set your Telegram bot token and other environment variables in the `.env` file.

5. Run `python3 main.py` to start the bot.

## Usage

StickerBot supports the following commands:

- `/newpack` - Create a new sticker pack.

- `/addsticker` - Add a sticker to an existing pack.

- `/delsticker` - Remove a sticker from a pack.

- `/delpack` - Delete a pack.

- `/getlink` - Get a link to share a pack.

When creating a new pack or adding a sticker, you can either upload the sticker file directly to Telegram, or provide a URL where the file can be downloaded. StickerBot will automatically upload the file to the Mega cloud storage and generate a link for it.

## Contributing

Contributions to StickerBot are welcome! If you find a bug or have a feature request, please open an issue on the project's GitHub repository. If you'd like to contribute code, please fork the repository and submit a pull request with your changes.

To run the tests for the project, install the development dependencies with `pip install -r requirements-dev.txt`, then run `pytest`.

## License

StickerBot is licensed under the MIT License. See the `LICENSE` file for more details.

er-pack

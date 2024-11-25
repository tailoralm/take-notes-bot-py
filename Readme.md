# Telegram Files & Notes Bot

This project focuses on developing a Telegram bot designed to assist users in saving files, such as receipts, documents, photos and notes directly from Telegram to a server.

## Recommendations

I use this project on a [private server](https://medium.com/@guido567/a-comprehensive-guide-to-self-hosting-hardware-software-and-connectivity-solutions-b63182d02552) with [FileBrowser](https://github.com/filebrowser/filebrowser), so i can send my stuffs via Telegram anytime and access them in the computer using the browser.

## Features

- **File Saving:** Users can send documents, images, and notes to the bot, which then stores these files on a server.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. The project is containerized using Docker, ensuring an easy setup and consistent environment across different machines.

### Prerequisites

- Docker
- A Telegram Bot Token (obtainable through BotFather on Telegram)

### Installation

1. **Setup Environment Variables**

   Create a `.env` file in the root directory of the project

    ```plaintext
    TELEGRAM_TOKEN='your telegram bot token'
    MY_TELEGRAM_ID='your chat id with the bot'
    ```

2. **Run**

## Usage

Just send your stuffs to the bot, he will save for you.

If you send an audio, the bot will transcript the audio for you.


## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to create an issue or pull request.

## License

This project is licensed under the [MIT License](LICENSE.md) - see the LICENSE file for details.


# Async ImageGen Bot

Welcome to **Async ImageGen Bot** – a cutting-edge Telegram bot that leverages state-of-the-art Huggingface image generation models to create stunning images in real time. Built using modern asynchronous Python, Redis caching, and containerized for scalability, this project is designed to deliver seamless and lightning-fast performance for image generation enthusiasts and developers alike.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview

The **Async ImageGen Bot** integrates two powerful Huggingface image-generation models:
- **FLUX.1-dev**: Generates high-quality images with a focus on photorealism.
- **stable-diffusion-3.5-large**: Produces images using advanced diffusion techniques for a unique artistic flair.

This bot accepts textual prompts via Telegram, processes them asynchronously using python-telegram-bot v20+, and fetches images via Huggingface's API with optimized error handling, Redis caching, and structured logging. Whether you need single or dual model generations, our bot seamlessly handles requests with minimal latency.

---

## Features

- **Asynchronous Processing**: Utilizes [httpx](https://www.python-httpx.org/) and asyncio for non-blocking API calls.
- **Dual Model Integration**: Choose from FLUX or Stable Diffusion, or use both concurrently.
- **Caching with Redis**: Minimizes redundant API calls to boost performance and reduce costs.
- **Structured Logging**: Simplifies debugging and production-level monitoring with JSON formatted logs.
- **Scalable & Containerized**: Easily deployable using Docker and orchestrated with Kubernetes for high-availability environments.
- **Open Source**: Fully built using open source tools and libraries — no paid solutions required!

---

## Architecture

The bot comprises several key components:

- **config.py**: Contains configuration settings and environment variable management, including API tokens and Redis configuration.
- **models.py**: Implements asynchronous integration with Huggingface models using `httpx` and caches results via Redis.
- **commands.py**: Provides asynchronous command handlers for the Telegram bot to process and respond to user commands.
- **monitoring.py**: Structured logging and error tracking using JSON logs.
- **main.py**: The main entry point that initializes the Telegram bot and manages the asynchronous event loop.
- **Dockerfile**: Ensures the bot can be containerized and deployed consistently across environments.

---

## Getting Started

### Prerequisites

- **Python 3.9+**: Ensure you have a modern Python version installed.
- **Redis**: Install and run Redis either locally or via a container.
- **Docker** (optional): For containerized deployments.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/async-imagegen-bot.git
   cd async-imagegen-bot
   ```

2. **Create a virtual environment and install dependencies:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

   Configure the following environment variables:
   - `TELEGRAM_TOKEN` (Your Telegram bot token)
   - `HF_API_TOKEN` (Your Huggingface API token)
   - `REDIS_HOST` (Address of your Redis server)
   - `REDIS_PORT` (Port number for Redis, default is 6379)

4. **Run the Bot:**

   ```bash
   python main.py
   ```

5. **Using Docker:**

   Build and run the Docker container:

   ```bash
   docker build -t async-imagegen-bot .
   docker run -e TELEGRAM_TOKEN=your_token -e HF_API_TOKEN=your_token -e REDIS_HOST=redis async-imagegen-bot
   ```

---

## Usage

Interact with your bot on Telegram using these commands:

- `/start`: Start the bot and display welcome instructions.
- `/flux <prompt>`: Generate an image using the FLUX model.
- `/stable <prompt>`: Generate an image using the Stable Diffusion model.
- `/both <prompt>`: Generate images concurrently using both models.

The bot provides progressive status messages and detailed feedback, ensuring you are informed throughout the generation process.

---

## Contributing

Contributions are welcome! If you'd like to extend the functionality of the Async ImageGen Bot, please follow these steps:

1. **Fork the repository.**
2. **Create a new branch** for your feature or bug fix.
3. **Write tests** for your changes.
4. **Submit a pull request** with a clear description of your modifications.

For any major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the terms of the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Thanks to the developers of [Huggingface](https://huggingface.co/) for their groundbreaking models.
- Kudos to the [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) community for their async support.
- Special mention to the maintainers of [Redis](https://redis.io/) and [Docker](https://www.docker.com/) for providing amazing open source tools.
- Inspired by modern open source practices and community guidelines to build scalable, high-performance applications.

---

*Happy coding and enjoy generating beautiful images!*

# Transit Alert Bot

A Discord bot to remind you when you need to catch your bus or train. Repo structure forked from [Python-hellofly-flask](https://github.com/fly-apps/python-hellofly-flask).

## Getting Started

### .env file

To get started with development of this bot, you will need to first create a `.env` file"

```
cp .env.example .env
```

After you have done that, copy and paste your [Bot Token](https://www.writebots.com/discord-bot-token/), [App ID](https://support-dev.discord.com/hc/en-us/articles/360028717192-Where-can-I-find-my-Application-Team-Server-ID-) and Guild ID into the newly-created `.env` file so that Python has access to these variables.

## Deploying the bot

By default, this bot is set up to deploy with [Fly.io](https://fly.io). If you have a Fly account, you can authenticate the `flyctl` CLI and use `flyctl deploy` to deploy this bot.

## register-commands.py

This file is used locally to test the registration of commands. By default, the development URL is enabled and registers commands with your server for testing. Global commands are cached, so using the server-specific URL allows you a faster feedback look when testing. Mmake sure to swap to the global URL to register commands when you're ready to launch it.
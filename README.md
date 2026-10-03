<p align="center">
    <a href="https://github.com/hypergram-org/hypergram">
        <img
            src="https://raw.githubusercontent.com/hypergram-org/artwork/master/hypergram_logo_github.png"
            alt="hypergram"
            height="128"
        />
    </a>
    <br />
    <b>Telegram MTProto API Framework for Python</b>
    <br />
    <a href="https://hypergram.icu"> Homepage </a>
    •
    <a href="https://docs.hypergram.icu"> Documentation </a>
    •
    <a href="https://t.me/hypergram_news"> News </a>
    •
    <a href="https://t.me/hypergram_chat"> Chat </a>
    <br />
    <br />
    <img
        src="https://img.shields.io/github/actions/workflow/status/hypergram-org/hypergram/python.yml?branch=dev&logo=github&label=CI"
        alt="CI Tests"
    />
    <a href="https://pypi.python.org/pypi/hypergram">
        <img
            src="https://img.shields.io/pypi/v/hypergram.svg?logo=pypi&logoColor=white&color=%23f55b25"
            alt="PyPI package version"
        />
    </a>
    <a href="https://pypi.python.org/pypi/hypergram">
        <img
            src="https://static.pepy.tech/badge/hypergram/month"
            alt="Downloads"
        />
    </a>
    <a href="https://pypi.python.org/pypi/hypergram">
        <img
            src="https://img.shields.io/pypi/pyversions/hypergram.svg?logo=python&logoColor=white&color=%23fd5216"
            alt="Python versions"
        />
    </a>
    <a href="https://github.com/hypergram-org/hypergram/blob/dev/COPYING">
        <img
            src="https://img.shields.io/github/license/hypergram-org/hypergram.svg?color=%23fd5216"
            alt="License"
        />
    </a>
</p>

## hypergram

> Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots

hypergram is an actively maintained hypergram fork for Python designed as a drop-in replacement for hypergram, hypergram provides support for the latest Telegram features including Gifts, Stories, Topics, Business Accounts, and more.

```python
from hypergram import Client, filters

app = Client("my_account")


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from hypergram!")


app.run()
```

**hypergram** is a modern, elegant and asynchronous [MTProto API](https://docs.hypergram.icu/topics/mtproto-vs-botapi)
framework. It enables you to easily interact with the main Telegram API through a user account (custom client) or a bot
identity (bot API alternative) using Python.

### Support

hypergram is an open source project. Your support helps us maintain and improve the library, consider supporting its development:

- `kurimuzonakuma.ton` - TON
- `TYAY3cVST3NY5mqs1M2qGV6PjXDjLLeC6v` - USDT TRC20

Thank you for supporting hypergram ❤️

### Key Features

- **Ready**: Install hypergram with pip and start building your applications right away.
- **Easy**: Makes the Telegram API simple and intuitive, while still allowing advanced usages.
- **Elegant**: Low-level details are abstracted and re-presented in a more convenient way.
- **Fast**: Boosted up by [TgCrypto](https://github.com/hypergram/tgcrypto), a high-performance cryptography library written in C.
- **Type-hinted**: Types and methods are all type-hinted, enabling excellent editor support.
- **Async**: Fully asynchronous (also usable synchronously if wanted, for convenience).
- **Powerful**: Full access to Telegram's API to execute any official client action and more.

### Installing

Stable version

```bash
pip install hypergram
```

Dev version

```bash
pip install https://github.com/hypergram-org/hypergram/archive/dev.zip --force-reinstall
```

Optional dependencies

```bash
pip install hypergram[fast]     # TgCrypto and uvloop for better performance
pip install hypergram[qrcode]   # QR code login support
```

### Resources

- Check out the [docs](https://docs.hypergram.icu) to learn more about hypergram, get started right
  away and discover more in-depth material for building your client applications.
- Join the [official channel](https://t.me/hypergram_news) and stay tuned for news, updates and announcements.
- Join the [official chat](https://t.me/hypergram_chat) to communicate with people.

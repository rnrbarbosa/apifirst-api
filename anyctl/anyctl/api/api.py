#!/usr/bin/env python3

import connexion
from aiohttp import web

if __name__ == '__main__':
    app = connexion.AioHttpApp(__name__, port=8080, specification_dir='./')
    app.add_api('openapi.yaml', arguments={'title': 'Hello World Example'})
    app.run()

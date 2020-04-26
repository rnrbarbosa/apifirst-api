#!/usr/bin/env python3

import connexion

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__)
    app.add_api('openapi.yaml')
    app.run(port=8080)
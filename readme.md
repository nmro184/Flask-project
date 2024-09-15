# Flask Message Handling Application

## Overview

This Flask application handles incoming messages, stores them in a database, and posts them to a Discord channel via a webhook. It also provides an endpoint to retrieve recent messages from the database.

## Features

- **Homepage**: Serves an HTML page located at `index.html`.
- **Receive Message**: Accepts POST requests to `/api` and processes the message.
- **Send to Discord and DB**: Posts messages to Discord and stores them in a database via the `/send_to_discord_and_db` endpoint.
- **Retrieve Recent Messages**: Fetches messages from the past 30 minutes via the `/get_recent_messages` endpoint.

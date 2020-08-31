# Bakalarka-Bot

A Discord bot showcasing the **wonderful** graph layout library named [drag](https://github.com/bigno78/drag).

Send `!mirek <number>` on a server and the bot responds with a **beautiful** graph with given size (4 - 150).

## Run using Docker

1. Create a file named `.env` setting the `DISCORD_TOKEN` to your discord token.
    ```bash
    $ cat .env
    DISCORD_TOKEN=<your discord token>
    ```
1. Execute these commands from the root folder of the repository:
    ```bash
    $ docker build -t bakalarka .
    $ docker run bakalarka
    ```

## Dependencies
(Automatically installed when run using Docker.)

- `drag` (https://github.com/bigno78/drag)
- `DAGmar.jar` (http://www.graphdrawing.org/download/DAGmar.tgz)
- `ImageMagick`
- `Graphviz`
- Python requirements:
  - `discord`
  - `python-dotenv`


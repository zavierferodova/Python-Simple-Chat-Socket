# Python-Simple-Chat-Socket
Here is just simple code for network communication practice.

## Usage
- Start server script with ``python server.py`` then start client also with ``python client.py``
- To exit on client side just type ``/cmd exit``

## Export to Public
You can use ngrok to make this socket visible for public access. First start the server script
```sh
python server.py
```

Then you can forward active port using ngrok
```sh
ngrok tcp 50001
```

After that edit PORT and HOST on client script based on forwaded ngrok address
```python
# client.py
HOST = '<ngrok_address>'
PORT = <ngrok_port>
```
Finally start the client script and start your conversation!
```sh
python client.py
```

Enjoy :)

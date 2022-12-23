# Python-Simple-Chat-Socket
Here is just simple code for computer communication practice.

## Export to Public Internet
You can use ngrok to make this socket visible for public access. And first start the server script
```sh
python server.py
```

Then you can forward active port using ngrok
```sh
ngrok tcp 50001
```
After that edit PORT and HOST on client script based on forwaded ngrok address
```python
HOST = '<ngrok_address>'
PORT = <ngrok_port>
```
Enjoy :)

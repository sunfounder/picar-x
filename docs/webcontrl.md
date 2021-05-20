# web-server- server process

Usage:
```python
ws = Websocket()
ws.test()
```
## Methods
- recv_server_func(websocket) - recv the data from client .
- map(value, inMin, inMax, outMin, outMax) - map the value
- remote_control(move) - recv joystock value to contrl car move
- camera_contrl(value) - recv joystock value to contrl camera move
- send_server_func(websocket) - send the data to the client.
- main_func() - the main logic api
- is_on_edge(ref, gs_list) - cliff check
- found_name - Determine whether the recording file exists
- main_logic_1(websocket,path) - build a run forever recv api .

- main_logic_2(websocket,path) - build a run forever send api.

## 文件说明
- file_server.py - 录音文件接收服务器库文件

- Music.py - 喇叭播放库文件

- picar_x.py - picar-x库文件

- vilib.py - 摄像头库文件

- web_server.py - websocket服务器库文件

- start_server.py  - 快捷启动websocket服务器和文件接收服务器文件

### 启动服务器命令: python3 start_server.py
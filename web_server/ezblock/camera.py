from ezblock.basic import _Basic_class
from http.server import BaseHTTPRequestHandler, HTTPServer
import io
import picamera
import socketserver
from threading import Condition, Thread
from ezblock.utils import getIP

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

def create_handler(output):
    class StreamingHandler(BaseHTTPRequestHandler):
        # output = output

        def do_GET(self):
            if self.path == '/':
                self.send_response(200)
                self.send_header('Location', 'mjpg')
                self.end_headers()
            elif self.path == '/mjpg':
                self.send_response(200)
                self.send_header('Age', 0)
                self.send_header('Cache-Control', 'no-cache, private')
                self.send_header('Pragma', 'no-cache')
                self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
                self.end_headers()
                try:
                    while True:
                        with output.condition:
                            output.condition.wait()
                            frame = output.frame
                        self.wfile.write(b'--FRAME\r\n')
                        self.send_header('Content-Type', 'image/jpeg')
                        self.send_header('Content-Length', len(frame))
                        self.end_headers()
                        self.wfile.write(frame)
                        self.wfile.write(b'\r\n')
                except Exception as e:
                    print('Removed streaming client %s: %s' % (self.client_address, str(e)))
            else:
                self.send_error(404)
                self.end_headers()
    return StreamingHandler

class StreamingServer(socketserver.ThreadingMixIn, HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

class Camera(_Basic_class):

    port = 9000
    RES = [
        "320x240",
        "640x480",
        "1024x576",
        "1280x800",
    ]

    def __init__(self, res=1, fps=12, port=9000, rotation=0):
        self.fps = fps
        self.port = port
        self.res = self.RES[res]

        self.output = StreamingOutput()
        self.camera = picamera.PiCamera(resolution=self.res, framerate=fps)
        self.camera.rotation = rotation
        self.camera.start_recording(self.output, format='mjpeg')

    def start(self): 
        self.ip = getIP()
        print("server starts at %s:%s" % (self.ip, self.port))
        self.address = (self.ip, self.port)
        streaming_handler = create_handler(self.output)
        self.server = StreamingServer(self.address, streaming_handler)
        self.t = Thread(target=self.server.serve_forever)
        self.t.start()

    def stop(self):
        self.t.join()
        self.server.socket.close()
        self.t.join()

if __name__ == '__main__':
    try:
        print(getIP()[0])
        Camera(0).start()
    except KeyboardInterrupt:
        print('KeyboardInterrupt')

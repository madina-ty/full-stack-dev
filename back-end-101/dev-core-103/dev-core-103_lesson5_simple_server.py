import socket
import http.server
import socketserver

# Функция для проверки, доступен ли порт на данном IP-адресе
def check_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f"Порт {port} на {ip} открыт.")
    else:
        print(f"Порт {port} на {ip} закрыт.")
    sock.close()

# Создаем класс обработчика HTTP-запросов
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("Hello, World!", "utf-8"))

# Задаем порт для сервера
PORT = 8080

# Создаем экземпляр сервера
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Сервер запущен на порту", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print("Сервер остановлен")

# Проверяем, открыт ли порт после запуска сервера
check_port('127.0.0.1', PORT)
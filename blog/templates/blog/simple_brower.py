import socket

## The Client
class WebBrowserC:
    print(f'[+] Address" ')
    def webbrowser(self):
        IP = input('')
        PORT = 80
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((IP, PORT))
        cmd = "GET f'{IP}'\r\n\r\n".encode() ## change \r\n to headers later".encode()
        clientSocket.send(cmd)
        while True:
            clientData = clientSocket.recv(512)
            if len(clientData) < 1:
                print(f'[+] No Server Response, sys exit')
                break
            print(clientData.decode(), end='')
        clientSocket.close()


browser = WebBrowserC()
browser.webbrowser()



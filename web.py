from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocol Suite</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #dbeafe, #ede9fe);
            margin: 0;
            padding: 25px;
            text-align: center;
        }

        .container {
            max-width: 950px;
            margin: auto;
            background: white;
            padding: 22px;
            border-radius: 15px;
            box-shadow: 0 5px 20px #999;
        }

        h1 {
            color: #312e81;
            margin: 5px;
        }

        .subtitle {
            color: #64748b;
            margin-bottom: 22px;
        }

        .layers {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
        }

        .layer {
            padding: 15px;
            border-radius: 12px;
            color: white;
        }

        .layer h2 {
            margin: 0 0 12px;
            font-size: 19px;
        }

        .application { background: #2563eb; }
        .transport { background: #0891b2; }
        .internet { background: #7c3aed; }
        .network { background: #059669; }

        .protocols {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 8px;
        }

        .protocols span {
            background: rgba(255,255,255,0.2);
            border: 1px solid rgba(255,255,255,0.5);
            padding: 7px 13px;
            border-radius: 20px;
            font-size: 14px;
        }

        footer {
            margin-top: 18px;
            color: #475569;
            font-size: 13px;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>🌐 TCP/IP Protocol Suite</h1>
    <p class="subtitle">
        Simple Web Server – List of Communication Protocols
    </p>

    <div class="layers">

        <div class="layer application">
            <h2>01. Application Layer</h2>
            <div class="protocols">
                <span>HTTP</span>
                <span>HTTPS</span>
                <span>FTP</span>
                <span>SMTP</span>
                <span>DNS</span>
                <span>DHCP</span>
                <span>Telnet</span>
            </div>
        </div>

        <div class="layer transport">
            <h2>02. Transport Layer</h2>
            <div class="protocols">
                <span>TCP</span>
                <span>UDP</span>
            </div>
        </div>

        <div class="layer internet">
            <h2>03. Internet Layer</h2>
            <div class="protocols">
                <span>IP</span>
                <span>ICMP</span>
                <span>IGMP</span>
                <span>ARP</span>
            </div>
        </div>

        <div class="layer network">
            <h2>04. Network Access Layer</h2>
            <div class="protocols">
                <span>Ethernet</span>
                <span>Wi-Fi</span>
                <span>PPP</span>
            </div>
        </div>

    </div>

    <footer>
        <b>TCP/IP Model</b> | Reliable Communication Across Networks
    </footer>

</div>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',420)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
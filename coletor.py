import platform
import socket
import getpass
import datetime

def coletar_dados():
    dados = {
        "usuario": getpass.getuser(),
        "sistema": platform.system(),
        "versao": platform.version(),
        "hostname": socket.gethostname(),
        "ip_local": socket.gethostbyname(socket.gethostname()),
        "data_hora": str(datetime.datetime.now())
    }
    return dados
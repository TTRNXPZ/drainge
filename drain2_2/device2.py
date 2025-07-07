import socket

def get_ip():
    return socket.gethostbyname(socket.gethostname())

def get_mac(interface='eth0'):
    try:
        with open(f'/sys/class/net/{interface}/address') as f:
            return f.read().strip()
    except:
        return 'N/A'

def get_hostname():
    return socket.gethostname()

def get_serial():
    try:
        with open('/proc/cpuinfo', 'r') as f:
            for line in f:
                if line.startswith('Serial'):
                    return line.strip().split(': ')[1]
    except:
        return 'N/A'

def get_site_id():
    return "site-001"

def build_device_info():
    return {
        "ip": get_ip(),
        "mac": get_mac(),
        "site_id": get_site_id(),
        "uuid": get_serial(),
        "name": get_hostname(),
        "sn": get_serial(),
        "index": "tontarn_sensor"
    }

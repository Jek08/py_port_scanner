import socket as s
import threading


def check_port_connection(ip, port_number, ports):
    """
    Check which port is open
    """
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    socket.settimeout(5)
    is_connected = socket.connect_ex((ip, port_number))
    if is_connected == 0:
        ports[port_number] = 'open'
    else:
        ports[port_number] = ''


def scan_port(ip):
    """
    Run thread on check_port_connection() simultaneously.
    Then print the open port after each thread has finished checking.
    """
    ports = dict()
    threads = list()

    for i in range(10000):
        t = threading.Thread(target=check_port_connection, args=(ip, i, ports))
        threads.append(t)
        t.start() # start each thread

    for i in range(10000):
        threads[i].join()

        if ports[i] is "open":
            print("Port %s : open." % i)


if __name__ == "__main__":
    target = input("Enter target hostname: ")
    target_ip = s.gethostbyname(target)
    
    new_format = "%(message)s"
    logging.basicConfig(format=new_format, level=logging.INFO)
    logging.info("Targeting on: %s" % target_ip)

    scan_port(target_ip)  # initiate the scan

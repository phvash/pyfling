import socket
import os
import time
import sys
import zipfile


def unpack(file_packets):

    flinged_file = ''
    for packet in file_packets:
        flinged_file += packet

    return flinged_file


def receive(s):
    file_packets = []

    while True:

        data = s.recv(1024)

        if not data:
            break
        else:
            file_packets.append(data)

    s.close()

    return file_packets


def write_file(received_file):

    target_dir = 'received'
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    file_name = time.strftime('%Y%m%d%H%M%S') + '.zip'
    path = os.path.join('received', file_name)
    file_obj = open(path, 'w')
    file_obj.write(received_file)
    file_obj.close()

    return path


def unzip(path):

    zipf_obj = zipfile.ZipFile(path)
    zipf_obj.extractall(path='received')
    os.remove(path)
    zipf_obj.close()
    # cleanup()


def cleanup():

    files_path = os.path.join('received', 'files')
    files = os.listdir(files_path)
    for each_file in files:
        old_path = os.path.join(files_path, each_file)
        new_path = os.path.join('received', each_file)
        os.rename(old_path, new_path)
    os.removedirs(files_path)


def main():
    if len(sys.argv) < 2:
        if __name__ == '__main__':
            print "Host address required! " \
              "Usage: $ python tcpClient.py [host_address]"
            sys.exit(1)
        else:
            host = raw_input("Enter host address: ")
    else:
        host = sys.argv[1]

    port = 5001

    s = socket.socket()
    s.connect((host, port))

    file_packets = receive(s)

    file_received = unpack(file_packets)
    path = write_file(file_received)

    print "Transfer complete...100% \n" \
          "-> Saved To: {} \n" \
          "-> File size: {} bytes \n" .format(path, os.path.getsize(path))

    unzip(path)


if __name__ == '__main__':
    main()

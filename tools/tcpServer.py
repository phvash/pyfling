import socket
import os
import time
import zipfile
import subprocess


def fetch_file(file_name):

    file_obj = open(file_name)
    file2fling = file_obj.readlines()
    file_obj.close()

    return file2fling


# def make_zip():
#
#     # path = os.path.join('server', 'files')
#     path = 'files'
#     file_name = time.strftime('%Y%m%d%H%M%S') + '.zip'
#     zipf = zipfile.ZipFile(file_name, 'w', zipfile.ZIP_DEFLATED)
#     for root, dirs, files in os.walk(path):
#         for each_file in files:
#             # zipf.write(os.path.join(files, each_file))
#             zipf.write(os.path.join(root, each_file))
#     zipf.close()
#     return file_name

def make_zip():

    file_name = time.strftime('%Y%m%d%H%M%S') + '.zip'
    zipf = zipfile.ZipFile(file_name, 'w', zipfile.ZIP_DEFLATED)

    # try:
    #     path = os.system('zenity --file-selection')
    #     print "Hi there!"
    #     zipf.write(path)
    #     zipfile.close()
    #     time.sleep(60)
    #     return file_name
    #
    # except:
    #     path = 'files'
    #     for root, dirs, files in os.walk(path):
    #         for each_file in files:
    #             zipf.write(os.path.join(root, each_file))

    if 'linux' in os.sys.platform:
        path = subprocess.check_output(['zenity', '--file-selection'])
        print path
        zipf.write(path.strip('\n'))


    zipf.close()
    return file_name


def clean_up(file_name):

    os.remove(file_name)


def main():

    # set host address and port to run on
    host = ''
    port = 5001

    # create a socket object
    s = socket.socket()
    s.bind((host, port))  # argument must be a tuple

    print 'Server started, waiting for connections'
    s.listen(1)
    # get a connection and address of client
    c, addr = s.accept()
    print 'Connection from: %s' % (str(addr))

    # package file to send

    file_name = make_zip()

    # send file to client

    to_send = fetch_file(file_name)

    print "Sending To: {}".format(str(addr))

    for value in to_send:
        c.send(value)
    c.close()

    print "Sent"

    clean_up(file_name)


if __name__ == '__main__':
    main()

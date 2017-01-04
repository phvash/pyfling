from tools import tcpServer, tcpClient


def main():

    # make connection 

    print "Create connection or join connection?"
    response = raw_input("Enter 'S' to send 'R' to receive: ").lower()
    start(response)


def start(response):

    if response == 's':
        tcpServer.main()
    elif response == 'r':
        tcpClient.main()
    else:
        print "Kindly enter a valid option"
        response = raw_input("Enter 'S' to send 'R' to receive: ").lower()
        start(response)

if __name__ == '__main__':
    main()

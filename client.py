import socket, select, string, sys
 
#main function
if __name__ == "__main__":
   
    #HOST = "127.0.0.1"
    HOST = raw_input("Please input IP to connect : ")
    PORT = input("Please enter port number you want to connect : ") 
     
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
     
    # connect to remote host
    try :
        sock.connect((HOST, PORT))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host'
     
    while 1:
        try:               
            cmd = raw_input("type message : ")
            sock.send(cmd)
            data = "\n"+sock.recv(1024)+"\n"	
            if data:
                print data         
        except:
            sock.close()

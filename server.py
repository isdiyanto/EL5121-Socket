import socket, select
  
if __name__ == "__main__":
      
    CONNECTION_LIST = []    # list of socket clients
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = input("Please enter port number you want to open ? ")
         
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)
 
    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)
 
    print "Server started on port " + str(PORT)
 
    while 1:
        # Get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
 
        for sock in read_sockets:
             
            #New connection
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print "Client (%s, %s) connected" % addr
                
            #Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
                    #In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data = sock.recv(RECV_BUFFER)
                    # echo back the client message
                    if data :
                        print "(%s, %s) send : " % addr + data
                        if data == '1':
                            filename='file_a.txt'
                            f = open(filename,'rb')
                            l = f.read(1024)
                            f.close()
                            content = "file_a.txt content : \n------------\n"+l+"\n------------"
                            sock.send(content)
                        elif data == '2':
                            filename='file_b.txt'
                            f = open(filename,'rb')
                            l = f.read(1024)
                            f.close()
                            content = "file_b.txt content : \n------------\n"+l+"\n------------"
                            sock.send(content)
                        else :
                            sock.send("your mesasage accepted, \n> type '1' to open file_a.txt \n> type '2' to open file_b.txt ")               
                except:
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    print "Client (%s, %s) is offline" % addr

                    continue
         
    server_socket.close()

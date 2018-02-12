# DataGramSockets
Using python3.x, we shall implement low level socket communication between a server and a client in the datagram protocol
to run the application, run the server first by typing python echo_server.py -l 12000.This passes the argument l to the variable local
port
Open a new terminal window in the current directory and run python echo_client.py -d localhost -p 12000 -l 13000 -f echo_client.py
This will run the program and the client will send the data which is the contents of the client file.
The server then echoes back these contents and the client does some simple computations
in sock352.py, we use the datagram protocol to create a socket object and thus, we dont need a listen and accept method

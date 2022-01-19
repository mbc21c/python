import socket

HOST = '127.0.0.1' 
# Server IP or Hostname
PORT = 12345 
# Pick an open Port (1000+ recommended), must match the client sport
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

#managing error exception
try:
	s.bind((HOST, PORT))
except socket.error:
	print('Bind failed ')

s.listen(5)
print('Socket awaiting messages')
(conn, addr) = s.accept()
print('Connected')

# awaiting for message
while True:
    data = conn.recv(1024)
    print('I sent a message back in response to: ' + data.decode('utf-8'))
    deCodeData = data.decode('utf-8')
    reply = ''

	# process your message
    if deCodeData == 'Hello':
        reply = 'Hi, back!'
    elif deCodeData == 'This is important':
        reply = 'OK, I have done the important thing you have asked me!'
	#and so on and on until...
    elif deCodeData == 'quit':
        conn.send('Terminating'.encode('utf-8'))
        break
    else:
        reply = 'Unknown command'

	# Sending reply
    conn.send(reply.encode('utf-8'))
conn.close() 
# Close connections
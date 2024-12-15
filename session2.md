## **Session 2: OSI Model and the Transport Layer**

### **Summary**  
This session explores the OSI model in more detail, focusing on the transport layer and its role in ensuring reliable communication through protocols like TCP and UDP.

### **Topics**  
1. **OSI Layers Overview**  
   The OSI model divides network communication into seven distinct layers, which allows for modular communication between different systems.  
   - **Physical Layer**: Hardware components like cables, switches.  
   - **Data Link Layer**: Handles physical addressing, such as MAC addresses.  
   - **Network Layer**: Handles logical addressing (IP addresses).  
   - **Transport Layer**: Manages reliable data transfer (TCP/UDP).  
   - **Session Layer**: Maintains sessions between applications.  
   - **Presentation Layer**: Data translation, encryption, compression.  
   - **Application Layer**: End-user protocols like HTTP, FTP.

2. **TCP vs. UDP**  
   - **TCP (Transmission Control Protocol)**: Connection-oriented, reliable. Ensures data is delivered in order and without errors (e.g., HTTP).  
   - **UDP (User Datagram Protocol)**: Connectionless, faster but unreliable. Used for real-time communication (e.g., video streaming).

   **Resources**:  
   - [IBM: TCP vs UDP](https://www.ibm.com/docs/en/zos/2.4.0?topic=internets-tcp-udp-ip)  

3. **TCP Handshake**  
   TCP uses a 3-way handshake to establish a connection:
   - **SYN**: Initiate a connection.  
   - **SYN-ACK**: Acknowledge the request.  
   - **ACK**: Final confirmation.

   **Resources**:  
   - [TCP Three-Way Handshake](https://www.geeksforgeeks.org/tcp-3-way-handshake-process/)  
   - [Simple explanation about TCP 3-way handshake](https://community.cisco.com/t5/networking-blogs/tcp-3-way-handshake/ba-p/3773721)

### **Exercises**  
- **Easy**: Write out the steps of the TCP 3-way handshake.  
- **Intermediate**: Implement a basic TCP server-client connection using Python’s `socket` module.  
- **Difficult**: Create a UDP-based Python application and simulate packet loss to observe the impact on the application.

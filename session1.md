## **Session 1: Introduction to Networks**

### **Summary**  
This session provides an overview of networks, introducing key concepts, types of networks, and fundamental protocols that every developer should understand. We will also explore the OSI and TCP/IP models that define how different parts of a network interact.

### **Topics**  
1. **What is a Network?**  
   A network is a group of computers and other devices connected to share resources. Common examples include home Wi-Fi, office networks, and the global Internet.  
   - **LAN (Local Area Network)**: A network within a small geographic area, such as a home or office.  
   - **WAN (Wide Area Network)**: A network that spans a larger geographic area, e.g., the Internet.

2. **OSI Model vs. TCP/IP Model**  
   - **OSI Model**: Conceptual model with 7 layers (Physical, Data Link, Network, Transport, Session, Presentation, Application).
   - **TCP/IP Model**: Practical model with 4 layers (Link, Internet, Transport, Application). TCP/IP is what is predominantly used in real-world networking.

   **Resources**:  
   - [Cisco - OSI Model](https://www.cisco.com/c/en/us/solutions/small-business/resource-center/networking/networking-basics.html)  
   - [OSI Model on Wikipedia](https://en.wikipedia.org/wiki/OSI_model)  
   - [TCP/IP Model on Wikipedia](https://en.wikipedia.org/wiki/Internet_protocol_suite)  

3. **Network Tools Overview**  
   - **Ping**: Tests if a device is reachable on the network (ICMP protocol).  
   - **Traceroute**: Shows the path packets take to reach a destination.  
   - **netstat**: Displays network connections, routing tables, and interface statistics.

   **Resources**:  
   - [Ping Command](https://man7.org/linux/man-pages/man8/ping.8.html)  
   - [Traceroute Command](https://man7.org/linux/man-pages/man8/traceroute.8.html)  

4. **IP Addressing**  
   - **IPv4**: 32-bit address (e.g., `192.168.0.1`), common for most networks.  
   - **IPv6**: 128-bit address, newer and designed to replace IPv4.  
   - **Ports**: Ports are used by protocols to determine where data should go. For example, HTTP uses port 80, HTTPS uses port 443, and SSH uses port 22.

   **Resources**:  
   - [What is an IP Address?](https://www.cloudflare.com/learning/network-layer/what-is-an-ip-address/)  

### **Exercises**  
- **Easy**: Use `ping` to test connectivity to a website such as `google.com`.  
- **Intermediate**: Use `traceroute` to observe the route to a website.  
- **Difficult**: Write a brief comparison between IPv4 and IPv6. Why is IPv6 adoption important?

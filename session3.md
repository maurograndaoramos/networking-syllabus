## **Session 3: DNS and Networking in Web Development**

### **Summary**  
This session explains DNS (Domain Name System), a critical element for web developers. Understanding DNS and its role in routing and resolving domain names to IP addresses is essential.

### **Topics**  
1. **What is DNS?**  
   DNS is the system that translates human-readable domain names (like `google.com`) into IP addresses that computers use to communicate.  
   - **DNS Records**:  
     - **A Record**: Maps domain names to IPv4 addresses.  
     - **CNAME Record**: Alias for another domain name.  
     - **MX Record**: Mail exchange records for email routing.

2. **How DNS Works**  
   DNS servers store mappings of domain names to IP addresses in a hierarchical manner:  
   - **Root DNS Servers**: Top-level DNS servers.  
   - **TLD (Top-Level Domain) Servers**: Responsible for `.com`, `.org`, etc.  
   - **Authoritative DNS Servers**: Provide the final resolution of the domain.

3. **Troubleshooting DNS**  
   - Use `nslookup` or `dig` to query DNS records and troubleshoot issues.  

   **Resources**:  
   - [What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)  
   - [Dig](https://man.openbsd.org/dig.1)

### **Exercises**  
- **Easy**: Use `nslookup` to find the IP address of a website (`example.com`).
- **Intermediate**: Configure your computer's `hosts` file to resolve a domain to a local IP address.  
- **Difficult**: Use `dig` to inspect DNS records for `example.com` and report the TTL (Time-to-Live) for A records.


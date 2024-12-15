## **Session 4: HTTP/HTTPS and APIs**

### **Summary**  
This session focuses on HTTP and HTTPS, the protocols that enable web applications. We’ll dive into the mechanics of web communication, focusing on status codes, methods, and security.

### **Topics**  
1. **HTTP Overview**  
   HTTP (Hypertext Transfer Protocol) is the foundation of data communication on the web.  
   - **Methods**: `GET`, `POST`, `PUT`, `DELETE`.  
   - **Status Codes**:  
     - **2xx**: Successful requests (e.g., `200 OK`).  
     - **3xx**: Redirects (e.g., `301 Moved Permanently`).  
     - **4xx**: Client errors (e.g., `404 Not Found`).  
     - **5xx**: Server errors (e.g., `500 Internal Server Error`).

2. **HTTPS and SSL/TLS**  
   HTTPS is HTTP over SSL/TLS, providing encryption and security for web communications. It ensures that data cannot be intercepted by attackers.  
   - **SSL/TLS Handshake**: How secure communication is established.

   **Resources**:  
   - [What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)  

3. **Debugging Web Communication**  
   - **Postman**: Tool for testing APIs.  
   - **curl**: Command-line tool to make HTTP requests.

   **Resources**:  
   - [Postman Documentation](https://learning.postman.com/docs/getting-started/introduction/)  
   - [Curl Documentation](https://curl.se/docs/)

### **Exercises**  
- **Easy**: Use Postman to send a `GET` request to `https://jsonplaceholder.typicode.com/`.  
- **Intermediate**: Use `curl` to send a `POST` request with a JSON body to a public API.  
- **Difficult**: Use Postman to test an API with different authentication methods (Basic Auth, Bearer Token).


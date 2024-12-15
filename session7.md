# **Session 7: Rapid Project - Building a Secure and Scalable Application** 

## **Objective**  
- Develop a secure and scalable web application in a limited time, focusing on network configuration and performance.  

### **Project Requirements**
1. **Network Infrastructure**  
   - Use **load balancing** to distribute traffic and ensure high availability. (NGINX or Traefik)
   - Apply network segmentation to isolate sensitive services (Docker).

2. **Security**  
   - Implement **HTTPS (SSL/TLS)** for secure communication.  

3. **REST** API
   - Develop an API that follows the HTTP Protocol, allowing users making the proper requests and returning the convenient status code 

## **Evaluation Criteria (0-20 points)**  

> NOTE: Each section MUST include proper Documentation section on `README.md` file

1. **Network Infrastructure (10 points)**  
   - Correct configuration of the load balancer with a controlled CIDR for each container 
  
2. **Security (5 points)**  
   - Correctly configured HTTPS with an self signed certificate.

4. **REST API** (**5 points**)
   - Develop a simple API where you must specify an endpoint of each type (GET, POST, PUT, DELETE) 
   - The API must handle requests properly by following the HTTP Protocol, returning the proper status codes

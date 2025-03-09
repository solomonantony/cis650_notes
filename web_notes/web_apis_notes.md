# Network programming
- Using the socket module, we can access the low level networking interface
- Network comminications use the port numbers in the range from 0 to 1023 (0 to 2 10 ). They are used by system processes that provide widely used types of network services.
- Protocols are rules for communication between two programs
- e.g. http is the protocol for communication between web client and web seb server
- e.g. smtp is the protocol for communication between mail client and mail seb server
- To communicate over any port using any protocol
- See https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers for details
# Web APIs using Hyper text transfer protocol - HTTP
- Web APIs provide a stable approach to accessing data on the web
- API = Application Programming Interface
- Web APIs are built on HTTP, a web standard
# Access Control
- Many web APIs require a username and password, or an API key
- These are usually available via a web site related to the web API
- The username/password or key can be used by the program making the web API call
- Depending on the web API, the username/password or key might be provided as a parameter in the URL in the header of the request
- There are several different approaches for access control, the next slide's program shows one example
## Query parameters
- Query parameters provide additional information as part of the request to a web API as key/value pairs
- Query parameters can be provided:
- as part of the URL, after the ? , and separated by &
- within the request body
- The Requests package get() function allows a dictionary to be passed as the second argument, representing the query parameters
- 

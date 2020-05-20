## PythoCrypt

This package is intended to contain some of the most famous encryption tools, that 
includes:
- Caesar algorithm

### Installation
Run into your terminal to install:

    pip install pythocrypt
    
### Documentation
Latest documentation is at:


    
### Examples

#### Using Caesar's cipher
To encrypt a message using Caesar shift:
```
from pythoncrypt import caesar

message = "Hello World"
message_encripted = caesar.encrypt(message)
```

For decryption is very similar from example above:
```
from pythoncrypt import caesar

message_encripted = ""
message = caesar.decrypt(message_encripted)
```

The default shift is `3`, but you can also change the shift distance, 
passing as parameter when calling decrypt method:
```
from pythoncrypt import caesar

message_encripted = ""
message = caesar.decrypt(message_encripted, shift=10)
```
    
### License
PythoCrypt is under the [MIT License](http://www.opensource.org/licenses/mit-license.php)

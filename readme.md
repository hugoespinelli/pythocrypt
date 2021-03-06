## PythoCrypt 
[![Build Status](https://travis-ci.org/hugoespinelli/pythocrypt.svg?branch=master)](https://travis-ci.org/hugoespinelli/pythocrypt)


This package is intended to contain some of the most famous encryption tools, that 
includes:
- Caesar shift
- Rail fence

### Installation
Run into your terminal to install:

    pip install pythocrypt
    
### Documentation
For more information, read the latest documentation is at:
https://hugoespinelli.github.io/pythocrypt/

You can also check pypi:
https://pypi.org/project/pythocrypt/
    
### Examples

#### Using Caesar's cipher
To encrypt a message using Caesar shift:
```
from pythoncrypt import caesar

message = "Hello World"
message_encrypted = caesar.encrypt(message)
```

For decryption is very similar from example above:
```
from pythoncrypt import caesar

message_encrypted = ""
message = caesar.decrypt(message_encripted)
```

The default shift is `3`, but you can also change the shift distance, 
passing as parameter when calling decrypt method:
```
from pythoncrypt import caesar

message_encrypted = ""
message = caesar.decrypt(message_encripted, shift=10)
```
    
### License
PythoCrypt is under the [MIT License](http://www.opensource.org/licenses/mit-license.php)

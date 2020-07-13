# Air Strike Decryption

According to the pre-decided code, you know that the symbols ‘(‘, ‘)’ and ‘*’ when arranged in a particular order determine locations. Your country is expecting an air strike and the information regarding the target location lies with the intelligence agency. You are conversing with them in a protected channel using the symbols to determine the location. If their reply says true, then that location spelled out using these symbols is a possible location for an attack.

You’ve received yet another message from the agency,it’s intercepted in the form of a string.

Now all that’s required is for you to check the validity of the location with the help of these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')' or vice versa. Left parenthesis '(' must go before the corresponding right parenthesis ')'. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string. An empty string is also valid.

### Input Format

A string S.

### Constraints

S is composed of characters ‘(‘ , ‘)’ and ‘*’ only.

### Output Format

Print true if the given string is valid otherwise print false.

### Sample Input 0

       (**)

### Sample Output 0

       true

### Sample Input 1

       ()()

### Sample Output 1

       true

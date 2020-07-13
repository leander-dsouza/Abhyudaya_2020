# Chief in Chains

The army chief of your country has been abducted by an enemy nation. A few eminent officers have been chosen to bring him back. They happen to be trapped in a room which opens by a passcode. They need to get out of the room to save their chief and to ultimately save their country. They realise that the room they're locked in was being watched by a camera and the passcode was some sort of pattern they had to form a queue in. Try to find the right passcode by switching the order of the officers as stated in the following question.

Each officer is described by a pair of integers (l,n) where ‘l’ is the height of an officer and ‘n’ represents the number of officers in front of the person with height greater than or equal to ‘l’.

Hurry up and reconstruct the queue in order to get out and save the army chief.

### Input Format

* An integer n denoting the number of people.

* Next n lines contains officer's height and number of officers having greater or equal height to the officer.

### Constraints

* The number of people are less than 10000.

* The height of officers is less than 100.

### Output Format

Print queue of pair of integers in order to save the army chief.

### Sample Input 0

       6
       5 0
       6 0
       5 1
       7 0
       7 1
       7 2

### Sample Output 0

       5 0
       5 1
       6 0
       7 0
       7 1
       7 2

### Sample Input 1

       5
       6 0
       6 1
       5 2
       7 0
       4 0

### Sample Output 1

       4 0
       6 0
       6 1
       5 2
       7 0

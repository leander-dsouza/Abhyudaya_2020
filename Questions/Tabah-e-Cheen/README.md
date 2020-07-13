# Tabah-e-Cheen

Due to the increasing tension in the Aksai Chin region , you, along with a few others soldiers took up the responsibility to talk things out with the Chinese army. They however, take you by surprise and attack you and your troop and later hold you all as hostages. In order to get out of the sealed room, you need to draw a pattern consisting of lines on the screen that the Chinese army uses to keep you there. An anonymous helper slides in the following question,the answer to which will get you all out of the hold of the Chinese army.

You’ve been provided 2 integer matrices A and B.Your task is to return the maximum number of connecting lines that can be drawn such that each number belongs to only one connecting line.

Also you need to keep in mind that a connecting line cannot intersect even at the endpoints.

A connecting line is a straight line connecting A[i] and B[j] such that A[i]=B[j].

### Input Format

* The first line contains two integers m and n, i.e. elements in A and B arrays.

* The second line contains m elements of array A, and

* The third line contains n elements of array B.

### Constraints

* 1 <= A.length <= 500,

* 1 <= B.length <= 500,

* 1 <= A[i], B[i] <= 2000

### Output Format

An integer which will be the maximum number of connecting lines.

### Sample Input 0

          3 3
          1 3 5
          1 5 3
          
### Sample Output 0

          2
          
### Explanation 0

We can draw 2 uncrossed lines as in the diagram. We cannot draw 3 uncrossed lines, because the line from A[1]=3 to B[2]=3 will intersect the line from A[2]=5 to B[1]=5.

### Sample Input 1

         3 3
         2 1 1
         5 7 10
          
### Sample Output 0

          0




          
    

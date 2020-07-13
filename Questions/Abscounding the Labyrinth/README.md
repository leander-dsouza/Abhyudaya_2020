# Abscounding the Labyrinth

You happen to be a person of nativism importance and your abduction has created panic which is developing into a war hysteria.

You need to escape the labyrinth soon as your responsibilities await you. The trick being, stepping into the wrong area of the labyrinth might trigger the enemy to abduct more people while stepping into the right block will give you more hints and resources to escape. Your target is to reach the last block of the 2D matrix, having more hints than triggering enemies for each area following the right path, that is after stepping on a positive value you get more hints and trigger enemy traps if stepping on a negative value.

Solve the following question to get back in control and save your country from going into war.

### Input Format

* Integer m and n denoting the number of rows and columns for the matrix.

* Next m lines contains n space separated integers.

### Constraints

* 0<=m<=100001

* 0<=n<=100001

### Output Format

An integer n, i.e. the minimum value required to get back in control by escaping the labyrinth.

### Sample Input 0

        2 2
       -11 17
       83 -72

### Sample Output 0

       12

### Explanation 0

Given the Labyrinth, the initial hints the person must be having should be at least 12 if he follows the optimal path DOWN->RIGHT.

### Sample Input 1

        3 3
        -9 17 -21
        -61 45 32
        72 19 -24

### Sample Output 1

        10

### Explanation 1

Given the Labyrinth, the initial hints the person must be having should be at least 10 if he follows the optimal path RIGHT->DOWN->RIGHT->DOWN.

# Airline Iternary

Given to you is a list of airline tickets represented in the form of pairs of departure and arrival airports [from,to] .Your task is to reconstruct the itinerary in order such that it must begin with ‘MSC’. All of the tickets belong to a man boarding from the airport with IATA code ‘MSC’.

**Note:** If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["MSC", "LGA"] has a smaller lexical order than ["MSC", "LGB"]. You may assume all tickets form at least one valid itinerary. One must use all the tickets once and only once.

### Input Format

* An integer n denoting the number of arrivals and departures.

* Next n lines contains strings A and B, i.e. pairs of departure and arrival airports [from,to]

### Constraints

* 1<=n<=100001

* A and B both strings are in uppercase.

### Output Format

Print the iternary with smallest lexical order when read as single string having locations separated with space.

### Sample Input 0

       1
       MSC XYZ

### Sample Output 0

       MSC XYZ

### Sample Input 1

       3
       DEF GHI
       ABC DEF
       MSC ABC

### Sample Output 1

       MSC ABC DEF GHI

# Movie-Theater-Seating-Challenge
Movie Theater Seating Challenge
Language used: Python

## Program Description:

design and write a seat assignment program to maximize both customer satisfaction and customer safety. For the purpose of public safety, assume that a buffer of three seats and/or one row is required.

## The algorithm follows following rules:

Customers that come first will be allocated seats in the middle rows.

Each group number must be in the range of 1 and the number of column in this theater

Each group will be allocated seats in a single row. If the group is larger than the number of seats in the row, split the group and allocate as many seats available in that  row for few members and for others allocate in the other row.

Full fill as many requests as possible.
After scanning all the rows, if the theater is not able to allocate nearby (consecutive) seats to a group, then allocate seats wherever there is a vacant seat.

If the numbers of requested seats are not available in the theater then, inform the customer about insufficient seats.

## Assumptions:

The theater cannot reserve seats for a group if the requested number of seats is greater than the available seats. In that case, the customers are informed about the insufficient number of available seats.

The reservation number(R###) will be in sequential order like (R001, R002, R003...) in the input file.

## Customer Satisfaction:

Since customers are reserving seats for groups, they would prefer sitting next to each other. So the first priority will be to allocate seats for the group in a single row.
Since the middle seats give a better viewing experience in the movie theater, customers who come first will be allocated seats in the middle rows.

## Maximum Theater Utilization:

To make sure that we are able to accommodate as many groups as possible and also keep them satisfied by allocating consecutive seats, we start allocating seats from the first column. This will allow us to allocate seats for maximum number of groups in a single row.
In one or two cases if we are not able to accommodate a group in a single row, then we allocate the seats wherever there is a vacant seat in the theater.

## Steps for running

run example : python main.py data1.txt. It will return the allocated seats file path

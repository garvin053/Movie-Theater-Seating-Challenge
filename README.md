# Movie-Theater-Seating-Challenge
Movie Theater Seating Challenge
Language used: Python

## Program Description:

design and write a seat assignment program to maximize both customer satisfaction and customer safety. For the purpose of public safety, assume that a buffer of three seats and/or one row is required.

## Assumptions:

1. The theater cannot reserve seats for a group if the requested number of seats is greater than the available seats. In that case, the customers are informed about the insufficient number of available seats.

2. There will be up to 26 rows in the movie theater. If there are more, switch over to numbering system. The row should be marked as numbers like '10' rather than 'J'

3. The reservation number(R###) will be in sequential order like (R001, R002, R003...) in the input file and all reservations are in the right format like (R001 2)

## Customer Satisfaction:

1. Since customers are reserving seats for groups, they would prefer sitting togather. So the first priority will be to allocate seats for the group in a single row.

2. Since the middle seats give a better viewing experience in the movie theater, customers who come first will be allocated seats in the middle rows.

## Maximum Theater Utilization:

1. To make sure that we are able to accommodate as many groups as possible and also keep them satisfied by allocating consecutive seats, we start allocating seats from the first column. This will allow us to allocate seats for maximum number of groups in a single row.

2. In one or two cases if we are not able to accommodate a group in a single row, then we allocate the seats wherever there is a available seat in the theater.

## The algorithm follows following rules:

1. Customers that come first will be allocated seats first and in the middle rows.

2. Each group number must be in the range of 1 and the number of columns in this theater

3. Each group will be allocated seats in a single row. If the group number is larger than the available number of seats in each row, split the group and allocate as many seats available in that row for few members and for others allocate in the other rows.

4. Full fill as many requests as possible.Start allocating seats from the first column.

5. If the numbers of requested seats are not available in the theater then, inform the customer about insufficient seats.


## Steps for running

run example : python main.py data1.txt. It will return the allocated seats file path

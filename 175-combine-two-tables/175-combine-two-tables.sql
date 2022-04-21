# Write your MySQL query statement below
select
    firstName, lastName, city, state
from 
    person P
left join
    address A on
    p.personId = A.personId;

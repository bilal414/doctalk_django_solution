Solution is based on Django & Django Rest Framework. 

Following API will be used to list all users and can we pass **dob_gt** in query parameter to get
profiles with date of birth greater than passed date.

We can also use **dob_lt** param to get profiles with date of birth less than passed date. 

if you have order by field then just pass ordering parameter with **-dob** to get in descending order 
`/profiles?ordering=-dob`
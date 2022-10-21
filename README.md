# parallelprogramng
Parallel programming is a technique where we use multiple threads to execute a task faster. 
This means that on modern multi-core architectures we can utilize more of the resources available to perform a task.

Asynchronous programming is subtly different. This normally involves longer running tasks and tasks which are perhaps waiting
on some kind of external stimuli. 
A good example of this is to perform a large calculation in a background thread so that the UI remains responsive.
With asynchronous code we are normally talking about code which executes at a different rate to our main application.


 async provides you a method of opening thousands of connections at once and swapping among each connection as they finish and return their results. 
 Basically, it sends the request to a connection and moves to the next one instead of waiting for the previous one’s response. 
 It continues like this until all the connections have returned the outputs. 


![Screenshot from 2022-10-21 16-01-46](https://user-images.githubusercontent.com/66484788/197202431-290d052d-50f3-4af4-a161-2d28716e0827.png)




## the output of code.
1) long time

![Screenshot from 2022-10-21 15-44-06](https://user-images.githubusercontent.com/66484788/197214752-1d7c09a3-6c0d-447a-9dfa-9c18bb3d1e4b.png)


2) less time

![Screenshot from 2022-10-21 16-59-28](https://user-images.githubusercontent.com/66484788/197213781-82ef1277-e945-48e6-970c-b4164705159c.png)

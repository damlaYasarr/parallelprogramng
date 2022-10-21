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
 
 ![image](file:///home/damlayasarr/Pictures/Screenshots/Screenshot%20from%202022-10-21%2016-01-46.png)

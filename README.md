# WitchScript
Tumblr Application built to help a sociology major gather data for her thesis. Makes use of Tumblr API to look at posts using specific tags (in this case witch related ones) for the last year and gather a random sample from those collected posts which are above a certain level of popularity. 

Technical process:
I use the /tagged api call to get the 20 most recent posts from the date January 1st 2019. I then change the time to the oldest post returned from the first call. I then call the api with /tagged again and repeat this going backwards until I reach the end date which I selected as January 1st 2018. I do this for each tag I want to examine and add it to an overall list of blog posts. I then loop through this list of blogposts and check if they have 3 or more of the tags I have selected in common, and have more than 100 notes and add them to the successful blogpost list. I then loop through the blog posts which have succeeded and randomly select them to add to my selected blog posts. I then take these 300 selected blog posts and like them through the tumblr api so that I can view them on the tumblr website under my account.

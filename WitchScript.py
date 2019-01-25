#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 23:14:44 2019

@author: kaimcconnell
"""
import pytumblr


client = pytumblr.TumblrRestClient(
  'YjnIsvRhkD60zHefBiSOpx2oQxr03IViRScbc0EWiI075cpnST',
  'rcTsPo0hyKefqoe2MRBBNN1RAxf6ze2E7uNNqVzyodi8kzlJB1',
  'QvWBCMNAkqdudhq3GodNncnzkaEzqn63JViJaRVHDIHbap2tuG',
  'qVtdVqQ01RdwcyWyqXTEr0Hg1Nx29eveWHImw24SXPJzYvm2gm'
)

tagList = ['witch', 'witchcraft', 'witches', 'wicca', 'magick', 'witchblr', 'wiccan', 'pagan', 'occult']
# Make the request
##COMENT THIS OUT IF NOT DOING YEAR
startTime = 1546300800
cutOffTime = 1514764800
#startTime = time.time()
#cutOffTime = curTime - 604800 #7 days
#86400 #One day back from current time
#31536000 a year from current time
#Start Time = 1546300800 1st of january 2019
#End Time = 1514764800 1st of january 2018

overallBlogs = []
##COMMENT THIS OUT IF NOT DOING YEAR
#for p in range(1,52):
    
for tag in tagList:
    
    searchTime = startTime
    while searchTime > cutOffTime:
#        response = requests.get('https://api.tumblr.com/v2/tagged?tag=' 
#                                + tag + '&before=' + str(searchTime) 
#                                + '&api_key=YjnIsvRhkD60zHefBiSOpx2oQxr03IViRScbc0EWiI075cpnST')
#        blogPosts = json.loads(response.content)
#        blogPosts = blogPosts['response']
        blogPosts = client.tagged(tag, before=searchTime)
        print('tagSearch ' + tag)
        for blogPost in blogPosts:
            if blogPost in overallBlogs:
                i = 0
            else:
                overallBlogs.append(blogPost)
            searchTime = blogPost['timestamp']
        print(searchTime)
                
    ##COMMENT THIS OUT IF NOT DOING YEAR
#    startTime = cutOffTime
#    cutOffTime = startTime - 604800



print(len(overallBlogs))


requiredNotes = 100

requiredTags = 3

numberOfBlogPostsWanted = 300


successfulBlogPosts = []

for blogPost in overallBlogs:
    
    
    id = blogPost['id']
    reblogKey = blogPost['reblog_key']
    postName = blogPost['blog_name']
    notes = blogPost['note_count']
    timeStamp = blogPost['timestamp']
    tags = blogPost['tags']
    
    if timeStamp > cutOffTime:
        if notes >= requiredNotes:
            
            numTags = 0
            for tag in tags:
                if tag in tagList:
                    numTags = numTags + 1
                    
            if numTags > requiredTags:
                print(id)
                print(reblogKey)
                print(postName)
                print(notes)
                successfulBlogPosts.append(blogPost)
    
#    if len(selectedBlogPosts) > numberOfBlogPostsWanted:
#        break

import random

selectedBlogPosts = []
while len(selectedBlogPosts) < numberOfBlogPostsWanted:
    selectNumber = random.randint(0, len(successfulBlogPosts))
    if successfulBlogPosts[selectNumber] in selectedBlogPosts:
        i = 0
    else:
        selectedBlogPosts.append(successfulBlogPosts[selectNumber])


print(len(selectedBlogPosts))
for blogPost in selectedBlogPosts:
    id = blogPost['id']
    reblogKey = blogPost['reblog_key']
    client.like(id, reblogKey)

#info = client.info()
#print(info)
// Add a vote to reviews
// We want to know who's voted and also how
// many times this item has been voted on
//<start id="reviews-upsert-vote-naive"/>  
db.reviews.update({_id: ObjectId("4c4b1476238d3b4dd5000041")},
  {$push: {voter_ids: ObjectId("4c4b1476238d3b4dd5000001")},
   $inc: {helpful_votes: 1}
  })
//<end id="reviews-upsert-vote-naive"/>  

//<start id="reviews-upsert-vote"/>  
query_selector = {_id: ObjectId("4c4b1476238d3b4dd5000041"),
  voter_ids: {$ne: ObjectId("4c4b1476238d3b4dd5000001")}}
db.reviews.update(query_selector,
  {$push: {voter_ids: ObjectId("4c4b1476238d3b4dd5000001")},
   $inc : {helpful_votes: 1}
  })
//<end id="reviews-upsert-vote"/>  


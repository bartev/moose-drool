//<start id="users-username"/>  
db.users.findOne({username: 'kbanker',
  hashed_password: 'bd1cfa194c3a603e7186780824b04419'})
//<end id="users-username"/>  

//<start id="users-username-fields"/>  
db.users.findOne({username: 'kbanker',
  hashed_password: 'bd1cfa194c3a603e7186780824b04419'},
  {_id: 1})
//<end id="users-username-fields"/>  

//<start id="users-username-fields-response"/>  
{ _id: ObjectId("4c4b1476238d3b4dd5000001") }
//<end id="users-username-fields-response"/>  

//<start id="users-lastname"/>  
db.users.find({last_name: 'Banker'})
//<end id="users-lastname"/>  

//<start id="users-sql-like"/>  
//SELECT * from users WHERE last_name LIKE 'Ba%'
//<end id="users-sql-like"/>  

//<start id="users-lastname-regex"/>  
db.users.find({last_name: /^Ba/})
//<end id="users-lastname-regex"/>  

//<start id="users-zips"/>  
db.users.find({'addresses.zip': {$gte: 10019, $lt: 10040}})
//<end id="users-zips"/>  

//<start id="orders-sku"/>  
db.orders.find({'line_items.sku': "9092"})
//<end id="orders-sku"/>  

//<start id="orders-sku-since"/>  
db.orders.find({'line_items.sku': "9092",
    'purchase_date': {$gte: new Date(2009, 1, 1)}})
//<end id="orders-sku-since"/>  

//<start id="orders-sku-since-index"/>  
db.orders.ensureIndex({'line_items.sku': 1, 'purchase_date': 1})
//<end id="orders-sku-since-index"/>  

//<start id="orders-sku-since-user"/>  
user_ids = db.orders.find({'line_items.sku': "9092",
  purchase_date: {'$gt': new Date(2009, 0, 1)}},
  {user_id: 1, _id: 0})
users = db.users.find({_id: {$in: user_ids}})
//<end id="orders-sku-since-user"/>  

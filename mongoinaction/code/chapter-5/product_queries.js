// Product page
db.products.findOne({'_id': ObjectId("4c4b1476238d3b4dd5003981")})

// Displaying a product page.
//<start id="product-page"/>  
product  = db.products.findOne({'slug': 'wheel-barrow-9092'})
category = db.categories.findOne({'_id': product['main_cat_id']})
reviews  = db.reviews.find({'product_id': product['_id']})
//<end id="product-page"/>  

//<start id="product-page-find-one"/>  
db.products.find({'slug': 'wheel-barrow-9092'}).limit(1)
//<end id="product-page-find-one"/>  

//<start id="product-page-review-skip-limit"/>  
reviews = db.reviews.find({'product_id': product['_id']}).skip(0).limit(12)
//<end id="product-page-review-skip-limit"/>  

//<start id="product-page-review-skip-limit-sort"/>  
reviews = db.reviews.find({'product_id': product['_id']}).
                           skip(0).limit(12).sort({helpful_votes: -1})
//<end id="product-page-review-skip-limit-sort"/>  


//<start id="product-page-final"/>  
var page_number = 10
product  = db.products.findOne({'slug': 'wheel-barrow-9092'})
category = db.categories.findOne({'_id': product['main_cat_id']})
reviews_count = db.reviews.count({'product_id': product['_id']})
reviews = db.reviews.find({'product_id': product['_id']}).
                         skip((page_number - 1) * 12).
                         limit(12).
                         sort({'helpful_votes': -1})
//<end id="product-page-final"/>  

//<start id="product-listing-page"/>  
category = db.categories.findOne({'slug': 'outdoors'})
siblings = db.categories.find({'parent_id': category['_id']})
products = db.products.find({'category_id': category['_id']}).
                           skip((page_number - 1) * 12).
                           limit(12).
                           sort({helpful_votes: -1})
//<end id="product-listing-page"/>  

// Displaying the category hierarchy
//<start id="category-page-root"/>  
categories = db.categories.find({'parent_id': null})
//<end id="category-page-root"/>  


// Add to cart
//<start id="orders-construct-item"/>  
cart_item = {
  _id:  ObjectId("4c4b1476238d3b4dd5003981"),
  slug: "wheel-barrow-9092",
  sku:  "9092",

  name: "Extra Large Wheel Barrow",

  pricing: {
    retail: 589700,
    sale:   489700
  }
}
//<end id="orders-construct-item"/>  

//<start id="orders-add-to-cart"/>  
selector = {user_id: ObjectId("4c4b1476238d3b4dd5000001"),
            state:   'CART',
            'line_items.id':
              {'$ne': ObjectId("4c4b1476238d3b4dd5003981")}
           }

update = {'$push': {'line_items': cart_item}}

db.orders.update(selector, update, true, false)
//<end id="orders-add-to-cart"/>  

//<start id="orders-initial-document"/>  
{
user_id: ObjectId("4c4b1476238d3b4dd5000001"),
state:  'CART',
line_items: [{
    _id:  ObjectId("4c4b1476238d3b4dd5003981"),
    slug: "wheel-barrow-9092",
    sku:  "9092",

    name: "Extra Large Wheel Barrow",

    pricing: {
      retail: 589700,
      sale:   489700
    }
  }]
}
//<end id="orders-initial-document"/>  

//<start id="orders-update-quantity"/>  
selector = {user_id: ObjectId("4c4b1476238d3b4dd5000001"),
            state:  "CART",
            'line_items.id': ObjectId("4c4b1476238d3b4dd5003981")}

update = {$inc:
            {'line_items.$.qty': 1,
             sub_total: cart_item['pricing']['sale']
            }
         }

db.orders.update(selector, update)
//<end id="orders-update-quantity"/>  

//<start id="orders-subsequent-document"/>  
{
'user_id': ObjectId("4c4b1476238d3b4dd5000001"),
'state'  : 'CART',
'line_items': [{
    _id:  ObjectId("4c4b1476238d3b4dd5003981"),
    qty:  2,
    slug: "wheel-barrow-9092",
    sku:  "9092",

    name: "Extra Large Wheel Barrow",

    pricing: {
      retail: 589700,
      sale:   489700
    }
  }],

  subtotal: 979400
}
//<end id="orders-subsequent-document"/>  

//<start id="orders-transition-state-1"/>  
  db.orders.findAndModify({
    query: {user_id: ObjectId("4c4b1476238d3b4dd5000001"),
              state: "CART" },

    update: {"$set": {"state": "PRE-AUTHORIZE"},
    new: true}}
  )
//<end id="orders-transition-state-1"/>  


//<start id="orders-transition-state-2"/>  
  db.orders.findAndModify({
    query: {user_id:  ObjectId("4c4b1476238d3b4dd5000001"),
               total: 99000,
               state: "PRE-AUTHORIZE" },

    update: {"$set": {"state": "AUTHORIZING"}}}
  )
//<end id="orders-transition-state-2"/>  


//<start id="orders-transition-state-3"/>  
  auth_doc = {ts: new Date(),
              cc: 3432003948293040,
              id: 2923838291029384483949348,
              gateway: "Authorize.net"}

  db.orders.findAndModify({
    query: {user_id: ObjectId("4c4b1476238d3b4dd5000001"),
               state: "AUTHORIZING" },

    update: {"$set":
                  {"state": "PRE-SHIPPING"},
                   "authorization": auth}}
  )
//<end id="orders-transition-state-3"/>  


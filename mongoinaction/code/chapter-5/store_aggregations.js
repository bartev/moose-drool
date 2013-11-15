//<start id="store-group-reduce"/>  
initial = {review: 0, votes: 0};

reduce  = function(doc, aggregator) {
            aggregator.reviews += 1.0;
            aggregator.votes   += doc.votes;
          }
//<end id="store-group-reduce"/>  


//<start id="store-group"/>  
results = db.reviews.group({
  key:      {user_id: true},
  initial:  {reviews: 0, votes: 0.0},
  reduce:   function(doc, aggregator) {
               aggregator.reviews += 1;
               aggregator.votes   += doc.votes;
            },
  finalize: function(doc) {
               doc.average_votes = doc.votes / doc.reviews;
            }
})
//<end id="store-group"/>  

//<start id="store-group-results"/>  
[
  {user_id: ObjectId("4d00065860c53a481aeab608"),
   votes: 25.0,
   reviews: 7,
   average: 3.57
  },

  {user_id: ObjectId("4d00065860c53a481aeab608"),
   votes: 25.0,
   reviews: 7,
   average: 3.57
  }
]
//<end id="store-group-results"/>  

//<start id="store-map"/>  
map = function() {
    var shipping_month = this.purchase_date.getMonth() +
      '-' + this.purchase_data.getFullYear();

    var items = 0;
    this.line_items.forEach(function(item) {
      tmpItems += item.quantity;
    });

    emit(shipping_month, {order_total: this.sub_total, items_total: 0});
  }
//<end id="store-map"/>  

//<start id="store-reduce"/>  
reduce = function(key, values) {
    var tmpTotal = 0;
    var tmpItems = 0;

    tmpTotal += doc.order_total;
    tmpItems += doc.items_total;

    return ( {total: tmpTotal, items: tmpItems} );
  }
//<end id="store-reduce"/>  

//<start id="store-map-reduce"/>  
filter = {purchase_date: {$gte: new Date(2010, 0, 1)}}
db.orders.mapReduce(map, reduce, {query: filter, out: 'totals'})
//<end id="store-map-reduce"/> 

//<start id="store-map-reduce-results"/>  
db.totals.find()
{ _id: "1-2011", value: { total: 32002300, items: 59 }}
{ _id: "2-2011", value: { total: 45439500, items: 71 }}
{ _id: "3-2011", value: { total: 54322300, items: 98 }}
{ _id: "4-2011", value: { total: 75534200, items: 115 }}
{ _id: "5-2011", value: { total: 81232100, items: 121 }}
//<end id="store-map-reduce-results"/> 

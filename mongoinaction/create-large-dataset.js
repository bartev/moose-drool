// Create 'numbers' collection and populate it
for (i=0; i < 200000; i++) {
	db.numbers.save({num i});
}

db.numbers.find({num: 500})
db.numbers.find({num : {$gt: 500}})
db.numbers.find({num : {$gt: 20, $lt: 25}})
db.numbers.find({num : {$gt: 199995}}).explain()

// Create an index
db.numbers.ensureIndex({num:1})
db.numbers.getIndexes()


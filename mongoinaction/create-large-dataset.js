// Create 'numbers' collection and populate it
for (i=0; i < 200000; i++) {
	db.numbers.save({num: i});
}
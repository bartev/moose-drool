// insert a document into users
db.users.insert({username: 'smith'})
db.users.insert({username: 'jones'})

// count how many entries in collection
db.users.count()

// Pass a query selector (matcher?)
db.users.find({'username' : 'jones'})
// Empty selector
db.users.find()

// Passing multiple entries is same as AND
// How about OR?
db.users.find({$or : [ {'username' : 'jones'}, {'username' : 'smith'}]})

// Update user 'smith' by adding country

// Adds country 'Canada'
db.users.update({username : 'smith'}, {$set : {country : 'Canada'}})

// Replaces entire record with {country:'Canada'} (lose data)
db.users.update({username:'smith'}, {country:'Canada'})
db.users.insert({username: 'smith', country:'Canada'})

// Remove a value
db.users.update({country : 'Canada'}, {$unset : {country : 1}})

// Add nested lists
db.users.update( {username : 'smith'}, {$set : {favorites : { cities: ['Chicago', 'Cheyenne'], movies : ['Casablanca', 'The Sting', 'Top Gun']}}})
db.users.update({username: 'jones'}, {$set : { favorites : { movies: ['Casablanca', 'Rocky']}}})

// Find users who like 'Casablanca'
// Need quotes to use dot notation
db.users.find({'favorites.movies' : 'Casablanca'})

// Add 'The Maltese Falcon' to users who like 'Casablanca'
// false means 'upsert' is not allowed
// true means it's a multi-update (otherwise it would only apply to the first matching document)
db.users.update({'favorites.movies': 'Casablanca'}, {$addToSet: {'favorites.movies': 'The Maltese Falcon'}}, false, true)
# Load the driver
require 'rubygems'
require 'mongo'

# Instantiate connection
$con 	= Mongo::Connection.new
# assign tutorial database to the $db variable
$db 	= $con['tutorial']
# Store reference to users collection to $users variable
$users 	= $db['users']


# Build some documents
smith = {"last_name" => "smith", "age" => 30}
jones = {"last_name" => "jones", "age" => 40}

# smith_id = $users.insert(smith)
# jones_id = $users.insert(jones)

# p $users.find_one({"_id" => smith_id})

cursor = $users.find({"age" => {"$gt" => 30}})
cursor.each do |doc|
	puts doc["last_name"]
end

# Drop the collection 'users'

# $db.drop_collection('users')

# or
# connection = Mongo::Connection.new
# db = connection['tutorial']
# db.drop_collection('users')

p "users.find()"
# $users.find().each do |doc| puts doc["last_name"] end


# Database commands
p "database commands"
# $admin_db = $con['admin']
# res = $admin_db.command({"listDatabases" => 1})
# res.each { |doc| puts doc }

p id = BSON::ObjectId.new
p id.generation_time

# Generate id from timestamp
jun_id = BSON::ObjectId.from_time(Time.utc(2013,6,1))
jul_id = BSON::ObjectId.from_time(Time.utc(2013,6,1))
nov_id = BSON::ObjectId.from_time(Time.utc(2013,11,30))

p "to november"
res = $users.find({'_id' => {'$gte' => jun_id, '$lt' => nov_id}})
res.each { |r| puts r["last_name"] }

p "to july"
res = $users.find({'_id' => {'$gte' => jun_id, '$lt' => jul_id}})
res.each { |r| puts r["last_name"] }

p $users.find_one()
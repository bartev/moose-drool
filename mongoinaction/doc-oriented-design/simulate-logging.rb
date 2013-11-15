require "rubygems"
require "mongo"
require "BSON"

VIEW_PRODUCT 	= 0
ADD_TO_CART 	= 1
CHECKOUT 		= 2
PURCHASE 		= 3

con = Mongo::Connection.new
@db = con['garden']



def add_five_hundred
	@db.drop_collection('user.actions')
	@db.create_collection('user.actions', :capped => true, :size => 16384)
	actions = @db['user.actions']	# refers to the garden.user.actions collection
	500.times do |n|					# Loop 500 times, using n as iterator
	doc = {
		:username => 'kbanker',
		:action_code => rand(4),	# random value between 0 and 3, inclusive
		:time => Time.now.utc,
		:n => n
	}
	actions.insert(doc)
	# puts doc
	end	
end

# add_five_hundred
@bson
def check_bson_size
	doc = {
		:_id => BSON::ObjectId.new,
		:username => "kbanker",
		:action_code => rand(5),
		:time => Time.now.utc,
		:n => 1
	}
	@bson = BSON::BSON_CODER.serialize(doc)
	puts "Document #{doc.inspect} takes up #{@bson.length} bytes as BSON"
end

def deser_bson
	deserialized_doc = BSON::BSON_CODER.deserialize(@bson)
	puts "Here's our document deserialized from BSON:"
	puts deserialized_doc.inspect
end

def bulk_insert
	docs = (0..40).map do |n|
		{
			:username => 'kbanker', 
			:action_code => rand(5),
			:time => Time.now.utc,
			:n => n
		}
	end
	@col = @db['test.bulk.insert']
	@ids = @col.insert(docs)
	puts "here are the ids from the bulk insert: #{@ids.inspect}"
end

# check_bson_size
# deser_bson
bulk_insert
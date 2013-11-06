$LOAD_PATH << File.dirname(__FILE__)
# require libraries
require "rubygems"
require "mongo"
require "sinatra"
require "config"

# Instantiate collection for tweets
configure do
	db = Mongo::Connection.new[DATABASE_NAME]
	TWEETS = db[COLLECTION_NAME]
end

get '/' do
	if params['tag']
		# Dynamically build query selector
		selector = {:tags => params['tag']}
	else
		# or use blank selector
		selector = {}
	end
	
	# issue query
	@tweets = TWEETS.find(selector).sort(["id", -1])
	
	# render view
	erb :tweets
end
	
$LOAD_PATH << File.dirname(__FILE__)
require 'rubygems'
require "mongo"
require "twitter"
require "config"

class TweetArchiver
	
	# Create a new instance of TweetArchiver
	def initialize(tag)
		# Instantiate a connection, db object, and collection 
		# object where we'll store the tweets
		connection 	= Mongo::Connection.new
		db			= connection[DATABASE_NAME]
		@tweets		= db[COLLECTION_NAME]
		
		# Create a compound index on tags ascending and id descending
		@tweets.create_index([['tags', 1], ['id', -1]])
		@tag 		= tag
		@tweets_found = 0
		
		# configure Twitter client with authentication info from config.rb
		Twitter.configure do |config|
			config.consumer_key 		= CONSUMER_KEY 
			config.consumer_secret		= CONSUMER_SECRET 
			config.oauth_token			= TOKEN 
			config.oauth_token_secret	= TOKEN_SECRET
			puts config
		end	
	end
	
	# Notify the user all the save_save_tweets_for method
	def update
		puts "Starting Twitter search for '#{@tag}'..."
		save_tweets_for(@tag)
		print "#{@tweets_found} tweets saved.\n\n"
	end
	
	# Search with twitter client and save the results to Mongo
	def save_tweets_for(term)
		Twitter.search(term).results.map do |tweet|
			@tweets_found += 1
			tweet_doc = tweet.to_hash
			tweet_doc[:tags] = term
			tweet_doc[:_id] = tweet_doc[:id]
			@tweets.save(tweet_doc)
		end
	end	
end



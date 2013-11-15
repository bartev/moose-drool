require 'rubygems'
require 'mongo'

# Get connection and collection
@conn = Mongo::Connection.new
@forum = @conn['forum']
@forum.drop_collection('comments')
@comments = @forum['comments']

# Create indexes
@comments.create_index("path")
@comments.create_index("thread_id")

# Get a unique id for the thread
@thread_id = BSON::ObjectId.new

# Insert seed data
@id1 = @comments.insert({:depth => 0,
                        :path  => nil,
                        :created => Time.now,
                        :username => "plotinus",
                        :body => "Who was Alexander the Great's teacher?",
                        :thread_id => @thread_id})

@id2 = @comments.insert({:depth => 0,
                        :path  => nil,
                        :created => Time.now,
                        :username => "seuclid",
                        :body => "So who really discarded the paralell postulate?",
                        :thread_id => @thread_id})

@id3 = @comments.insert({:depth => 1,
                        :path  => @id1.to_s,
                        :created => Time.now,
                        :username => "asophist",
                        :body => "It was definitely Socrates.",
                        :thread_id => @thread_id})

@id4 = @comments.insert({:depth => 2,
                        :path  => @id1.to_s + ":" + @id3.to_s,
                        :created => Time.now,
                        :username => "daletheia",
                        :body => "On you sophist...It was actually Aristotle!",
                        :thread_id => @thread_id})

#<start id="threaded">   
def threaded_list(cursor, opts={})
  list      = []
  child_map = {}
  start_depth = opts[:start_depth] || 0

  cursor.each do |comment|
    if comment['depth'] == start_depth
      list.push(comment)
    else
      matches = comment['path'].match(/([\d|\w]+)$/)
      immediate_parent_id = matches[1]
      if immediate_parent_id
        child_map[immediate_parent_id] ||= []
        child_map[immediate_parent_id] << comment
      end
    end
  end

  assemble(list, child_map)
end
#<end id="threaded">   

#<start id="assemble">   
def assemble(comments, map)
  list = []
  comments.each do |comment|
    list.push(comment)
    child_comments = map[comment['_id'].to_s]
    if child_comments
      list.concat(assemble(child_comments, map))
    end
  end

  list
end
#<end id="assemble">   

#<start id="print_threaded">   
def print_threaded_list(cursor, opts={})
  threaded_list(cursor, opts).each do |item|
    indent = "  " * item['depth']
    puts indent + item['body'] + " #{item['path']}"
  end
end
#<end id="print_threaded">   

# Return all results
#<start id="query_print_threaded">   
cursor = @comments.find.sort("created")
print_threaded_list(cursor)
#<end id="query_print_threaded">   

# Return particular subtree
cursor = @comments.find(
  :path => Regexp.new("^" + @id1.to_s)).sort("created")
puts "\nList 2"
print_threaded_list(cursor, :start_depth => 1)

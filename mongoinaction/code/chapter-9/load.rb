require 'rubygems'
require 'mongo'
require 'names'

#<start id="write_docs">
@con  = Mongo::Connection.new("localhost", 40000)
@col  = @con['cloud']['spreadsheets']
@data = "abcde" * 1000

def write_user_docs(iterations=0, name_count=200)
  iterations.times do |n|
    name_count.times do |n|
      doc = { :filename => "sheet-#{n}",
              :updated_at => Time.now.utc,
              :username => Names::LIST[n],
              :data => @data
            }
      @col.insert(doc)
    end
  end
end
#<start id="write_docs">

if ARGV.empty? || !(ARGV[0] =~ /^\d+$/)
  puts "Usage: load.rb [iterations] [name_count]"
else
  iterations = ARGV[0].to_i

  if ARGV[1] && ARGV[1] =~ /^\d+$/
    name_count = ARGV[1].to_i
  else
    name_count = 200
  end

  write_user_docs(iterations, name_count)
end

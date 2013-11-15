require 'rubygems'
require 'mongo'

module Mongo
  class GridIO
    def eof?
      @file_position >= @file_length
    end
  end
end

#<start id="store-file"/>  
@con  = Mongo::Connection.new
@db   = @con["images"]

@grid = Mongo::Grid.new(@db)

filename = File.join(File.dirname(__FILE__), "canyon.jpg")
file = File.open(filename, "r")

file_id = @grid.put(file, :filename => "canyon.jpg")
#<end id="store-file"/>  

#<start id="copy-file"/>  
image_io = @grid.get(file_id)

copy_filename = File.join(File.dirname(__FILE__), "canyon-copy.jpg")
copy = File.open(copy_filename, "w")

while !image_io.eof? do
  copy.write(image_io.read(256 * 1024))
end

copy.close
#<start id="copy-file"/>  

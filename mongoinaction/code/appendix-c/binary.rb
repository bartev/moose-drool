#<start id="image-data"/>  
require 'rubygems'
require 'mongo'

image_filename = File.join(File.dirname(__FILE__), "canyon-thumb.jpg")
image_data = File.open(image_filename).read

bson_image_data = BSON::Binary.new(image_data)
#<end id="image-data"/>  

#<start id="save-image-data"/>  
doc = {"name" => "monument-thumb.jpg",
       "data" => bson_image_data }

@con = Mongo::Connection.new
@thumbnails = @con['images']['thumbnails']
@image_id = @thumbnails.insert(doc)
#<end id="save-image-data"/>  

#<start id="copy-image-data"/>  
doc = @thumbnails.find_one({"_id" => @image_id})
if image_data == doc["data"].to_s
  puts "Stored image is equal to the original file!"
end
#<end id="copy-image-data"/>  

#<start id="update-md5-data"/>  
require 'md5'
md5 = Digest::MD5.file(image_filename).digest
bson_md5 = BSON::Binary.new(md5, BSON::Binary::SUBTYPE_MD5)

@thumbnails.update({:_id => @image_id}, {"$set" => {:md5 => bson_md5}})
#<end id="update-md5-data"/>  

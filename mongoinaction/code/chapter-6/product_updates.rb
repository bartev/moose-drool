require 'mongo'
require 'rubygems'

@connection = Mongo::Connection.new
@db = @connection['green']

@reviews  = @db['reviews']
@products = @db['products']

# Set average rating
#<start id="products-set-average-rating"/>  
average = 0.0
count   = 0
total   = 0
cursor = @reviews.find({:product_id => product_id}, :fields => ["rating"])
while cursor.has_next? && review = cursor.next()
  total += review['rating']
  count += 1
end

average = total / count

@products.update({:_id => BSON::ObjectID("4c4b1476238d3b4dd5003981")},
   {'$set' => {:total_reviews => count, :average_review => average}})
#<end id="products-set-average-rating"/>  

# Generate a list of ancestors
#<start id="categories-set-ancestors"/>  
def generate_ancestors(_id, parent_id)
  ancestor_list = []
  while parent = @categories.find_one(:_id => parent_id) do
    ancestor_list.unshift(parent)
    parent_id = parent['parent_id']
  end

  @categories.update({:_id => _id},
    {"$set" => {:ancestors => ancestor_list}})
end
#<end id="categories-set-ancestors"/>  

# Add a new category
#<start id="categories-add-new"/>  
category = {
  :parent_id => parent_id,
  :slug => "gardening",
  :name => "Gardening",
  :description => "All gardening implements, tools, seeds, and soil."
}
gardening_id = @categories.insert(category)
generate_ancestors(gardening_id, parent_id)
#<end id="categories-add-new"/>  

#<start id="categories-move-outdoors"/>  
#alvin: these are missing their object ids
@categories.update({:_id => outdoors_id},
                   {'$set' => {:parent_id => gardening_id}})
#<end id="categories-move-outdoors"/>  

#<start id="categories-move-outdoors-descendants"/>  
@categories.find({'ancestors.id' => outdoors_id}).each do |category|
  generate_ancestors(category['_id'], outdoors_id)
end
#<end id="categories-move-outdoors-descendants"/>  


#<start id="categories-update-outdoors-name"/>  
doc = @categories.find_one({:_id => outdoors_id})
doc['name'] = "The Great Outdoors"
@categories.update({:_id => outdoors_id}, doc)

@categories.update({'ancestors.id' => outdoors_id},
  {'$set' => {'ancestors.$' => doc}}, :multi => true)
#<end id="categories-update-outdoors-name"/>  

require "rubygems"
require "mongo"
require File.join(File.dirname(__FILE__), "..", "lib", "inventory.rb")

@con = Mongo::Connection.new
@db = @con['green']

@orders    = @db['orders']
@inventory = @db['inventory']

@orders.remove
@inventory.remove

include InventoryState

#<start id="inventory-populate"/>  
3.times do
  @inventory.insert({:sku => 'shovel',   :state => AVAILABLE})
  @inventory.insert({:sku => 'rake',     :state => AVAILABLE})
  @inventory.insert({:sku => 'clippers', :state => AVAILABLE})
end
#<end id="inventory-populate"/>  

#<start id="inventory-add-to-cart"/>  
@order_id = @orders.insert({:username => 'kbanker', :item_ids => []})
@fetcher  = InventoryFetcher.new(:orders    => @orders,
                                 :inventory => @inventory)

@fetcher.add_to_cart(@order_id,
                     {:sku => "shovel", :qty => 3},
                     {:sku => "clippers", :qty => 1})

order = @orders.find_one({"_id" => @order_id})
puts "\nHere's the order:"
p order
#<end id="inventory-add-to-cart"/>  

#<start id="inventory-order-post-add"/>  
{"_id" => BSON::ObjectId('4cdf3668238d3b6e3200000a'),
 "username"=>"kbanker",
 "item_ids" => [BSON::ObjectId('4cdf3668238d3b6e32000001'),
                BSON::ObjectId('4cdf3668238d3b6e32000004'),
                BSON::ObjectId('4cdf3668238d3b6e32000007'),
                BSON::ObjectId('4cdf3668238d3b6e32000009')],
}
#<end id="inventory-order-post-add"/>  

#<start id="inventory-examine-add-to-cart"/>  
puts "\nHere's each item:"
order['item_ids'].each do |item_id|
  item = @inventory.find_one({"_id" => item_id})
  p item
end
#<end id="inventory-examine-add-to-cart"/>  

#<start id="inventory-items-post-add"/>  
{"_id" => BSON::ObjectId('4cdf3668238d3b6e32000001'),
  "sku"=>"shovel", "state"=>1, "ts"=>"Sun Nov 14 01:07:52 UTC 2010"}

{"_id"=>BSON::ObjectId('4cdf3668238d3b6e32000004'),
  "sku"=>"shovel", "state"=>1, "ts"=>"Sun Nov 14 01:07:52 UTC 2010"}

{"_id"=>BSON::ObjectId('4cdf3668238d3b6e32000007'),
  "sku"=>"shovel", "state"=>1, "ts"=>"Sun Nov 14 01:07:52 UTC 2010"}

{"_id"=>BSON::ObjectId('4cdf3668238d3b6e32000009'),
  "sku"=>"clippers", "state"=>1, "ts"=>"Sun Nov 14 01:07:52 UTC 2010"}
#<end id="inventory-items-post-add"/>  

#<start id="inventory-add-to-cart-fail"/>  
begin
  @fetcher.add_to_cart(@order_id, {:sku => "shovel",   :qty => 1},
                                  {:sku => "clippers", :qty => 1})
rescue InventoryFetchFailure => e
  puts "Failed to fetch inventory: #{e}"
end
#<end id="inventory-add-to-cart-fail"/>  

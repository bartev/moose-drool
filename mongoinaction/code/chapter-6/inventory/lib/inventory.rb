require 'rubygems'
require 'mongo'

class InventoryFetchFailure < StandardError
end

module InventoryState
  AVAILABLE = 0
  IN_CART   = 1
  PRE_ORDER = 2
  PURCHASED = 3
end

class InventoryFetcher
  include InventoryState

  def initialize(opts={})
    @orders    = opts[:orders]
    @inventory = opts[:inventory]
  end

#<start id="inventory-add-to-cart"/>  
  def add_to_cart(order_id, *items)
    item_selectors = []
    items.each do |item|
      item[:qty].times do
        item_selectors << {:sku => item[:sku]}
      end
    end

    transition_state(order_id, item_selectors, :from => AVAILABLE, :to => IN_CART)
  end
#<end id="inventory-add-to-cart"/>  

  private

#<start id="inventory-transition-state"/>  
  def transition_state(order_id, selectors, opts={})
    items_transitioned = []

    begin
      for selector in selectors do
        query = selector.merge(:state => opts[:from])

        physical_item = @inventory.find_and_modify(:query => query,
          :update => {'$set' => {:state => opts[:to], :ts => Time.now.utc}})

        if physical_item.nil?
          raise InventoryFetchFailure
        end

        items_transitioned << physical_item['_id']

        @orders.update({:_id => order_id},
                       {"$push" => {:item_ids => physical_item['_id']}})
      end

    rescue Mongo::OperationFailure, InventoryFetchFailure
      rollback(order_id, items_transitioned, opts[:from], opts[:to])
      raise InventoryFetchFailure, "Failed to add #{selector[:sku]}"
    end

    items_transitioned.size
  end
#<end id="inventory-transition-state"/>  

#<start id="inventory-rollback"/>  
  def rollback(order_id, item_ids, old_state, new_state)
    @orders.update({"_id" => order_id},
                   {"$pullAll" => {:item_ids => item_ids}})

    item_ids.each do |id|
      @inventory.find_and_modify(
        :query  => {"_id" => id, :state => new_state},
        :update => {"$set" => {:state => old_state, :ts => Time.now.utc}}
      )
    end
  end
#<end id="inventory-rollback"/>  

end

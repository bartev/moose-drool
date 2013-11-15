require 'test/test_helper'

class InventoryTest < Test::Unit::TestCase

  $con = Mongo::Connection.new

  def setup
    @db        = $con['inventory-test']
    @inventory = @db['inventory']
    @orders    = @db['orders']

    @inventory.remove
    @orders.remove
  end

  # Nine shovels, rakes, and clippers (three of each) added to the
  # inventory collection. For simplicity's sake, we assume that
  # the sku is synonomous with the product name.

  def populate_inventory
    3.times do
      @inventory.insert({:sku => 'shovel',   :state => InventoryState::AVAILABLE})
      @inventory.insert({:sku => 'rake',     :state => InventoryState::AVAILABLE})
      @inventory.insert({:sku => 'clippers', :state => InventoryState::AVAILABLE})
    end
  end

  context "An order with standard inventory:" do
    setup do
      @fetcher  = InventoryFetcher.new(:orders => @orders, :inventory => @inventory)
      @order_id = @orders.insert({:username => 'kbanker', :item_ids => []})
      populate_inventory
    end

    should "contain nine inventory items" do
      assert_equal 3, @inventory.find({:sku => "shovel"}).count
      assert_equal 3, @inventory.find({:sku => "rake"}).count
      assert_equal 3, @inventory.find({:sku => "clippers"}).count
    end

    context "when available items are added to cart" do
      setup do
        @fetcher.add_to_cart(@order_id, {:sku => "shovel", :qty => 3},
                                        {:sku => "clippers", :qty => 1})
      end

      should "add items to order" do
        order = @orders.find_one({"_id" => @order_id})
        assert_equal 4, order['item_ids'].length

        order['item_ids'].each do |item_id|
          item = @inventory.find_one({"_id" => item_id})
          assert_equal InventoryState::IN_CART, item['state']
        end
      end

      should "fail to add unavailable items to cart" do
        assert_raise InventoryFetchFailure do
          @fetcher.add_to_cart(@order_id, {:sku => "shovel", :qty => 1})
        end
      end
    end

    context "when an add_to_cart operation fails" do
      setup do
        assert_raise InventoryFetchFailure do
          @fetcher.add_to_cart(@order_id, {:sku => "shovel", :qty => 5})
        end
      end

      should "add no items to the order" do
        order = @orders.find_one({"_id" => @order_id})
        assert_equal [], order["item_ids"]
      end

      should "leave all items in an available state" do
        assert_equal 9, @inventory.find({:state => InventoryState::AVAILABLE}).count
      end
    end
  end
end

require 'mongo'
require 'rubygems'

@connection = Mongo::Connection.new
@db = @connection['green']

@users = @db['users']

# Update email address
#<start id="users-email-update-replace"/>  
user_id = BSON::ObjectId("4c4b1476238d3b4dd5000001")
doc     = @users.find_one({:_id => user_id})

doc['email'] = 'mongodb-user@10gen.com'
@users.update({:_id => user_id}, doc, :safe => true)
#<end id="users-email-update-replace"/>  

# Update email address
#<start id="users-email-update"/>  
@users.update({:_id => user_id},
  {'$set' => {:email => 'mongodb-user@10gen.com'}},
  :safe => true)
#<end id="users-email-update"/>  

# Adding a shipping address by replacement
#<start id="users-address-add-replace"/>  
doc = @users.find_one({:_id => user_id})

new_address = {
       :name   => "work",
       :street => "17 W. 18th St.",
       :city   => "New York",
       :state  => "NY",
       :zip    => 10011
}
doc['shipping_addresses'].append(new_address)
@users.update({:_id => user_id}, doc)
#<end id="users-address-add-replace"/>  

#<start id="users-address-add-target"/>  
@users.update({:_id => user_id},
  {'$push' => {:addresses =>
      {:name => "work",
       :street => "17 W. 18th St.",
       :city   => "New York",
       :state => "NY",
       :zip    => 10011
      }
    }
  })
#<end id="users-address-add-target"/>  


# Using safe mode
#<start id="users-email-update-safe"/>  
@users.update({:_id => user_id},
  {'$set' => {:email => 'kylebanker@gmail.com'} }, :safe => true)
#<end id="users-email-update-safe"/>  

#<start id="users-email-update-exception"/>  
#Mongo::OperationFailure: E11001 duplicate key on update
#<end id="users-email-update-exception"/>  


#<start id="users-template"/>  

#<end id="users-template"/>  


<?php
  // basic
  // <start
  //<start id="basic"/>  
  $basic = array( "username" => "jones", "zip" => 10011 );
  //<end id="basic"/>  

  // complex
  //<start id="complex"/>  
  $doc = array( "url"   => "org.mongodb",
                "tags"  => array( "database", "open-source"),
                "attrs" => array( "last_access" => new MongoDate(),
                                  "pingtime" => 20
                                )
              );
  //<end id="complex"/>  
?>


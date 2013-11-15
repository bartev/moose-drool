<?php
  // Basic, single-node connection
  //<start id="standard"/>  
  $conn = new Mongo( "localhost", 27017 );
  //<end id="standard"/>  

  // Replica set connection
  //<start id="replset"/>  
  $repl_conn = new Mongo( "mongo://localhost:30000,localhost:30001",
                array( "replicaSet" => true ));
  //<end id="replset"/>  

  // Persistent connections
  //<start id="persistent"/>  
  $conn = new Mongo( "localhost", 27017, array( "persist" => "x" ) );
  //<end id="persistent"/>  
?>


<start id="code">   
<?php
  $m = new Mongo( "localhost", 27017 );
  $db = $m->crawler;
  $coll = $db->sites;

  $doc = array( "url"   => "org.mongodb",
                "tags"  => array( "database", "open-source"),
                "attrs" => array( "last_access" => new MongoDate(),
                                  "pingtime" => 20
                                )
              );

  $coll->insert( $doc );

  print "Initial document:\n";
  print print_r( $doc );

  print "Updating pingtime...\n";
  $coll->update(
    array( "_id"  => $doc["_id"] ),
    array( '$set' => array( 'attrs.pingtime' => 30 ) )
  );

  print "After update:\n";
  $cursor = $coll->find();
  print print_r( $cursor->getNext() );

  print "\nNumber of site documents: " . $coll->count() . "\n";

  print "Removing documents...\n";
  $coll->remove();
?>
<end id="code">   

// Note: Java docs are at http://api.mongodb.org/java/current/index.html
// This can be downloaded at https://gist.github.com/795748
// Compile and run it as follows:

// On *.nix systems:
// javac -cp mongo.jar:. Sample.java
// java -cp mongo.jar:. Sample

// On Windows:
// javac -cp mongo.jar;. Sample.java
// java -cp mongo.jar;. Sample
//<start id="code">   
import com.mongodb.Mongo;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.BasicDBObject;
import com.mongodb.DBObject;
import com.mongodb.DBCursor;
import com.mongodb.WriteConcern;
import java.util.Date;

public class Sample {

  public static void main(String[] args) {

    Mongo conn;
    try {
      conn = new Mongo("localhost", 27017);
    } catch (Exception e) {
      throw new RuntimeException(e);
    }

    WriteConcern w = new WriteConcern( 1, 2000 );
    conn.setWriteConcern( w );

    DB db = conn.getDB( "crawler" );
    DBCollection coll = db.getCollection( "sites" );

    DBObject doc = new BasicDBObject();
    String[] tags = { "database", "open-source" };

    doc.put("url", "org.mongodb");
    doc.put("tags", tags);

    DBObject attrs = new BasicDBObject();
    attrs.put( "lastAccess", new Date() );
    attrs.put( "pingtime", 20 );

    doc.put( "attrs", attrs );

    coll.insert(doc);

    System.out.println( "Initial document:\n" );
    System.out.println( doc.toString() );

    System.out.println( "Updating pingtime...\n" );
    coll.update( new BasicDBObject( "_id", doc.get("_id") ),
       new BasicDBObject( "$set", new BasicDBObject( "pingtime", 30 ) ) );

    DBCursor cursor = coll.find();

    System.out.println( "After update\n" );
    System.out.println( cursor.next().toString() );

    System.out.println( "Number of site documents: " + coll.count() );

    System.out.println( "Removing documents...\n" );
    coll.remove( new BasicDBObject() );
  }
}
//<end id="code">   

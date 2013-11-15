// Note: Java docs are at http://api.mongodb.org/java/current/index.html
// This can be downloaded at https://gist.github.com/795748
// Compile and run it as follows:

// On *.nix systems:
// javac -cp mongo.jar:. Sample.java
// java -cp mongo.jar:. Sample

// On Windows:
// javac -cp mongo.jar;. Sample.java
// java -cp mongo.jar;. Sample
import com.mongodb.Mongo;
import com.mongodb.DB;
import com.mongodb.BasicDBObject;
import com.mongodb.DBObject;
import java.util.Date;

public class Sample {

  public static void main(String[] args) {

    // Simple doc
    //<start id="simple">   
    DBObject simple = new BasicDBObject( "username", "Jones" );
    simple.put( "zip", 10011 );
    //<end id="simple">   

    System.out.println( doc.toString() );

    // Complex document
    //<start id="complex">   
    DBObject doc = new BasicDBObject();
    String[] tags = { "database", "open-source" };

    doc.put("url", "org.mongodb");
    doc.put("tags", tags);

    DBObject attrs = new BasicDBObject();
    attrs.put( "lastAccess", new Date() );
    attrs.put( "pingtime", 20 );

    doc.put( "attrs", attrs );

    System.out.println( doc.toString() );
    //<end id="complex">   
  }
}

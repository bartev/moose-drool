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
import com.mongodb.WriteConcern;

public class Connect {

  public static void main(String[] args) {

    // Basic connection
    //<start id="standard">   
    try {
      Mongo conn = new Mongo("localhost", 27017);
    } catch (Exception e) {
      throw new RuntimeException(e);
    }
    //<end id="standard">   

    //<start id="wc">   
    WriteConcern w = new WriteConcern( 1, 2000 );
    conn.setWriteConcern( w );
    //<end id="wc">   

    // Replica set connection
    //<start id="replset">   
    List servers = new ArrayList();
    servers.add( new ServerAddress( "localhost" , 30000 ) );
    servers.add( new ServerAddress( "localhost" , 30001 ) );

    try {
      Mongo replConn = new Mongo( servers );
    } catch (Exception e) {
      throw new RuntimeException(e);
    //<end id="replset">   

    // Send reads to secondaries
    replConn.slaveOk();
  }
}

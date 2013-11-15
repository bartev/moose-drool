//<start id="code">   
#include <iostream>
#include <ctime>
#include "client/dbclient.h"

using namespace mongo;

int main() {
    DBClientConnection conn;

    try {
      conn.connect("localhost:27017");
    }
    catch( DBException &e ) {
        cout << "caught " << e.what() << endl;
    }

    BSONObj doc = BSON( GENOID << "url" << "org.mongodb"
      << "tags" << BSON_ARRAY( "database" << "open-source" )
      << "attrs" << BSON( "lastVisited" << DATENOW << "pingtime" << 20 ) );

    cout << "Initial document:\n" << doc.jsonString() << "\n";
    conn.insert( "crawler.sites", doc );

    cout << "Updating pingtime...\n";
    BSONObj update = BSON( "$set" << BSON( "attrs.pingtime" << 30) );
    conn.update( "crawler.sites", QUERY("_id" << doc["_id"]), update);

    cout << "After update:\n";
    auto_ptr<DBClientCursor> cursor;
    cursor = conn.query( "crawler.sites", QUERY( "_id" << doc["_id"]) );
    cout << cursor->next().jsonString() << "\n";

    cout << "Number of site documents: " <<
      conn.count( "crawler.sites" ) << "\n";

    cout << "Removing documents...\n";
    conn.remove( "crawler.sites", BSONObj() );

    return 0;
}
//<end id="code">   

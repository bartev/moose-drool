#include <iostream>
#include <ctime>
#include "client/dbclient.h"

using namespace mongo;

int main() {

    // Simple doc
    //<start id="simple">   
    BSONObjBuilder simple;
    simple.genOID().append("username", "Jones").append( "zip", 10011 );
    BSONObj doc = simple.obj();

    cout << doc.jsonString();
    //<end id="simple">   

    // Simple doc with macros
    //<start id="simple-macro">   
    BSONObj o = BSON( GENOID << "username" << "Jones" << "zip" << 10011 );
    cout << o.jsonString();
    //<end id="simple-macro">   

    // Complex document
    //<start id="complex">   
    BSONObjBuilder site;
    site.genOID().append("url", "org.mongodb");
    BSONObjBuilder tags;
    tags.append("0", "database");
    tags.append("1", "open-source");
    site.appendArray( "tags", tags.obj() );

    BSONObjBuilder attrs;
    time_t now = time(0);
    attrs.appendTimeT( "lastVisited", now );
    attrs.append( "pingtime", 20 );
    site.append( "attrs", attrs.obj() );

    BSONObj site_obj = site.obj();
    //<end id="complex">   

    cout << "Complex document:\n" << site_obj.jsonString() << "\n";

    // Complex document concise
    //<start id="complex-macro">   
    BSONObj site_concise = BSON( GENOID << "url" << "org.mongodb"
      << "tags" << BSON_ARRAY( "database" << "open-source" )
      << "attrs" << BSON( "lastVisited" << DATENOW << "pingtime" << 20 ) );
    //<end id="complex-macro">   

    cout << "Complex concise document:\n" << site_concise.jsonString() << "\n";

    // Basic query
    //<start id="query">   
    BSONObj selector = BSON( "_id" << 1 );
    Query * q1 = new Query( selector );
    cout << q1->toString() << "\n";
    //<end id="query">   

    // Query using query macro
    //<start id="query-macro">   
    Query q2 = QUERY( "pingtime" << LT << 20 );
    cout << q2.toString() << "\n";
    //<end id="query-macro">   

    return 0;
}

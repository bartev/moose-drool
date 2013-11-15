#include <iostream>
#include "client/dbclient.h"

// g++ connections.cpp -lmongoclient -lboost_thread -lboost_filesystem -o connections

using namespace mongo;

int main() {
    // Standard connection
    //<start id="standard">   
    DBClientConnection conn;

    try {
      conn.connect("localhost:27017");
    }
    catch( DBException &e ) {
        cout << "caught " << e.what() << endl;
    }
    //<end id="standard">   

    //<start id="replset">   
    std::vector<HostAndPort> seeds (2);
    seeds.push_back( HostAndPort( "localhost", 30000 ) );
    seeds.push_back( HostAndPort( "localhost", 30001 ) );

    DBClientReplicaSet repl_conn( "myset", seeds );
    try {
      repl_conn.connect();
    catch( DBException &e ) {
        cout << "caught " << e.what() << endl;
    }

    cout << repl_conn.toString();
    //<end id="replset">   

    // Test replica set insert
    repl_conn.insert( "foo.bar", BSON( "a" << 1 ) );

    return 0;
}

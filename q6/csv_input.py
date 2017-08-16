from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.auth import PlainTextAuthProvider
import csv

cluster = Cluster(
    contact_points=[
        "34.232.206.20", "34.231.95.40", "34.230.111.171"  # AWS_VPC_US_EAST_1 (Amazon Web Services (VPC))
    ],
    load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='AWS_VPC_US_EAST_1'),  # your local data centre
    port=9042,
    auth_provider=PlainTextAuthProvider(username='iccassandra', password='46b60c31d96514bc1a7f7e79f8a368b4')
)

session = cluster.connect()

print('Connected to cluster %s' % cluster.metadata.cluster_name)


def create_schema():
    # For retesting purposes - I have been trying to figure out
    session.execute("DROP TABLE IF EXISTS movies.items")
    session.execute("DROP KEYSPACE IF EXISTS movies ")
    session.execute(
        "CREATE KEYSPACE IF NOT EXISTS movies WITH replication " + "= {'class':'NetworkTopologyStrategy',  'AWS_VPC_US_EAST_1' : 3}  AND durable_writes = true;")
    session.execute("CREATE TABLE IF NOT EXISTS movies.items (" +
                    "movie_id int PRIMARY KEY," +
                    "title text," +
                    "release_year int," +
                    "genre text," +
                    "director text" +
                    ");")
    print("Schema Created")


def load_data():
    print("Loading data into movies")
    # Open CSV for each row
    query = "INSERT INTO movies.items (movie_id, title, release_year, genre, director) VALUES (?, ?, ?, ?, ?)"
    prepared = session.prepare(query)
    uid = 1
    with open('movies.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            session.execute(prepared, (uid, row['title'], int(row['release_year']), row['genre'], row['director']))
            uid += 1
    print("Data has been loaded")
    # make a quick check
    table = session.execute("SELECT * FROM movies.items")
    print(table.column_names)
    for row in table.current_rows:
        print(row)


create_schema()
load_data()

"""
for host in cluster.metadata.all_hosts():
    print ('Datacenter: %s; Host: %s; Rack: %s' % (host.datacenter, host.address, host.rack))
"""
cluster.shutdown()

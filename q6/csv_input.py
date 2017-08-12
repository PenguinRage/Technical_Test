from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.auth import PlainTextAuthProvider

cluster = Cluster(
    contact_points=[
        "34.232.206.20", "34.231.95.40", "34.230.111.171" # AWS_VPC_US_EAST_1 (Amazon Web Services (VPC))
    ],
    load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='AWS_VPC_US_EAST_1'), # your local data centre
    port=9042,
        auth_provider = PlainTextAuthProvider(username='iccassandra', password='46b60c31d96514bc1a7f7e79f8a368b4')
)

session = cluster.connect()

print 'Connected to cluster %s' % cluster.metadata.cluster_name

for host in cluster.metadata.all_hosts():
    print 'Datacenter: %s; Host: %s; Rack: %s' % (host.datacenter, host.address, host.rack)

cluster.shutdown()

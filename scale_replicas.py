import json
import subprocess


def get_node_count(cluster):
    cmd = f"kubectl get nodes --context={cluster} --no-headers | wc -l"
    return int(subprocess.check_output(cmd, shell=True).decode('utf-8').strip())

def update_replicas(cluster, deployment, replicas):
    cmd = f"kubectl scale deployment {deployment} --replicas={replicas} --context={cluster}"
    subprocess.run(cmd, shell=True)

eks_cluster = ""
aks_cluster = ""

eks_nodes = get_node_count(eks_cluster)
aks_nodes = get_node_count(aks_cluster)
total_nodes = eks_nodes + aks_nodes

total_replicas = 10  # 총 replica 수
eks_replicas = int(total_replicas * (eks_nodes / total_nodes))
aks_replicas = total_replicas - eks_replicas

deployment = "nginx-deployment"
update_replicas(eks_cluster, deployment, eks_replicas)
update_replicas(aks_cluster, deployment, aks_replicas)

print(f"EKS replicas: {eks_replicas}")
print(f"AKS replicas: {aks_replicas}")

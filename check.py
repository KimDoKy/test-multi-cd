import json
import subprocess

def get_pod(cluster, component):
    cmd = f"kubectl get {component} --context={cluster} --no-headers -o wide"
    return subprocess.check_output(cmd, shell=True).decode('utf-8').strip()

eks_cluster = ""
aks_cluster = ""

component = ("po", "deployment")

eks_nodes = get_pod(eks_cluster, component[0])
aks_nodes = get_pod(aks_cluster, component[0])

print(f"=== eks ===\n{eks_nodes}")
print(f"=== aks ===\n{aks_nodes}")

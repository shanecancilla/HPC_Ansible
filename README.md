# HPC_Ansible

Agenda (7/13/2023 Meeting):
1. Make sure we didn't miss any steps in the management set up.

Agenda (7/12/2023 Meeting):
1. Run the mgmt.yml and make sure it works.
2. Create one vars file to use for mgmt.
3. Assign compute node tasks to everyone.

Agenda (07/11/2023 Meeting):
1. Run each step individually and confirm it works.
2. Make var file the same all around.
3. Finalize the mgmt ansible by creating one conglomerate yml file.

Run Ansible on Management Node with Minimal OS:  
1. Install epel-release, ansible, and git  
	dnf install -y epel-release  
	dnf install -y ansible git  
2. Clone the git repo  
	git clone https://github.com/shanecancilla/HPC_Ansible.git  
3. Set up Ansible host file /etc/ansible/hosts  
	[management]  
	oxygeni  
  
	[compute]  
	eoxygen[2:8]  
4. Congfigre /etc/hosts to allow Ansible to ping the nodes (refer to Network Details page on Confluence)  
5. Set up ssh keys (for management node, will eventually need to do compute nodes later(?))
        ssh-keygen -R oxygeni   
	ssh-copy-id oxygeni   
7. Go to management directory in HPC_Ansible  
	cd /root/HPC_Ansible/management  
8. Run Ansible playbook  
	ansible-playbook mgmt.yml  
  
If needed, disable and stop NetworkManager  
	systemctl disable --now NetworkManager  
	systemctl stop NetworkManager  
  
8. Boot up a compute node (ex: oxygen5)  
	pm --off oxygen5  
	pm --on oxygen5  
	conmon oxygen5  

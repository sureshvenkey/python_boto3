'''
Creates inventory file ec2 instances, volumes & security group in current working
directory. file name as follows ec2_instances_inv.csv, ec2_volumes_inv.csv
Created on 02-Oct-2019

@author: venkatraj
'''
import boto3
import csv
from pprint import pprint

session=boto3.session.Session(profile_name="default")
ec2_re=session.resource(service_name="ec2",region_name="ap-south-1")
ec2_cli=session.client(service_name="ec2",region_name="ap-south-1")
ec2_header_csv=['S_No','ami_launch_index', 'architecture', 'block_device_mappings', 'capacity_reservation_id', 'capacity_reservation_specification', 'classic_address', 'client_token', 'cpu_options', 'ebs_optimized', 'elastic_gpu_associations', 'elastic_inference_accelerator_associations', 'ena_support', 'hibernation_options', 'hypervisor', 'iam_instance_profile', 'id', 'image', 'image_id', 'instance_id', 'instance_lifecycle', 'instance_type', 'kernel_id', 'key_name', 'key_pair', 'launch_time', 'licenses', 'meta', 'monitoring', 'network_interfaces', 'network_interfaces_attribute', 'placement', 'placement_group', 'platform', 'private_dns_name', 'private_ip_address', 'product_codes', 'public_dns_name', 'public_ip_address', 'ramdisk_id', 'root_device_name', 'root_device_type', 'security_groups', 'source_dest_check', 'spot_instance_request_id', 'sriov_net_support', 'state', 'state_reason', 'state_transition_reason', 'subnet', 'subnet_id', 'tags', 'virtualization_type', 'volumes', 'vpc', 'vpc_addresses', 'vpc_id']
S_No=1
ec2invfile=open("ec2_instances_inv.csv","w", newline='')
csv_w=csv.writer(ec2invfile)
csv_w.writerow(ec2_header_csv)
for each_in in ec2_re.instances.all():
    csv_w.writerow([S_No,each_in.ami_launch_index, each_in.architecture, each_in.block_device_mappings, each_in.capacity_reservation_id, each_in.capacity_reservation_specification, each_in.classic_address, each_in.client_token, each_in.cpu_options, each_in.ebs_optimized, each_in.elastic_gpu_associations, each_in.elastic_inference_accelerator_associations, each_in.ena_support, each_in.hibernation_options, each_in.hypervisor, each_in.iam_instance_profile, each_in.id, each_in.image, each_in.image_id, each_in.instance_id, each_in.instance_lifecycle, each_in.instance_type, each_in.kernel_id, each_in.key_name, each_in.key_pair, each_in.launch_time, each_in.licenses, each_in.meta, each_in.monitoring, each_in.network_interfaces, each_in.network_interfaces_attribute, each_in.placement, each_in.placement_group, each_in.platform, each_in.private_dns_name, each_in.private_ip_address, each_in.product_codes, each_in.public_dns_name, each_in.public_ip_address, each_in.ramdisk_id, each_in.root_device_name, each_in.root_device_type, each_in.security_groups, each_in.source_dest_check, each_in.spot_instance_request_id, each_in.sriov_net_support, each_in.state, each_in.state_reason, each_in.state_transition_reason, each_in.subnet, each_in.subnet_id, each_in.tags, each_in.virtualization_type, each_in.volumes, each_in.vpc, each_in.vpc_addresses, each_in.vpc_id])
    S_No=S_No+1
print ("EC2 Inventory file created - ec2_instances_inv.csv")
ec2invfile.close()

vol_header_csv=['S_No', 'attachments', 'availability_zone', 'create_time', 'encrypted', 'id', 'iops', 'kms_key_id', 'meta', 'size', 'snapshot_id', 'snapshots', 'state', 'tags', 'volume_id', 'volume_type']
S_No=1
volinvfile=open("ec2_volumes_inv.csv","w", newline='')
csv_w=csv.writer(volinvfile)
csv_w.writerow(vol_header_csv)
for each_ec2_vol in ec2_re.volumes.all():
    csv_w.writerow([S_No, each_ec2_vol.attachments, each_ec2_vol.availability_zone, each_ec2_vol.create_time, each_ec2_vol.encrypted, each_ec2_vol.id, each_ec2_vol.iops, each_ec2_vol.kms_key_id, each_ec2_vol.meta, each_ec2_vol.size, each_ec2_vol.snapshot_id, each_ec2_vol.snapshots, each_ec2_vol.state, each_ec2_vol.tags, each_ec2_vol.volume_id, each_ec2_vol.volume_type])
    S_No=S_No+1
print ("Volume Inventory file created - ec2_volumes_inv.csv")
volinvfile.close()

sg_header_csv=['S_No', 'security_group_id', 'description', 'group_id', 'group_name', 'ip_permissions', 'ip_permissions_egress', 'owner_id', 'tags', 'vpc_id']
S_No=1
sginvfile=open("ec2_sg_inv.csv","w", newline='')
csv_w=csv.writer(sginvfile)
csv_w.writerow(sg_header_csv)
for each_ec2_sg in ec2_re.security_groups.all():
    csv_w.writerow([S_No, each_ec2_sg.id, each_ec2_sg.description, each_ec2_sg.group_id, each_ec2_sg.group_name, each_ec2_sg.ip_permissions, each_ec2_sg.ip_permissions_egress, each_ec2_sg.owner_id, each_ec2_sg.tags, each_ec2_sg.vpc_id])
    S_No=S_No+1
print ("Security Group Inventory file created - ec2_sg_inv.csv")
sginvfile.close()

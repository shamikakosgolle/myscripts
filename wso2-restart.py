import subprocess
 
# Run the kubectl command to get pod information
result = subprocess.run(["/usr/local/bin/kubectl", "get", "pods", "-n", "wso2"], capture_output=True, text=True)
 
# Split the output into lines
lines = result.stdout.split('\n')
k8_list2 = lines[:-1]
 
dict2 ={}
for i in k8_list2:
  j =i.split()
  pod_name = j[0]  # Get the pod name
  if "d" in j[-1] and "wso2apim-gateway" in j[0] and int(j[-1].split('d')[0]) > 1:
    dict2[pod_name] = j[-1].split('d')[0]  # Add the rest of the values to the dictionary
 
 
sorted_pod_info_dict = dict(sorted(dict2.items(), key=lambda item: int(item[1])))
print(sorted_pod_info_dict)
if sorted_pod_info_dict:
    last_key, last_value = sorted_pod_info_dict.popitem()
    # Print the last key and value
    with open("kubectl_output.txt", "w") as output_file:
        subprocess.run(["/usr/local/bin/kubectl", "delete", "pod", last_key, "-n", "wso2"], stdout=output_file, text=True)
else:
    print("Dictionary is empty")

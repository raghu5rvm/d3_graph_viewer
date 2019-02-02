import os
import sys
import json
import time
import random
if __name__=="__main__":
    
    file_path = sys.argv[1]
    dest_dir = sys.argv[2]
    content = [line.rstrip('\n') for line in open( file_path )]
    l = len(content)
    print ("num of lines:",l)
    start_line = 1#max(0,int(input("Enter start line o parse:")))
    end_line = 654#min(l-1,int(input("Enter end line o parse:")))
    delim = input("Enter delimiter:")
    nodes_list = []
    links_list = []
    visited_nodes = []
    data = {}
    node_id_count = 0
    node_id_list = {}
    for i in range(start_line,end_line+1):
        curr_line = content[i]
        clean_val = ''
        clean_key = ''
        if delim in curr_line:
            myKey,myVal = curr_line.split(delim)
            clean_key = myKey.replace('"','')
            clean_val = myVal.replace('"','')
            clean_key = clean_key.strip()
            clean_val = clean_val.strip()       
            if(clean_val != clean_key): 
                link_data = {"source":clean_key,"target":clean_val,"value":1}
                links_list.append(link_data)
                
        else:
            clean_key = curr_line.replace('"','')
            clean_key = clean_key.strip()
            clean_val = clean_key
        
        print ("key:",clean_key)
        if clean_key not in visited_nodes:
            visited_nodes.append(clean_key)
            node_data1 = {"name":clean_key,"group":random.randint(1,150)}
            nodes_list.append(node_data1)
            node_id_list[clean_key] = node_id_count
            node_id_count += 1
            
        if clean_val not in visited_nodes:
            visited_nodes.append(clean_val)
            node_data2 = {"name":clean_val,"group":random.randint(1,150)}
            nodes_list.append(node_data2)
            node_id_list[clean_val] = node_id_count
            node_id_count += 1
            
        if(clean_key not in data):
            data[clean_key] = [clean_val]
        elif(clean_val != "none"):
            data[clean_key].append(clean_val)
    
    dest_file = os.path.join(dest_dir,"valid_data.json")
    with open(dest_file,"w") as f:
        json.dump(data,f)
    
    final_links = []
    for l in links_list:
        src = l["source"]
        if src in visited_nodes and src in node_id_list:
            src_idx = node_id_list[src]
        target = l["target"]
        if target in visited_nodes and src in node_id_list:
            target_idx = node_id_list[target]
        curr_link_data = {"source":src_idx,"target":target_idx,"value":1}
        final_links.append(curr_link_data)
            
    
    
    
    dest_file_d3 = os.path.join(dest_dir,"valid_data_d3.json")
    d3_data = {"nodes":nodes_list,"links":final_links}
    with open(dest_file_d3,"w") as f2:
        json.dump(d3_data,f2)
        

#!/bin/python3
import numpy as np
import pandas as pd
import scapy.all as scapy
import sys

def sniffing():
    scapy.sniff(store=False, prn=process_packet)

def process_packet(packet):
    packet_value = f"{packet.show}\n"
    file_val = packet_value.split("\n")
    main_array = []
    for i in file_val:
        append_array = []
        append_array.append(i)
        main_array.append(append_array)
        
    for n in range(0, len(main_array)):
        p = main_array[n]
        array_main = []
        for i in p:
            val_str = str(i)
    #         print(val_str)

    new_array_vals = []        
    for i in range(0, len(main_array)):
        array_str = []
        for n in main_array[i]:
            val_str = str(n)
            array_str.append(val_str)
            new_array_vals.append(array_str)
            
            
    new_arr = []
    for i in new_array_vals:
        vals = i[0].split()
        new_arr.append(vals)
    # print(new_arr)

    value_array = []
    for i in new_arr:
        data_y = []
        for n in i:
            if n[:4] == "psrc" or i[:4] == "pdst":
                data_y.append(n)
                value_array.append(data_y)
            elif n[:3] == "dst" or n[:3] == "src":
                data_y.append(n)
                value_array.append(data_y)


    #data_frame_val = pd.DataFrame(value_array, columns=["mac destination", "mac source", 
                                                        #"ip source", "ip destination"])
    return value_array
    #return data_frame_val
    
sniffing()
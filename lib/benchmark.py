import imp
import os
import shutil

cmdbench_dir = os.path.dirname(os.path.abspath(__file__)) + '/cmdbench/bioinformatics'

fp, pathname, description = imp.find_module('multibench', [cmdbench_dir])
multibench = imp.load_module('multibench', fp, pathname, description)

def clean_if_exists(path):
    if os.path.exists(path):
        if(os.path.isfile(path)):
            os.remove(path)
        else:
            shutil.rmtree(path)
            os.mkdir(path)

def create_folder_if_doesnt_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)
            
def get_last_n_lines(string, n):
    return "\n".join(string.split("\n")[-n:])
    
def benchmark_list_to_results(benchmark_firsts_list):
    return {
        "memory": max(list(map(lambda result: result.memory.max, benchmark_firsts_list))),
        "disk_read": max(list(map(lambda result: result.disk.read_chars, benchmark_firsts_list))),
        "disk_write": max(list(map(lambda result: result.disk.write_chars, benchmark_firsts_list))),
        "runtime": sum(list(map(lambda result: result.process.execution_time, benchmark_firsts_list)))
    }

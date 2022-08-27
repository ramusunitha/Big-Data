def str_modification(input_str):
    cap=input_str.capitalize()
    upcase=input_str.upper()
    length=len(input_str)
    str_list=input_str.split()
    word_count=len(str_list)
    bool=input_str.endswith('s')
    replace_str=input_str.replace('e','a')
    final_result=(cap,upcase,length,word_count,bool,replace_str)
    return final_result

counter=36
counter+=1
print("\nScenario - {}".format(counter))
instr='inceptez technologies'
finres=str_modification(instr)
print("Input string is: {}".format(instr))
print("Final Result from the String Modification is: {}".format(finres))
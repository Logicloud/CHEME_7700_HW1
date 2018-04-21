import numpy as np

def find_data(File):                # Locate data, change 'Scientific Notation' and 'String' into float style, rewrite it into a list and count how many Entries are there
    Data_start = str('"Entry"')     # The sign where data is going to start
    Found_data = False          
    data_list = []                  
    with open(File,'r') as file:    # Open file
        for line in file:           # Read file line by line
            if Data_start in line:  # If the sign is in line, start recording data in next line
                Found_data = True
                continue            # Ensure data recording from next line
            if Found_data:          
                number = line.split()                             # Split a line into strings
                number = [w.replace('zero','0.').replace('one','1.').replace('two','2.').replace('three','3.')      # Replace 'String' with float style strings
                .replace('four','4.').replace('five','5.').replace('six','6.').replace('seven','7.')
                .replace('eight','8.').replace('nine','9.').replace('ten','10.').replace('eleven','11.')
                .replace('twelve','12.') for w in number]
                number = [w.replace('D','E') for w in number]     # Replace 'D' in 'Scientific Notation' with 'E'
                if not 'End' in number:                           # Filter out Notes in data 
                    if not 'WARNING!!!:' in number:
                        if not 'ERROR:' in number:
                            data_list.append(number)              # Write a data list 
                            count = int(number[0])                # Count how many Entries in this data file
    return data_list, count                                       # Return data list and the number of Entries

def AVG(data_line, count):                                        # Calculate the averages of 'Integer', 'Scientific Notation', and 'String'             
    int_sum = 0                                                   # The sum of each data type
    sci_sum = 0                                                   # 'int_sum' for 'Integer', 'sci_sum' for 'Scientific Notation', and 'str_sum' for 'String' 
    str_sum = 0
    for i in range (count-1):                                     # Add up data
        int_sum += float(data_line[i][1])
        sci_sum += float(data_line[i][2])
        str_sum += float(data_line[i][3])
    int_avg = int_sum / count                                     # Calculate average for each data type
    sci_avg = sci_sum / count
    str_avg = str_sum / count
    return int_avg, sci_avg, str_avg                              # Return averages

def STDEV(data_line, count, int_avg, sci_avg, str_avg):           # Calculate standard deviations of 'Integer', 'Scientific Notation', and 'String'
    int_diff = 0                                                  # Sum of the square of the differences between each data and the average
    sci_diff = 0
    str_diff = 0
    for i in range(count - 1):                                    # Add up square of differences
        int_diff += (float(data_line[i][1]) - int_avg)**2
        sci_diff += (float(data_line[i][2]) - sci_avg)**2
        str_diff += (float(data_line[i][3]) - str_avg)**2
    int_stdev = (int_diff / count)**0.5                           # Calculate standard deviations for each data type
    sci_stdev = (sci_diff / count)**0.5
    str_stdev = (str_diff / count)**0.5                           
    return int_stdev, sci_stdev, str_stdev                        # Return averages

input_file = 'DataFile1.txt'                                                                # Run for Data file 1 
data, count = find_data(input_file)                                                         # Write data list and count the number of entries
int_avg_1, sci_avg_1, str_avg_1 = AVG(data, count)                                          # Calculate averages
int_stdev_1, sci_stdev_1, str_stdev_1 = STDEV(data,count,int_avg_1, sci_avg_1, str_avg_1)   # Calculate standard deviation

input_file = 'DataFile2.txt'                                                                # Run for Data file 2
data, count = find_data(input_file)
int_avg_2, sci_avg_2, str_avg_2 = AVG(data, count) 
int_stdev_2, sci_stdev_2, str_stdev_2 = STDEV(data,count,int_avg_2, sci_avg_2, str_avg_2)

input_file = 'DataFile3.txt'                                                                # Run for Data file 3 
data, count = find_data(input_file)
int_avg_3, sci_avg_3, str_avg_3 = AVG(data, count) 
int_stdev_3, sci_stdev_3, str_stdev_3 = STDEV(data,count,int_avg_3, sci_avg_3, str_avg_3)
                                                                                            # Write title and lines for each data file
title = ('"FileName", "Integers AVG", "Integers STDEV", "Scientific Notation AVG", "Scientific Notation STDEV", "String AVG", "String STDEV"'+'\r\n')
Data1 = ('DataFile1.txt    ', str(int_avg_1)+'    ', str(int_stdev_1)+ '    ', str(sci_avg_1)+ '    ', str(sci_stdev_1)+ '    ', str(str_stdev_1)+ '    ', str(str_avg_1)+'\r\n')
Data2 = ('DataFile2.txt    ', str(int_avg_2)+'    ', str(int_stdev_2)+ '    ', str(sci_avg_2)+ '    ', str(sci_stdev_2)+ '    ', str(str_stdev_2)+ '    ', str(str_avg_2)+'\r\n')
Data3 = ('DataFile3.txt    ', str(int_avg_3)+'    ', str(int_stdev_3)+ '    ', str(sci_avg_3)+ '    ', str(sci_stdev_3)+ '    ', str(str_stdev_3)+ '    ', str(str_avg_3)+ '    ')

f = open("test.txt",'w')           # Start write .txt file
f.write(title)                     # Write title
f.writelines(Data1)                # Write Data 
f.writelines(Data2)
f.writelines(Data3)
f.close()                          # Close file
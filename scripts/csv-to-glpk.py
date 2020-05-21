import argparse
import pandas as pd

# Declare Constants

# Declare Functions

def get_args():
    '''
    Gets the arguments from the command line.
    '''
    parser = argparse.ArgumentParser("Run inference on an input video")
    # -- Create the descriptions for the commands    
    i_desc = "The location of the input file"
    o_desc = "The location of the output file"
    
    # -- Add required and optional groups
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')

    # -- Create the arguments
    required.add_argument("-i", help=i_desc, required=True)    
    optional.add_argument("-o", help=o_desc, default="./output.txt")
    args = parser.parse_args()

    return args

def compile_equations(args):

    #Convert custom arguments
    filename = str(args.i)

    try:
        df = pd.read_csv(filename)
        print("File", filename, "read succesfully.\n")
    except:
        print("Error: *.csv file not chosen or not in specified path.\n")
	
    # Creating a vector of text equations
    eq = []

    # Creating the file header made of variale initializations 
    hdr = []

    # Creating the first equation c1 for x1
    c1 = ""
    for i in range(len(df.x1)):
        c1 = c1 + str(df.x1[i]) + " * " + "lam"+str(i+1)
        if i != len(df.x1)-1:
            c1 = c1 + " + "     

    c1 = c1 + " <= " + str(df.x1[0]) + " * t;"
    eq.append(c1)

    # Creating the second equation c2 for y1
    c2 = ""
    for i in range(len(df.y1)):
        c2 = c2 + str(df.y1[i]) + " * " + "lam"+str(i+1)
        if i != len(df.y1)-1:
            c2 = c2 + " + "   

    c2 = c2 + " >= " + str(df.y1[0]) + ";"
    eq.append(c2)

    # Creating the second equation c3 for y2
    c3 = ""
    for i in range(len(df.y2)):
        c3 = c3 + str(df.y2[i]) + " * " + "lam"+str(i+1)
        if i != len(df.y2)-1:
            c3 = c3 + " + "   

    c3 = c3 + " >= " + str(df.y2[0]) + ";"
    eq.append(c3)

    # Creating the second equation c4 for y3
    c4 = ""
    for i in range(len(df.y3)):
        c4 = c4 + str(df.y3[i]) + " * " + "lam"+str(i+1)
        if i != len(df.y3)-1:
            c4 = c4 + " + "   

    c4 = c4 + " >= " + str(df.y3[0]) + ";"
    eq.append(c4)

    # Creating the second equation c5 for y4 or b1 (undesirable outputs)
    c5 = ""
    # Creating the last equation
    c6 = ""
    for i in range(len(df.y4)):
        hdr.append("var lam"+str(i+1)+" >= 0;")
        c5 = c5 + str(df.y4[i]) + " * " + "lam"+str(i+1)
        c6 = c6 + "lam"+str(i+1)
        if i != len(df.y4)-1:
            c5 = c5 + " + "   
            c6 = c6 + " + "  

    c5 = c5 + " = " + str(df.y4[0]) + ";"
    eq.append(c5)

    c6 = c6 + " = 1;"
    eq.append(c6)
    print("Equations compiled succesfully.\n")
    print(hdr)

    # Compile custom arguments	
    filepath = args.o
 
    with open(filepath, 'w') as file_handler:
        file_handler.write("var t >= 0;\n\n")   

        for item in hdr:
            file_handler.write("{}\n".format(item))
            
        file_handler.write("\n\nminimize obj: t;\n\n")    

        for count, item in enumerate (eq, start=1):
            file_handler.write("c" + str(count) + ": ")
            file_handler.write("{}\n".format(item))
            file_handler.write("\n")

        file_handler.write("solve;\n")
        file_handler.write("display t;\n")
        file_handler.write("end;\n")
        
        print("File saved to ",filepath,"\n")  


def main():
    args = get_args()
    compile_equations(args)
	    

if __name__ == "__main__":
    main()

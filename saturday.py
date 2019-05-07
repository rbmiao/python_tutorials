#import modules
import os

_CURRENT_DIR = '/home/vagrant/web/hackerrank'


def rec_tree_traverse(curr_dir, indent):
    "recurcive function to traverse the directory"
    #print "[traverse_tree]"

    try :
        print(os.listdir(curr_dir))
        dfList = [os.path.join(curr_dir, f_or_d) for f_or_d in os.listdir(curr_dir)]
        print(dfList)
    except:
        print("wrong path name/directory name")
        return
    #dfList="/home/vagrant/web/"
    for file_or_dir in dfList:

        if os.path.isdir(file_or_dir):
            #print "dir  : ",
            print(indent + file_or_dir + "\\")
            rec_tree_traverse(file_or_dir, indent*2)

        if os.path.isfile(file_or_dir):
            #print "file : ",
            print( indent + file_or_dir )

    #end if for loop
#end of traverse_tree()

#def main():
base_dir = _CURRENT_DIR
rec_tree_traverse(base_dir," "*4)

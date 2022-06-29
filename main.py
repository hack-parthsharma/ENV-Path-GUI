
#! /usr/bin/python3
#! @author: @ruhend
#? Date Created : #1

# establish imports here
from tkinter import *
from tkinter import ttk
from logic import logic
# import tktable

# global variables here
global __SNO__
__SNO__ = 1
global __PATHS__
__PATHS__ = logic.listPATHs()
global __SHELL__
__SHELL__ = logic.getSHELL()
# start class here
'''
###           ###
#   main Class  #
###           ###
'''
def addNewPath():
    _newPath = NewPathElement_ib.get()
    if _newPath in __PATHS__:
        print(' > Already Exsisting')
    else:
        PathElements_tb.insert(parent='',index='end',value=(len(__PATHS__)+1,_newPath))
        __PATHS__.append(_newPath)
        logic.addPATH(_newPath,__SHELL__)
        print(' > Added : '+str(_newPath))

def deleteExistingPath():
    if PathElements_tb.selection():
        selection = PathElements_tb.selection()
        for i in selection:
            print(' > Deleting '+str(i))
            path_extraction_dict = (PathElements_tb.item(i)).get("values")
            path_extraction_element = path_extraction_dict[1]
            path_extraction_element = "\:"+path_extraction_element.replace("/","\\/")
            logic.deletePATH(path_extraction_element)        
            # print(path_extraction_element+"\\/"+path_extraction_element)
            PathElements_tb.delete(i)
    else:
        print(' > Select a path to delete')    

root = Tk()
root.geometry('800x460')
root.title('env-path-editor')

NewPathElement_ib = Entry(root, width = 60,borderwidth=1)
NewPathElement_ib.grid(row=1,column=1,pady=50,padx=65,columnspan=2)

AddPathElement_bt = Button(root,text = 'Add',command=lambda: addNewPath()).grid(row=1,column=3)


PathElements_tb = ttk.Treeview(root)
# verscrlbar = ttk.Scrollbar(root,orient ="vertical", command = PathElements_tb.yview)
# verscrlbar.grid(rowspan=10)
# PathElements_tb.configure(xscrollcommand = verscrlbar.set)
PathElements_tb['columns'] = ('S.No.', 'Path directory')
PathElements_tb.column("#0",width=0)
PathElements_tb.column("S.No.",anchor=W, width=70)
PathElements_tb.column("Path directory", anchor=W, width=600)
PathElements_tb.heading("S.No.", text="S.No.",anchor=W)
PathElements_tb.heading("Path directory", text="Path Directory",anchor=W)
for i in range(len(__PATHS__)):
    PathElements_tb.insert(parent='',index='end',values=(i+1,__PATHS__[i]))
PathElements_tb.grid(row=2,column=1, columnspan=3,padx=65)

deleteExistingPath_bt = Button(root, text='Delete',command=lambda: deleteExistingPath())
deleteExistingPath_bt.grid(row=3,column=1,pady=50,padx=65,columnspan=4)
root.mainloop()

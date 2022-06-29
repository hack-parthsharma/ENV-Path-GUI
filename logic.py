
#! /usr/bin/python3
#! @author: @ruhend
#? Date Created : #1

# establish imports here


# global variables here
import os
import subprocess
# start class here
'''
###            ###
#   logic Class  #
###            ###
'''


class logic:
    def listPATHs():
        command = os.environ["PATH"]
        pathArray = []
        for i in command.split(':'):
            pathArray.append(i)
        return(pathArray)

    def getSHELL():
        shell_path = os.getenv("SHELL")
        return shell_path

    def addPATH(new_path__, shell_path):
        print(' > SHELL path : {}'.format(shell_path))
        try:
            if shell_path == '/bin/zsh':
                os.system('echo "export PATH=$PATH:{}" >> ~/.zshrc'.format(new_path__))
            elif shell_path == '/bin/bash':
                os.system('echo "export PATH=$PATH:{}" >> ~/.bashrc'.format(new_path__))
            elif shell_path == '/bin/fish':
                os.system('set -gx PATH {} $PATH'.format(new_path__))
            print(" > {} is now added to the $PATH".format(new_path__))
            # os.system('source ~/.zshrc')
        except Exception as e:
            print(e)
            
    def deletePATH(path):
        home_path = os.getenv("HOME")
        try:
            # os.system("sed -i 's/"+path+"/' "+home_path+"/.zshrc")
            os.system("sed -i 's/"+path+"//' "+home_path+"/.zshrc")

        except Exception as e:
            print(e)    



# define main function
    def main(self):
        print('hi')
        logic.listPATHs()



logicHandler = logic()

# main function
if __name__ == '__main__':
    logicHandler.main()

### END OF CLASS ###

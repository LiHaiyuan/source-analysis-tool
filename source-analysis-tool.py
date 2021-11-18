'''
Copyright 2021 Haiyuan Li All Rights Reserved
'''
g_app_version = 'pre-0.1'


class WorkSpace:

    def __init__(self):
        self.dirlist = []
    
    def add_dir(self, dirname):
        self.dirlist.append(dirname)


# Add an directory to the workspace

def main():
    print ('Source Analysis Tool')

if __name__ == '__main__':
    main()
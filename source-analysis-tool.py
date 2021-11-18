'''
Copyright 2021 Haiyuan Li All Rights Reserved
'''

class WorkSpace:

    def __init__(self):
        self.dirlist = []
    
    def add_dir(self, dirname):
        self.dirlist.append(dirname)


# Add an directory to the workspace
g_app_version = 'pre-0.1'
g_app_dispname = 'SourCE Analysis Tool'
g_banner = ' '.join([g_app_dispname, g_app_version]) 

def main():
    print (g_banner)

if __name__ == '__main__':
    main()
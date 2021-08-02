import subprocess
import sys

def install(name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])

def main():

    my_packages = ['oauth2client','google-api-python-client', 
    'progress',
    'progressbar2', 
    'httplib2shim',
    'google_auth_oauthlib',
    'google-auth-httplib2']

    installed_pr = []

    for package in my_packages:
        install(package)
        print('\n')
           
    print('Setup Completed')
if __name__ == '__main__':
    main()        
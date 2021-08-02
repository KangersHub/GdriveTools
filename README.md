# gdrive-tools

 A python based  all-in-one tool for Google Drive 
 
---

# Uses For Gdrive-Tools
  ✓ generate SA
  
  ✓ Add the SA and Add them to TD automatically
  
  ✓ Generate token for gdrive

---

# How To Setup?
 
## on your machine/pc run  <code>python setup.py</code> to install the required Python Requirements.....


---

## Getting Google OAuth API credential file..

```
- Visit the [Google Cloud Console](https://console.developers.google.com/apis/credentials)
- Go to the OAuth Consent tab, fill it, and save.
- Go to the Credentials tab and click Create Credentials -> OAuth Client ID
- Choose Desktop and Create.
- Use the download button to download your credentials.
- Move that file to the root of the the place where gdrive tools is located and rename it to <code>credentials.json</code>
- Visit [Google API page](https://console.developers.google.com/apis/library)
- Search for Drive and enable it if it is disabled
```

Finally, run the <code>python generate_drive_token.py</code> to generate **token.pickle** file for Google Drive ...

---

## For Using Service Accounts Stuff follow this below:--

```
python3 gen_sa_accounts.py --quick-setup 1 --new-only
```
A folder named accounts will be created which will contain keys for the Service Accounts.

Or you can create Service Accounts to current project, no need to create new one

- List your projects ids
```
python3 gen_sa_accounts.py --list-projects
```
- Enable services automatically by this command
```
python3 gen_sa_accounts.py --enable-services $PROJECTID
```
- Create Sevice Accounts to current project
```
python3 gen_sa_accounts.py --create-sas $PROJECTID
```
- Download Sevice Accounts as accounts folder
```
python3 gen_sa_accounts.py --download-keys $PROJECTID
```
If you want to add Service Accounts to Google Group, follow these steps

- Mount accounts folder
```
cd accounts
```
- Grab emails form all accounts to emails.txt file that would be created in accounts folder
```
grep -oPh '"client_email": "\K[^"]+' *.json > emails.txt
```
- Unmount acounts folder
```
cd -
```
Then add emails from emails.txt to Google Group, after that add Google Group to your Shared Drive and promote it to manager.

**NOTE**: If you have created SAs in past from this script, you can also just re download the keys by running:
```
python3 gen_sa_accounts.py --download-keys project_id
```

</details>

## Add all the Service Accounts to the Team Drive
- Run:
```
python3 add_to_team_drive.py -d SharedTeamDriveID.here
```

---
### note:-- [if you dont want to use service accounts dont follow the instructions above](#getting-google-oauth-api-credential-file)

---
## Where to RUN this tool??

### You can run on REPL.IT -- [<img height=30 src="https://repl.it/badge/github/XcodersHub/GdriveTools">](https://repl.it/github/XcodersHub/GdriveTools)

### Or you can Run it on your Local Pc -- (must have python installed)

---


## thats All For Help.... Join--  https://t.me/XcodersHub for more

---
import requests, re, csv

def read_emails_from_csv(csv_filename):
	#assuming a csv file where email is the fourth category..

	with open(csv_filename, 'rU') as csvfile:
		emailreader = csv.reader(csvfile, delimiter=',' , dialect=csv.excel_tab)
		
		emails = []
		for row in emailreader:
			emails.append(row[0])
		return emails 
	

def get_githubs():
# boiler plate to pull in json from kimono of github emails
# these get returned as links + kimurls, so neeed a function to parse back
	#githubs is a list, where each item is a list of url + property1 which includes text and href
	return requests.get("https://www.kimonolabs.com/api/a65ge0py?apikey=sHlv8VajTMCK5ePLUPL1Yg2nbf9iOs9H&kimwithurl=1", headers={"authorization" : "Bearer GVQYtv386iCgG06OVfNoJpJRL81uHFuo"}).json()['results']['collection1']

def get_email_from_url(url):
#take a url and transform back into email
#returns emai
	result = re.search('q=(.*)&type', url)
	return result.group(1).replace("%40", "@")

def create_githubs_email_list(git_list):
#take a list of githubs a
	github_emails = {}
	for git in git_list:
		github_emails[get_email_from_url(git['url'])] = git['property1']['href']
	return github_emails

def merge_emails(email_list, git_email_list):
	merged_list = []

	for email in email_list:

		try:
			git_email_list[email]
			merged_list.append( (email, git_email_list[email]) )
			print email ,"," , git_email_list[email]
			#print email, git_emai
		except:
			merged_list.append( (email, "no github found") )
			print email, "," ,"No Github found"

	return merged_list

def main():
	
	emails = read_emails_from_csv('email_test.csv')
	githubs = get_githubs()
	github_email_list = create_githubs_email_list(githubs)
	return merge_emails(email_list = emails, git_email_list = github_email_list)


merged_list = main()




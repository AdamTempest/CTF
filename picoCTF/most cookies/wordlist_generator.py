
# core function
def generate_wordlist(cookie_names):
	with open('wordlist.txt','w') as f:

	        for i in cookie_names:
	                f.write(i+"\n")


# validates input
def check_input(user_data):
	if '[' not in user_data:
		user_data = user_data.replace("\"",'') if '\"' in user_data else user_data.replace('\'','')
		return user_data.split(', ') if ', ' in user_data else user_data.split(',')
	else:
		print("[!] Error: Please Enter a list in the following format. \nExample- \"Enter: cookie_a, cookie b, cookie c\"")
		main()


# puts everyting together
def main():
	cookie_names = input("\nEnter the list of cookie names without any brackets. \nEnter: ")
	#print("\n[*] Checking the validity of your input ... \n")
	cookie_list = check_input(cookie_names)
	print("\n[*] Generating the wordlist ... \n")
	generate_wordlist(cookie_list)
	print("\n[+] Created the wordlist.py \n")



if __name__ == "__main__":
	main()

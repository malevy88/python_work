name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

print("Python")
print("\tPython")

print("Languages:\nPython\nC\nJavascript")

print("Languages: \n\tPython\n\tC\n\tJavascript")

favorite_language = 'python '
new_favorite_language = favorite_language.rstrip()
print(new_favorite_language)

nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://') # removes the HTTPS from the nostarch_url

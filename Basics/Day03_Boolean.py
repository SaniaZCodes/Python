logged_in_input=input("Is the user logged in? (True/False): ")

premium_input=input("Does the user have Premium? (True/False): ")

is_logged_in=logged_in_input.lower()=="true"
is_premium=premium_input.lower()=="true"

can_access_content=is_logged_in
can_download_video=is_logged_in and is_premium
show_ads=not is_premium

print("App Permission System Log")
print(f"Can Access Content: {can_access_content}")
print(f"Can Download Video: {can_download_video}")
print(f"Does Add Show: {show_ads}")

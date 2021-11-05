# Identify the spam comments from the given list below and write a code to show the user whether the comment is a spam comment or not?
options_text = ["hello","make a lot of money","buy now","how are you","subscribe this", "click this","Have a nice day"]

print(options_text)
text = input("\nplease select any 1 comment from the above options\n").lower()
if "make a lot of money" in text:
    spam = True
elif "buy now" in text:
    spam = True
elif "subscribe this" in text:
    spam = True
elif "click this" in text:
    spam = True
elif "hello" in text:
    spam = False
elif "how are you" in text:
    spam = False
elif "have a nice day" in text:
    spam = False
    
if spam:
  #Above line means if spam = True
    print("This is Spam")
else:    
    print("Not a Spam")




import yagmail
import time

if __name__ == "__main__":
    main = yagmail.SMTP("Your mail send", "Your Password App")
    root = "mail you send"
    subj = "Text"
    body = "Text - content"
    path = "path to photo" #send photo or attachments
    for _ in range(20): # send 
        main.send(to=root, subject=subj, contents=body,  attachments= None)
        time.sleep(1) 
    print("Completed") # finish

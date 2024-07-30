import yagmail
import time

if __name__ == "__main__":
    main = yagmail.SMTP("studyvuhoc@gmail.com", "dmojluovaehglwij")
    root = "2vhoc7@gmail.com"
    subj = "Chào mày, tao là học"
    body = "Tôi là học, được gửi bằng code python"
    path = 0
    for _ in range(20):
        main.send(to=root, subject=subj, contents=body,  attachments= None)
        time.sleep(1)
    print("Completed")
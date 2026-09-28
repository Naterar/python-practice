def show_account(account_name):
    print(account_name)


show_account("Son Yu")
show_account("Alex Smith")

log_line = "2026-09-28T14:22:01Z,WS-04,syu,10.0.4.17,FAILURE"

log_line_list = log_line.split(",")

print(log_line_list)
print(log_line_list[2])

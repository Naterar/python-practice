def parse_logon_line(raw_line):
    fields = raw_line.split(",")
    timestamp = fields[0]
    workspace_id = fields[1]
    user_id = fields[2]
    ip_address = fields[3]
    status = fields[4]
    print(f"Timestamp: {timestamp}")
    print(f"Workspace ID: {workspace_id}")
    print(f"User ID: {user_id}")
    print(f"IP Address: {ip_address}")
    print(f"Status: {status}")


parse_logon_line("2026-09-28T14:22:01Z,WS-04,José,10.0.4.17,FAILURE")

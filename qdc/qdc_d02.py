def parse_logon_line(raw_line):
    fields = raw_line.split(",")
    event = {
        "timestamp": fields[0],
        "workspace_id": fields[1],
        "user_id": fields[2],
        "ip_address": fields[3],
        "status": fields[4]
    }
    return event


parsed = parse_logon_line("2026-09-28T14:22:01Z,WS-04,syu,10.0.4.17,FAILURE")
ryu_failed_event = parse_logon_line(
    "2026-10-28T17:42:11Z,WS-88,ryu,10.0.4.18,FAILURE")
print(parsed)
print(ryu_failed_event)

print(parsed["user_id"])
print(ryu_failed_event["status"])


# print(parse_logon_line(""))
print(parse_logon_line("a,b,c"))

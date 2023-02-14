import subprocess


def start_client(name):
    logfile = open(f'{name}_log.txt', 'w+')

    process = subprocess.Popen(["xcodebuild", "-project", "./WebDriverAgent/WebDriverAgent.xcodeproj", "-scheme",
                                "WebDriverAgentRunner", "-destination", "platform=iOS,name=iPhone1", "test"],
                               stdout=logfile)
    return process


def read_ip_from_log(name):
    logfile = open(f'{name}_log.txt', 'r')
    for l in logfile.readlines():
        if "ServerURLHere" in l:
            ip_line = l
            logfile.close()
            without_prefix = ip_line.split(" ")[3].removeprefix("ServerURLHere->")
            return without_prefix[:-16]

    raise Exception()

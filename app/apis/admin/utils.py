import subprocess

def get_disk_usage(parameters: str):
    allowed_parameters = ["-a"]
    input_parameters = parameters.split()
    for parameter in input_parameters:
        if parameter not in allowed_parameters:
            return "Invalid parameter, malicious input detected!"
    command = ["df", "-h"]
    command.extend(input_parameters)

    try:
        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        usage = result.stdout.strip().decode()
    except:
        raise Exception("An unexpected error was observed")

    return usage
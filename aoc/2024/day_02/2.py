reports = []
with open("reports.txt") as file:
    reports = [list(map(int, line.split())) for line in file]

def safe_with_removal(report):
    for removed_ele in range(len(report)):
        if (check_if_valid(report[:removed_ele] + report[removed_ele + 1:])):
            return True
    return False

def check_if_valid(report):
    increasing = report[0] < report[1]

    for idx in range(0, len(report) - 1):
        difference = report[idx + 1] - report[idx]
        if increasing and not 1 <= difference <= 3:
            return False
        elif not increasing and not -3 <= difference <= -1:
            return False
        
    return True
            
def get_valid_report_count(reports):
    valid_count = 0
    for report in reports:
        valid = check_if_valid(report)
        if not valid:
            valid = safe_with_removal(report)

        valid_count += int(valid)

    return valid_count

print(get_valid_report_count(reports))
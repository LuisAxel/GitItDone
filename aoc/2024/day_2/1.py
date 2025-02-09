reports = []
with open("reports.txt") as file:
    reports = [list(map(int, line.split())) for line in file]

def get_valid_report_count(reports):
    valid_count = 0
    for report in reports:
        increasing = report[0] < report[1]
        is_valid = True

        for idx in range(0, len(report) - 1):
            difference = report[idx + 1] - report[idx]
            if increasing and not (1 <= difference <= 3):
                is_valid = False
                break
            elif not increasing and not (-3 <= difference <= -1):
                is_valid = False
                break
        valid_count += int(is_valid)

    return valid_count

print(get_valid_report_count(reports))
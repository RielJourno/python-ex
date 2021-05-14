import requests


def main():
    # Enter in FileToCheck your full file name
    fileToChack = '84c82835a5d21bbcf75a61706d8ab549'
    makeMarkdownTable(fileToChack)

# The function that the home assignment ask
def makeMarkdownTable(fileToCheck):
    myApiKey = 'f5576d979d3e63956894546ffb3e6ff74c3e6e0f65859e7905ac8197f9d2ae57'
    jsonReport, scansData = getReport(myApiKey, fileToCheck)
    makeFileToDillinger(jsonReport, scansData)
    return tableDesign(jsonReport, scansData)

# Get the report from Virus Total API and analysis the data
def getReport(ApiKey, fileToCheck):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': ApiKey, 'resource': fileToCheck}
    response = requests.get(url, params=params)

    # checking status code error
    if response.status_code == 203:
        print(f"Request rate limit exceeded. status code error: {response.status_code}")
        exit()
    elif response.status_code == 400:
        print(f"Bad request. Your request was somehow incorrect. status code error: {response.status_code}")
        exit()
    elif response.status_code == 403:
        print(f"Forbidden. You don't have enough privileges to make the request. status code error: {response.status_code}")
        exit()

    # analysis the data
    elif response.status_code == 200:
        data = {"MD5" : f"{response.json()['md5']}",
                "SHA-1" : f"{response.json()['sha1']}",
                "SHA-256" : f"{response.json()['sha256']}",
                "Total Scans" : f"{response.json()['total']}",
                "Positive Scans" : f"{response.json()['positives']}"
                }

        scans = []
        result =[]
        for scan in response.json()['scans']:
            scans.append(scan)
            result.append(response.json()['scans'][f'{scan}']['result'])

        originAndResult = [scans, result]
        return data, originAndResult
    else:
        print(f"you have a response status code error: {response.status_code}")
        exit()


# Design the tables in Dillinger.io format (print the data to the screen)
def tableDesign(jsonReport, scans):
    print()
    ScannedFileTable = f"""## Scanned File
| MD5 | SHA-1 | SHA-256 |
| ------ | ------ | ------ |
| {jsonReport['MD5']} | {jsonReport['SHA-1']} | {jsonReport['SHA-256']} |"""

    resultTable = f"""## Results
| Total Scans | Positive Scans |
| ------ | ------ |
| {jsonReport['Total Scans']} | {jsonReport['Positive Scans']} |"""

    scansTable = """## Scans
| Scan Origin | Scan Result |
| ------ | ------ |"""

    print(ScannedFileTable)
    print(resultTable)
    print(scansTable)
    for i in range(len(scans[0])):
        print(f"| {scans[0][i]} | {scans[1][i]} |")


# Design the tables in Dillinger.io format (make a txt file)
def makeFileToDillinger(jsonReport, scans):
    with open("DillingerFile.txt", "w") as file:
        file.write("## Scanned File \n"
                   "| MD5 | SHA-1 | SHA-256 | \n"
                   "| ------ | ------ | ------ |\n"
                   f"| {jsonReport['MD5']} | {jsonReport['SHA-1']} | {jsonReport['SHA-256']} |\n")

        file.write("## Results \n"
                   "| Total Scans | Positive Scans |\n"
                   "| ------ | ------ | \n"
                   f"| {jsonReport['Total Scans']} | {jsonReport['Positive Scans']} | \n")

        file.write("## Scans \n"
                   "| Scan Origin | Scan Result | \n"
                   "| ------ | ------ | \n")
        for i in range(len(scans[0])):
            file.write(f"| {scans[0][i]} | {scans[1][i]} | \n")

main()

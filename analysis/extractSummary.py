import json
import sys

filename=sys.argv[1]

print("Showing summary for file file {} ...".format(filename))


pr_count=0
bug_count=0

with open(filename) as f:
    data = json.load(f)

    for ob in data:
        labelsMapped=list(map(lambda o: o["name"],ob["data"]["labels"]))

        if "bug" not in labelsMapped:
            continue

        bug_count=bug_count+1
        print("=====")
        print("BUG TITLE: '{}', LABELS: {}".format(ob["data"]["title"],labelsMapped))
        if "pull_request" in ob["data"]:
            pr_count=pr_count+1
            print(ob["data"]["pull_request"]) 
        else:
            print("<No PR>")
        print("=====")

print("{} Bugs.".format(pr_count))
print("{} Bugs with PRs.".format(pr_count))

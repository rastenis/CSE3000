import json
import sys

filename=sys.argv[1]

print("Showing summary for file file {} ...".format(filename))

total_count=0
pr_count=0
bug_count=0
pr_label_count=0
verified_count=0

with open(filename) as f:
    data = json.load(f)

    for ob in data:
        labelsMapped=list(map(lambda o: o["name"],ob["data"]["labels"]))

        total_count=total_count+1

        if "bug" not in labelsMapped:
            continue

        if "has_pr" in labelsMapped:
            pr_label_count=pr_label_count+1

        if "verified" in labelsMapped:
            verified_count=verified_count+1

        bug_count=bug_count+1
        print("=====")
        print("BUG TITLE: '{}', LABELS: {}".format(ob["data"]["title"],labelsMapped))
        if "pull_request" in ob["data"]:
            pr_count=pr_count+1
            print(ob["data"]["pull_request"]) 
        else:
            print("<No PR>")
        print("=====")

print("{} total issues.".format(total_count))
print("{} Bugs.".format(pr_count))
print("{} Bugs with PRs.".format(pr_count))
print("{} Verified bugs.".format(verified_count))
print("{} Bugs with the 'has_pr' label.".format(pr_label_count))


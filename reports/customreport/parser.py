import json
from jinja2 import Environment, FileSystemLoader
import os

base_dir = os.path.dirname(__file__)

output_json = os.path.join(
    base_dir,
    "..",
    "output.json"
)

with open(output_json, "r") as file:
    results = json.load(file)

total = len(results)

passed = len(
    [x for x in results if x["status"] == "PASS"]
)

failed = len(
    [x for x in results if x["status"] == "FAIL"]
)

pass_percentage = round(
    (passed / total) * 100,
    2
) if total > 0 else 0

env = Environment(
    loader=FileSystemLoader(base_dir)
)

template = env.get_template("template.html")

html = template.render(
    results=results,
    total=total,
    passed=passed,
    failed=failed,
    pass_percentage=pass_percentage,
    environment="QA",
    browser="Chrome"
)

report_file = os.path.join(
    base_dir,
    "report.html"
)

with open(report_file, "w", encoding="utf-8") as file:
    file.write(html)

print("Report Generated Successfully")
"""Self-check for resume.py: python tools/test_resume.py (temp workspace, never yours)."""
import json, os, subprocess, sys, tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))
WS = tempfile.mkdtemp()
ENV = dict(os.environ, CAMPAIGN_WORKSPACE=WS)
os.makedirs(os.path.join(WS, "resume"))
json.dump({"name": "Asha Rao", "contact": ["Pune", "asha@example.com"],
           "experience": [{"id": "e1", "title": "Actuarial Analyst", "org": "Acme Re", "dates": "2022 - 2026",
                           "bullets": [{"id": "e1.1", "text": "Built a reserving model used for 40 portfolios."},
                                       {"id": "e1.2", "text": "Cut quarterly close from 10 days to 6."}]}],
           "skills": [{"group": "Tools", "items": "R, Python, Prophet"}]},
          open(os.path.join(WS, "resume", "master.json"), "w"))


def check(variant, ok=True):
    path = os.path.join(WS, "v.json")
    json.dump(variant, open(path, "w"))
    p = subprocess.run([sys.executable, os.path.join(TOOLS, "resume.py"), "check", path], env=ENV, capture_output=True, text=True)
    assert (p.returncode == 0) == ok, (variant, p.stdout, p.stderr)
    return p.stdout + p.stderr


good = {"label": "pricing", "summary": "Actuary who builds models teams keep using, across 40 portfolios.",
        "experience": [{"id": "e1", "bullets": [{"id": "e1.2", "text": "Shortened the quarterly close from 10 days to 6."}, "e1.1"]}],
        "skills": ["Tools"]}
assert "ok" in check(good)
assert "adds numbers ['8']" in check({**good, "experience": [{"id": "e1", "bullets": [{"id": "e1.2", "text": "Cut close to 8 days."}]}]}, ok=False)
assert "summary uses numbers" in check({**good, "summary": "Saved 2 million."}, ok=False)
assert "e9 is not in master" in check({**good, "experience": [{"id": "e9", "bullets": []}]}, ok=False)

subprocess.run([sys.executable, os.path.join(TOOLS, "workbook.py"), "init", "resume"], env=ENV, check=True, capture_output=True)
spec = os.path.join(WS, "s.json")
json.dump({"add": {"Context": [{"Category": "Off limits", "Fact": "Employer clients", "Value": "Prophet; Zeta Insurance"}]}}, open(spec, "w"))
subprocess.run([sys.executable, os.path.join(TOOLS, "workbook.py"), "write", spec], env=ENV, check=True, capture_output=True)
assert "off-limits text appears: 'Prophet'" in check(good, ok=False)

sys.path.insert(0, TOOLS)
os.environ["CAMPAIGN_WORKSPACE"] = WS
import resume
page = resume.to_html(resume.build(os.path.join(WS, "v.json"))[0])
assert "<li>Shortened the quarterly close" in page and "Acme Re" in page
print("all resume checks passed")

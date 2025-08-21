post = "https://ceronman.com/2005/01/29/dos-semanas-con-ubuntu/"
slug = None

import subprocess
import re
def cmd(command):
    subprocess.check_output(command, shell=True)

cmd(f"curl https://r.jina.ai/{post} -o newpost.md")

ported = [
    "+++\n"
]

content = False
for line in open("newpost.md"):
    if m := re.match(r'Title: (.*)', line):
        ported.append(f'title = "{m.group(1)}"\n')

    if m := re.match(r'Published Time: (.*)', line):
        ported.append(f'date = {m.group(1)[:10]}\n')
        ported.append('+++\n')

    if "Markdown Content:" in line:
        content = True
        continue

    if '[Skip to content]' in line:
        continue

    if '*   Tagged' in line:
        content = False
        continue

    if content:
        ported.append(line)

ported = "".join(ported)
name = slug if slug else post.strip("/").split("/")[-1]

open(f"content/blog/{name}.md", "w").write(ported)

cmd("rm newpost.md")

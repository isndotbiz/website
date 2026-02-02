# Builder script - creates generate_v3_assets.py
import os
output = os.path.join(os.path.dirname(__file__), "generate_v3_assets.py")
lines = []
lines.append("#!/usr/bin/env python3")
lines.append("import requests, os, io, time, json")
lines.append("from PIL import Image")
lines.append("")
with open(output, "w") as out:
    out.write(chr(10).join(lines))
print("created")

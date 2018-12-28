#!/usr/bin/env python

from __future__ import print_function

import glob
import os.path as osp


def tabulate(rows):
    html = '<table>'
    for row in rows:
        html += '\n\t<tr>'
        for col in row:
            html += '\n\t\t<td align="center">{}</td>'.format(col)
        html += '\n\t</tr>'
    html += '\n</table>'
    return html


def main():
    examples = []
    for py_file in sorted(glob.glob('examples/*.py')):
        img_file = osp.splitext(osp.basename(py_file))[0] + '.jpg'
        img_file = osp.join('examples/.readme', img_file)
        if not osp.exists(img_file):
            continue
        examples.append((
            '<pre><a href="{}">{}</a></pre>'.format(py_file, py_file),
            '<img src="{}" width="70%" />'.format(img_file),
        ))
    examples = tabulate(examples)

    dependencies = []
    with open('requirements.txt') as f:
        for req in f:
            req = req.strip()
            dependencies.append(
                '- [{0}](https://pypi.org/project/{0})'.format(req)
            )
    dependencies = '\n'.join(dependencies)

    py_file = 'getting_started.py'
    with open(py_file) as f:
        active = False
        lines = []
        for line in f:
            if line == '# GETTING_STARTED {{\n':
                active = True
                continue
            elif line == '# }} GETTING_STARTED\n':
                active = False
                continue
            if active:
                lines.append(line)
    getting_started = ''.join(lines)

    README = '''\
<!-- DO NOT EDIT THIS FILE MANUALLY. This file is generated by generate_readme.py. -->

# imgviz: Image Visualization Tools

[![PyPI Version](https://img.shields.io/pypi/v/imgviz.svg)](https://pypi.python.org/pypi/imgviz)
[![Python Versions](https://img.shields.io/pypi/pyversions/imgviz.svg)](https://pypi.org/project/imgviz)
[![Build Status](https://travis-ci.com/wkentaro/imgviz.svg?token=zM5rExyvuRoJThsnqHAF&branch=master)](https://travis-ci.com/wkentaro/imgviz)

## Installation

```bash
pip install imgviz
```


## Dependencies

{dependencies}

## Getting Started

```python
# getting_started.py

{getting_started}```

<img src=".readme/getting_started.jpg" width="80%" />

## [Examples](examples)

{examples}
'''  # NOQA

    README = README.format(
        getting_started=getting_started,
        dependencies=dependencies,
        examples=examples,
    )

    print(README, end='')


if __name__ == '__main__':
    main()

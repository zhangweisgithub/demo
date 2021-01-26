# !/usr/bin/env python
# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader


def generate_html(body, starttime, stoptime):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('./template.html')
    with open("result.html", 'w+', encoding="utf-8") as fout:
        html_content = template.render(start_time=starttime,
                                       stop_time=stoptime,
                                       body=body)
        fout.write(html_content)


if __name__ == "__main__":
    body = []
    result = {'cabID': 1, 'shijian': 2019, 'final_result': "正常", 'info': "无",
              'image_path': "test.jpg"}
    body.append(result)
    generate_html(body, 2019, 2021)

"""
title: wpscan tools
description: A simple wrapper for running wpscan.
author: r3m1ck
author_url: https://github.com/rosdyana/
version: 0.0.1
license: MIT
"""

import subprocess


class Tools:
    def __init__(self):
        self.citation = True
        pass


async def perform_wpscan(self, url: str, options: str = None) -> str:
    """
    Perform a scan using wpscan.
    :param url: The URL of the WordPress site to scan.
    :param options: Additional options to pass to wpscan.
    """
    command = f"wpscan --url {url}"
    if options:
        command += f" {options}"
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return f"""
    Here are the results of the scan:
    {output.decode()}.
        """
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output.decode()}")

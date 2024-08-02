"""
title: nmap tools
description: A simple wrapper for nmap to scan for hosts on a network.
author: r3m1ck
author_url: https://github.com/rosdyana/
version: 0.0.1
license: MIT
"""

import subprocess
import re


class NmapWrapper:
    def __init__(self, options="-sP"):
        self.options = options

    def run(self, target):
        command = f"nmap {self.options} {target}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Error running nmap: {result.stderr}")
        return self.parse(result.stdout)

    def parse(self, output):
        hosts = []
        for line in output.split("\n"):
            if "Nmap scan report for" in line:
                match = re.search(r"Nmap scan report for (.+)", line)
                if match:
                    hosts.append(match.group(1))
        return hosts


class Tools:
    def __init__(self):
        self.citation = True
        pass

    async def scan_host_using_nmap(self, target: str) -> str:
        """
        Perform a network scan using nmap.
        :param target: The target IP address or range to scan.
        :return: A string containing the hosts found.
        """
        nmap = NmapWrapper()
        try:
            hosts = nmap.run(target)
            return "Hosts found: " + str(hosts)
        except Exception as e:
            return str(e)

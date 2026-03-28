import subprocess
import os
import shutil
import glob
import sys 
import ipaddress
import re
import time
import json
import argparse
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class HydraAutomator:
    
   # Checking the validty of IP
    def checkip(self, ip):
        try:


        except ValueError:

    # Checking the existence of tools
    def toolchecker(self,gobuster,nmap):        

    
    
    # Function that runs hydra with the given parameters
    def hydra(ip,port,usarname,password):


if __name__== "__main__":
    ip = input("Enter the target IP address: ")
    port =input("Enter the target port: ")
    username = input("Enter the username to test: ")
    password = input("Enter the password to test: ")


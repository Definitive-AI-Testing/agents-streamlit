import socketio
import asyncio
import os
import git
import streamlit as st
from client import *

from dotenv import load_dotenv
load_dotenv()

#asyncio.run(start_server())

if __name__ == '__main__':
    from streamlit.web.bootstrap import run
    #asyncio.run(start_server())    

    real_script = 'aider_gui.py'
    real_script = 'main.py'
    run(real_script, False, [], {})    

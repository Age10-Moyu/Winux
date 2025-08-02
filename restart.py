import shared
from shared import dynamic_in as dynamic
from shared import dm_in as dm
from shared import notepad_in as notepad
from .method import get
dynamic=get(shared.dynamic_in)
dm=get(shared.dm_in)
notepad=get(shared.notepad_in)
import __init__
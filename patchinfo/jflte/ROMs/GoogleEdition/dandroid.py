from multiboot.fileinfo import FileInfo
import multiboot.autopatcher as autopatcher
from multiboot.autopatchers.jflte import GoogleEditionPatcher
import re

file_info = FileInfo()

filename_regex           = r"^(danvdh-GE|Dandroid).*\.zip$"
file_info.name           = 'Dandroid'
file_info.ramdisk        = 'jflte/GoogleEdition/GoogleEdition.def'
file_info.patch          = [ autopatcher.auto_patch, GoogleEditionPatcher.qcom_audio_fix ]
file_info.extract        = [ autopatcher.files_to_auto_patch, GoogleEditionPatcher.files_for_qcom_audio_fix ]

def matches(filename):
  if re.search(filename_regex, filename):
    return True
  else:
    return False

def get_file_info():
  return file_info

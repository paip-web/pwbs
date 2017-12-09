__title__ = 'pwbs'
__version__ = '0.0.1-dev1'
__author__ = 'Patryk Adamczyk'
__license__ = 'MIT'
__docformat__ = 'restructuredtext en'

__all__ = ()

import sys
from os import path, getcwd

def main(args=sys.argv):
    """Główna Funkcja Programu"""
    cwd = getcwd()
    script_cwd = path.abspath(path.dirname(__file__))
    print("PAiP Web Build System v" + __version__)
    sys.exit()

if __name__ == '__main__': # pragma: no cover
    sys.exit(main(sys.argv))

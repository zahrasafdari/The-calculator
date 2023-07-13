import sys
from pathlib import Path
file = Path(__file__). resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))


if __name__ == '__main__':
    from calculator.gui import run_gui
    run_gui()
    

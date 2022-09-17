"""
Plots dust covers in scribus. Provides interface to allow custom dust covers
"""

import csv
import sys

import dust_jacket
import dust_jacket_plotter

try:
    import scribus
except ImportError:
    print ("This script only runs from within Scribus.")
    sys.exit(1)

def main():
    """
    Present csv dialog, open and read, then use plotter class to plot
    """
    params_csv_file = scribus.fileDialog("Select the BookBuddy csv export",
            "CSV files (*.csv)")
    with open(params_csv_file, "r") as params_csv:
        params = csv.reader(params_csv)
        for param in params
            dj = DustJacket(**param)
            with SimpleDustJacketPlotter(dj) as plotter:
                plotter.plot_left_fold()
                plotter.plot_left_trim()
                plotter.plot_spine()
                plotter.plot_right_trim()
                plotter.plot_right_fold()
                plotter.plot_outer()

if __name__ == '__main__':
    if scribus.scribus_version_info[:3] < (1,5,8):
        scribus.messageBox("Scribus - Python3 script",
            "This script requires Scribus 1.5.8 or newer. " \
                    f"You're running {scribus.scribus_version}.",
                    scribus.ICON_CRITICAL)
        sys.exit() 
    try:
        scribus.setRedraw(False)
        main()
    finally:
        scribus.setRedraw(True)
        scribus.redrawAll()

#Un utilitaire graphique pour voir les dépendances pip installées sur le systeme
import math
import pkg_resources
import curses

def main(stdscr):
    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.curs_set(0)

    # Get terminal dimensions
    rows, columns = stdscr.getmaxyx()
    n_col = 4
    # Get installed packages
    installed_packages = [package.key for package in pkg_resources.working_set]
    current_package_index = 0
    current_page_index = 0
    page_size = (rows-7) * n_col
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, f"{len(installed_packages)} installed packages, current page: {current_page_index+1}", curses.color_pair(2))
        for index, package in enumerate(installed_packages[current_page_index*page_size:current_page_index*page_size+page_size]):
            # Calculate x and y coordinates for the grid
            y = index // n_col
            x = index % n_col
            # Highlight current package
            if current_package_index == index + current_page_index*page_size:
                stdscr.addstr(y + 1, x * (columns // n_col), package.ljust(columns // n_col), curses.color_pair(1))
            else:
                stdscr.addstr(y + 1, x * (columns // n_col), package.ljust(columns // n_col))
        package = installed_packages[current_package_index]
        dist = pkg_resources.get_distribution(package)
        version = dist.version
        location = dist.location
        stdscr.addstr(rows-5, 0, f"{package}", curses.color_pair(1))
        stdscr.addstr(rows-4, 0, f"version : {version}", curses.color_pair(2))
        stdscr.addstr(rows-3, 0, f"location: {location}", curses.color_pair(2))
        stdscr.addstr(rows-1, 0, "Commands : n - next page  p - previous page")
        c = stdscr.getch()
        # Arrow up
        if c == curses.KEY_UP:
            current_package_index -= n_col
            if current_package_index < 0:
                current_package_index = len(installed_packages) - 1
        # Arrow down
        elif c == curses.KEY_DOWN:
            current_package_index += n_col
            if current_package_index >= len(installed_packages):
                current_package_index = 0
        elif c == curses.KEY_RIGHT:
            current_package_index += 1
            if current_package_index >= len(installed_packages):
                current_package_index = 0
        elif c == curses.KEY_LEFT:
            current_package_index -= 1
            if current_package_index < 0:
                current_package_index = len(installed_packages) - 1
        elif c == ord("n"):
            current_page_index += 1
            if current_page_index * page_size >= len(installed_packages):
                current_page_index = 0
        elif c == ord("p"):
            current_page_index -= 1
            if current_page_index < 0:
                current_page_index = (len(installed_packages) -1) // page_size
curses.wrapper(main)


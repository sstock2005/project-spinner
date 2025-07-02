from typing import Tuple
from tkinter import *
import config
import random
import math
    
def frame2color(frame: int) -> str:
    """Converts winning frame number to represented color.

    Args:
        frame (int): Winning frame number

    Returns:
        str: The represented color. (blue, red, yellow, green)
    """
    
    match frame:
        case 0:
            return 'blue'
        case 1:
            return 'blue'
        case 2:
            return 'red'
        case 3:
            return 'red'
        case 4:
            return 'yellow'
        case 5:
            return 'yellow'
        case 6:
            return 'green'
        case 7:
            return 'green'

def color2proj(color: str, projects: list[str]) -> str:
    """Converts the winning color and a randomized list of projects to the winning project.

    Args:
        color (str): The winning color
        projects (list[str]): The randomized list of projects from color2config(str)

    Returns:
        str: The winning project
    """
    
    match color:
        case 'blue':
            return projects[0]
        case 'red':
            return projects[1]
        case 'yellow':
            return projects[2]
        case 'green':
            return projects[3]
        
def color2config(color: str) -> Tuple[str, list[str]]:
    """Converts winning color to corresponding values from config file.

    Args:
        color (str): Winning color

    Returns:
        Tuple[str, list[str]]: The winning language and a randomized list of projects
    """
    
    cfg = config.get()
    lang = cfg['Language'][color]
    proj_len = len(cfg['Project'].values())
    proj_list = cfg['Project']
    
    projects = []
    
    while len(projects) < 4:
        project = proj_list[f'{random.randint(0, proj_len - 1)}']
        
        while project in projects:
            project = proj_list[f'{random.randint(0, proj_len - 1)}']
            
        projects.append(project)
        
    return lang, projects

def get_inbetween(first_point_radians: float) -> float:
    """Used to get the in between of a circle sector

    Args:
        first_point_radians (float): correspoing raidan on unit circle (ex. math.pi / 2)

    Returns:
        float: middle of next sector in the unit circle
    """
    
    return first_point_radians + math.radians(22.5)

def get_points(angle: float, r: int, cx: float, cy: float) -> Tuple[float, float]:
    """Returns the corresponding points on a circle
    
    Args:
        angle (float): The angle in radians
        r (int): The radius of the circle
        cx: (float): The x coordinate of the center of the circle
        cy: (float): The y coordinate of the center of the circle
        
    Returns:
        Tuple[float, float]: (x, y) coordinates
    """
    
    x = cx + r * math.cos(angle)
    y = cy - r * math.sin(angle) # subtract because tkinter uses inverse y coordinates
    
    return x, y

def create_spinner_inbetween(master: Misc, width: int, height: int, colors: list[str]) -> Tuple[Canvas, Tuple[float, float], float]:
    """Creates a spinner that is shifted for us to spin!

    Args:
        master (Misc): Parent Widget
        width (int): Canvas Width
        height (int): Canvas Height
        colors (list[str]): Spinner Colors
        
    Returns:
        Tuple[Canvas, Tuple[float, float], float]: Canvas Drawing Object, Circle Center Coordingates (x, y), Circle Radius
    """
    
    spinner = Canvas(master, width=width, height=height)
    
    spinner_oval_x0 = 10
    spinner_oval_y0 = 50
    spinner_oval_x1 = 590 # may have to adjust this
    spinner_oval_y1 = 630 # may have to adjust this
    spinner_oval_center_x = (spinner_oval_x0 + spinner_oval_x1) / 2
    spinner_oval_center_y = (spinner_oval_y0 + spinner_oval_y1) / 2
    spinner_oval_radius = (spinner_oval_x1 - spinner_oval_x0) / 2

    triangle_line_x0, triangle_line_y0 = get_points(math.pi / 2, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)
    
    spinner_line0_x0, spinner_line0_y0 = get_points(get_inbetween(math.pi / 2), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)
    spinner_line0_x1, spinner_line0_y1 = get_points(get_inbetween(3 * math.pi / 2), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)

    spinner_line1_x0, spinner_line1_y0 = get_points(get_inbetween(math.pi), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)
    spinner_line1_x1, spinner_line1_y1 = get_points(get_inbetween(0), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)

    spinner_line2_x0, spinner_line2_y0 = get_points(get_inbetween(3 * math.pi / 4), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)
    spinner_line2_x1, spinner_line2_y1 = get_points(get_inbetween(7 * math.pi / 4), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)

    spinner_line3_x0, spinner_line3_y0 = get_points(get_inbetween(5 * math.pi / 4), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)
    spinner_line3_x1, spinner_line3_y1 = get_points(get_inbetween(math.pi / 4), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line0_x0, spinner_line0_y0),
                           get_points(math.pi / 2, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line3_x1, spinner_line3_y1),
                           fill=colors[0],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line3_x1, spinner_line3_y1),
                           get_points(math.pi / 4, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line1_x1, spinner_line1_y1),
                           fill=colors[1],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line1_x1, spinner_line1_y1),
                           get_points(0, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line2_x1, spinner_line2_y1),
                           fill=colors[2],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line2_x1, spinner_line2_y1),
                           get_points(7 * math.pi / 4, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line0_x1, spinner_line0_y1),
                           fill=colors[3],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line0_x1, spinner_line0_y1),
                           get_points(3 * math.pi / 2, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line3_x0, spinner_line3_y0),
                           fill=colors[0],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line3_x0, spinner_line3_y0),
                           get_points(5 * math.pi / 4, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line1_x0, spinner_line1_y0),
                           fill=colors[1],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line1_x0, spinner_line1_y0),
                           get_points(math.pi, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line2_x0, spinner_line2_y0),
                           fill=colors[2],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line2_x0, spinner_line2_y0),
                           get_points(3 * math.pi / 4, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line0_x0, spinner_line0_y0),
                           fill=colors[3],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((triangle_line_x0, triangle_line_y0 + 60),
                           (triangle_line_x0 - 30, triangle_line_y0),
                           (triangle_line_x0+ 30, triangle_line_y0),
                           fill='black')
    
    return spinner

def create_spinner(master: Misc, width: int, height: int, colors: list[str]) -> Tuple[Canvas, Tuple[float, float], float]:
    """Creates a spinner for us to spin!

    Args:
        master (Misc): Parent Widget
        width (int): Canvas Width
        height (int): Canvas Height
        colors (list[str]): Spinner Colors
        
    Returns:
        Tuple[Canvas, Tuple[float, float], float]: Canvas Drawing Object, Circle Center Coordingates (x, y), Circle Radius
    """
    
    spinner = Canvas(master, width=width, height=height)
    
    spinner_oval_x0 = 10
    spinner_oval_y0 = 50
    spinner_oval_x1 = 590 # may have to adjust this
    spinner_oval_y1 = 630 # may have to adjust this
    spinner_oval_center_x = (spinner_oval_x0 + spinner_oval_x1) / 2
    spinner_oval_center_y = (spinner_oval_y0 + spinner_oval_y1) / 2
    spinner_oval_radius = (spinner_oval_x1 - spinner_oval_x0) / 2

    spinner_line0_x0, spinner_line0_y0 = get_points(math.pi / 2, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)
    spinner_line0_x1, spinner_line0_y1 = get_points(3 * math.pi / 2, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)

    spinner_line1_x0, spinner_line1_y0 = get_points(math.pi, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)
    spinner_line1_x1, spinner_line1_y1 = get_points(0, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)

    spinner_line2_x0, spinner_line2_y0 = get_points(3 * math.pi / 4, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)
    spinner_line2_x1, spinner_line2_y1 = get_points(7 * math.pi / 4, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)

    spinner_line3_x0, spinner_line3_y0 = get_points(5 * math.pi / 4, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)
    spinner_line3_x1, spinner_line3_y1 = get_points(math.pi / 4, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line0_x0, spinner_line0_y0),
                           get_points(get_inbetween(math.pi / 4), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line3_x1, spinner_line3_y1),
                           fill=colors[0],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line3_x1, spinner_line3_y1),
                           get_points(get_inbetween(0), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line1_x1, spinner_line1_y1),
                           fill=colors[1],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line1_x1, spinner_line1_y1),
                           get_points(get_inbetween(7 * math.pi / 4), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line2_x1, spinner_line2_y1),
                           fill=colors[2],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line2_x1, spinner_line2_y1),
                           get_points(get_inbetween(3 * math.pi / 2), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line0_x1, spinner_line0_y1),
                           fill=colors[3],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line0_x1, spinner_line0_y1),
                           get_points(get_inbetween(5 * math.pi / 4), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line3_x0, spinner_line3_y0),
                           fill=colors[0],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line3_x0, spinner_line3_y0),
                           get_points(get_inbetween(math.pi), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line1_x0, spinner_line1_y0),
                           fill=colors[1],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line1_x0, spinner_line1_y0),
                           get_points(get_inbetween(3 * math.pi / 4), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line2_x0, spinner_line2_y0),
                           fill=colors[2],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line2_x0, spinner_line2_y0),
                           get_points(get_inbetween(math.pi / 2), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line0_x0, spinner_line0_y0),
                           fill=colors[3],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_line0_x0, spinner_line0_y0 + 60),
                           (spinner_line0_x0 - 30, spinner_line0_y0),
                           (spinner_line0_x0 + 30, spinner_line0_y0),
                           fill='black')
    
    return spinner

def spin(master: Misc, frame: int, width: int, height: int, colors: list[str]) -> Canvas:
    """Function to animate our spinner.

    Args:
        master (Misc): Parent Widget
        frame (int): The given frame from the animation
        width (int): Canvas Width
        height (int): Canvas Height
        colors (list[str]): Spinner Colors

    Returns:
        Tuple[Canvas, Tuple[float, float], float]: Canvas Drawing Object, Circle Center Coordingates (x, y), Circle Radius
    """
    
    match frame:
        case 0:
            return create_spinner(master, width, height, colors)
        case 1:
            return create_spinner_inbetween(master, width, height, colors)
        case 2:
            order = [1, 2, 3, 0]
            
            sorted_colors = [colors[i] for i in order]
            
            return create_spinner(master, width, height, colors=sorted_colors)
        case 3:
            order = [1, 2, 3, 0]
            
            sorted_colors = [colors[i] for i in order]
            
            return create_spinner_inbetween(master, width, height, colors=sorted_colors)
        case 4:
            order = [2, 3, 0, 1]
            
            sorted_colors = [colors[i] for i in order]
            
            return create_spinner(master, width, height, colors=sorted_colors)
        case 5:
            order = [2, 3, 0, 1]
            
            sorted_colors = [colors[i] for i in order]
            
            return create_spinner_inbetween(master, width, height, colors=sorted_colors)
        case 6:
            order = [3, 0, 1, 2]
            
            sorted_colors = [colors[i] for i in order]
            
            return create_spinner(master, width, height, colors=sorted_colors)
        case 7:
            order = [3, 0, 1, 2]
            
            sorted_colors = [colors[i] for i in order]
            
            return create_spinner_inbetween(master, width, height, colors=sorted_colors)
from typing import Tuple
from tkinter import *
import math

def get_middle_of_circle_sector_custom(first_point_radians: float) -> float:
    """_summary_

    Args:
        first_point_radians (float): correspoing raidan on unit circle (ex. math.pi / 2)

    Returns:
        float: middle of next sector in the unit circle
    """
    
    return first_point_radians + math.radians(22.5)

def get_circl_points_from_angle(angle: float, r: int, cx: float, cy: float) -> Tuple[float, float]:
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

    spinner_line0_x0, spinner_line0_y0 = get_circl_points_from_angle(math.pi / 2, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)
    spinner_line0_x1, spinner_line0_y1 = get_circl_points_from_angle(3 * math.pi / 2, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)

    spinner_line1_x0, spinner_line1_y0 = get_circl_points_from_angle(math.pi, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)
    spinner_line1_x1, spinner_line1_y1 = get_circl_points_from_angle(0, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)

    spinner_line2_x0, spinner_line2_y0 = get_circl_points_from_angle(3 * math.pi / 4, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)
    spinner_line2_x1, spinner_line2_y1 = get_circl_points_from_angle(7 * math.pi / 4, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)

    spinner_line3_x0, spinner_line3_y0 = get_circl_points_from_angle(5 * math.pi / 4, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)
    spinner_line3_x1, spinner_line3_y1 = get_circl_points_from_angle(math.pi / 4, spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y)

    # spinner.create_oval(spinner_oval_x0, spinner_oval_y0, spinner_oval_x1, spinner_oval_y1, width=3) # maybe we don't use?
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line0_x0, spinner_line0_y0),
                           get_circl_points_from_angle(get_middle_of_circle_sector_custom(math.pi / 4), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line3_x1, spinner_line3_y1),
                           fill=colors[0],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line3_x1, spinner_line3_y1),
                           get_circl_points_from_angle(get_middle_of_circle_sector_custom(0), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line1_x1, spinner_line1_y1),
                           fill=colors[1],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line1_x1, spinner_line1_y1),
                           get_circl_points_from_angle(get_middle_of_circle_sector_custom(7 * math.pi / 4), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line2_x1, spinner_line2_y1),
                           fill=colors[2],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line2_x1, spinner_line2_y1),
                           get_circl_points_from_angle(get_middle_of_circle_sector_custom(3 * math.pi / 2), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line0_x1, spinner_line0_y1),
                           fill=colors[3],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line0_x1, spinner_line0_y1),
                           get_circl_points_from_angle(get_middle_of_circle_sector_custom(5 * math.pi / 4), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line3_x0, spinner_line3_y0),
                           fill=colors[0],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line3_x0, spinner_line3_y0),
                           get_circl_points_from_angle(get_middle_of_circle_sector_custom(math.pi), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line1_x0, spinner_line1_y0),
                           fill=colors[1],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line1_x0, spinner_line1_y0),
                           get_circl_points_from_angle(get_middle_of_circle_sector_custom(3 * math.pi / 4), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line2_x0, spinner_line2_y0),
                           fill=colors[2],
                           width=3,
                           outline='black')
    
    spinner.create_polygon((spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line2_x0, spinner_line2_y0),
                           get_circl_points_from_angle(get_middle_of_circle_sector_custom(math.pi / 2), spinner_oval_radius, spinner_oval_center_x, spinner_oval_center_y),
                           (spinner_line0_x0, spinner_line0_y0),
                           fill=colors[3],
                           width=3,
                           outline='black')
    
    spinner.create_line(spinner_line0_x0, spinner_line0_y0, spinner_line0_x1, spinner_line0_y1, width=3)
    spinner.create_line(spinner_line1_x0, spinner_line1_y0, spinner_line1_x1, spinner_line1_y1, width=3)
    spinner.create_line(spinner_line2_x0, spinner_line2_y0, spinner_line2_x1, spinner_line2_y1, width=3)
    spinner.create_line(spinner_line3_x0, spinner_line3_y0, spinner_line3_x1, spinner_line3_y1, width=3)
    
    spinner.create_polygon((spinner_line0_x0, spinner_line0_y0 + 60),
                           (spinner_line0_x0 - 30, spinner_line0_y0),
                           (spinner_line0_x0 + 30, spinner_line0_y0),
                           fill='black')
    
    return spinner, (spinner_oval_center_x, spinner_oval_center_y), spinner_oval_radius

def spin(master: Misc, frame: int, width: int, height: int, colors: list[str], spinner_oval_center: Tuple[float, float], spinner_oval_radius: float) -> Tuple[Canvas, Tuple[float, float], float]:
    """WIP"""
    
    match frame:
        case 0:
            return create_spinner(master, width, height, colors)
        case 1:
            
            pass
        
    pass
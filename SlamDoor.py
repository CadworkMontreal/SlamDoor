# Copyright 2020 Cadwork.
# All rights reserved.
# This file is part of SlamDoor,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

# import required controllers
import attribute_controller, element_controller, menu_controller, utility_controller

def adjust_openings(angle_value):
  # gets the active elements from 3D
  active_elements = element_controller.get_active_identifiable_element_ids()

  # creates an empty list to hold openings
  openings = []

  # loops over all returned active elements
  for element in active_elements:
    # check if element is an opening
    if attribute_controller.is_opening(element):
      # append to openings list if true
      openings.append(element)

  # set the opening angle of the parent variant to 'angle_value'
  element_controller.set_parent_opening_variants_opening_angle(openings, angle_value)

# creates menu items to be displayed
menu_items = ['Close Doors','Open Doors','','Return']

# displays menu to user and get selected menu item text
selected_menu_item = menu_controller.display_simple_menu(menu_items)

# modify these values to change the angles
close_angle = 0
open_angle = 60

if selected_menu_item == 'Close Doors':
  # selected item was 'Close Doors' so openings set to 'close_angle'
  adjust_openings(close_angle)

if selected_menu_item == 'Open Doors':
  # selected item was 'Open Doors' so openings set to 'open_angle'
  adjust_openings(open_angle)

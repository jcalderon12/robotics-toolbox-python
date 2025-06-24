#!/usr/bin/env python

import numpy as np
from roboticstoolbox.robot.Robot import Robot
from statsmodels.genmod.families import links
from roboticstoolbox.robot.Link import Link

class P3Bot(Robot):
    """
    Class that imports a P3Bot URDF model

    ``P3Bot()`` is a class which imports a P3Bot robot definition
    from a URDF file.  The model describes its kinematic and graphical
    characteristics.

    .. runblock:: pycon

        >>> import roboticstoolbox as rtb
        >>> robot = rtb.models.URDF.P3Bot()
        >>> print(robot)

    .. codeauthor:: Jorge Calderon Gonzalez
    """

    def __init__(self):
        links, name, urdf_string, urdf_filepath = self.URDF_read(
            "p3bot_description/urdf/P3Bot_scaled.urdf"
        )

        gripper_r_base = links[16]
        gripper_l_base = links[34]

        # # Find the finger links
        # r_gripper_links = [link for link in links if link.parent == gripper_r_base]
        # l_gripper_links = [link for link in links if link.parent == gripper_l_base]

        # # New intermediate links
        # r_gripper = Link(name="r_gripper", parent=gripper_r_base)
        # l_gripper = Link(name="l_gripper", parent=gripper_l_base)
        # links.append(r_gripper)
        # links.append(l_gripper)

        # # Set the finger link parent to be the new gripper base link
        # for g_link in r_gripper_links:
        #     g_link._parent = r_gripper

        # for g_link in l_gripper_links:
            # g_link._parent = l_gripper

        super().__init__(
            links,
            name=name,
            manufacturer="Robolab",
            # gripper_links=[r_gripper, l_gripper],
            urdf_string=urdf_string,
            urdf_filepath=urdf_filepath,
        )

        self.qdlim = np.array(
            [ 1.5, 0.6, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]
        )


if __name__ == "__main__":  # pragma nocover

    robot = P3Bot()
    print(robot)
    print(robot.grippers)

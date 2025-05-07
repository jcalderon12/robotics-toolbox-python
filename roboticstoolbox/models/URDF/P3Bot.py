#!/usr/bin/env python

import numpy as np
from roboticstoolbox.robot.Robot import Robot
from statsmodels.genmod.families import links


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

        super().__init__(
            links,
            name=name,
            manufacturer="Robolab",
            gripper_links=links[16],
            urdf_string=urdf_string,
            urdf_filepath=urdf_filepath,
        )

        self.qdlim = np.array(
            [ 4.0, 2.1750, 2.1750, 2.1750, 2.1750, 2.6100, 2.6100, 2.6100, 3.0, 3.0]
        )

if __name__ == "__main__":  # pragma nocover

    robot = P3Bot()
    print(robot)

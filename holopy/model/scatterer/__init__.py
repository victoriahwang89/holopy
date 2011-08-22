# Copyright 2011, Vinothan N. Manoharan, Thomas G. Dimiduk, Rebecca W. Perry,
# Jerome Fung, and Ryan McGorty
#
# This file is part of Holopy.
#
# Holopy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Holopy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Holopy.  If not, see <http://www.gnu.org/licenses/>.

'''
Modules for defining different types of scatterers, including
scattering primitives such as Spheres, and more complex objects such
as Clusters.

.. moduleauthor:: Vinothan N. Manoharan <vnm@seas.harvard.edu>
.. moduleauthor:: Thomas G. Dimiduk <tdimiduk@physics.harvard.edu>
'''

class Scatterer(object):
    """
    abstract base class for scatterers

    """

    def parameter_list(self):
        """
        Return's the scatterer's parameters as an 1d array in a defined order.
        This form is suitable for passing to a minimizer
        """
        raise NotImplementedError

    @classmethod
    def make_from_parameter_list(cls, params):
        """
        Make a new scatterer from a parameter list of the form reterned by
        parameter_list().
        """
        raise NotImplementedError


from sphere import Sphere
from coatedsphere import CoatedSphere
from composite import Composite
from spherecluster import SphereCluster
from spheredimer import SphereDimer


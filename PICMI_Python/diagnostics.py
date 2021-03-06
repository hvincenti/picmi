"""Classes following the PICMI standard
These should be the base classes for Python implementation of the PICMI standard
The classes in the file are all diagnostics related
"""
import numpy as np

from .base import _ClassWithInit

# ----------------------------
# Simulation frame diagnostics
# ----------------------------


class PICMI_FieldDiagnostic(_ClassWithInit):
    """
    Defines the electromagnetic field diagnostics in the simulation frame
      - grid: Grid object for the diagnostic
      - period=1: Period of time steps that the diagnostic is performed
      - data_list=["rho", "E", "B", "J"]: List of quantities to write out
      - write_dir='.': Directory where data is to be written
      - step_min=None: Minimum step at which diagnostics could be written (optional)
                       Defaults to step 0.
      - step_max=None: Maximum step at which diagnostics could be written (optional)
                       Defaults to no limit.
      - number_of_cells=None: Number of cells in each dimension (optional)
                              If not given, will be obtained from grid.
      - lower_bound=None: Lower corner of diagnostics box in each direction (optional)
                          If not given, will be obtained from grid.
      - upper_bound=None: Higher corner of diagnostics box in each direction (optional)
                          If not given, will be obtained from grid.

    """
    def __init__(self, grid, period = 1,
                 data_list = ["rho", "E", "B", "J"],
                 write_dir = None,
                 step_min = None,
                 step_max = None,
                 number_of_cells = None,
                 lower_bound = None,
                 upper_bound = None,
                 **kw):

        self.grid = grid
        self.period = period
        self.data_list = data_list
        self.write_dir = write_dir
        self.step_min = step_min
        self.step_max = step_max

        if number_of_cells is None:
            number_of_cells = grid.number_of_cells
        if lower_bound is None:
            lower_bound = grid.lower_bound
        if upper_bound is None:
            upper_bound = grid.upper_bound

        self.number_of_cells = number_of_cells
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

        self.handle_init(kw)


class PICMI_ElectrostaticFieldDiagnostic(_ClassWithInit):
    """
    Defines the electrostatic field diagnostics in the simulation frame
      - grid: Grid object for the diagnostic
      - period=1: Period of time steps that the diagnostic is performed
      - data_list=["rho", "phi"]: List of quantities to write out
      - write_dir='.': Directory where data is to be written
      - step_min=None: Minimum step at which diagnostics could be written (optional)
                       Defaults to step 0.
      - step_max=None: Maximum step at which diagnostics could be written (optional)
                       Defaults to no limit.
      - number_of_cells=None: Number of cells in each dimension (optional)
                              If not given, will be obtained from grid.
      - lower_bound=None: Lower corner of diagnostics box in each direction (optional)
                          If not given, will be obtained from grid.
      - upper_bound=None: Higher corner of diagnostics box in each direction (optional)
                          If not given, will be obtained from grid.
    """
    def __init__(self, grid, period = 1,
                 data_list = ["rho", "phi"],
                 write_dir = None,
                 step_min = None,
                 step_max = None,
                 number_of_cells = None,
                 lower_bound = None,
                 upper_bound = None,
                 **kw):

        self.grid = grid
        self.period = period
        self.data_list = data_list
        self.write_dir = write_dir
        self.step_min = step_min
        self.step_max = step_max

        if number_of_cells is None:
            number_of_cells = grid.number_of_cells
        if lower_bound is None:
            lower_bound = grid.lower_bound
        if upper_bound is None:
            upper_bound = grid.upper_bound

        self.number_of_cells = number_of_cells
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

        self.handle_init(kw)


class PICMI_ParticleDiagnostic(_ClassWithInit) :
    """
    Defines the particle diagnostics in the simulation frame
      - period=1: Period of time steps that the diagnostic is performed
      - species: Species or list of species to write out
                 Note that the name attribute must be defined for the species.
      - data_list=["position", "momentum", "weighting"]: The data to be written out
      - write_dir='.': Directory where data is to be written
      - step_min=None: Minimum step at which diagnostics could be written (optional)
                       Defaults to step 0.
      - step_max=None: Maximum step at which diagnostics could be written (optional)
                       Defaults to no limit.
    """

    def __init__(self, period = 1,
                 species = None,
                 data_list = ["position", "momentum", "weighting"],
                 write_dir = None,
                 step_min = None,
                 step_max = None,
                 **kw):

        self.period = period
        self.species = species
        self.data_list = data_list
        self.write_dir = write_dir
        self.step_min = step_min
        self.step_max = step_max

        self.handle_init(kw)


# ----------------------------
# Lab frame diagnostics
# ----------------------------


class PICMI_LabFrameFieldDiagnostic(_ClassWithInit):
    """
    Defines the electromagnetic field diagnostics in the lab frame
      - num_snapshots: Number of lab frame snapshots to make
      - dt_snapshots: Time between each snapshot
      - data_list=["rho", "E", "B", "J"]: List of quantities to write out
      - write_dir='.': Directory where data is to be written
    """
    def __init__(self, num_snapshots, dt_snapshots,
                 data_list = ["rho", "E", "B", "J"],
                 write_dir = None,
                 **kw):

        self.num_snapshots = num_snapshots
        self.dt_snapshots = dt_snapshots
        self.data_list = data_list
        self.write_dir = write_dir

        self.handle_init(kw)


class PICMI_LabFrameParticleDiagnostic(_ClassWithInit):
    """
    Defines the particle diagnostics in the lab frame
      - num_snapshots: Number of lab frame snapshots to make
      - dt_snapshots: Time between each snapshot
      - species: Species or list of species to write out
                 Note that the name attribute must be defined for the species.
      - data_list=["position", "momentum", "weighting"]: The data to be written out
      - write_dir='.': Directory where data is to be written
    """
    def __init__(self, num_snapshots, dt_snapshots,
                 species = None,
                 data_list = ["position", "momentum", "weighting"],
                 write_dir = None,
                 **kw):

        self.num_snapshots = num_snapshots
        self.dt_snapshots = dt_snapshots
        self.species = species
        self.data_list = data_list
        self.write_dir = write_dir

        self.handle_init(kw)

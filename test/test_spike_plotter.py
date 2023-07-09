
import pytest
from spikeanalysis.spike_plotter import SpikePlotter


def test_spikePlotter_attributes():

    plotter = SpikePlotter(None)
    assert plotter.dpi ==800, "dpi is wrong"
    assert plotter.figsize == (10,8)

def test_SpikePlotter_kwargs():

    plotter = SpikePlotter(None, **{'dpi': 1200, 'x_axis': 'Time (ms)'})
    assert plotter.dpi == 1200
    assert plotter.x_axis == 'Time (ms)', 'check time is used'
    assert plotter.figsize == (10,8), 'fig size should not be changed from default'


def test_SpikePlotter_wrong_kwarg():
    with pytest.raises(AssertionError):
        plotter = SpikePlotter(None, **{'x': 5}), 'code should check for bad kwargs'

def test_wrong_init():
    with pytest.raises(AssertionError):
        plotter = SpikePlotter(1), 'code should not accept arbitrary objects for plotting'
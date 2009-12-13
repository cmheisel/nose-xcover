"""Companion to nose.plugins.cover. Enable by adding --with-xcoverage to your
arguments. A Cobertura-style XML file, honoring the options you pass to 
--with-coverage, will be generated in coverage.xml"""

import logging
import sys
from nose.plugins import cover, Plugin
log = logging.getLogger('nose.plugins.xcover')


class XCoverage(cover.Coverage):
    """
    Add Cobertura-style XML coverage reports to the built-in nose.plugins.cover plugin.
    """

    def options(self, parser, env):
        """
        Add options to command line.
        """
        Plugin.options(self, parser, env)

    def report(self, stream):
        """
        Output code coverage report.
        """
        import coverage
        coverage.stop()
        modules = [ module
                    for name, module in sys.modules.items()
                    if self.wantModuleCoverage(name, module) ]
        log.debug("Coverage report will cover modules: %s", modules)
        morfs = [ m.__file__ for m in modules if hasattr(m, '__file__') ]
        coverage._the_coverage.xml_report(morfs, outfile='coverage.xml')

"""Companion to nose.plugins.cover. Enable by adding --with-xcoverage to your
arguments. A Cobertura-style XML file, honoring the options you pass to
--with-coverage, will be generated in coverage.xml"""

import logging
import sys
try:
    # Python 2
    import StringIO
except ImportError:
    # Python 3
    from io import StringIO

from nose.plugins import cover, Plugin
log = logging.getLogger('nose.plugins.xcover')


class XCoverage(cover.Coverage):
    """
    Add Cobertura-style XML coverage reports
    to the built-in nose.plugins.cover plugin.
    """

    def options(self, parser, env):
        """
        Add options to command line.
        """
        Plugin.options(self, parser, env)
        parser.add_option('--xcoverage-file', action='store',
                          default=env.get('NOSE_XCOVER_FILE', 'coverage.xml'),
                          dest='xcoverage_file',
                          metavar="FILE",
                          help='Path to xml coverage report.'
                          'Default is coverage.xml in the working directory. '
                          '[NOSE_XCOVERAGE_FILE]')
        parser.add_option('--xcoverage-to-stdout', action='store',
                          default=env.get('NOSE_XCOVER_TO_STDOUT', True),
                          dest='xcoverage_to_stdout',
                          help='Print coverage information to stdout.'
                          'Default is True (output coverage information to stdout). '
                          '[NOSE_XCOVER_TO_STDOUT]')
        
    def configure(self, options, config):
        coverage_on = options.enable_plugin_coverage
        xcoverage_on = options.enable_plugin_xcoverage
        if xcoverage_on and coverage_on:
            log.error(
                """You can not use both --with-xcover and --with-coverage. Using --with-xcover implies --with-coverage""")
            raise TypeError

        cover.old_log = cover.log
        cover.log = log
        super(XCoverage, self).configure(options, config)
        cover.log = cover.old_log

        self.xcoverageFile = options.xcoverage_file
        
        to_stdout = str(options.xcoverage_to_stdout)
        self.xcoverageToStdout = False if '0' in to_stdout or 'false' in to_stdout.lower() else True

    def report(self, stream):
        """
        Output code coverage report.
        """
        if not self.xcoverageToStdout:
            # This will create a false stream where output will be ignored
            stream = StringIO.StringIO()
            
        super(XCoverage, self).report(stream)
        if not hasattr(self, 'coverInstance'):
            # nose coverage plugin 1.0 and earlier
            import coverage
            self.coverInstance = coverage._the_coverage

        modules = [module
                    for name, module in sys.modules.items()
                    if self.wantModuleCoverage(name, module)]
        log.debug("Coverage report will cover modules: %s", modules)
        morfs = [m.__file__ for m in modules if hasattr(m, '__file__')]
        self.coverInstance.xml_report(morfs, outfile=self.xcoverageFile)

# This simple plugin is based on:
# http://www.somebits.com/~nelson/weblog-files/countuniq.txt
import sublime
import sublime_plugin
import re
import sys


class CreateHistogramCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        regions = self.view.sel()
        if len(regions) == 1 and regions[0].empty():
            # Selection is empty, use the entire buffer.
            regions = [sublime.Region(0, self.view.size())]

        for region in regions:

            # Determine the current line ending setting, so we can rejoin the
            # sorted lines using the correct line ending character.
            line_ending_character = '\n'  # Default.
            line_endings = self.view.line_endings()
            if line_endings == 'CR':
                line_ending_character = '\r'
            elif line_endings == 'Windows':
                line_ending_character = '\r\n'

            # Count up all the lines
            lines = [self.view.substr(r) for r in self.view.lines(region)]
            data = {}
            for l in lines:
                data[l] = data.setdefault(l, 0) + 1

            # Sort the data by frequency
            counts = list(zip(data.values(), data.keys()))
            counts.sort()
            counts.reverse()

            # Print out the bins
            output = ""
            for count, item in counts:
                output +=  "%7d %s%s" % (count, item, line_ending_character)

            self.view.replace(edit, region, output)

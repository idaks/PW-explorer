import os
from pygments.lexers import PrologLexer
from pygments.formatters import HtmlFormatter
from IPython.core.display import HTML
from IPython.display import display
from pygments import highlight


## Helper functions meant for Jupyter Notebooks.

class ASPRules(str):

    def __new__(self, descriptor):

        if isinstance(descriptor, list):
            descriptor = list(map(lambda x: x.strip(), descriptor))
            tmp_str = "\n".join(descriptor)
        elif os.path.isfile(descriptor):
            with open(descriptor, 'r') as f:
                tmp_str = f.read()
        else:
            tmp_str = descriptor
        tmp_str = tmp_str.strip()
        return super(ASPRules, self).__new__(self, tmp_str)

    def tolist(self):
        return self.splitlines()

    def _repr_html_(self):
        display(HTML("""
        <style>
        {pygments_css}
        </style>
        """.format(pygments_css=HtmlFormatter().get_style_defs('.highlight'))))
        if len(self.splitlines()) > 1:
            return HTML(data=highlight(self, PrologLexer(), HtmlFormatter(linenos='inline')))._repr_html_()
        else:
            return HTML(data=highlight(self, PrologLexer(), HtmlFormatter()))._repr_html_()
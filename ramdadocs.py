import sublime, sublime_plugin
from urllib.request import urlopen
import re

class RamdaDocsCommand(sublime_plugin.WindowCommand):
  def run(self,):
    print(self)
    self.window.show_input_panel('Enter a ramda function', '', self.fetchDoc, None, None)
    pass

  def append_data(self, data):
    self.ramda_docs_view.set_read_only(False)
    self.ramda_docs_view.run_command('insert_snippet', {'contents': data})
    self.ramda_docs_view.set_read_only(True)

  def show_docs_panel(self, text):
    data = urlopen('https://raw.githubusercontent.com/ramda/ramda/v0.24.1/src/' + text + '.js')
    text = data.read().decode('utf-8')
    search = re.compile(r'\/\*\*(.*)\*\/', re.MULTILINE|re.DOTALL)
    v = search.findall(text)

    self.append_data(v[0])
    self.window.run_command('show_panel', {'panel': 'output.ramda_docs_view'})

  def fetchDoc(self, text):
    if not hasattr(self, 'ramda_docs_view'):
      hasattr(self, 'ramda_docs_view')
    self.ramda_docs_view = self.window.get_output_panel('ramda_docs_view')
    try:
      self.show_docs_panel(text)
    except:
      self.append_data('No such function')
      self.window.run_command('show_panel', {'panel': 'output.ramda_docs_view'})
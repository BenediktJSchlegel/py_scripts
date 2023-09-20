import sys
import urllib.request

class EnvironmentHelper:
  def __init__(self, local, colab):
    self.is_colab = 'google.colab' in sys.modules
    self.colab_base = colab
    self.local_base = local

  def get_path(self):
    if self.is_colab:
      return self.colab_base
    else:
      return self.local_base

  def load_script(self, url, name):
    if not os.path.exists("/functions"):
      os.mkdir('/functions')

    urllib.request.urlretrieve(url, "functions/" + name)

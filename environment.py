import sys
import urllib.request

class EnvironmentHelper:
  def __init__(self, local_data_root, colab_data_root, colab_root, local_root):
    self.is_colab = 'google.colab' in sys.modules
    self.colab_base = colab_data_root
    self.local_base = local_data_root
    self.colab_workdir = colab_root
    self.local_workdir = local_root

    self.include_scripts()


  def include_scripts(self):
    if self.is_colab:
      sys.path.append(self.colab_workdir + '/content/functions')
    else:
      sys.path.append(self.local_workdir + '/content/functions')


  def get_path(self):
    if self.is_colab:
      return self.colab_base
    else:
      return self.local_base

  def load_script(self, url, name):
    if not os.path.exists("/functions"):
      os.mkdir('/functions')

    urllib.request.urlretrieve(url, "functions/" + name)

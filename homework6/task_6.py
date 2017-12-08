import platform
import os
import sys
import pip
import json
import yaml
import commands
def info_catcher():
    sys_inf=[]
    sysinf = {}
    sys_inf.append(platform.python_version())  # Installed python version
    sys_inf.append(commands.getoutput("echo $VIRTUAL_ENV"))  # Python path
    site_packages = next(p for p in sys.path if 'site-packages' in p)
    sys_inf.append(site_packages)  # Site-packages location
    sys_inf.append(sys.executable)  # Python exec location
    installed_packages = pip.get_installed_distributions()  # Installed packages name and version
    installed_packages_list = sorted(["%s=%s" % (i.key, i.version) for i in installed_packages])
    sys_inf.append((installed_packages_list[:]))
    sys_inf.append((os.popen("which pip").read()).strip('\n'))  #  Pip location
    for l in range (2):
        sys_inf.append((os.popen("pyenv version-name").read()).strip('\n')) # name
    sys_qw=['version','python-path','site-packages','exec-location','packages name and version','pip location','name','version',]
    for i in range(len(sys_qw)):
        sysinf[sys_qw[i]] = sys_inf[i]
    with open ('json_rep.json','w') as f:
        json.dump(sysinf,f,sort_keys=True,indent=3,separators=(',', ':'))
    with open ('yaml_rep.yaml','w') as f:
        yaml.dump(sysinf,f)
    return sys_inf


if __name__ == '__main__':
    a = info_catcher()
    print(a)


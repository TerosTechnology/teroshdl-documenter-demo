import yaml
import subprocess
import sys


def git_clone(repository):
    cmd = 'git clone {}'.format(repository)
    cmd = [cmd]
    exec_command(cmd)


def execute_teroshdl(name, folder, output_type):
    signal_extract = 'all'
    constants_extract = 'all'
    processes_extract = 'all'

    output_path = f"./teroshdl_doc/{name}_doc"
    cmd = f"teroshdl-hdl-documenter -o {output_type} --fsm -s {signal_extract} -c {constants_extract} -p {processes_extract} --dep --outpath {output_path} --input {folder}"
    exec_command(cmd)


def exec_command(cmd):
    p = subprocess.Popen(cmd, shell=True)
    p.wait()


def read_repositories(config_path):
    with open(config_path, 'r') as yaml_in:
        yaml_object = yaml.safe_load(yaml_in)
        return yaml_object


OUTPUT_TYPE = 'html'
if (len(sys.argv) > 1):
    OUTPUT_TYPE = sys.argv[1]

CONFIG_PATH = './config.yml'
################################################################################
# HTML
################################################################################
if (OUTPUT_TYPE == 'html'):
    html_index = '<ul>\n'
    repositories = read_repositories(CONFIG_PATH)
    for rep in repositories:
        name = rep
        repository = repositories[name]
        url = repository['url']
        folder = repository['folder']

        html_index += f"    <li>Project: <a href=\"teroshdl_doc/{name}_doc/index.html\">{name}</a></li>\n"
        git_clone(url)
        execute_teroshdl(name, folder, OUTPUT_TYPE)
    html_index += '</ul>\n'

    with open('teroshdl_doc/index.html', "w") as text_file:
        print(html_index, file=text_file)

################################################################################
# Markdown
################################################################################
if (OUTPUT_TYPE == 'markdown'):
    html_index = '# Open source projects:\n'
    repositories = read_repositories(CONFIG_PATH)
    for rep in repositories:
        name = rep
        repository = repositories[name]
        url = repository['url']
        folder = repository['folder']

        html_index += f"Project: [${name} ](./teroshdl_doc/{name}_doc/README.md)\n"
        git_clone(url)
        execute_teroshdl(name, folder, OUTPUT_TYPE)

    with open('teroshdl_doc/README.md', "w") as text_file:
        print(html_index, file=text_file)

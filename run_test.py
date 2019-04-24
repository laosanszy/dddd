import pytest
from Common import Shell

if __name__ == '__main__':
    # pytest.main(['-s', '-q', './TestCase'])
    shell = Shell.Shell()
    # xml_report_path = './Report/xml/'
    # html_report_path = './Report/html/'

    pytest.main(['-s', '-q', '--alluredir', './Report/xml/', './TestCase'])

    cmd = "allure generate ./Report/xml/ -o ./Report/html/ --clean"

    try:
        shell.invoke(cmd)
    except Exception:
        print('xxxx')
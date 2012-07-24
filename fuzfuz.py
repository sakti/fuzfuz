"""Simple fuzzing script based on dictionary"""

import os
import os.path
import cmd
import logging
import logging.handlers

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
EXECUTOR_DIR = os.path.join(ROOT_DIR, 'executor')


def walk_data_dir(data_dir):
    "recursive walking in directory, return list of files"
    for dir_name, sub_dirs, files in os.walk(data_dir):
        for file in files:
            yield os.path.join(dir_name, file)


def parse_content(fh):
    "parse file content, return list of lines"
    for line in fh:
        line = line.strip()
        if line and not line.startswith('# '):
            yield line


def get_payloads(filenames):
    "get fuzz payloads from file"
    for name in filenames:
        if name.endswith('.txt'):
            with open(name) as reader:
                for item in parse_content(reader):
                    yield item


def get_list_executor(dirname):
    "search module in ``executor`` directory"
    list_executor = {}
    for item in os.listdir(dirname):
        path = os.path.join(dirname, item)
        if (item.endswith('.py') and
            item != '__init__.py' and
            os.path.isfile(path)):
            item = item[:-3]
            tmpmodule = __import__('executor.%s' % item)
            tmpmodule = getattr(tmpmodule, item)
            try:
                getattr(tmpmodule, 'execute')
                getattr(tmpmodule, 'LIST_OPTIONS')
                list_executor[item] = tmpmodule
            except:
                continue
    return list_executor


class FuzFuz(cmd.Cmd, object):
    """FuzFuz command processor"""

    def __init__(self):
        super(FuzFuz, self).__init__()
        self.do_reset('')

    def do_set(self, line):
        "set key value\n\nSet option key and value"
        line = line.split()
        if len(line) != 2:
            print "format error"
        else:
            self.options[line[0]] = line[1]
        self._init_logging()

    def do_show(self, line):
        "show\nshow key\n\nShow options [key], default show all options"
        for key, value in self.options.iteritems():
            print "%s\t: %s" % (key, value)

        print "\nmandatory options:"
        for option in self._get_options():
            print option

        if self._get_current_executor():
            print '\n'
            executor_title = ('Executor: %s' %
                    self._get_current_executor().__name__)
            print executor_title
            print '=' * len(executor_title)
            print self._get_current_executor().__doc__
            print '\n'

    def do_EOF(self, line):
        return True

    def do_list(self, line):
        "list available executor, you must select one executor before fuzzing"
        for executor in self.executors:
            print executor

    def do_select(self, line):
        "select an executor"
        if line in self.executors:
            self.executor = line
            self.prompt = 'FuzFuz %s > ' % line
        else:
            print "Executor '%s' not available" % line

    def do_reset(self, line):
        "reset all option"
        self.options = {'log': 'run.log'}
        self.prompt = 'FuzFuz > '
        self.executors = get_list_executor(EXECUTOR_DIR)
        self.executor = ''
        self.logging = None

    def _init_logging(self):
        "logging initialization"
        if self._get_current_executor():
            self.logging = logging.getLogger('fuzfuz %s' %
                            self._get_current_executor().__name__)
            filename = self.options.get('log')
            formatter = logging.Formatter(
                        '[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
            handler = logging.handlers.WatchedFileHandler(filename=filename)
            handler.setFormatter(formatter)
            self.logging.addHandler(handler)
            self.logging.setLevel(logging.DEBUG)

    def _get_current_executor(self):
        "return current executor"
        if self.executor:
            return self.executors[self.executor]

    def _get_options(self):
        "get all options of current executor"
        if self.executor:
            return self._get_current_executor().LIST_OPTIONS
        else:
            return '-'

    def _check_options(self):
        "check if user options comply all executor options"
        for option in self._get_options():
            if not option in self.options:
                return False
        return True

    def do_run(self, line):
        "run fuzzing"
        if not self.executor:
            print 'please select executor'
            return

        if not self._check_options():
            print 'please set all mandatory options'
            return

        payloads = get_payloads(walk_data_dir(DATA_DIR))

        try:
            self._get_current_executor().execute(self.options,
                                                    payloads,
                                                    self.logging)
        except KeyboardInterrupt:
            print 'STOPPING'

if __name__ == '__main__':
    FuzFuz().cmdloop()

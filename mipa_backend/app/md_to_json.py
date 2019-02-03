import re
import json
import pdb
import os

accepted_fields = ['id', 'title', 'categories', 'difficulty', 'question', 'solution', 'solutionCode', 'hints', 'tests']
could_have_code = ['question', 'solution', 'solutionCode']

class MdToJson:
    def __init__(self, slug):
        self.slug = slug

    def json_result(self):
        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, '../base_challenges/' + self.slug + '.md')
        challenge_file = open(file_path)
        hints = challenge_file.read()
        hints = hints[2:] # pop first #_s bc it does not get split
        # main split between h1s are 2 newlines and then 1 hash with a space
        sections = re.split(r'\n\n#\s', hints) 
        
        dict = {}
        for sect in sections:
            end_of_key = re.search(r'\n', sect).end()
            k = self.prettify_key(sect[0:end_of_key]).strip()
            v = sect[end_of_key:]
            if k not in accepted_fields:
                raise NameError(str(k) + " not in accepted fields")
            if k == 'hints':
                v = self.handle_hints(sect)
            dict[k] = v
        return dict
        
    @staticmethod
    def handle_hints(v):
        tmp = {}
        splitter = re.split(r'(\[[a-z]{2}\]\n)', v)
        splitter = filter(lambda a: a != 'Hints\n', splitter)
        regex = re.compile(r'\.q.*')
        hints = filter(regex.search, splitter)
        for hint in hints:
            hint_kv = re.split(r'(\.\w\_.*\n)', hint)
            hint_kv_stripped = map(lambda s: s.strip(), hint_kv)
            hint_kv_filtered = filter(None, hint_kv_stripped)
            for kv in hint_kv_filtered:
                kind = re.match(r'(\.\w\_\s*?)', kv).group(0)
                final_val = kv.replace(kind, '')
                tmp[kind] = final_val
        return tmp

    @staticmethod
    def prettify_key(k):
      if '# ' in k:
          return k[2:][0].lower() + k[2:][1:]
      else:
          return k[0].lower() + k[1:]  # prettify key
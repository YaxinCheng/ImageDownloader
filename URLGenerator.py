import json

def source(filePath):
    target = None
    with open(filePath) as file:
        target = json.load(file)
    if target is None\
        or 'templates' not in target:
         raise ValueError('Config file not exist or missing templates key')
    async def iterator():
        startPage: int = int(target.get('start', 1))
        templates = target['templates']
        if isinstance(templates, str): templates = [templates]
        while True:
            for template in templates:
                yield template.format(startPage)
            startPage += 1
    return iterator
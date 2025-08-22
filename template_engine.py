import os
import mimetypes
import settings

#This is the file error class
class FileError(Exception):
    pass

#This is the render error class
#It is raised when ever one or more kwargs is not passed
#and they are assigned None by default
class RenderError(Exception):
    pass


class FileCheck:
    # this is the section to check the file and return something
    def __init__(self, file):
        self.file = file
        self.file_paths = []
        for template_dir in settings.TEMPLATES_DIRS:
            file_path = os.path.join(template_dir, self.file)
            self.file_paths.append(file_path)


    def __call__(self):
        file_exists = False
        file_path = ''
        for path in self.file_paths:
            if os.path.exists(path):
                file_path = path
                file_exists = True
                break
        if file_exists == False:
            raise FileError("File doesn't exist")
        elif file_exists == True:
            if os.path.is_file(file_path):
                mime, _ = mimetypes.guess_type(file_path)
                if mime == 'text/html':
                    template_size = os.path.getsize(file_path)
                    if int(template_size) > int(settings.MAX_BYTE_SIZE):
                        raise FileError(f"Template size too big, Maximum {int(settings.MAX_BYTE_SIZE)} allowed.")
                    else:
                        return file_path
                else:
                    raise FileError("The file provided is not HTML, only HTML accepted.")
            else:
                raise FileError("The path entered does not point to a file.")



def RenderFor(template, context):
    pass


def RenderIf(template, context):
    pass



class Render:
    def __init__(self, template_path, context):
        self.template_path = template_path
        self.context = context
    def __call__(self):
        pass
        # This part uses jinja
        # This will be your own template engine
        #return rendered_template



class Template_Engine:
    def __init__(self, request = None, template = None, context = None):
        if request == None:
            raise RenderError('Request object is Required, Not passed')
        else:
            if template == None:
                raise RenderError('Template is Required, Not passed')
            else:
                self.request = request
                self.template = template
                self.context = context

    def __call__(self):
        template_path = FileCheck(self.template)()
        rendered_html = Render(template_path, self.context)
        return rendered_html()
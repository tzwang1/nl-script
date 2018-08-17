import os
import zipfile
import glob
import shutil

'''
Script that downloads NL zips from RTC, and reorganizes them into the new structure.
'''

# Global Variables
NL_templates = "---NL_Templates"
NL_migration = "NL_Migration"
new_NL_migration = "New_" + NL_migration

def delete_recreate_component_dir(component_path):
    '''
    Delete and recreate a directory, to ensure that it doesn't
    contain any left over the proper contents files from previous
    runs.
    '''
    if os.path.exists(component_path) and os.path.isdir(component_path):
        shutil.rmtree(component_path)
        os.path.mkdir(component_path)

def initialize_new_component_folder(parent_folder, component_name):
    '''
    Create a new component folder called component_name in parent_folder
    by copying the template in --NL_Templates.
    '''
    pass

def copy_properties_files(new_component_folder, old_component_folder):
    '''
    Copies .properties files and com folder from old_component_folder 
    to new component_folder.
    '''
    pass

                
if __name__ == "__main__":
    # Create new NL migration directory
    if not os.path.exists(new_NL_migration):
        os.mkdir(new_NL_migration)


    for component in os.listdir(NL_migration):
        new_component_path = os.path.join(new_NL_migration, component)
        delete_recreate_component_dir(new_component_path)
        for datetime in os.listdir(os.path.join(NL_migration, component)):
            for package_file in os.listdir(os.path.join(NL_migration, component, datetime)):
                package_file_path = os.path.join(NL_migration, component, datetime, package_file)
                if zipfile.is_zipfile(package_file_path):
                    package_folder = package_file.rstrip('.zip')
                    package_zip = zipfile.ZipFile(package_file_path)
                    package_zip.extractall(path=os.path.join(new_component_path, package_folder))
                    # TODO: initialize new component folder in new_NL_migration folder
                    # initialize_new_component_folder()
                    # TODO: Copy properties files
                    # copy_properties_files()
                    # TODO: copy .project files
                    # TODO: edit manifest ID and label to be the plugin name, and version to be plugin version, and host ID to be plugin name
                    
                    



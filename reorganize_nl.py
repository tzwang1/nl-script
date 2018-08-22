import os
import zipfile
import glob
import shutil
from pathlib import Path
from email._header_value_parser import DOT

'''
Script that downloads NL zips from RTC, and reorganizes them into the new structure.
'''

# Global Variables
NL_templates = "---NL_Templates"
NL_migration = "NL_Migration"
new_NL_migration = "New_" + NL_migration
TEMP_DIR = os.path.join(str(Path.home()), 'temp')

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

def replace_strings_in_file(file_path, replacing_str, wanted_str):
    fd_r = open(file_path, "r")
    content = fd_r.read();
    content_new = content
    fd_r.close()
    if replacing_str in content:
        content_new = content.replace(replacing_str, wanted_str)
    else:
        print("GG")
    fd_w = open(file_path, "w")
    fd_w.write(content_new)
    fd_w.close()
    return


if __name__ == "__main__":
    '''
    #Testing purpose:
    cwd = os.path.join(os.getcwd(), "test_jars")
    for nl_jars in os.listdir(cwd):
        nl_jars_path = os.path.join(cwd, nl_jars)
        jar_zip = zipfile.ZipFile(nl_jars_path)
        jar_zip.extractall(os.path.join(cwd))
    '''
    
    fd_w = ""
    if os.path.exists(os.path.join("llc.map")):
        os.remove(os.path.join("llc.map"))
        fd_w = open("llc.map", "w+")
    llc_map = ""
    # Create new NL migration directory
    if not os.path.exists(new_NL_migration):
        os.mkdir(new_NL_migration)
  
#     if os.path.exists(TEMP_DIR):
#         shutil.rmtree(TEMP_DIR)
#      
#     for component in os.listdir(NL_migration):
#         new_component_path = os.path.join(new_NL_migration, component)
#         #print(new_component_path)
#         delete_recreate_component_dir(new_component_path)
#         for datetime in os.listdir(os.path.join(NL_migration, component)):
#             for package_file in os.listdir(os.path.join(NL_migration, component, datetime)):
#                 package_file_path = os.path.join(NL_migration, component, datetime, package_file)
#                 if zipfile.is_zipfile(package_file_path):
#                     package_folder = package_file.rstrip('.zip')
#                     package_zip = zipfile.ZipFile(package_file_path)
#                     package_zip.extractall(path=os.path.join(TEMP_DIR, component, package_folder))
#                     # TODO: initialize new component folder in new_NL_migration folder
#                     # initialize_new_component_folder()
#                     # TODO: Copy properties files
#                     # copy_properties_files()
#                     # TODO: copy .project files
#                     # TODO: edit manifest ID and label to be the plugin name, and version to be plugin version, and host ID to be plugin name
#        
    # Extract the jar files               
#     for component in os.listdir(TEMP_DIR):
#         for package_file in os.listdir(os.path.join(TEMP_DIR, component)):
#             print(package_file)
#             package_file_path = os.path.join(TEMP_DIR, component, package_file)
#             package_plugin_path = os.path.join(package_file_path, "eclipse", "plugins")
#             package_feature_path = os.path.join(package_file_path, "eclipse", "features")
#             for nl_jar in os.listdir(package_plugin_path):
#                 nl_jar_path = os.path.join(package_plugin_path, nl_jar)
#                 index_temp = nl_jar.find('_')
#                 if index_temp != -1: 
#                     package_folder = nl_jar[0: (index_temp)]
#                     print("packge_folder: ", package_folder)
#                     print("nl_jar: ", nl_jar, ", isExists= ", os.path.exists(nl_jar_path), ", isZip: ", zipfile.is_zipfile(nl_jar_path))
#                     component_extract = component + "_Extracted"
#                     (zipfile.ZipFile(nl_jar_path)).extractall(os.path.join(TEMP_DIR, component_extract, "plugins", package_folder))
        
                    
#     for component in os.listdir(TEMP_DIR):
#         if "Extracted" in component: 
#             for plugin_file in os.listdir(os.path.join(TEMP_DIR, component, "plugins")):
#                 
#                 plugin_file_path = os.path.join(TEMP_DIR, component, "plugins", plugin_file)
#                 print(plugin_file_path)
#                 if os.path.isdir(plugin_file_path):
#                     for item in os.listdir(plugin_file_path):
#                         if item == "com":
#                             shutil.move(os.path.join(plugin_file_path, "com"), os.path.join(plugin_file_path, "src", "com"))
#                     #copy the .project file and build.properties
#                     shutil.copy(os.path.join(NL_templates, "com.ibm.debug.pdt.codecoverage.core.nl1", ".project"), plugin_file_path)
#                     shutil.copy(os.path.join(NL_templates, "com.ibm.debug.pdt.codecoverage.core.nl1", "build.properties"), plugin_file_path)
#                     
#                     #read the file and make modifications
#                     replace_strings_in_file(os.path.join(plugin_file_path, ".project"), "@@@PLUGIN_NL_FRAGMENT_ID@@@", plugin_file)

        
    for component in os.listdir(TEMP_DIR):
        if "Extracted" not in component: 
            for package_file in os.listdir(os.path.join(TEMP_DIR, component)):
                print(package_file)
                package_file_path = os.path.join(TEMP_DIR, component, package_file)
                package_plugin_path = os.path.join(package_file_path, "eclipse", "plugins")
                package_feature_path = os.path.join(package_file_path, "eclipse", "features")
                llc_map += "************************************************************************************\n"
                for feature_file in os.listdir(package_feature_path):
                    print("feature_file: ", feature_file)
                    feature_file_path = os.path.join(package_feature_path, feature_file)
                    index_temp = feature_file.find('_')
                    if index_temp != -1:
                        feature_folder = feature_file[0: index_temp]
                        print(">>>Previous", feature_folder)
                        if "nls1" not in feature_folder and  "nls2" not in feature_folder and "nls2bidi" not in feature_folder:
                            if "1" in feature_file:
                                feature_folder = feature_folder + "_feature.nls1"
                            elif "2" in feature_file:
                                feature_folder = feature_folder + "_feature.nls2"
                            elif "2bidi" in feature_file:
                                feature_folder = feature_folder + "_feature.nls2bidi"
                        print(">>>Modified", feature_folder)
                        
                        
#                         if not os.path.exists(os.path.join(TEMP_DIR, component + "_Extracted", "features")):
#                             os.mkdir(os.path.join(TEMP_DIR, component + "_Extracted", "features"))
#                         if not os.path.exists(os.path.join(TEMP_DIR, component + "_Extracted", "features", feature_folder)):
#                             os.mkdir(os.path.join(TEMP_DIR, component + "_Extracted", "features", feature_folder))
#                         shutil.copy(os.path.join(NL_templates, "com.ibm.debug.pdt.codecoverage.core.nls1.feature", ".project"), os.path.join(TEMP_DIR, component + "_Extracted", "features", feature_folder))
#                         shutil.copy(os.path.join(NL_templates, "com.ibm.debug.pdt.codecoverage.core.nls1.feature", "build.properties"), os.path.join(TEMP_DIR, component + "_Extracted", "features", feature_folder))
#                         shutil.copy(os.path.join(package_feature_path, feature_file, "feature.xml"), os.path.join(TEMP_DIR, component + "_Extracted", "features", feature_folder))
#                         
#                         replace_strings_in_file(os.path.join(TEMP_DIR, component + "_Extracted", "features", feature_folder, ".project"), "@@@PLUGIN_NL_FEATURE_ID@@@", feature_folder)
                        
                        temp_str = "feature@" + feature_folder + "=COPY,," + feature_folder + "\n"
                        llc_map += temp_str
                for nl_jar in os.listdir(package_plugin_path):
                    nl_jar_path = os.path.join(package_plugin_path, nl_jar)
                    index_temp = nl_jar.find('_')
                    if index_temp != -1: 
                        package_folder = nl_jar[0: (index_temp)]
                        temp_str = "fragment@" + package_folder + "=COPY,," + package_folder + "\n"
                        llc_map += temp_str
#                         print("packge_folder: ", package_folder)
#                         print("nl_jar: ", nl_jar, ", isExists= ", os.path.exists(nl_jar_path), ", isZip: ", zipfile.is_zipfile(nl_jar_path))
#                         component_extract = component + "_Extracted"
#                         (zipfile.ZipFile(nl_jar_path)).extractall(os.path.join(TEMP_DIR, component_extract, "plugins", package_folder))
                
                        
                        
#     for component in os.listdir(TEMP_DIR):
#         if "Extracted" not in component: 
#             llc_map += "-----------------------" + component +" Features-----------------------\n"
#             for package_file in os.listdir(os.path.join(TEMP_DIR, component)):
#                 print(package_file)
#                 package_file_path = os.path.join(TEMP_DIR, component, package_file)
#                 package_plugin_path = os.path.join(package_file_path, "eclipse", "plugins")
#                 package_feature_path = os.path.join(package_file_path, "eclipse", "features")
#                 for feature_file in os.listdir(package_feature_path):
#                     print("feature_file: ", feature_file)
#                     feature_file_path = os.path.join(package_feature_path, feature_file)
#                     index_temp = feature_file.find('_')
#                     if index_temp != -1:
#                         feature_folder = feature_file[0: index_temp]
#                         print(">>>Previous", feature_folder)
#                         if "nls1" not in feature_folder and  "nls2" not in feature_folder and "nls2bidi" not in feature_folder:
#                             if "1" in feature_file:
#                                 feature_folder = feature_folder + "_feature.nls1"
#                             elif "2" in feature_file:
#                                 feature_folder = feature_folder + "_feature.nls2"
#                             elif "2bidi" in feature_file:
#                                 feature_folder = feature_folder + "_feature.nls2bidi"
#                         print(">>>Modified", feature_folder)
#                         
#                         
#                         if not os.path.exists(os.path.join(TEMP_DIR, component + "_Extracted", "features")):
#                             os.mkdir(os.path.join(TEMP_DIR, component + "_Extracted", "features"))
#                         if not os.path.exists(os.path.join(TEMP_DIR, component + "_Extracted", "features", feature_folder)):
#                             os.mkdir(os.path.join(TEMP_DIR, component + "_Extracted", "features", feature_folder))
#                         shutil.copy(os.path.join(NL_templates, "com.ibm.debug.pdt.codecoverage.core.nls1.feature", ".project"), os.path.join(TEMP_DIR, component + "_Extracted", "features", feature_folder))
#                         shutil.copy(os.path.join(NL_templates, "com.ibm.debug.pdt.codecoverage.core.nls1.feature", "build.properties"), os.path.join(TEMP_DIR, component + "_Extracted", "features", feature_folder))
#                         shutil.copy(os.path.join(package_feature_path, feature_file, "feature.xml"), os.path.join(TEMP_DIR, component + "_Extracted", "features", feature_folder))
#                         
#                         replace_strings_in_file(os.path.join(TEMP_DIR, component + "_Extracted", "features", feature_folder, ".project"), "@@@PLUGIN_NL_FEATURE_ID@@@", feature_folder)
#                         
#                         temp_str = "feature@" + feature_folder + "=COPY,," + feature_folder + "\n"
#                         llc_map += temp_str

                        
                        
    #Store the value of llc_map into llc.map
    fd_w.write(llc_map)
    fd_w.close()                   
                        
                        
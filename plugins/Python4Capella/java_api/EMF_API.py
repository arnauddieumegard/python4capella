loadModule('/Capella/EMF')
include('workspace://Python4Capella/java_api/Java_API.py')
if False:
    from java_api.Java_API import *
import sys

def e_all_contents(e_obj):
    """Gets all elements contained directly and indirectly in the given EObject"""
    return eAllContents(e_obj);
def get_e_classifier(ns_uri, eclass_name):
    """Gets the EClassifier for the given namespace URI and eclassifier name"""
    return getEClassifier(ns_uri, eclass_name)
def create_e_object(ns_uri, eclass_name):
    """Creates an EObject of the given type (namespace URI and EClass name)"""
    return create(ns_uri, eclass_name)
def create_e_list(java_list, cls):
    """Creates a JavaList"""
    return JavaList(java_list, cls)
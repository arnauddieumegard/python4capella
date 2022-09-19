include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *
include('workspace://Python4Capella/simplified_api/pvmt.py')
if False:
    from simplified_api.pvmt import *
include('workspace://Python4Capella/simplified_api/requirement.py')
if False:
    from simplified_api.requirement import *

import unittest

class capella_tests(unittest.TestCase):

    def test_CapellaModel_system_engineering_getter(self):
        tested = CapellaModel()
        tested.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        tested.get_system_engineering()
        pass

    def test_CapellaModel_progress_status_getter(self):
        tested = CapellaModel()
        tested.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        tested.get_progress_status()
        pass

    def test_CapellaModel_referenced_libraries_getter(self):
        tested = CapellaModel()
        tested.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        tested.get_referenced_libraries()
        pass

    def test_CapellaModel_referenced_libraries_setter(self):
        tested = CapellaModel()
        tested.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        value = CapellaLibrary()
        tested.get_referenced_libraries().add(value)
        pass

    def test_CapellaModel_all_diagrams_getter(self):
        tested = CapellaModel()
        tested.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        tested.get_all_diagrams()
        pass

    def test_CapellaModel_get_diagrams(self):
        tested = CapellaModel()
        tested.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        param1 = "value"
        tested.get_diagrams(param1)
        pass

    def test_CapellaModel_open(self):
        tested = CapellaModel()
        tested.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        param1 = "value"
        tested.open(param1)
        pass

    def test_CapellaModel_create(self):
        tested = CapellaModel()
        tested.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        param1 = "value"
        tested.create(param1)
        pass

    def test_CapellaModel_save(self):
        tested = CapellaModel()
        tested.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        tested.save()
        pass

    def test_CapellaLibrary_system_engineering_getter(self):
        tested = CapellaLibrary()
        tested.get_system_engineering()
        pass

    def test_CapellaLibrary_progress_status_getter(self):
        tested = CapellaLibrary()
        tested.get_progress_status()
        pass

    def test_CapellaLibrary_referenced_libraries_getter(self):
        tested = CapellaLibrary()
        tested.get_referenced_libraries()
        pass

    def test_CapellaLibrary_referenced_libraries_setter(self):
        tested = CapellaLibrary()
        value = CapellaLibrary()
        tested.get_referenced_libraries().add(value)
        pass

    def test_CapellaLibrary_all_diagrams_getter(self):
        tested = CapellaLibrary()
        tested.get_all_diagrams()
        pass

    def test_CapellaLibrary_get_diagrams(self):
        tested = CapellaLibrary()
        param1 = "value"
        tested.get_diagrams(param1)
        pass

    def test_CapellaLibrary_open(self):
        tested = CapellaLibrary()
        param1 = "value"
        tested.open(param1)
        pass

    def test_CapellaLibrary_create(self):
        tested = CapellaLibrary()
        param1 = "value"
        tested.create(param1)
        pass

    def test_CapellaLibrary_save(self):
        tested = CapellaLibrary()
        tested.save()
        pass

    def test_SystemEngineering_owned_property_value_pkgs_getter(self):
        tested = SystemEngineering()
        tested.get_owned_property_value_pkgs()
        pass

    def test_SystemEngineering_id_getter(self):
        tested = SystemEngineering()
        tested.get_id()
        pass

    def test_SystemEngineering_id_setter(self):
        tested = SystemEngineering()
        value = "value"
        tested.set_id(value)
        pass

    def test_SystemEngineering_sid_getter(self):
        tested = SystemEngineering()
        tested.get_sid()
        pass

    def test_SystemEngineering_sid_setter(self):
        tested = SystemEngineering()
        value = "value"
        tested.set_sid(value)
        pass

    def test_SystemEngineering_name_getter(self):
        tested = SystemEngineering()
        tested.get_name()
        pass

    def test_SystemEngineering_name_setter(self):
        tested = SystemEngineering()
        value = "value"
        tested.set_name(value)
        pass

    def test_SystemEngineering_summary_getter(self):
        tested = SystemEngineering()
        tested.get_summary()
        pass

    def test_SystemEngineering_summary_setter(self):
        tested = SystemEngineering()
        value = "value"
        tested.set_summary(value)
        pass

    def test_SystemEngineering_description_getter(self):
        tested = SystemEngineering()
        tested.get_description()
        pass

    def test_SystemEngineering_description_setter(self):
        tested = SystemEngineering()
        value = "value"
        tested.set_description(value)
        pass

    def test_SystemEngineering_status_getter(self):
        tested = SystemEngineering()
        tested.get_status()
        pass

    def test_SystemEngineering_status_setter(self):
        tested = SystemEngineering()
        value = "value"
        tested.set_status(value)
        pass

    def test_SystemEngineering_review_getter(self):
        tested = SystemEngineering()
        tested.get_review()
        pass

    def test_SystemEngineering_review_setter(self):
        tested = SystemEngineering()
        value = "value"
        tested.set_review(value)
        pass

    def test_SystemEngineering_visible_in_documentation_getter(self):
        tested = SystemEngineering()
        tested.get_visible_in_documentation()
        pass

    def test_SystemEngineering_visible_in_documentation_setter(self):
        tested = SystemEngineering()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_SystemEngineering_visible_for_traceability_getter(self):
        tested = SystemEngineering()
        tested.get_visible_for_traceability()
        pass

    def test_SystemEngineering_visible_for_traceability_setter(self):
        tested = SystemEngineering()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_SystemEngineering_owned_constraints_getter(self):
        tested = SystemEngineering()
        tested.get_owned_constraints()
        pass

    def test_SystemEngineering_constraints_getter(self):
        tested = SystemEngineering()
        tested.get_constraints()
        pass

    def test_SystemEngineering_constraints_setter(self):
        tested = SystemEngineering()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_SystemEngineering_owned_property_values_getter(self):
        tested = SystemEngineering()
        tested.get_owned_property_values()
        pass

    def test_SystemEngineering_applied_property_values_getter(self):
        tested = SystemEngineering()
        tested.get_applied_property_values()
        pass

    def test_SystemEngineering_applied_property_values_setter(self):
        tested = SystemEngineering()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_SystemEngineering_owned_property_value_groups_getter(self):
        tested = SystemEngineering()
        tested.get_owned_property_value_groups()
        pass

    def test_SystemEngineering_applied_property_value_groups_getter(self):
        tested = SystemEngineering()
        tested.get_applied_property_value_groups()
        pass

    def test_SystemEngineering_applied_property_value_groups_setter(self):
        tested = SystemEngineering()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_SystemEngineering_owned_enumeration_property_types_getter(self):
        tested = SystemEngineering()
        tested.get_owned_enumeration_property_types()
        pass

    def test_SystemEngineering_owned_diagrams_getter(self):
        tested = SystemEngineering()
        tested.get_owned_diagrams()
        pass

    def test_SystemEngineering_element_of_interest_for_diagrams_getter(self):
        tested = SystemEngineering()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_SystemEngineering_element_of_interest_for_diagrams_setter(self):
        tested = SystemEngineering()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_SystemEngineering_contextual_element_for_diagrams_getter(self):
        tested = SystemEngineering()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_SystemEngineering_contextual_element_for_diagrams_setter(self):
        tested = SystemEngineering()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_SystemEngineering_representing_diagrams_getter(self):
        tested = SystemEngineering()
        tested.get_representing_diagrams()
        pass

    def test_SystemEngineering__r_e_cs_getter(self):
        tested = SystemEngineering()
        tested.get__r_e_cs()
        pass

    def test_SystemEngineering__r_e_cs_setter(self):
        tested = SystemEngineering()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_SystemEngineering__r_p_ls_getter(self):
        tested = SystemEngineering()
        tested.get__r_p_ls()
        pass

    def test_SystemEngineering__r_p_ls_setter(self):
        tested = SystemEngineering()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_SystemEngineering_get_label(self):
        tested = SystemEngineering()
        tested.get_label()
        pass

    def test_SystemEngineering_get_element_type(self):
        tested = SystemEngineering()
        tested.get_element_type()
        pass

    def test_SystemEngineering_get_container(self):
        tested = SystemEngineering()
        tested.get_container()
        pass

    def test_SystemEngineering_get_contents(self):
        tested = SystemEngineering()
        tested.get_contents()
        pass

    def test_SystemEngineering_get_all_contents(self):
        tested = SystemEngineering()
        tested.get_all_contents()
        pass

    def test_SystemEngineering_get_all_contents_by_type(self):
        tested = SystemEngineering()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_SystemEngineering_get_available_s_b_queries(self):
        tested = SystemEngineering()
        tested.get_available_s_b_queries()
        pass

    def test_SystemEngineering_get_query_result(self):
        tested = SystemEngineering()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_SystemEngineering_rec_catalogs_getter(self):
        tested = SystemEngineering()
        tested.get_rec_catalogs()
        pass

    def test_SystemEngineering_operational_analysis_getter(self):
        tested = SystemEngineering()
        tested.get_operational_analysis()
        pass

    def test_SystemEngineering_system_analysis_getter(self):
        tested = SystemEngineering()
        tested.get_system_analysis()
        pass

    def test_SystemEngineering_logical_architecture_getter(self):
        tested = SystemEngineering()
        tested.get_logical_architecture()
        pass

    def test_SystemEngineering_physical_architecture_getter(self):
        tested = SystemEngineering()
        tested.get_physical_architecture()
        pass

    def test_SystemEngineering_e_p_b_s_architecture_getter(self):
        tested = SystemEngineering()
        tested.get_e_p_b_s_architecture()
        pass

    def test_Constraint_id_getter(self):
        tested = Constraint()
        tested.get_id()
        pass

    def test_Constraint_id_setter(self):
        tested = Constraint()
        value = "value"
        tested.set_id(value)
        pass

    def test_Constraint_sid_getter(self):
        tested = Constraint()
        tested.get_sid()
        pass

    def test_Constraint_sid_setter(self):
        tested = Constraint()
        value = "value"
        tested.set_sid(value)
        pass

    def test_Constraint_name_getter(self):
        tested = Constraint()
        tested.get_name()
        pass

    def test_Constraint_name_setter(self):
        tested = Constraint()
        value = "value"
        tested.set_name(value)
        pass

    def test_Constraint_summary_getter(self):
        tested = Constraint()
        tested.get_summary()
        pass

    def test_Constraint_summary_setter(self):
        tested = Constraint()
        value = "value"
        tested.set_summary(value)
        pass

    def test_Constraint_description_getter(self):
        tested = Constraint()
        tested.get_description()
        pass

    def test_Constraint_description_setter(self):
        tested = Constraint()
        value = "value"
        tested.set_description(value)
        pass

    def test_Constraint_status_getter(self):
        tested = Constraint()
        tested.get_status()
        pass

    def test_Constraint_status_setter(self):
        tested = Constraint()
        value = "value"
        tested.set_status(value)
        pass

    def test_Constraint_review_getter(self):
        tested = Constraint()
        tested.get_review()
        pass

    def test_Constraint_review_setter(self):
        tested = Constraint()
        value = "value"
        tested.set_review(value)
        pass

    def test_Constraint_visible_in_documentation_getter(self):
        tested = Constraint()
        tested.get_visible_in_documentation()
        pass

    def test_Constraint_visible_in_documentation_setter(self):
        tested = Constraint()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_Constraint_visible_for_traceability_getter(self):
        tested = Constraint()
        tested.get_visible_for_traceability()
        pass

    def test_Constraint_visible_for_traceability_setter(self):
        tested = Constraint()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_Constraint_owned_constraints_getter(self):
        tested = Constraint()
        tested.get_owned_constraints()
        pass

    def test_Constraint_constraints_getter(self):
        tested = Constraint()
        tested.get_constraints()
        pass

    def test_Constraint_constraints_setter(self):
        tested = Constraint()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_Constraint_owned_property_values_getter(self):
        tested = Constraint()
        tested.get_owned_property_values()
        pass

    def test_Constraint_applied_property_values_getter(self):
        tested = Constraint()
        tested.get_applied_property_values()
        pass

    def test_Constraint_applied_property_values_setter(self):
        tested = Constraint()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_Constraint_owned_property_value_groups_getter(self):
        tested = Constraint()
        tested.get_owned_property_value_groups()
        pass

    def test_Constraint_applied_property_value_groups_getter(self):
        tested = Constraint()
        tested.get_applied_property_value_groups()
        pass

    def test_Constraint_applied_property_value_groups_setter(self):
        tested = Constraint()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_Constraint_owned_enumeration_property_types_getter(self):
        tested = Constraint()
        tested.get_owned_enumeration_property_types()
        pass

    def test_Constraint_owned_diagrams_getter(self):
        tested = Constraint()
        tested.get_owned_diagrams()
        pass

    def test_Constraint_element_of_interest_for_diagrams_getter(self):
        tested = Constraint()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_Constraint_element_of_interest_for_diagrams_setter(self):
        tested = Constraint()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_Constraint_contextual_element_for_diagrams_getter(self):
        tested = Constraint()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_Constraint_contextual_element_for_diagrams_setter(self):
        tested = Constraint()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_Constraint_representing_diagrams_getter(self):
        tested = Constraint()
        tested.get_representing_diagrams()
        pass

    def test_Constraint__r_e_cs_getter(self):
        tested = Constraint()
        tested.get__r_e_cs()
        pass

    def test_Constraint__r_e_cs_setter(self):
        tested = Constraint()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_Constraint__r_p_ls_getter(self):
        tested = Constraint()
        tested.get__r_p_ls()
        pass

    def test_Constraint__r_p_ls_setter(self):
        tested = Constraint()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_Constraint_get_label(self):
        tested = Constraint()
        tested.get_label()
        pass

    def test_Constraint_get_element_type(self):
        tested = Constraint()
        tested.get_element_type()
        pass

    def test_Constraint_get_container(self):
        tested = Constraint()
        tested.get_container()
        pass

    def test_Constraint_get_contents(self):
        tested = Constraint()
        tested.get_contents()
        pass

    def test_Constraint_get_all_contents(self):
        tested = Constraint()
        tested.get_all_contents()
        pass

    def test_Constraint_get_all_contents_by_type(self):
        tested = Constraint()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_Constraint_get_available_s_b_queries(self):
        tested = Constraint()
        tested.get_available_s_b_queries()
        pass

    def test_Constraint_get_query_result(self):
        tested = Constraint()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_Constraint_specification_getter(self):
        tested = Constraint()
        tested.get_specification()
        pass

    def test_Constraint_specification_setter(self):
        tested = Constraint()
        value = "value"
        tested.set_specification(value)
        pass

    def test_Constraint_constrained_elements_getter(self):
        tested = Constraint()
        tested.get_constrained_elements()
        pass

    def test_Constraint_constrained_elements_setter(self):
        tested = Constraint()
        value = RelationType()
        tested.get_constrained_elements().add(value)
        pass

    def test_PropertyValue_id_getter(self):
        tested = PropertyValue()
        tested.get_id()
        pass

    def test_PropertyValue_id_setter(self):
        tested = PropertyValue()
        value = "value"
        tested.set_id(value)
        pass

    def test_PropertyValue_sid_getter(self):
        tested = PropertyValue()
        tested.get_sid()
        pass

    def test_PropertyValue_sid_setter(self):
        tested = PropertyValue()
        value = "value"
        tested.set_sid(value)
        pass

    def test_PropertyValue_name_getter(self):
        tested = PropertyValue()
        tested.get_name()
        pass

    def test_PropertyValue_name_setter(self):
        tested = PropertyValue()
        value = "value"
        tested.set_name(value)
        pass

    def test_PropertyValue_summary_getter(self):
        tested = PropertyValue()
        tested.get_summary()
        pass

    def test_PropertyValue_summary_setter(self):
        tested = PropertyValue()
        value = "value"
        tested.set_summary(value)
        pass

    def test_PropertyValue_description_getter(self):
        tested = PropertyValue()
        tested.get_description()
        pass

    def test_PropertyValue_description_setter(self):
        tested = PropertyValue()
        value = "value"
        tested.set_description(value)
        pass

    def test_PropertyValue_status_getter(self):
        tested = PropertyValue()
        tested.get_status()
        pass

    def test_PropertyValue_status_setter(self):
        tested = PropertyValue()
        value = "value"
        tested.set_status(value)
        pass

    def test_PropertyValue_review_getter(self):
        tested = PropertyValue()
        tested.get_review()
        pass

    def test_PropertyValue_review_setter(self):
        tested = PropertyValue()
        value = "value"
        tested.set_review(value)
        pass

    def test_PropertyValue_visible_in_documentation_getter(self):
        tested = PropertyValue()
        tested.get_visible_in_documentation()
        pass

    def test_PropertyValue_visible_in_documentation_setter(self):
        tested = PropertyValue()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_PropertyValue_visible_for_traceability_getter(self):
        tested = PropertyValue()
        tested.get_visible_for_traceability()
        pass

    def test_PropertyValue_visible_for_traceability_setter(self):
        tested = PropertyValue()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_PropertyValue_owned_constraints_getter(self):
        tested = PropertyValue()
        tested.get_owned_constraints()
        pass

    def test_PropertyValue_constraints_getter(self):
        tested = PropertyValue()
        tested.get_constraints()
        pass

    def test_PropertyValue_constraints_setter(self):
        tested = PropertyValue()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_PropertyValue_owned_property_values_getter(self):
        tested = PropertyValue()
        tested.get_owned_property_values()
        pass

    def test_PropertyValue_applied_property_values_getter(self):
        tested = PropertyValue()
        tested.get_applied_property_values()
        pass

    def test_PropertyValue_applied_property_values_setter(self):
        tested = PropertyValue()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_PropertyValue_owned_property_value_groups_getter(self):
        tested = PropertyValue()
        tested.get_owned_property_value_groups()
        pass

    def test_PropertyValue_applied_property_value_groups_getter(self):
        tested = PropertyValue()
        tested.get_applied_property_value_groups()
        pass

    def test_PropertyValue_applied_property_value_groups_setter(self):
        tested = PropertyValue()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_PropertyValue_owned_enumeration_property_types_getter(self):
        tested = PropertyValue()
        tested.get_owned_enumeration_property_types()
        pass

    def test_PropertyValue_owned_diagrams_getter(self):
        tested = PropertyValue()
        tested.get_owned_diagrams()
        pass

    def test_PropertyValue_element_of_interest_for_diagrams_getter(self):
        tested = PropertyValue()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_PropertyValue_element_of_interest_for_diagrams_setter(self):
        tested = PropertyValue()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_PropertyValue_contextual_element_for_diagrams_getter(self):
        tested = PropertyValue()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_PropertyValue_contextual_element_for_diagrams_setter(self):
        tested = PropertyValue()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_PropertyValue_representing_diagrams_getter(self):
        tested = PropertyValue()
        tested.get_representing_diagrams()
        pass

    def test_PropertyValue__r_e_cs_getter(self):
        tested = PropertyValue()
        tested.get__r_e_cs()
        pass

    def test_PropertyValue__r_e_cs_setter(self):
        tested = PropertyValue()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_PropertyValue__r_p_ls_getter(self):
        tested = PropertyValue()
        tested.get__r_p_ls()
        pass

    def test_PropertyValue__r_p_ls_setter(self):
        tested = PropertyValue()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_PropertyValue_get_label(self):
        tested = PropertyValue()
        tested.get_label()
        pass

    def test_PropertyValue_get_element_type(self):
        tested = PropertyValue()
        tested.get_element_type()
        pass

    def test_PropertyValue_get_container(self):
        tested = PropertyValue()
        tested.get_container()
        pass

    def test_PropertyValue_get_contents(self):
        tested = PropertyValue()
        tested.get_contents()
        pass

    def test_PropertyValue_get_all_contents(self):
        tested = PropertyValue()
        tested.get_all_contents()
        pass

    def test_PropertyValue_get_all_contents_by_type(self):
        tested = PropertyValue()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_PropertyValue_get_available_s_b_queries(self):
        tested = PropertyValue()
        tested.get_available_s_b_queries()
        pass

    def test_PropertyValue_get_query_result(self):
        tested = PropertyValue()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_PropertyValue_kind_getter(self):
        tested = PropertyValue()
        tested.get_kind()
        pass

    def test_PropertyValue_kind_setter(self):
        tested = PropertyValue()
        value = PropertyValueKind()
        tested.set_kind(value)
        pass

    def test_PropertyValue_value_getter(self):
        tested = PropertyValue()
        tested.get_value()
        pass

    def test_PropertyValue_value_setter(self):
        tested = PropertyValue()
        value = "value"
        tested.set_value(value)
        pass

    def test_PropertyValue_valued_elements_getter(self):
        tested = PropertyValue()
        tested.get_valued_elements()
        pass

    def test_PropertyValue_valued_elements_setter(self):
        tested = PropertyValue()
        value = RelationType()
        tested.get_valued_elements().add(value)
        pass

    def test_PropertyValue_type_getter(self):
        tested = PropertyValue()
        tested.get_type()
        pass

    def test_PropertyValueGroup_id_getter(self):
        tested = PropertyValueGroup()
        tested.get_id()
        pass

    def test_PropertyValueGroup_id_setter(self):
        tested = PropertyValueGroup()
        value = "value"
        tested.set_id(value)
        pass

    def test_PropertyValueGroup_sid_getter(self):
        tested = PropertyValueGroup()
        tested.get_sid()
        pass

    def test_PropertyValueGroup_sid_setter(self):
        tested = PropertyValueGroup()
        value = "value"
        tested.set_sid(value)
        pass

    def test_PropertyValueGroup_name_getter(self):
        tested = PropertyValueGroup()
        tested.get_name()
        pass

    def test_PropertyValueGroup_name_setter(self):
        tested = PropertyValueGroup()
        value = "value"
        tested.set_name(value)
        pass

    def test_PropertyValueGroup_summary_getter(self):
        tested = PropertyValueGroup()
        tested.get_summary()
        pass

    def test_PropertyValueGroup_summary_setter(self):
        tested = PropertyValueGroup()
        value = "value"
        tested.set_summary(value)
        pass

    def test_PropertyValueGroup_description_getter(self):
        tested = PropertyValueGroup()
        tested.get_description()
        pass

    def test_PropertyValueGroup_description_setter(self):
        tested = PropertyValueGroup()
        value = "value"
        tested.set_description(value)
        pass

    def test_PropertyValueGroup_status_getter(self):
        tested = PropertyValueGroup()
        tested.get_status()
        pass

    def test_PropertyValueGroup_status_setter(self):
        tested = PropertyValueGroup()
        value = "value"
        tested.set_status(value)
        pass

    def test_PropertyValueGroup_review_getter(self):
        tested = PropertyValueGroup()
        tested.get_review()
        pass

    def test_PropertyValueGroup_review_setter(self):
        tested = PropertyValueGroup()
        value = "value"
        tested.set_review(value)
        pass

    def test_PropertyValueGroup_visible_in_documentation_getter(self):
        tested = PropertyValueGroup()
        tested.get_visible_in_documentation()
        pass

    def test_PropertyValueGroup_visible_in_documentation_setter(self):
        tested = PropertyValueGroup()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_PropertyValueGroup_visible_for_traceability_getter(self):
        tested = PropertyValueGroup()
        tested.get_visible_for_traceability()
        pass

    def test_PropertyValueGroup_visible_for_traceability_setter(self):
        tested = PropertyValueGroup()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_PropertyValueGroup_owned_constraints_getter(self):
        tested = PropertyValueGroup()
        tested.get_owned_constraints()
        pass

    def test_PropertyValueGroup_constraints_getter(self):
        tested = PropertyValueGroup()
        tested.get_constraints()
        pass

    def test_PropertyValueGroup_constraints_setter(self):
        tested = PropertyValueGroup()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_PropertyValueGroup_owned_property_values_getter(self):
        tested = PropertyValueGroup()
        tested.get_owned_property_values()
        pass

    def test_PropertyValueGroup_applied_property_values_getter(self):
        tested = PropertyValueGroup()
        tested.get_applied_property_values()
        pass

    def test_PropertyValueGroup_applied_property_values_setter(self):
        tested = PropertyValueGroup()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_PropertyValueGroup_owned_property_value_groups_getter(self):
        tested = PropertyValueGroup()
        tested.get_owned_property_value_groups()
        pass

    def test_PropertyValueGroup_applied_property_value_groups_getter(self):
        tested = PropertyValueGroup()
        tested.get_applied_property_value_groups()
        pass

    def test_PropertyValueGroup_applied_property_value_groups_setter(self):
        tested = PropertyValueGroup()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_PropertyValueGroup_owned_enumeration_property_types_getter(self):
        tested = PropertyValueGroup()
        tested.get_owned_enumeration_property_types()
        pass

    def test_PropertyValueGroup_owned_diagrams_getter(self):
        tested = PropertyValueGroup()
        tested.get_owned_diagrams()
        pass

    def test_PropertyValueGroup_element_of_interest_for_diagrams_getter(self):
        tested = PropertyValueGroup()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_PropertyValueGroup_element_of_interest_for_diagrams_setter(self):
        tested = PropertyValueGroup()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_PropertyValueGroup_contextual_element_for_diagrams_getter(self):
        tested = PropertyValueGroup()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_PropertyValueGroup_contextual_element_for_diagrams_setter(self):
        tested = PropertyValueGroup()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_PropertyValueGroup_representing_diagrams_getter(self):
        tested = PropertyValueGroup()
        tested.get_representing_diagrams()
        pass

    def test_PropertyValueGroup__r_e_cs_getter(self):
        tested = PropertyValueGroup()
        tested.get__r_e_cs()
        pass

    def test_PropertyValueGroup__r_e_cs_setter(self):
        tested = PropertyValueGroup()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_PropertyValueGroup__r_p_ls_getter(self):
        tested = PropertyValueGroup()
        tested.get__r_p_ls()
        pass

    def test_PropertyValueGroup__r_p_ls_setter(self):
        tested = PropertyValueGroup()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_PropertyValueGroup_get_label(self):
        tested = PropertyValueGroup()
        tested.get_label()
        pass

    def test_PropertyValueGroup_get_element_type(self):
        tested = PropertyValueGroup()
        tested.get_element_type()
        pass

    def test_PropertyValueGroup_get_container(self):
        tested = PropertyValueGroup()
        tested.get_container()
        pass

    def test_PropertyValueGroup_get_contents(self):
        tested = PropertyValueGroup()
        tested.get_contents()
        pass

    def test_PropertyValueGroup_get_all_contents(self):
        tested = PropertyValueGroup()
        tested.get_all_contents()
        pass

    def test_PropertyValueGroup_get_all_contents_by_type(self):
        tested = PropertyValueGroup()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_PropertyValueGroup_get_available_s_b_queries(self):
        tested = PropertyValueGroup()
        tested.get_available_s_b_queries()
        pass

    def test_PropertyValueGroup_get_query_result(self):
        tested = PropertyValueGroup()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_PropertyValueGroup_valued_elements_getter(self):
        tested = PropertyValueGroup()
        tested.get_valued_elements()
        pass

    def test_PropertyValueGroup_valued_elements_setter(self):
        tested = PropertyValueGroup()
        value = RelationType()
        tested.get_valued_elements().add(value)
        pass

    def test_PropertyValuePkg_owned_property_value_pkgs_getter(self):
        tested = PropertyValuePkg()
        tested.get_owned_property_value_pkgs()
        pass

    def test_PropertyValuePkg_id_getter(self):
        tested = PropertyValuePkg()
        tested.get_id()
        pass

    def test_PropertyValuePkg_id_setter(self):
        tested = PropertyValuePkg()
        value = "value"
        tested.set_id(value)
        pass

    def test_PropertyValuePkg_sid_getter(self):
        tested = PropertyValuePkg()
        tested.get_sid()
        pass

    def test_PropertyValuePkg_sid_setter(self):
        tested = PropertyValuePkg()
        value = "value"
        tested.set_sid(value)
        pass

    def test_PropertyValuePkg_name_getter(self):
        tested = PropertyValuePkg()
        tested.get_name()
        pass

    def test_PropertyValuePkg_name_setter(self):
        tested = PropertyValuePkg()
        value = "value"
        tested.set_name(value)
        pass

    def test_PropertyValuePkg_summary_getter(self):
        tested = PropertyValuePkg()
        tested.get_summary()
        pass

    def test_PropertyValuePkg_summary_setter(self):
        tested = PropertyValuePkg()
        value = "value"
        tested.set_summary(value)
        pass

    def test_PropertyValuePkg_description_getter(self):
        tested = PropertyValuePkg()
        tested.get_description()
        pass

    def test_PropertyValuePkg_description_setter(self):
        tested = PropertyValuePkg()
        value = "value"
        tested.set_description(value)
        pass

    def test_PropertyValuePkg_status_getter(self):
        tested = PropertyValuePkg()
        tested.get_status()
        pass

    def test_PropertyValuePkg_status_setter(self):
        tested = PropertyValuePkg()
        value = "value"
        tested.set_status(value)
        pass

    def test_PropertyValuePkg_review_getter(self):
        tested = PropertyValuePkg()
        tested.get_review()
        pass

    def test_PropertyValuePkg_review_setter(self):
        tested = PropertyValuePkg()
        value = "value"
        tested.set_review(value)
        pass

    def test_PropertyValuePkg_visible_in_documentation_getter(self):
        tested = PropertyValuePkg()
        tested.get_visible_in_documentation()
        pass

    def test_PropertyValuePkg_visible_in_documentation_setter(self):
        tested = PropertyValuePkg()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_PropertyValuePkg_visible_for_traceability_getter(self):
        tested = PropertyValuePkg()
        tested.get_visible_for_traceability()
        pass

    def test_PropertyValuePkg_visible_for_traceability_setter(self):
        tested = PropertyValuePkg()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_PropertyValuePkg_owned_constraints_getter(self):
        tested = PropertyValuePkg()
        tested.get_owned_constraints()
        pass

    def test_PropertyValuePkg_constraints_getter(self):
        tested = PropertyValuePkg()
        tested.get_constraints()
        pass

    def test_PropertyValuePkg_constraints_setter(self):
        tested = PropertyValuePkg()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_PropertyValuePkg_owned_property_values_getter(self):
        tested = PropertyValuePkg()
        tested.get_owned_property_values()
        pass

    def test_PropertyValuePkg_applied_property_values_getter(self):
        tested = PropertyValuePkg()
        tested.get_applied_property_values()
        pass

    def test_PropertyValuePkg_applied_property_values_setter(self):
        tested = PropertyValuePkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_PropertyValuePkg_owned_property_value_groups_getter(self):
        tested = PropertyValuePkg()
        tested.get_owned_property_value_groups()
        pass

    def test_PropertyValuePkg_applied_property_value_groups_getter(self):
        tested = PropertyValuePkg()
        tested.get_applied_property_value_groups()
        pass

    def test_PropertyValuePkg_applied_property_value_groups_setter(self):
        tested = PropertyValuePkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_PropertyValuePkg_owned_enumeration_property_types_getter(self):
        tested = PropertyValuePkg()
        tested.get_owned_enumeration_property_types()
        pass

    def test_PropertyValuePkg_owned_diagrams_getter(self):
        tested = PropertyValuePkg()
        tested.get_owned_diagrams()
        pass

    def test_PropertyValuePkg_element_of_interest_for_diagrams_getter(self):
        tested = PropertyValuePkg()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_PropertyValuePkg_element_of_interest_for_diagrams_setter(self):
        tested = PropertyValuePkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_PropertyValuePkg_contextual_element_for_diagrams_getter(self):
        tested = PropertyValuePkg()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_PropertyValuePkg_contextual_element_for_diagrams_setter(self):
        tested = PropertyValuePkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_PropertyValuePkg_representing_diagrams_getter(self):
        tested = PropertyValuePkg()
        tested.get_representing_diagrams()
        pass

    def test_PropertyValuePkg__r_e_cs_getter(self):
        tested = PropertyValuePkg()
        tested.get__r_e_cs()
        pass

    def test_PropertyValuePkg__r_e_cs_setter(self):
        tested = PropertyValuePkg()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_PropertyValuePkg__r_p_ls_getter(self):
        tested = PropertyValuePkg()
        tested.get__r_p_ls()
        pass

    def test_PropertyValuePkg__r_p_ls_setter(self):
        tested = PropertyValuePkg()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_PropertyValuePkg_get_label(self):
        tested = PropertyValuePkg()
        tested.get_label()
        pass

    def test_PropertyValuePkg_get_element_type(self):
        tested = PropertyValuePkg()
        tested.get_element_type()
        pass

    def test_PropertyValuePkg_get_container(self):
        tested = PropertyValuePkg()
        tested.get_container()
        pass

    def test_PropertyValuePkg_get_contents(self):
        tested = PropertyValuePkg()
        tested.get_contents()
        pass

    def test_PropertyValuePkg_get_all_contents(self):
        tested = PropertyValuePkg()
        tested.get_all_contents()
        pass

    def test_PropertyValuePkg_get_all_contents_by_type(self):
        tested = PropertyValuePkg()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_PropertyValuePkg_get_available_s_b_queries(self):
        tested = PropertyValuePkg()
        tested.get_available_s_b_queries()
        pass

    def test_PropertyValuePkg_get_query_result(self):
        tested = PropertyValuePkg()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_EnumerationPropertyType_id_getter(self):
        tested = EnumerationPropertyType()
        tested.get_id()
        pass

    def test_EnumerationPropertyType_id_setter(self):
        tested = EnumerationPropertyType()
        value = "value"
        tested.set_id(value)
        pass

    def test_EnumerationPropertyType_sid_getter(self):
        tested = EnumerationPropertyType()
        tested.get_sid()
        pass

    def test_EnumerationPropertyType_sid_setter(self):
        tested = EnumerationPropertyType()
        value = "value"
        tested.set_sid(value)
        pass

    def test_EnumerationPropertyType_name_getter(self):
        tested = EnumerationPropertyType()
        tested.get_name()
        pass

    def test_EnumerationPropertyType_name_setter(self):
        tested = EnumerationPropertyType()
        value = "value"
        tested.set_name(value)
        pass

    def test_EnumerationPropertyType_summary_getter(self):
        tested = EnumerationPropertyType()
        tested.get_summary()
        pass

    def test_EnumerationPropertyType_summary_setter(self):
        tested = EnumerationPropertyType()
        value = "value"
        tested.set_summary(value)
        pass

    def test_EnumerationPropertyType_description_getter(self):
        tested = EnumerationPropertyType()
        tested.get_description()
        pass

    def test_EnumerationPropertyType_description_setter(self):
        tested = EnumerationPropertyType()
        value = "value"
        tested.set_description(value)
        pass

    def test_EnumerationPropertyType_status_getter(self):
        tested = EnumerationPropertyType()
        tested.get_status()
        pass

    def test_EnumerationPropertyType_status_setter(self):
        tested = EnumerationPropertyType()
        value = "value"
        tested.set_status(value)
        pass

    def test_EnumerationPropertyType_review_getter(self):
        tested = EnumerationPropertyType()
        tested.get_review()
        pass

    def test_EnumerationPropertyType_review_setter(self):
        tested = EnumerationPropertyType()
        value = "value"
        tested.set_review(value)
        pass

    def test_EnumerationPropertyType_visible_in_documentation_getter(self):
        tested = EnumerationPropertyType()
        tested.get_visible_in_documentation()
        pass

    def test_EnumerationPropertyType_visible_in_documentation_setter(self):
        tested = EnumerationPropertyType()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_EnumerationPropertyType_visible_for_traceability_getter(self):
        tested = EnumerationPropertyType()
        tested.get_visible_for_traceability()
        pass

    def test_EnumerationPropertyType_visible_for_traceability_setter(self):
        tested = EnumerationPropertyType()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_EnumerationPropertyType_owned_constraints_getter(self):
        tested = EnumerationPropertyType()
        tested.get_owned_constraints()
        pass

    def test_EnumerationPropertyType_constraints_getter(self):
        tested = EnumerationPropertyType()
        tested.get_constraints()
        pass

    def test_EnumerationPropertyType_constraints_setter(self):
        tested = EnumerationPropertyType()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_EnumerationPropertyType_owned_property_values_getter(self):
        tested = EnumerationPropertyType()
        tested.get_owned_property_values()
        pass

    def test_EnumerationPropertyType_applied_property_values_getter(self):
        tested = EnumerationPropertyType()
        tested.get_applied_property_values()
        pass

    def test_EnumerationPropertyType_applied_property_values_setter(self):
        tested = EnumerationPropertyType()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_EnumerationPropertyType_owned_property_value_groups_getter(self):
        tested = EnumerationPropertyType()
        tested.get_owned_property_value_groups()
        pass

    def test_EnumerationPropertyType_applied_property_value_groups_getter(self):
        tested = EnumerationPropertyType()
        tested.get_applied_property_value_groups()
        pass

    def test_EnumerationPropertyType_applied_property_value_groups_setter(self):
        tested = EnumerationPropertyType()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_EnumerationPropertyType_owned_enumeration_property_types_getter(self):
        tested = EnumerationPropertyType()
        tested.get_owned_enumeration_property_types()
        pass

    def test_EnumerationPropertyType_owned_diagrams_getter(self):
        tested = EnumerationPropertyType()
        tested.get_owned_diagrams()
        pass

    def test_EnumerationPropertyType_element_of_interest_for_diagrams_getter(self):
        tested = EnumerationPropertyType()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_EnumerationPropertyType_element_of_interest_for_diagrams_setter(self):
        tested = EnumerationPropertyType()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_EnumerationPropertyType_contextual_element_for_diagrams_getter(self):
        tested = EnumerationPropertyType()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_EnumerationPropertyType_contextual_element_for_diagrams_setter(self):
        tested = EnumerationPropertyType()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_EnumerationPropertyType_representing_diagrams_getter(self):
        tested = EnumerationPropertyType()
        tested.get_representing_diagrams()
        pass

    def test_EnumerationPropertyType__r_e_cs_getter(self):
        tested = EnumerationPropertyType()
        tested.get__r_e_cs()
        pass

    def test_EnumerationPropertyType__r_e_cs_setter(self):
        tested = EnumerationPropertyType()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_EnumerationPropertyType__r_p_ls_getter(self):
        tested = EnumerationPropertyType()
        tested.get__r_p_ls()
        pass

    def test_EnumerationPropertyType__r_p_ls_setter(self):
        tested = EnumerationPropertyType()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_EnumerationPropertyType_get_label(self):
        tested = EnumerationPropertyType()
        tested.get_label()
        pass

    def test_EnumerationPropertyType_get_element_type(self):
        tested = EnumerationPropertyType()
        tested.get_element_type()
        pass

    def test_EnumerationPropertyType_get_container(self):
        tested = EnumerationPropertyType()
        tested.get_container()
        pass

    def test_EnumerationPropertyType_get_contents(self):
        tested = EnumerationPropertyType()
        tested.get_contents()
        pass

    def test_EnumerationPropertyType_get_all_contents(self):
        tested = EnumerationPropertyType()
        tested.get_all_contents()
        pass

    def test_EnumerationPropertyType_get_all_contents_by_type(self):
        tested = EnumerationPropertyType()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_EnumerationPropertyType_get_available_s_b_queries(self):
        tested = EnumerationPropertyType()
        tested.get_available_s_b_queries()
        pass

    def test_EnumerationPropertyType_get_query_result(self):
        tested = EnumerationPropertyType()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_EnumerationPropertyType_owned_literals_getter(self):
        tested = EnumerationPropertyType()
        tested.get_owned_literals()
        pass

    def test_EnumerationPropertyLiteral_id_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_id()
        pass

    def test_EnumerationPropertyLiteral_id_setter(self):
        tested = EnumerationPropertyLiteral()
        value = "value"
        tested.set_id(value)
        pass

    def test_EnumerationPropertyLiteral_sid_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_sid()
        pass

    def test_EnumerationPropertyLiteral_sid_setter(self):
        tested = EnumerationPropertyLiteral()
        value = "value"
        tested.set_sid(value)
        pass

    def test_EnumerationPropertyLiteral_name_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_name()
        pass

    def test_EnumerationPropertyLiteral_name_setter(self):
        tested = EnumerationPropertyLiteral()
        value = "value"
        tested.set_name(value)
        pass

    def test_EnumerationPropertyLiteral_summary_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_summary()
        pass

    def test_EnumerationPropertyLiteral_summary_setter(self):
        tested = EnumerationPropertyLiteral()
        value = "value"
        tested.set_summary(value)
        pass

    def test_EnumerationPropertyLiteral_description_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_description()
        pass

    def test_EnumerationPropertyLiteral_description_setter(self):
        tested = EnumerationPropertyLiteral()
        value = "value"
        tested.set_description(value)
        pass

    def test_EnumerationPropertyLiteral_status_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_status()
        pass

    def test_EnumerationPropertyLiteral_status_setter(self):
        tested = EnumerationPropertyLiteral()
        value = "value"
        tested.set_status(value)
        pass

    def test_EnumerationPropertyLiteral_review_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_review()
        pass

    def test_EnumerationPropertyLiteral_review_setter(self):
        tested = EnumerationPropertyLiteral()
        value = "value"
        tested.set_review(value)
        pass

    def test_EnumerationPropertyLiteral_visible_in_documentation_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_visible_in_documentation()
        pass

    def test_EnumerationPropertyLiteral_visible_in_documentation_setter(self):
        tested = EnumerationPropertyLiteral()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_EnumerationPropertyLiteral_visible_for_traceability_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_visible_for_traceability()
        pass

    def test_EnumerationPropertyLiteral_visible_for_traceability_setter(self):
        tested = EnumerationPropertyLiteral()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_EnumerationPropertyLiteral_owned_constraints_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_owned_constraints()
        pass

    def test_EnumerationPropertyLiteral_constraints_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_constraints()
        pass

    def test_EnumerationPropertyLiteral_constraints_setter(self):
        tested = EnumerationPropertyLiteral()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_EnumerationPropertyLiteral_owned_property_values_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_owned_property_values()
        pass

    def test_EnumerationPropertyLiteral_applied_property_values_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_applied_property_values()
        pass

    def test_EnumerationPropertyLiteral_applied_property_values_setter(self):
        tested = EnumerationPropertyLiteral()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_EnumerationPropertyLiteral_owned_property_value_groups_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_owned_property_value_groups()
        pass

    def test_EnumerationPropertyLiteral_applied_property_value_groups_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_applied_property_value_groups()
        pass

    def test_EnumerationPropertyLiteral_applied_property_value_groups_setter(self):
        tested = EnumerationPropertyLiteral()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_EnumerationPropertyLiteral_owned_enumeration_property_types_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_owned_enumeration_property_types()
        pass

    def test_EnumerationPropertyLiteral_owned_diagrams_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_owned_diagrams()
        pass

    def test_EnumerationPropertyLiteral_element_of_interest_for_diagrams_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_EnumerationPropertyLiteral_element_of_interest_for_diagrams_setter(self):
        tested = EnumerationPropertyLiteral()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_EnumerationPropertyLiteral_contextual_element_for_diagrams_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_EnumerationPropertyLiteral_contextual_element_for_diagrams_setter(self):
        tested = EnumerationPropertyLiteral()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_EnumerationPropertyLiteral_representing_diagrams_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get_representing_diagrams()
        pass

    def test_EnumerationPropertyLiteral__r_e_cs_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get__r_e_cs()
        pass

    def test_EnumerationPropertyLiteral__r_e_cs_setter(self):
        tested = EnumerationPropertyLiteral()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_EnumerationPropertyLiteral__r_p_ls_getter(self):
        tested = EnumerationPropertyLiteral()
        tested.get__r_p_ls()
        pass

    def test_EnumerationPropertyLiteral__r_p_ls_setter(self):
        tested = EnumerationPropertyLiteral()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_EnumerationPropertyLiteral_get_label(self):
        tested = EnumerationPropertyLiteral()
        tested.get_label()
        pass

    def test_EnumerationPropertyLiteral_get_element_type(self):
        tested = EnumerationPropertyLiteral()
        tested.get_element_type()
        pass

    def test_EnumerationPropertyLiteral_get_container(self):
        tested = EnumerationPropertyLiteral()
        tested.get_container()
        pass

    def test_EnumerationPropertyLiteral_get_contents(self):
        tested = EnumerationPropertyLiteral()
        tested.get_contents()
        pass

    def test_EnumerationPropertyLiteral_get_all_contents(self):
        tested = EnumerationPropertyLiteral()
        tested.get_all_contents()
        pass

    def test_EnumerationPropertyLiteral_get_all_contents_by_type(self):
        tested = EnumerationPropertyLiteral()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_EnumerationPropertyLiteral_get_available_s_b_queries(self):
        tested = EnumerationPropertyLiteral()
        tested.get_available_s_b_queries()
        pass

    def test_EnumerationPropertyLiteral_get_query_result(self):
        tested = EnumerationPropertyLiteral()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_Diagram_uid_getter(self):
        tested = Diagram()
        tested.get_uid()
        pass

    def test_Diagram_uid_setter(self):
        tested = Diagram()
        value = "value"
        tested.set_uid(value)
        pass

    def test_Diagram_name_getter(self):
        tested = Diagram()
        tested.get_name()
        pass

    def test_Diagram_name_setter(self):
        tested = Diagram()
        value = "value"
        tested.set_name(value)
        pass

    def test_Diagram_type_getter(self):
        tested = Diagram()
        tested.get_type()
        pass

    def test_Diagram_type_setter(self):
        tested = Diagram()
        value = "value"
        tested.set_type(value)
        pass

    def test_Diagram_package_getter(self):
        tested = Diagram()
        tested.get_package()
        pass

    def test_Diagram_package_setter(self):
        tested = Diagram()
        value = "value"
        tested.set_package(value)
        pass

    def test_Diagram_description_getter(self):
        tested = Diagram()
        tested.get_description()
        pass

    def test_Diagram_description_setter(self):
        tested = Diagram()
        value = "value"
        tested.set_description(value)
        pass

    def test_Diagram_status_getter(self):
        tested = Diagram()
        tested.get_status()
        pass

    def test_Diagram_status_setter(self):
        tested = Diagram()
        value = "value"
        tested.set_status(value)
        pass

    def test_Diagram_review_getter(self):
        tested = Diagram()
        tested.get_review()
        pass

    def test_Diagram_review_setter(self):
        tested = Diagram()
        value = "value"
        tested.set_review(value)
        pass

    def test_Diagram_visible_in_documentation_getter(self):
        tested = Diagram()
        tested.get_visible_in_documentation()
        pass

    def test_Diagram_visible_in_documentation_setter(self):
        tested = Diagram()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_Diagram_visible_for_traceability_getter(self):
        tested = Diagram()
        tested.get_visible_for_traceability()
        pass

    def test_Diagram_visible_for_traceability_setter(self):
        tested = Diagram()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_Diagram_synchronized_getter(self):
        tested = Diagram()
        tested.get_synchronized()
        pass

    def test_Diagram_synchronized_setter(self):
        tested = Diagram()
        value = True
        tested.set_synchronized(value)
        pass

    def test_Diagram_target_getter(self):
        tested = Diagram()
        tested.get_target()
        pass

    def test_Diagram_represented_elements_getter(self):
        tested = Diagram()
        tested.get_represented_elements()
        pass

    def test_Diagram_contextual_elements_getter(self):
        tested = Diagram()
        tested.get_contextual_elements()
        pass

    def test_Diagram_contextual_elements_setter(self):
        tested = Diagram()
        value = RelationType()
        tested.get_contextual_elements().add(value)
        pass

    def test_Diagram_elements_of_interest_getter(self):
        tested = Diagram()
        tested.get_elements_of_interest()
        pass

    def test_Diagram_elements_of_interest_setter(self):
        tested = Diagram()
        value = RelationType()
        tested.get_elements_of_interest().add(value)
        pass

    def test_Diagram_export_as_image(self):
        tested = Diagram()
        param1 = "value"
        param2 = ExportFormat()
        tested.export_as_image(param1, param2)
        pass

    def test_REC_decription_getter(self):
        tested = REC()
        tested.get_decription()
        pass

    def test_REC_decription_setter(self):
        tested = REC()
        value = "value"
        tested.set_decription(value)
        pass

    def test_REC_author_getter(self):
        tested = REC()
        tested.get_author()
        pass

    def test_REC_author_setter(self):
        tested = REC()
        value = "value"
        tested.set_author(value)
        pass

    def test_REC_environment_getter(self):
        tested = REC()
        tested.get_environment()
        pass

    def test_REC_environment_setter(self):
        tested = REC()
        value = "value"
        tested.set_environment(value)
        pass

    def test_REC_tags_getter(self):
        tested = REC()
        tested.get_tags()
        pass

    def test_REC_tags_setter(self):
        tested = REC()
        value = "value"
        tested.set_tags(value)
        pass

    def test_REC_id_getter(self):
        tested = REC()
        tested.get_id()
        pass

    def test_REC_id_setter(self):
        tested = REC()
        value = "value"
        tested.set_id(value)
        pass

    def test_REC_name_getter(self):
        tested = REC()
        tested.get_name()
        pass

    def test_REC_name_setter(self):
        tested = REC()
        value = "value"
        tested.set_name(value)
        pass

    def test_REC_owned_diagrams_getter(self):
        tested = REC()
        tested.get_owned_diagrams()
        pass

    def test_REC_element_of_interest_for_diagrams_getter(self):
        tested = REC()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_REC_element_of_interest_for_diagrams_setter(self):
        tested = REC()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_REC_contextual_element_for_diagrams_getter(self):
        tested = REC()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_REC_contextual_element_for_diagrams_setter(self):
        tested = REC()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_REC_representing_diagrams_getter(self):
        tested = REC()
        tested.get_representing_diagrams()
        pass

    def test_REC__r_e_cs_getter(self):
        tested = REC()
        tested.get__r_e_cs()
        pass

    def test_REC__r_e_cs_setter(self):
        tested = REC()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_REC__r_p_ls_getter(self):
        tested = REC()
        tested.get__r_p_ls()
        pass

    def test_REC__r_p_ls_setter(self):
        tested = REC()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_REC_get_label(self):
        tested = REC()
        tested.get_label()
        pass

    def test_REC_get_element_type(self):
        tested = REC()
        tested.get_element_type()
        pass

    def test_REC_get_container(self):
        tested = REC()
        tested.get_container()
        pass

    def test_REC_get_contents(self):
        tested = REC()
        tested.get_contents()
        pass

    def test_REC_get_all_contents(self):
        tested = REC()
        tested.get_all_contents()
        pass

    def test_REC_get_all_contents_by_type(self):
        tested = REC()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_REC_get_available_s_b_queries(self):
        tested = REC()
        tested.get_available_s_b_queries()
        pass

    def test_REC_get_query_result(self):
        tested = REC()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_REC_referenced_elements_getter(self):
        tested = REC()
        tested.get_referenced_elements()
        pass

    def test_REC_referenced_elements_setter(self):
        tested = REC()
        value = RelationType()
        tested.get_referenced_elements().add(value)
        pass

    def test_REC_default_replica_compliancy_getter(self):
        tested = REC()
        tested.get_default_replica_compliancy()
        pass

    def test_REC_default_replica_compliancy_setter(self):
        tested = REC()
        value = CompliancyDefinition()
        tested.set_default_replica_compliancy(value)
        pass

    def test_REC_replicated_elements_getter(self):
        tested = REC()
        tested.get_replicated_elements()
        pass

    def test_REC_replicated_elements_setter(self):
        tested = REC()
        value = RPL()
        tested.get_replicated_elements().add(value)
        pass

    def test_RPL_decription_getter(self):
        tested = RPL()
        tested.get_decription()
        pass

    def test_RPL_decription_setter(self):
        tested = RPL()
        value = "value"
        tested.set_decription(value)
        pass

    def test_RPL_author_getter(self):
        tested = RPL()
        tested.get_author()
        pass

    def test_RPL_author_setter(self):
        tested = RPL()
        value = "value"
        tested.set_author(value)
        pass

    def test_RPL_environment_getter(self):
        tested = RPL()
        tested.get_environment()
        pass

    def test_RPL_environment_setter(self):
        tested = RPL()
        value = "value"
        tested.set_environment(value)
        pass

    def test_RPL_tags_getter(self):
        tested = RPL()
        tested.get_tags()
        pass

    def test_RPL_tags_setter(self):
        tested = RPL()
        value = "value"
        tested.set_tags(value)
        pass

    def test_RPL_id_getter(self):
        tested = RPL()
        tested.get_id()
        pass

    def test_RPL_id_setter(self):
        tested = RPL()
        value = "value"
        tested.set_id(value)
        pass

    def test_RPL_name_getter(self):
        tested = RPL()
        tested.get_name()
        pass

    def test_RPL_name_setter(self):
        tested = RPL()
        value = "value"
        tested.set_name(value)
        pass

    def test_RPL_owned_diagrams_getter(self):
        tested = RPL()
        tested.get_owned_diagrams()
        pass

    def test_RPL_element_of_interest_for_diagrams_getter(self):
        tested = RPL()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_RPL_element_of_interest_for_diagrams_setter(self):
        tested = RPL()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_RPL_contextual_element_for_diagrams_getter(self):
        tested = RPL()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_RPL_contextual_element_for_diagrams_setter(self):
        tested = RPL()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_RPL_representing_diagrams_getter(self):
        tested = RPL()
        tested.get_representing_diagrams()
        pass

    def test_RPL__r_e_cs_getter(self):
        tested = RPL()
        tested.get__r_e_cs()
        pass

    def test_RPL__r_e_cs_setter(self):
        tested = RPL()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_RPL__r_p_ls_getter(self):
        tested = RPL()
        tested.get__r_p_ls()
        pass

    def test_RPL__r_p_ls_setter(self):
        tested = RPL()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_RPL_get_label(self):
        tested = RPL()
        tested.get_label()
        pass

    def test_RPL_get_element_type(self):
        tested = RPL()
        tested.get_element_type()
        pass

    def test_RPL_get_container(self):
        tested = RPL()
        tested.get_container()
        pass

    def test_RPL_get_contents(self):
        tested = RPL()
        tested.get_contents()
        pass

    def test_RPL_get_all_contents(self):
        tested = RPL()
        tested.get_all_contents()
        pass

    def test_RPL_get_all_contents_by_type(self):
        tested = RPL()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_RPL_get_available_s_b_queries(self):
        tested = RPL()
        tested.get_available_s_b_queries()
        pass

    def test_RPL_get_query_result(self):
        tested = RPL()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_RPL_referenced_elements_getter(self):
        tested = RPL()
        tested.get_referenced_elements()
        pass

    def test_RPL_referenced_elements_setter(self):
        tested = RPL()
        value = RelationType()
        tested.get_referenced_elements().add(value)
        pass

    def test_RPL_suffix_getter(self):
        tested = RPL()
        tested.get_suffix()
        pass

    def test_RPL_suffix_setter(self):
        tested = RPL()
        value = "value"
        tested.set_suffix(value)
        pass

    def test_RPL_read_only_getter(self):
        tested = RPL()
        tested.get_read_only()
        pass

    def test_RPL_read_only_setter(self):
        tested = RPL()
        value = True
        tested.set_read_only(value)
        pass

    def test_RPL_origin_getter(self):
        tested = RPL()
        tested.get_origin()
        pass

    def test_RPL_origin_setter(self):
        tested = RPL()
        value = REC()
        tested.set_origin(value)
        pass

    def test_RPL_current_compliancy_getter(self):
        tested = RPL()
        tested.get_current_compliancy()
        pass

    def test_RPL_current_compliancy_setter(self):
        tested = RPL()
        value = CompliancyDefinition()
        tested.set_current_compliancy(value)
        pass

    def test_CatalogElementPkg_id_getter(self):
        tested = CatalogElementPkg()
        tested.get_id()
        pass

    def test_CatalogElementPkg_id_setter(self):
        tested = CatalogElementPkg()
        value = "value"
        tested.set_id(value)
        pass

    def test_CatalogElementPkg_name_getter(self):
        tested = CatalogElementPkg()
        tested.get_name()
        pass

    def test_CatalogElementPkg_name_setter(self):
        tested = CatalogElementPkg()
        value = "value"
        tested.set_name(value)
        pass

    def test_CatalogElementPkg_owned_diagrams_getter(self):
        tested = CatalogElementPkg()
        tested.get_owned_diagrams()
        pass

    def test_CatalogElementPkg_element_of_interest_for_diagrams_getter(self):
        tested = CatalogElementPkg()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_CatalogElementPkg_element_of_interest_for_diagrams_setter(self):
        tested = CatalogElementPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_CatalogElementPkg_contextual_element_for_diagrams_getter(self):
        tested = CatalogElementPkg()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_CatalogElementPkg_contextual_element_for_diagrams_setter(self):
        tested = CatalogElementPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_CatalogElementPkg_representing_diagrams_getter(self):
        tested = CatalogElementPkg()
        tested.get_representing_diagrams()
        pass

    def test_CatalogElementPkg__r_e_cs_getter(self):
        tested = CatalogElementPkg()
        tested.get__r_e_cs()
        pass

    def test_CatalogElementPkg__r_e_cs_setter(self):
        tested = CatalogElementPkg()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_CatalogElementPkg__r_p_ls_getter(self):
        tested = CatalogElementPkg()
        tested.get__r_p_ls()
        pass

    def test_CatalogElementPkg__r_p_ls_setter(self):
        tested = CatalogElementPkg()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_CatalogElementPkg_get_label(self):
        tested = CatalogElementPkg()
        tested.get_label()
        pass

    def test_CatalogElementPkg_get_element_type(self):
        tested = CatalogElementPkg()
        tested.get_element_type()
        pass

    def test_CatalogElementPkg_get_container(self):
        tested = CatalogElementPkg()
        tested.get_container()
        pass

    def test_CatalogElementPkg_get_contents(self):
        tested = CatalogElementPkg()
        tested.get_contents()
        pass

    def test_CatalogElementPkg_get_all_contents(self):
        tested = CatalogElementPkg()
        tested.get_all_contents()
        pass

    def test_CatalogElementPkg_get_all_contents_by_type(self):
        tested = CatalogElementPkg()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_CatalogElementPkg_get_available_s_b_queries(self):
        tested = CatalogElementPkg()
        tested.get_available_s_b_queries()
        pass

    def test_CatalogElementPkg_get_query_result(self):
        tested = CatalogElementPkg()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_CatalogElementPkg_owned_element_pkgs_getter(self):
        tested = CatalogElementPkg()
        tested.get_owned_element_pkgs()
        pass

    def test_CatalogElementPkg_owned_recs_getter(self):
        tested = CatalogElementPkg()
        tested.get_owned_recs()
        pass

    def test_CatalogElementPkg_owned_rpls_getter(self):
        tested = CatalogElementPkg()
        tested.get_owned_rpls()
        pass

    def test_RecCatalog_owned_element_pkgs_getter(self):
        tested = RecCatalog()
        tested.get_owned_element_pkgs()
        pass

    def test_RecCatalog_owned_recs_getter(self):
        tested = RecCatalog()
        tested.get_owned_recs()
        pass

    def test_RecCatalog_owned_rpls_getter(self):
        tested = RecCatalog()
        tested.get_owned_rpls()
        pass

    def test_RecCatalog_id_getter(self):
        tested = RecCatalog()
        tested.get_id()
        pass

    def test_RecCatalog_id_setter(self):
        tested = RecCatalog()
        value = "value"
        tested.set_id(value)
        pass

    def test_RecCatalog_name_getter(self):
        tested = RecCatalog()
        tested.get_name()
        pass

    def test_RecCatalog_name_setter(self):
        tested = RecCatalog()
        value = "value"
        tested.set_name(value)
        pass

    def test_RecCatalog_owned_diagrams_getter(self):
        tested = RecCatalog()
        tested.get_owned_diagrams()
        pass

    def test_RecCatalog_element_of_interest_for_diagrams_getter(self):
        tested = RecCatalog()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_RecCatalog_element_of_interest_for_diagrams_setter(self):
        tested = RecCatalog()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_RecCatalog_contextual_element_for_diagrams_getter(self):
        tested = RecCatalog()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_RecCatalog_contextual_element_for_diagrams_setter(self):
        tested = RecCatalog()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_RecCatalog_representing_diagrams_getter(self):
        tested = RecCatalog()
        tested.get_representing_diagrams()
        pass

    def test_RecCatalog__r_e_cs_getter(self):
        tested = RecCatalog()
        tested.get__r_e_cs()
        pass

    def test_RecCatalog__r_e_cs_setter(self):
        tested = RecCatalog()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_RecCatalog__r_p_ls_getter(self):
        tested = RecCatalog()
        tested.get__r_p_ls()
        pass

    def test_RecCatalog__r_p_ls_setter(self):
        tested = RecCatalog()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_RecCatalog_get_label(self):
        tested = RecCatalog()
        tested.get_label()
        pass

    def test_RecCatalog_get_element_type(self):
        tested = RecCatalog()
        tested.get_element_type()
        pass

    def test_RecCatalog_get_container(self):
        tested = RecCatalog()
        tested.get_container()
        pass

    def test_RecCatalog_get_contents(self):
        tested = RecCatalog()
        tested.get_contents()
        pass

    def test_RecCatalog_get_all_contents(self):
        tested = RecCatalog()
        tested.get_all_contents()
        pass

    def test_RecCatalog_get_all_contents_by_type(self):
        tested = RecCatalog()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_RecCatalog_get_available_s_b_queries(self):
        tested = RecCatalog()
        tested.get_available_s_b_queries()
        pass

    def test_RecCatalog_get_query_result(self):
        tested = RecCatalog()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_RecCatalog_owned_compliancy_definition_pkg_getter(self):
        tested = RecCatalog()
        tested.get_owned_compliancy_definition_pkg()
        pass

    def test_CompliancyDefinitionPkg_id_getter(self):
        tested = CompliancyDefinitionPkg()
        tested.get_id()
        pass

    def test_CompliancyDefinitionPkg_id_setter(self):
        tested = CompliancyDefinitionPkg()
        value = "value"
        tested.set_id(value)
        pass

    def test_CompliancyDefinitionPkg_name_getter(self):
        tested = CompliancyDefinitionPkg()
        tested.get_name()
        pass

    def test_CompliancyDefinitionPkg_name_setter(self):
        tested = CompliancyDefinitionPkg()
        value = "value"
        tested.set_name(value)
        pass

    def test_CompliancyDefinitionPkg_owned_diagrams_getter(self):
        tested = CompliancyDefinitionPkg()
        tested.get_owned_diagrams()
        pass

    def test_CompliancyDefinitionPkg_element_of_interest_for_diagrams_getter(self):
        tested = CompliancyDefinitionPkg()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_CompliancyDefinitionPkg_element_of_interest_for_diagrams_setter(self):
        tested = CompliancyDefinitionPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_CompliancyDefinitionPkg_contextual_element_for_diagrams_getter(self):
        tested = CompliancyDefinitionPkg()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_CompliancyDefinitionPkg_contextual_element_for_diagrams_setter(self):
        tested = CompliancyDefinitionPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_CompliancyDefinitionPkg_representing_diagrams_getter(self):
        tested = CompliancyDefinitionPkg()
        tested.get_representing_diagrams()
        pass

    def test_CompliancyDefinitionPkg__r_e_cs_getter(self):
        tested = CompliancyDefinitionPkg()
        tested.get__r_e_cs()
        pass

    def test_CompliancyDefinitionPkg__r_e_cs_setter(self):
        tested = CompliancyDefinitionPkg()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_CompliancyDefinitionPkg__r_p_ls_getter(self):
        tested = CompliancyDefinitionPkg()
        tested.get__r_p_ls()
        pass

    def test_CompliancyDefinitionPkg__r_p_ls_setter(self):
        tested = CompliancyDefinitionPkg()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_CompliancyDefinitionPkg_get_label(self):
        tested = CompliancyDefinitionPkg()
        tested.get_label()
        pass

    def test_CompliancyDefinitionPkg_get_element_type(self):
        tested = CompliancyDefinitionPkg()
        tested.get_element_type()
        pass

    def test_CompliancyDefinitionPkg_get_container(self):
        tested = CompliancyDefinitionPkg()
        tested.get_container()
        pass

    def test_CompliancyDefinitionPkg_get_contents(self):
        tested = CompliancyDefinitionPkg()
        tested.get_contents()
        pass

    def test_CompliancyDefinitionPkg_get_all_contents(self):
        tested = CompliancyDefinitionPkg()
        tested.get_all_contents()
        pass

    def test_CompliancyDefinitionPkg_get_all_contents_by_type(self):
        tested = CompliancyDefinitionPkg()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_CompliancyDefinitionPkg_get_available_s_b_queries(self):
        tested = CompliancyDefinitionPkg()
        tested.get_available_s_b_queries()
        pass

    def test_CompliancyDefinitionPkg_get_query_result(self):
        tested = CompliancyDefinitionPkg()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_CompliancyDefinitionPkg_owned_definitions_getter(self):
        tested = CompliancyDefinitionPkg()
        tested.get_owned_definitions()
        pass

    def test_CompliancyDefinition_id_getter(self):
        tested = CompliancyDefinition()
        tested.get_id()
        pass

    def test_CompliancyDefinition_id_setter(self):
        tested = CompliancyDefinition()
        value = "value"
        tested.set_id(value)
        pass

    def test_CompliancyDefinition_name_getter(self):
        tested = CompliancyDefinition()
        tested.get_name()
        pass

    def test_CompliancyDefinition_name_setter(self):
        tested = CompliancyDefinition()
        value = "value"
        tested.set_name(value)
        pass

    def test_CompliancyDefinition_owned_diagrams_getter(self):
        tested = CompliancyDefinition()
        tested.get_owned_diagrams()
        pass

    def test_CompliancyDefinition_element_of_interest_for_diagrams_getter(self):
        tested = CompliancyDefinition()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_CompliancyDefinition_element_of_interest_for_diagrams_setter(self):
        tested = CompliancyDefinition()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_CompliancyDefinition_contextual_element_for_diagrams_getter(self):
        tested = CompliancyDefinition()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_CompliancyDefinition_contextual_element_for_diagrams_setter(self):
        tested = CompliancyDefinition()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_CompliancyDefinition_representing_diagrams_getter(self):
        tested = CompliancyDefinition()
        tested.get_representing_diagrams()
        pass

    def test_CompliancyDefinition__r_e_cs_getter(self):
        tested = CompliancyDefinition()
        tested.get__r_e_cs()
        pass

    def test_CompliancyDefinition__r_e_cs_setter(self):
        tested = CompliancyDefinition()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_CompliancyDefinition__r_p_ls_getter(self):
        tested = CompliancyDefinition()
        tested.get__r_p_ls()
        pass

    def test_CompliancyDefinition__r_p_ls_setter(self):
        tested = CompliancyDefinition()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_CompliancyDefinition_get_label(self):
        tested = CompliancyDefinition()
        tested.get_label()
        pass

    def test_CompliancyDefinition_get_element_type(self):
        tested = CompliancyDefinition()
        tested.get_element_type()
        pass

    def test_CompliancyDefinition_get_container(self):
        tested = CompliancyDefinition()
        tested.get_container()
        pass

    def test_CompliancyDefinition_get_contents(self):
        tested = CompliancyDefinition()
        tested.get_contents()
        pass

    def test_CompliancyDefinition_get_all_contents(self):
        tested = CompliancyDefinition()
        tested.get_all_contents()
        pass

    def test_CompliancyDefinition_get_all_contents_by_type(self):
        tested = CompliancyDefinition()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_CompliancyDefinition_get_available_s_b_queries(self):
        tested = CompliancyDefinition()
        tested.get_available_s_b_queries()
        pass

    def test_CompliancyDefinition_get_query_result(self):
        tested = CompliancyDefinition()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_CompliancyDefinition_description_getter(self):
        tested = CompliancyDefinition()
        tested.get_description()
        pass

    def test_CompliancyDefinition_description_setter(self):
        tested = CompliancyDefinition()
        value = "value"
        tested.set_description(value)
        pass

    def test_OperationalAnalysis_owned_property_value_pkgs_getter(self):
        tested = OperationalAnalysis()
        tested.get_owned_property_value_pkgs()
        pass

    def test_OperationalAnalysis_id_getter(self):
        tested = OperationalAnalysis()
        tested.get_id()
        pass

    def test_OperationalAnalysis_id_setter(self):
        tested = OperationalAnalysis()
        value = "value"
        tested.set_id(value)
        pass

    def test_OperationalAnalysis_sid_getter(self):
        tested = OperationalAnalysis()
        tested.get_sid()
        pass

    def test_OperationalAnalysis_sid_setter(self):
        tested = OperationalAnalysis()
        value = "value"
        tested.set_sid(value)
        pass

    def test_OperationalAnalysis_name_getter(self):
        tested = OperationalAnalysis()
        tested.get_name()
        pass

    def test_OperationalAnalysis_name_setter(self):
        tested = OperationalAnalysis()
        value = "value"
        tested.set_name(value)
        pass

    def test_OperationalAnalysis_summary_getter(self):
        tested = OperationalAnalysis()
        tested.get_summary()
        pass

    def test_OperationalAnalysis_summary_setter(self):
        tested = OperationalAnalysis()
        value = "value"
        tested.set_summary(value)
        pass

    def test_OperationalAnalysis_description_getter(self):
        tested = OperationalAnalysis()
        tested.get_description()
        pass

    def test_OperationalAnalysis_description_setter(self):
        tested = OperationalAnalysis()
        value = "value"
        tested.set_description(value)
        pass

    def test_OperationalAnalysis_status_getter(self):
        tested = OperationalAnalysis()
        tested.get_status()
        pass

    def test_OperationalAnalysis_status_setter(self):
        tested = OperationalAnalysis()
        value = "value"
        tested.set_status(value)
        pass

    def test_OperationalAnalysis_review_getter(self):
        tested = OperationalAnalysis()
        tested.get_review()
        pass

    def test_OperationalAnalysis_review_setter(self):
        tested = OperationalAnalysis()
        value = "value"
        tested.set_review(value)
        pass

    def test_OperationalAnalysis_visible_in_documentation_getter(self):
        tested = OperationalAnalysis()
        tested.get_visible_in_documentation()
        pass

    def test_OperationalAnalysis_visible_in_documentation_setter(self):
        tested = OperationalAnalysis()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_OperationalAnalysis_visible_for_traceability_getter(self):
        tested = OperationalAnalysis()
        tested.get_visible_for_traceability()
        pass

    def test_OperationalAnalysis_visible_for_traceability_setter(self):
        tested = OperationalAnalysis()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_OperationalAnalysis_owned_constraints_getter(self):
        tested = OperationalAnalysis()
        tested.get_owned_constraints()
        pass

    def test_OperationalAnalysis_constraints_getter(self):
        tested = OperationalAnalysis()
        tested.get_constraints()
        pass

    def test_OperationalAnalysis_constraints_setter(self):
        tested = OperationalAnalysis()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_OperationalAnalysis_owned_property_values_getter(self):
        tested = OperationalAnalysis()
        tested.get_owned_property_values()
        pass

    def test_OperationalAnalysis_applied_property_values_getter(self):
        tested = OperationalAnalysis()
        tested.get_applied_property_values()
        pass

    def test_OperationalAnalysis_applied_property_values_setter(self):
        tested = OperationalAnalysis()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_OperationalAnalysis_owned_property_value_groups_getter(self):
        tested = OperationalAnalysis()
        tested.get_owned_property_value_groups()
        pass

    def test_OperationalAnalysis_applied_property_value_groups_getter(self):
        tested = OperationalAnalysis()
        tested.get_applied_property_value_groups()
        pass

    def test_OperationalAnalysis_applied_property_value_groups_setter(self):
        tested = OperationalAnalysis()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_OperationalAnalysis_owned_enumeration_property_types_getter(self):
        tested = OperationalAnalysis()
        tested.get_owned_enumeration_property_types()
        pass

    def test_OperationalAnalysis_owned_diagrams_getter(self):
        tested = OperationalAnalysis()
        tested.get_owned_diagrams()
        pass

    def test_OperationalAnalysis_element_of_interest_for_diagrams_getter(self):
        tested = OperationalAnalysis()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_OperationalAnalysis_element_of_interest_for_diagrams_setter(self):
        tested = OperationalAnalysis()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_OperationalAnalysis_contextual_element_for_diagrams_getter(self):
        tested = OperationalAnalysis()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_OperationalAnalysis_contextual_element_for_diagrams_setter(self):
        tested = OperationalAnalysis()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_OperationalAnalysis_representing_diagrams_getter(self):
        tested = OperationalAnalysis()
        tested.get_representing_diagrams()
        pass

    def test_OperationalAnalysis__r_e_cs_getter(self):
        tested = OperationalAnalysis()
        tested.get__r_e_cs()
        pass

    def test_OperationalAnalysis__r_e_cs_setter(self):
        tested = OperationalAnalysis()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_OperationalAnalysis__r_p_ls_getter(self):
        tested = OperationalAnalysis()
        tested.get__r_p_ls()
        pass

    def test_OperationalAnalysis__r_p_ls_setter(self):
        tested = OperationalAnalysis()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_OperationalAnalysis_get_label(self):
        tested = OperationalAnalysis()
        tested.get_label()
        pass

    def test_OperationalAnalysis_get_element_type(self):
        tested = OperationalAnalysis()
        tested.get_element_type()
        pass

    def test_OperationalAnalysis_get_container(self):
        tested = OperationalAnalysis()
        tested.get_container()
        pass

    def test_OperationalAnalysis_get_contents(self):
        tested = OperationalAnalysis()
        tested.get_contents()
        pass

    def test_OperationalAnalysis_get_all_contents(self):
        tested = OperationalAnalysis()
        tested.get_all_contents()
        pass

    def test_OperationalAnalysis_get_all_contents_by_type(self):
        tested = OperationalAnalysis()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_OperationalAnalysis_get_available_s_b_queries(self):
        tested = OperationalAnalysis()
        tested.get_available_s_b_queries()
        pass

    def test_OperationalAnalysis_get_query_result(self):
        tested = OperationalAnalysis()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_OperationalAnalysis_operational_activity_pkg_getter(self):
        tested = OperationalAnalysis()
        tested.get_operational_activity_pkg()
        pass

    def test_OperationalAnalysis_operational_capability_pkg_getter(self):
        tested = OperationalAnalysis()
        tested.get_operational_capability_pkg()
        pass

    def test_OperationalAnalysis_interface_pkg_getter(self):
        tested = OperationalAnalysis()
        tested.get_interface_pkg()
        pass

    def test_OperationalAnalysis_data_pkg_getter(self):
        tested = OperationalAnalysis()
        tested.get_data_pkg()
        pass

    def test_OperationalAnalysis_entity_pkg_getter(self):
        tested = OperationalAnalysis()
        tested.get_entity_pkg()
        pass

    def test_OperationalActivityPkg_owned_property_value_pkgs_getter(self):
        tested = OperationalActivityPkg()
        tested.get_owned_property_value_pkgs()
        pass

    def test_OperationalActivityPkg_id_getter(self):
        tested = OperationalActivityPkg()
        tested.get_id()
        pass

    def test_OperationalActivityPkg_id_setter(self):
        tested = OperationalActivityPkg()
        value = "value"
        tested.set_id(value)
        pass

    def test_OperationalActivityPkg_sid_getter(self):
        tested = OperationalActivityPkg()
        tested.get_sid()
        pass

    def test_OperationalActivityPkg_sid_setter(self):
        tested = OperationalActivityPkg()
        value = "value"
        tested.set_sid(value)
        pass

    def test_OperationalActivityPkg_name_getter(self):
        tested = OperationalActivityPkg()
        tested.get_name()
        pass

    def test_OperationalActivityPkg_name_setter(self):
        tested = OperationalActivityPkg()
        value = "value"
        tested.set_name(value)
        pass

    def test_OperationalActivityPkg_summary_getter(self):
        tested = OperationalActivityPkg()
        tested.get_summary()
        pass

    def test_OperationalActivityPkg_summary_setter(self):
        tested = OperationalActivityPkg()
        value = "value"
        tested.set_summary(value)
        pass

    def test_OperationalActivityPkg_description_getter(self):
        tested = OperationalActivityPkg()
        tested.get_description()
        pass

    def test_OperationalActivityPkg_description_setter(self):
        tested = OperationalActivityPkg()
        value = "value"
        tested.set_description(value)
        pass

    def test_OperationalActivityPkg_status_getter(self):
        tested = OperationalActivityPkg()
        tested.get_status()
        pass

    def test_OperationalActivityPkg_status_setter(self):
        tested = OperationalActivityPkg()
        value = "value"
        tested.set_status(value)
        pass

    def test_OperationalActivityPkg_review_getter(self):
        tested = OperationalActivityPkg()
        tested.get_review()
        pass

    def test_OperationalActivityPkg_review_setter(self):
        tested = OperationalActivityPkg()
        value = "value"
        tested.set_review(value)
        pass

    def test_OperationalActivityPkg_visible_in_documentation_getter(self):
        tested = OperationalActivityPkg()
        tested.get_visible_in_documentation()
        pass

    def test_OperationalActivityPkg_visible_in_documentation_setter(self):
        tested = OperationalActivityPkg()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_OperationalActivityPkg_visible_for_traceability_getter(self):
        tested = OperationalActivityPkg()
        tested.get_visible_for_traceability()
        pass

    def test_OperationalActivityPkg_visible_for_traceability_setter(self):
        tested = OperationalActivityPkg()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_OperationalActivityPkg_owned_constraints_getter(self):
        tested = OperationalActivityPkg()
        tested.get_owned_constraints()
        pass

    def test_OperationalActivityPkg_constraints_getter(self):
        tested = OperationalActivityPkg()
        tested.get_constraints()
        pass

    def test_OperationalActivityPkg_constraints_setter(self):
        tested = OperationalActivityPkg()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_OperationalActivityPkg_owned_property_values_getter(self):
        tested = OperationalActivityPkg()
        tested.get_owned_property_values()
        pass

    def test_OperationalActivityPkg_applied_property_values_getter(self):
        tested = OperationalActivityPkg()
        tested.get_applied_property_values()
        pass

    def test_OperationalActivityPkg_applied_property_values_setter(self):
        tested = OperationalActivityPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_OperationalActivityPkg_owned_property_value_groups_getter(self):
        tested = OperationalActivityPkg()
        tested.get_owned_property_value_groups()
        pass

    def test_OperationalActivityPkg_applied_property_value_groups_getter(self):
        tested = OperationalActivityPkg()
        tested.get_applied_property_value_groups()
        pass

    def test_OperationalActivityPkg_applied_property_value_groups_setter(self):
        tested = OperationalActivityPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_OperationalActivityPkg_owned_enumeration_property_types_getter(self):
        tested = OperationalActivityPkg()
        tested.get_owned_enumeration_property_types()
        pass

    def test_OperationalActivityPkg_owned_diagrams_getter(self):
        tested = OperationalActivityPkg()
        tested.get_owned_diagrams()
        pass

    def test_OperationalActivityPkg_element_of_interest_for_diagrams_getter(self):
        tested = OperationalActivityPkg()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_OperationalActivityPkg_element_of_interest_for_diagrams_setter(self):
        tested = OperationalActivityPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_OperationalActivityPkg_contextual_element_for_diagrams_getter(self):
        tested = OperationalActivityPkg()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_OperationalActivityPkg_contextual_element_for_diagrams_setter(self):
        tested = OperationalActivityPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_OperationalActivityPkg_representing_diagrams_getter(self):
        tested = OperationalActivityPkg()
        tested.get_representing_diagrams()
        pass

    def test_OperationalActivityPkg__r_e_cs_getter(self):
        tested = OperationalActivityPkg()
        tested.get__r_e_cs()
        pass

    def test_OperationalActivityPkg__r_e_cs_setter(self):
        tested = OperationalActivityPkg()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_OperationalActivityPkg__r_p_ls_getter(self):
        tested = OperationalActivityPkg()
        tested.get__r_p_ls()
        pass

    def test_OperationalActivityPkg__r_p_ls_setter(self):
        tested = OperationalActivityPkg()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_OperationalActivityPkg_get_label(self):
        tested = OperationalActivityPkg()
        tested.get_label()
        pass

    def test_OperationalActivityPkg_get_element_type(self):
        tested = OperationalActivityPkg()
        tested.get_element_type()
        pass

    def test_OperationalActivityPkg_get_container(self):
        tested = OperationalActivityPkg()
        tested.get_container()
        pass

    def test_OperationalActivityPkg_get_contents(self):
        tested = OperationalActivityPkg()
        tested.get_contents()
        pass

    def test_OperationalActivityPkg_get_all_contents(self):
        tested = OperationalActivityPkg()
        tested.get_all_contents()
        pass

    def test_OperationalActivityPkg_get_all_contents_by_type(self):
        tested = OperationalActivityPkg()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_OperationalActivityPkg_get_available_s_b_queries(self):
        tested = OperationalActivityPkg()
        tested.get_available_s_b_queries()
        pass

    def test_OperationalActivityPkg_get_query_result(self):
        tested = OperationalActivityPkg()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_OperationalActivityPkg_owned_operational_activity_pkgs_getter(self):
        tested = OperationalActivityPkg()
        tested.get_owned_operational_activity_pkgs()
        pass

    def test_OperationalActivityPkg_owned_operational_activities_getter(self):
        tested = OperationalActivityPkg()
        tested.get_owned_operational_activities()
        pass

    def test_OperationalActivity_available_in_states_getter(self):
        tested = OperationalActivity()
        tested.get_available_in_states()
        pass

    def test_OperationalActivity_available_in_states_setter(self):
        tested = OperationalActivity()
        value = State()
        tested.get_available_in_states().add(value)
        pass

    def test_OperationalActivity_id_getter(self):
        tested = OperationalActivity()
        tested.get_id()
        pass

    def test_OperationalActivity_id_setter(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_id(value)
        pass

    def test_OperationalActivity_sid_getter(self):
        tested = OperationalActivity()
        tested.get_sid()
        pass

    def test_OperationalActivity_sid_setter(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_sid(value)
        pass

    def test_OperationalActivity_name_getter(self):
        tested = OperationalActivity()
        tested.get_name()
        pass

    def test_OperationalActivity_name_setter(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_name(value)
        pass

    def test_OperationalActivity_summary_getter(self):
        tested = OperationalActivity()
        tested.get_summary()
        pass

    def test_OperationalActivity_summary_setter(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_summary(value)
        pass

    def test_OperationalActivity_description_getter(self):
        tested = OperationalActivity()
        tested.get_description()
        pass

    def test_OperationalActivity_description_setter(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_description(value)
        pass

    def test_OperationalActivity_status_getter(self):
        tested = OperationalActivity()
        tested.get_status()
        pass

    def test_OperationalActivity_status_setter(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_status(value)
        pass

    def test_OperationalActivity_review_getter(self):
        tested = OperationalActivity()
        tested.get_review()
        pass

    def test_OperationalActivity_review_setter(self):
        tested = OperationalActivity()
        value = "value"
        tested.set_review(value)
        pass

    def test_OperationalActivity_visible_in_documentation_getter(self):
        tested = OperationalActivity()
        tested.get_visible_in_documentation()
        pass

    def test_OperationalActivity_visible_in_documentation_setter(self):
        tested = OperationalActivity()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_OperationalActivity_visible_for_traceability_getter(self):
        tested = OperationalActivity()
        tested.get_visible_for_traceability()
        pass

    def test_OperationalActivity_visible_for_traceability_setter(self):
        tested = OperationalActivity()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_OperationalActivity_owned_constraints_getter(self):
        tested = OperationalActivity()
        tested.get_owned_constraints()
        pass

    def test_OperationalActivity_constraints_getter(self):
        tested = OperationalActivity()
        tested.get_constraints()
        pass

    def test_OperationalActivity_constraints_setter(self):
        tested = OperationalActivity()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_OperationalActivity_owned_property_values_getter(self):
        tested = OperationalActivity()
        tested.get_owned_property_values()
        pass

    def test_OperationalActivity_applied_property_values_getter(self):
        tested = OperationalActivity()
        tested.get_applied_property_values()
        pass

    def test_OperationalActivity_applied_property_values_setter(self):
        tested = OperationalActivity()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_OperationalActivity_owned_property_value_groups_getter(self):
        tested = OperationalActivity()
        tested.get_owned_property_value_groups()
        pass

    def test_OperationalActivity_applied_property_value_groups_getter(self):
        tested = OperationalActivity()
        tested.get_applied_property_value_groups()
        pass

    def test_OperationalActivity_applied_property_value_groups_setter(self):
        tested = OperationalActivity()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_OperationalActivity_owned_enumeration_property_types_getter(self):
        tested = OperationalActivity()
        tested.get_owned_enumeration_property_types()
        pass

    def test_OperationalActivity_owned_diagrams_getter(self):
        tested = OperationalActivity()
        tested.get_owned_diagrams()
        pass

    def test_OperationalActivity_element_of_interest_for_diagrams_getter(self):
        tested = OperationalActivity()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_OperationalActivity_element_of_interest_for_diagrams_setter(self):
        tested = OperationalActivity()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_OperationalActivity_contextual_element_for_diagrams_getter(self):
        tested = OperationalActivity()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_OperationalActivity_contextual_element_for_diagrams_setter(self):
        tested = OperationalActivity()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_OperationalActivity_representing_diagrams_getter(self):
        tested = OperationalActivity()
        tested.get_representing_diagrams()
        pass

    def test_OperationalActivity__r_e_cs_getter(self):
        tested = OperationalActivity()
        tested.get__r_e_cs()
        pass

    def test_OperationalActivity__r_e_cs_setter(self):
        tested = OperationalActivity()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_OperationalActivity__r_p_ls_getter(self):
        tested = OperationalActivity()
        tested.get__r_p_ls()
        pass

    def test_OperationalActivity__r_p_ls_setter(self):
        tested = OperationalActivity()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_OperationalActivity_get_label(self):
        tested = OperationalActivity()
        tested.get_label()
        pass

    def test_OperationalActivity_get_element_type(self):
        tested = OperationalActivity()
        tested.get_element_type()
        pass

    def test_OperationalActivity_get_container(self):
        tested = OperationalActivity()
        tested.get_container()
        pass

    def test_OperationalActivity_get_contents(self):
        tested = OperationalActivity()
        tested.get_contents()
        pass

    def test_OperationalActivity_get_all_contents(self):
        tested = OperationalActivity()
        tested.get_all_contents()
        pass

    def test_OperationalActivity_get_all_contents_by_type(self):
        tested = OperationalActivity()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_OperationalActivity_get_available_s_b_queries(self):
        tested = OperationalActivity()
        tested.get_available_s_b_queries()
        pass

    def test_OperationalActivity_get_query_result(self):
        tested = OperationalActivity()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_OperationalActivity_contained_operational_activities_getter(self):
        tested = OperationalActivity()
        tested.get_contained_operational_activities()
        pass

    def test_OperationalActivity_owned_operational_activity_pkgs_getter(self):
        tested = OperationalActivity()
        tested.get_owned_operational_activity_pkgs()
        pass

    def test_OperationalActivity_incoming_getter(self):
        tested = OperationalActivity()
        tested.get_incoming()
        pass

    def test_OperationalActivity_incoming_setter(self):
        tested = OperationalActivity()
        value = Interaction()
        tested.get_incoming().add(value)
        pass

    def test_OperationalActivity_outgoing_getter(self):
        tested = OperationalActivity()
        tested.get_outgoing()
        pass

    def test_OperationalActivity_outgoing_setter(self):
        tested = OperationalActivity()
        value = Interaction()
        tested.get_outgoing().add(value)
        pass

    def test_OperationalActivity_allocating_entity_getter(self):
        tested = OperationalActivity()
        tested.get_allocating_entity()
        pass

    def test_OperationalActivity_allocating_entity_setter(self):
        tested = OperationalActivity()
        value = OperationalActor()
        tested.set_allocating_entity(value)
        pass

    def test_OperationalActivity_owned_operational_processes_getter(self):
        tested = OperationalActivity()
        tested.get_owned_operational_processes()
        pass

    def test_OperationalActivity_involving_operational_processes_getter(self):
        tested = OperationalActivity()
        tested.get_involving_operational_processes()
        pass

    def test_OperationalActivity_involving_operational_capabilities_getter(self):
        tested = OperationalActivity()
        tested.get_involving_operational_capabilities()
        pass

    def test_OperationalActivity_involving_operational_capabilities_setter(self):
        tested = OperationalActivity()
        value = OperationalCapability()
        tested.get_involving_operational_capabilities().add(value)
        pass

    def test_OperationalActivity_realizing_system_functions_getter(self):
        tested = OperationalActivity()
        tested.get_realizing_system_functions()
        pass

    def test_OperationalActivity_realizing_system_functions_setter(self):
        tested = OperationalActivity()
        value = SystemFunction()
        tested.get_realizing_system_functions().add(value)
        pass

    def test_Interaction_id_getter(self):
        tested = Interaction()
        tested.get_id()
        pass

    def test_Interaction_id_setter(self):
        tested = Interaction()
        value = "value"
        tested.set_id(value)
        pass

    def test_Interaction_sid_getter(self):
        tested = Interaction()
        tested.get_sid()
        pass

    def test_Interaction_sid_setter(self):
        tested = Interaction()
        value = "value"
        tested.set_sid(value)
        pass

    def test_Interaction_name_getter(self):
        tested = Interaction()
        tested.get_name()
        pass

    def test_Interaction_name_setter(self):
        tested = Interaction()
        value = "value"
        tested.set_name(value)
        pass

    def test_Interaction_summary_getter(self):
        tested = Interaction()
        tested.get_summary()
        pass

    def test_Interaction_summary_setter(self):
        tested = Interaction()
        value = "value"
        tested.set_summary(value)
        pass

    def test_Interaction_description_getter(self):
        tested = Interaction()
        tested.get_description()
        pass

    def test_Interaction_description_setter(self):
        tested = Interaction()
        value = "value"
        tested.set_description(value)
        pass

    def test_Interaction_status_getter(self):
        tested = Interaction()
        tested.get_status()
        pass

    def test_Interaction_status_setter(self):
        tested = Interaction()
        value = "value"
        tested.set_status(value)
        pass

    def test_Interaction_review_getter(self):
        tested = Interaction()
        tested.get_review()
        pass

    def test_Interaction_review_setter(self):
        tested = Interaction()
        value = "value"
        tested.set_review(value)
        pass

    def test_Interaction_visible_in_documentation_getter(self):
        tested = Interaction()
        tested.get_visible_in_documentation()
        pass

    def test_Interaction_visible_in_documentation_setter(self):
        tested = Interaction()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_Interaction_visible_for_traceability_getter(self):
        tested = Interaction()
        tested.get_visible_for_traceability()
        pass

    def test_Interaction_visible_for_traceability_setter(self):
        tested = Interaction()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_Interaction_owned_constraints_getter(self):
        tested = Interaction()
        tested.get_owned_constraints()
        pass

    def test_Interaction_constraints_getter(self):
        tested = Interaction()
        tested.get_constraints()
        pass

    def test_Interaction_constraints_setter(self):
        tested = Interaction()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_Interaction_owned_property_values_getter(self):
        tested = Interaction()
        tested.get_owned_property_values()
        pass

    def test_Interaction_applied_property_values_getter(self):
        tested = Interaction()
        tested.get_applied_property_values()
        pass

    def test_Interaction_applied_property_values_setter(self):
        tested = Interaction()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_Interaction_owned_property_value_groups_getter(self):
        tested = Interaction()
        tested.get_owned_property_value_groups()
        pass

    def test_Interaction_applied_property_value_groups_getter(self):
        tested = Interaction()
        tested.get_applied_property_value_groups()
        pass

    def test_Interaction_applied_property_value_groups_setter(self):
        tested = Interaction()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_Interaction_owned_enumeration_property_types_getter(self):
        tested = Interaction()
        tested.get_owned_enumeration_property_types()
        pass

    def test_Interaction_owned_diagrams_getter(self):
        tested = Interaction()
        tested.get_owned_diagrams()
        pass

    def test_Interaction_element_of_interest_for_diagrams_getter(self):
        tested = Interaction()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_Interaction_element_of_interest_for_diagrams_setter(self):
        tested = Interaction()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_Interaction_contextual_element_for_diagrams_getter(self):
        tested = Interaction()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_Interaction_contextual_element_for_diagrams_setter(self):
        tested = Interaction()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_Interaction_representing_diagrams_getter(self):
        tested = Interaction()
        tested.get_representing_diagrams()
        pass

    def test_Interaction__r_e_cs_getter(self):
        tested = Interaction()
        tested.get__r_e_cs()
        pass

    def test_Interaction__r_e_cs_setter(self):
        tested = Interaction()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_Interaction__r_p_ls_getter(self):
        tested = Interaction()
        tested.get__r_p_ls()
        pass

    def test_Interaction__r_p_ls_setter(self):
        tested = Interaction()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_Interaction_get_label(self):
        tested = Interaction()
        tested.get_label()
        pass

    def test_Interaction_get_element_type(self):
        tested = Interaction()
        tested.get_element_type()
        pass

    def test_Interaction_get_container(self):
        tested = Interaction()
        tested.get_container()
        pass

    def test_Interaction_get_contents(self):
        tested = Interaction()
        tested.get_contents()
        pass

    def test_Interaction_get_all_contents(self):
        tested = Interaction()
        tested.get_all_contents()
        pass

    def test_Interaction_get_all_contents_by_type(self):
        tested = Interaction()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_Interaction_get_available_s_b_queries(self):
        tested = Interaction()
        tested.get_available_s_b_queries()
        pass

    def test_Interaction_get_query_result(self):
        tested = Interaction()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_Interaction_source_getter(self):
        tested = Interaction()
        tested.get_source()
        pass

    def test_Interaction_source_setter(self):
        tested = Interaction()
        value = OperationalActivity()
        tested.set_source(value)
        pass

    def test_Interaction_target_getter(self):
        tested = Interaction()
        tested.get_target()
        pass

    def test_Interaction_target_setter(self):
        tested = Interaction()
        value = OperationalActivity()
        tested.set_target(value)
        pass

    def test_Interaction_allocating_communication_mean_getter(self):
        tested = Interaction()
        tested.get_allocating_communication_mean()
        pass

    def test_Interaction_allocating_communication_mean_setter(self):
        tested = Interaction()
        value = CommunicationMean()
        tested.set_allocating_communication_mean(value)
        pass

    def test_Interaction_involving_operational_processes_getter(self):
        tested = Interaction()
        tested.get_involving_operational_processes()
        pass

    def test_Interaction_exchanged_items_getter(self):
        tested = Interaction()
        tested.get_exchanged_items()
        pass

    def test_Interaction_exchanged_items_setter(self):
        tested = Interaction()
        value = ExchangeItem()
        tested.get_exchanged_items().add(value)
        pass

    def test_Interaction_realizing_functional_exchanges_getter(self):
        tested = Interaction()
        tested.get_realizing_functional_exchanges()
        pass

    def test_Interaction_realizing_functional_exchanges_setter(self):
        tested = Interaction()
        value = FunctionalExchange()
        tested.get_realizing_functional_exchanges().add(value)
        pass

    def test_OperationalProcess_id_getter(self):
        tested = OperationalProcess()
        tested.get_id()
        pass

    def test_OperationalProcess_id_setter(self):
        tested = OperationalProcess()
        value = "value"
        tested.set_id(value)
        pass

    def test_OperationalProcess_sid_getter(self):
        tested = OperationalProcess()
        tested.get_sid()
        pass

    def test_OperationalProcess_sid_setter(self):
        tested = OperationalProcess()
        value = "value"
        tested.set_sid(value)
        pass

    def test_OperationalProcess_name_getter(self):
        tested = OperationalProcess()
        tested.get_name()
        pass

    def test_OperationalProcess_name_setter(self):
        tested = OperationalProcess()
        value = "value"
        tested.set_name(value)
        pass

    def test_OperationalProcess_summary_getter(self):
        tested = OperationalProcess()
        tested.get_summary()
        pass

    def test_OperationalProcess_summary_setter(self):
        tested = OperationalProcess()
        value = "value"
        tested.set_summary(value)
        pass

    def test_OperationalProcess_description_getter(self):
        tested = OperationalProcess()
        tested.get_description()
        pass

    def test_OperationalProcess_description_setter(self):
        tested = OperationalProcess()
        value = "value"
        tested.set_description(value)
        pass

    def test_OperationalProcess_status_getter(self):
        tested = OperationalProcess()
        tested.get_status()
        pass

    def test_OperationalProcess_status_setter(self):
        tested = OperationalProcess()
        value = "value"
        tested.set_status(value)
        pass

    def test_OperationalProcess_review_getter(self):
        tested = OperationalProcess()
        tested.get_review()
        pass

    def test_OperationalProcess_review_setter(self):
        tested = OperationalProcess()
        value = "value"
        tested.set_review(value)
        pass

    def test_OperationalProcess_visible_in_documentation_getter(self):
        tested = OperationalProcess()
        tested.get_visible_in_documentation()
        pass

    def test_OperationalProcess_visible_in_documentation_setter(self):
        tested = OperationalProcess()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_OperationalProcess_visible_for_traceability_getter(self):
        tested = OperationalProcess()
        tested.get_visible_for_traceability()
        pass

    def test_OperationalProcess_visible_for_traceability_setter(self):
        tested = OperationalProcess()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_OperationalProcess_owned_constraints_getter(self):
        tested = OperationalProcess()
        tested.get_owned_constraints()
        pass

    def test_OperationalProcess_constraints_getter(self):
        tested = OperationalProcess()
        tested.get_constraints()
        pass

    def test_OperationalProcess_constraints_setter(self):
        tested = OperationalProcess()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_OperationalProcess_owned_property_values_getter(self):
        tested = OperationalProcess()
        tested.get_owned_property_values()
        pass

    def test_OperationalProcess_applied_property_values_getter(self):
        tested = OperationalProcess()
        tested.get_applied_property_values()
        pass

    def test_OperationalProcess_applied_property_values_setter(self):
        tested = OperationalProcess()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_OperationalProcess_owned_property_value_groups_getter(self):
        tested = OperationalProcess()
        tested.get_owned_property_value_groups()
        pass

    def test_OperationalProcess_applied_property_value_groups_getter(self):
        tested = OperationalProcess()
        tested.get_applied_property_value_groups()
        pass

    def test_OperationalProcess_applied_property_value_groups_setter(self):
        tested = OperationalProcess()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_OperationalProcess_owned_enumeration_property_types_getter(self):
        tested = OperationalProcess()
        tested.get_owned_enumeration_property_types()
        pass

    def test_OperationalProcess_owned_diagrams_getter(self):
        tested = OperationalProcess()
        tested.get_owned_diagrams()
        pass

    def test_OperationalProcess_element_of_interest_for_diagrams_getter(self):
        tested = OperationalProcess()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_OperationalProcess_element_of_interest_for_diagrams_setter(self):
        tested = OperationalProcess()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_OperationalProcess_contextual_element_for_diagrams_getter(self):
        tested = OperationalProcess()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_OperationalProcess_contextual_element_for_diagrams_setter(self):
        tested = OperationalProcess()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_OperationalProcess_representing_diagrams_getter(self):
        tested = OperationalProcess()
        tested.get_representing_diagrams()
        pass

    def test_OperationalProcess__r_e_cs_getter(self):
        tested = OperationalProcess()
        tested.get__r_e_cs()
        pass

    def test_OperationalProcess__r_e_cs_setter(self):
        tested = OperationalProcess()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_OperationalProcess__r_p_ls_getter(self):
        tested = OperationalProcess()
        tested.get__r_p_ls()
        pass

    def test_OperationalProcess__r_p_ls_setter(self):
        tested = OperationalProcess()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_OperationalProcess_get_label(self):
        tested = OperationalProcess()
        tested.get_label()
        pass

    def test_OperationalProcess_get_element_type(self):
        tested = OperationalProcess()
        tested.get_element_type()
        pass

    def test_OperationalProcess_get_container(self):
        tested = OperationalProcess()
        tested.get_container()
        pass

    def test_OperationalProcess_get_contents(self):
        tested = OperationalProcess()
        tested.get_contents()
        pass

    def test_OperationalProcess_get_all_contents(self):
        tested = OperationalProcess()
        tested.get_all_contents()
        pass

    def test_OperationalProcess_get_all_contents_by_type(self):
        tested = OperationalProcess()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_OperationalProcess_get_available_s_b_queries(self):
        tested = OperationalProcess()
        tested.get_available_s_b_queries()
        pass

    def test_OperationalProcess_get_query_result(self):
        tested = OperationalProcess()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_OperationalProcess_involved_operational_activities_getter(self):
        tested = OperationalProcess()
        tested.get_involved_operational_activities()
        pass

    def test_OperationalProcess_involved_interactions_getter(self):
        tested = OperationalProcess()
        tested.get_involved_interactions()
        pass

    def test_OperationalProcess_involved_operational_processes_getter(self):
        tested = OperationalProcess()
        tested.get_involved_operational_processes()
        pass

    def test_OperationalProcess_pre_condition_getter(self):
        tested = OperationalProcess()
        tested.get_pre_condition()
        pass

    def test_OperationalProcess_pre_condition_setter(self):
        tested = OperationalProcess()
        value = Constraint()
        tested.set_pre_condition(value)
        pass

    def test_OperationalProcess_post_condition_getter(self):
        tested = OperationalProcess()
        tested.get_post_condition()
        pass

    def test_OperationalProcess_post_condition_setter(self):
        tested = OperationalProcess()
        value = Constraint()
        tested.set_post_condition(value)
        pass

    def test_OperationalProcess_available_in_states_getter(self):
        tested = OperationalProcess()
        tested.get_available_in_states()
        pass

    def test_OperationalProcess_available_in_states_setter(self):
        tested = OperationalProcess()
        value = State()
        tested.get_available_in_states().add(value)
        pass

    def test_OperationalProcess_involving_operational_capabilities_getter(self):
        tested = OperationalProcess()
        tested.get_involving_operational_capabilities()
        pass

    def test_OperationalProcess_involving_operational_capabilities_setter(self):
        tested = OperationalProcess()
        value = OperationalCapability()
        tested.get_involving_operational_capabilities().add(value)
        pass

    def test_OperationalProcess_realizing_functional_chains_getter(self):
        tested = OperationalProcess()
        tested.get_realizing_functional_chains()
        pass

    def test_OperationalProcess_realizing_functional_chains_setter(self):
        tested = OperationalProcess()
        value = FunctionalChain()
        tested.get_realizing_functional_chains().add(value)
        pass

    def test_OperationalCapabilityPkg_owned_property_value_pkgs_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_owned_property_value_pkgs()
        pass

    def test_OperationalCapabilityPkg_id_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_id()
        pass

    def test_OperationalCapabilityPkg_id_setter(self):
        tested = OperationalCapabilityPkg()
        value = "value"
        tested.set_id(value)
        pass

    def test_OperationalCapabilityPkg_sid_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_sid()
        pass

    def test_OperationalCapabilityPkg_sid_setter(self):
        tested = OperationalCapabilityPkg()
        value = "value"
        tested.set_sid(value)
        pass

    def test_OperationalCapabilityPkg_name_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_name()
        pass

    def test_OperationalCapabilityPkg_name_setter(self):
        tested = OperationalCapabilityPkg()
        value = "value"
        tested.set_name(value)
        pass

    def test_OperationalCapabilityPkg_summary_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_summary()
        pass

    def test_OperationalCapabilityPkg_summary_setter(self):
        tested = OperationalCapabilityPkg()
        value = "value"
        tested.set_summary(value)
        pass

    def test_OperationalCapabilityPkg_description_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_description()
        pass

    def test_OperationalCapabilityPkg_description_setter(self):
        tested = OperationalCapabilityPkg()
        value = "value"
        tested.set_description(value)
        pass

    def test_OperationalCapabilityPkg_status_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_status()
        pass

    def test_OperationalCapabilityPkg_status_setter(self):
        tested = OperationalCapabilityPkg()
        value = "value"
        tested.set_status(value)
        pass

    def test_OperationalCapabilityPkg_review_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_review()
        pass

    def test_OperationalCapabilityPkg_review_setter(self):
        tested = OperationalCapabilityPkg()
        value = "value"
        tested.set_review(value)
        pass

    def test_OperationalCapabilityPkg_visible_in_documentation_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_visible_in_documentation()
        pass

    def test_OperationalCapabilityPkg_visible_in_documentation_setter(self):
        tested = OperationalCapabilityPkg()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_OperationalCapabilityPkg_visible_for_traceability_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_visible_for_traceability()
        pass

    def test_OperationalCapabilityPkg_visible_for_traceability_setter(self):
        tested = OperationalCapabilityPkg()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_OperationalCapabilityPkg_owned_constraints_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_owned_constraints()
        pass

    def test_OperationalCapabilityPkg_constraints_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_constraints()
        pass

    def test_OperationalCapabilityPkg_constraints_setter(self):
        tested = OperationalCapabilityPkg()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_OperationalCapabilityPkg_owned_property_values_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_owned_property_values()
        pass

    def test_OperationalCapabilityPkg_applied_property_values_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_applied_property_values()
        pass

    def test_OperationalCapabilityPkg_applied_property_values_setter(self):
        tested = OperationalCapabilityPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_OperationalCapabilityPkg_owned_property_value_groups_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_owned_property_value_groups()
        pass

    def test_OperationalCapabilityPkg_applied_property_value_groups_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_applied_property_value_groups()
        pass

    def test_OperationalCapabilityPkg_applied_property_value_groups_setter(self):
        tested = OperationalCapabilityPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_OperationalCapabilityPkg_owned_enumeration_property_types_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_owned_enumeration_property_types()
        pass

    def test_OperationalCapabilityPkg_owned_diagrams_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_owned_diagrams()
        pass

    def test_OperationalCapabilityPkg_element_of_interest_for_diagrams_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_OperationalCapabilityPkg_element_of_interest_for_diagrams_setter(self):
        tested = OperationalCapabilityPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_OperationalCapabilityPkg_contextual_element_for_diagrams_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_OperationalCapabilityPkg_contextual_element_for_diagrams_setter(self):
        tested = OperationalCapabilityPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_OperationalCapabilityPkg_representing_diagrams_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_representing_diagrams()
        pass

    def test_OperationalCapabilityPkg__r_e_cs_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get__r_e_cs()
        pass

    def test_OperationalCapabilityPkg__r_e_cs_setter(self):
        tested = OperationalCapabilityPkg()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_OperationalCapabilityPkg__r_p_ls_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get__r_p_ls()
        pass

    def test_OperationalCapabilityPkg__r_p_ls_setter(self):
        tested = OperationalCapabilityPkg()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_OperationalCapabilityPkg_get_label(self):
        tested = OperationalCapabilityPkg()
        tested.get_label()
        pass

    def test_OperationalCapabilityPkg_get_element_type(self):
        tested = OperationalCapabilityPkg()
        tested.get_element_type()
        pass

    def test_OperationalCapabilityPkg_get_container(self):
        tested = OperationalCapabilityPkg()
        tested.get_container()
        pass

    def test_OperationalCapabilityPkg_get_contents(self):
        tested = OperationalCapabilityPkg()
        tested.get_contents()
        pass

    def test_OperationalCapabilityPkg_get_all_contents(self):
        tested = OperationalCapabilityPkg()
        tested.get_all_contents()
        pass

    def test_OperationalCapabilityPkg_get_all_contents_by_type(self):
        tested = OperationalCapabilityPkg()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_OperationalCapabilityPkg_get_available_s_b_queries(self):
        tested = OperationalCapabilityPkg()
        tested.get_available_s_b_queries()
        pass

    def test_OperationalCapabilityPkg_get_query_result(self):
        tested = OperationalCapabilityPkg()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_OperationalCapabilityPkg_owned_operational_capability_pkgs_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_owned_operational_capability_pkgs()
        pass

    def test_OperationalCapabilityPkg_owned_operational_capabilities_getter(self):
        tested = OperationalCapabilityPkg()
        tested.get_owned_operational_capabilities()
        pass

    def test_OperationalCapability_pre_condition_getter(self):
        tested = OperationalCapability()
        tested.get_pre_condition()
        pass

    def test_OperationalCapability_pre_condition_setter(self):
        tested = OperationalCapability()
        value = Constraint()
        tested.set_pre_condition(value)
        pass

    def test_OperationalCapability_post_condition_getter(self):
        tested = OperationalCapability()
        tested.get_post_condition()
        pass

    def test_OperationalCapability_post_condition_setter(self):
        tested = OperationalCapability()
        value = Constraint()
        tested.set_post_condition(value)
        pass

    def test_OperationalCapability_owned_scenarios_getter(self):
        tested = OperationalCapability()
        tested.get_owned_scenarios()
        pass

    def test_OperationalCapability_super_getter(self):
        tested = OperationalCapability()
        tested.get_super()
        pass

    def test_OperationalCapability_super_setter(self):
        tested = OperationalCapability()
        value = CapabilityRealization()
        tested.get_super().add(value)
        pass

    def test_OperationalCapability_sub_getter(self):
        tested = OperationalCapability()
        tested.get_sub()
        pass

    def test_OperationalCapability_sub_setter(self):
        tested = OperationalCapability()
        value = CapabilityRealization()
        tested.get_sub().add(value)
        pass

    def test_OperationalCapability_included_capabilities_getter(self):
        tested = OperationalCapability()
        tested.get_included_capabilities()
        pass

    def test_OperationalCapability_included_capabilities_setter(self):
        tested = OperationalCapability()
        value = CapabilityRealization()
        tested.get_included_capabilities().add(value)
        pass

    def test_OperationalCapability_including_capabilities_getter(self):
        tested = OperationalCapability()
        tested.get_including_capabilities()
        pass

    def test_OperationalCapability_including_capabilities_setter(self):
        tested = OperationalCapability()
        value = CapabilityRealization()
        tested.get_including_capabilities().add(value)
        pass

    def test_OperationalCapability_extended_capabilities_getter(self):
        tested = OperationalCapability()
        tested.get_extended_capabilities()
        pass

    def test_OperationalCapability_extended_capabilities_setter(self):
        tested = OperationalCapability()
        value = CapabilityRealization()
        tested.get_extended_capabilities().add(value)
        pass

    def test_OperationalCapability_extending_capabilities_getter(self):
        tested = OperationalCapability()
        tested.get_extending_capabilities()
        pass

    def test_OperationalCapability_extending_capabilities_setter(self):
        tested = OperationalCapability()
        value = CapabilityRealization()
        tested.get_extending_capabilities().add(value)
        pass

    def test_OperationalCapability_available_in_states_getter(self):
        tested = OperationalCapability()
        tested.get_available_in_states()
        pass

    def test_OperationalCapability_available_in_states_setter(self):
        tested = OperationalCapability()
        value = State()
        tested.get_available_in_states().add(value)
        pass

    def test_OperationalCapability_owned_property_value_pkgs_getter(self):
        tested = OperationalCapability()
        tested.get_owned_property_value_pkgs()
        pass

    def test_OperationalCapability_id_getter(self):
        tested = OperationalCapability()
        tested.get_id()
        pass

    def test_OperationalCapability_id_setter(self):
        tested = OperationalCapability()
        value = "value"
        tested.set_id(value)
        pass

    def test_OperationalCapability_sid_getter(self):
        tested = OperationalCapability()
        tested.get_sid()
        pass

    def test_OperationalCapability_sid_setter(self):
        tested = OperationalCapability()
        value = "value"
        tested.set_sid(value)
        pass

    def test_OperationalCapability_name_getter(self):
        tested = OperationalCapability()
        tested.get_name()
        pass

    def test_OperationalCapability_name_setter(self):
        tested = OperationalCapability()
        value = "value"
        tested.set_name(value)
        pass

    def test_OperationalCapability_summary_getter(self):
        tested = OperationalCapability()
        tested.get_summary()
        pass

    def test_OperationalCapability_summary_setter(self):
        tested = OperationalCapability()
        value = "value"
        tested.set_summary(value)
        pass

    def test_OperationalCapability_description_getter(self):
        tested = OperationalCapability()
        tested.get_description()
        pass

    def test_OperationalCapability_description_setter(self):
        tested = OperationalCapability()
        value = "value"
        tested.set_description(value)
        pass

    def test_OperationalCapability_status_getter(self):
        tested = OperationalCapability()
        tested.get_status()
        pass

    def test_OperationalCapability_status_setter(self):
        tested = OperationalCapability()
        value = "value"
        tested.set_status(value)
        pass

    def test_OperationalCapability_review_getter(self):
        tested = OperationalCapability()
        tested.get_review()
        pass

    def test_OperationalCapability_review_setter(self):
        tested = OperationalCapability()
        value = "value"
        tested.set_review(value)
        pass

    def test_OperationalCapability_visible_in_documentation_getter(self):
        tested = OperationalCapability()
        tested.get_visible_in_documentation()
        pass

    def test_OperationalCapability_visible_in_documentation_setter(self):
        tested = OperationalCapability()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_OperationalCapability_visible_for_traceability_getter(self):
        tested = OperationalCapability()
        tested.get_visible_for_traceability()
        pass

    def test_OperationalCapability_visible_for_traceability_setter(self):
        tested = OperationalCapability()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_OperationalCapability_owned_constraints_getter(self):
        tested = OperationalCapability()
        tested.get_owned_constraints()
        pass

    def test_OperationalCapability_constraints_getter(self):
        tested = OperationalCapability()
        tested.get_constraints()
        pass

    def test_OperationalCapability_constraints_setter(self):
        tested = OperationalCapability()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_OperationalCapability_owned_property_values_getter(self):
        tested = OperationalCapability()
        tested.get_owned_property_values()
        pass

    def test_OperationalCapability_applied_property_values_getter(self):
        tested = OperationalCapability()
        tested.get_applied_property_values()
        pass

    def test_OperationalCapability_applied_property_values_setter(self):
        tested = OperationalCapability()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_OperationalCapability_owned_property_value_groups_getter(self):
        tested = OperationalCapability()
        tested.get_owned_property_value_groups()
        pass

    def test_OperationalCapability_applied_property_value_groups_getter(self):
        tested = OperationalCapability()
        tested.get_applied_property_value_groups()
        pass

    def test_OperationalCapability_applied_property_value_groups_setter(self):
        tested = OperationalCapability()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_OperationalCapability_owned_enumeration_property_types_getter(self):
        tested = OperationalCapability()
        tested.get_owned_enumeration_property_types()
        pass

    def test_OperationalCapability_owned_diagrams_getter(self):
        tested = OperationalCapability()
        tested.get_owned_diagrams()
        pass

    def test_OperationalCapability_element_of_interest_for_diagrams_getter(self):
        tested = OperationalCapability()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_OperationalCapability_element_of_interest_for_diagrams_setter(self):
        tested = OperationalCapability()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_OperationalCapability_contextual_element_for_diagrams_getter(self):
        tested = OperationalCapability()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_OperationalCapability_contextual_element_for_diagrams_setter(self):
        tested = OperationalCapability()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_OperationalCapability_representing_diagrams_getter(self):
        tested = OperationalCapability()
        tested.get_representing_diagrams()
        pass

    def test_OperationalCapability__r_e_cs_getter(self):
        tested = OperationalCapability()
        tested.get__r_e_cs()
        pass

    def test_OperationalCapability__r_e_cs_setter(self):
        tested = OperationalCapability()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_OperationalCapability__r_p_ls_getter(self):
        tested = OperationalCapability()
        tested.get__r_p_ls()
        pass

    def test_OperationalCapability__r_p_ls_setter(self):
        tested = OperationalCapability()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_OperationalCapability_get_label(self):
        tested = OperationalCapability()
        tested.get_label()
        pass

    def test_OperationalCapability_get_element_type(self):
        tested = OperationalCapability()
        tested.get_element_type()
        pass

    def test_OperationalCapability_get_container(self):
        tested = OperationalCapability()
        tested.get_container()
        pass

    def test_OperationalCapability_get_contents(self):
        tested = OperationalCapability()
        tested.get_contents()
        pass

    def test_OperationalCapability_get_all_contents(self):
        tested = OperationalCapability()
        tested.get_all_contents()
        pass

    def test_OperationalCapability_get_all_contents_by_type(self):
        tested = OperationalCapability()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_OperationalCapability_get_available_s_b_queries(self):
        tested = OperationalCapability()
        tested.get_available_s_b_queries()
        pass

    def test_OperationalCapability_get_query_result(self):
        tested = OperationalCapability()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_OperationalCapability_owned_operational_processes_getter(self):
        tested = OperationalCapability()
        tested.get_owned_operational_processes()
        pass

    def test_OperationalCapability_involved_operational_processes_getter(self):
        tested = OperationalCapability()
        tested.get_involved_operational_processes()
        pass

    def test_OperationalCapability_involved_operational_processes_setter(self):
        tested = OperationalCapability()
        value = OperationalProcess()
        tested.get_involved_operational_processes().add(value)
        pass

    def test_OperationalCapability_involved_operational_activities_getter(self):
        tested = OperationalCapability()
        tested.get_involved_operational_activities()
        pass

    def test_OperationalCapability_involved_operational_activities_setter(self):
        tested = OperationalCapability()
        value = OperationalActivity()
        tested.get_involved_operational_activities().add(value)
        pass

    def test_OperationalCapability_involved_entities_getter(self):
        tested = OperationalCapability()
        tested.get_involved_entities()
        pass

    def test_OperationalCapability_involved_entities_setter(self):
        tested = OperationalCapability()
        value = OperationalActor()
        tested.get_involved_entities().add(value)
        pass

    def test_OperationalCapability_realizing_capabilities_getter(self):
        tested = OperationalCapability()
        tested.get_realizing_capabilities()
        pass

    def test_OperationalCapability_realizing_capabilities_setter(self):
        tested = OperationalCapability()
        value = Capability()
        tested.get_realizing_capabilities().add(value)
        pass

    def test_EntityPkg_owned_property_value_pkgs_getter(self):
        tested = EntityPkg()
        tested.get_owned_property_value_pkgs()
        pass

    def test_EntityPkg_id_getter(self):
        tested = EntityPkg()
        tested.get_id()
        pass

    def test_EntityPkg_id_setter(self):
        tested = EntityPkg()
        value = "value"
        tested.set_id(value)
        pass

    def test_EntityPkg_sid_getter(self):
        tested = EntityPkg()
        tested.get_sid()
        pass

    def test_EntityPkg_sid_setter(self):
        tested = EntityPkg()
        value = "value"
        tested.set_sid(value)
        pass

    def test_EntityPkg_name_getter(self):
        tested = EntityPkg()
        tested.get_name()
        pass

    def test_EntityPkg_name_setter(self):
        tested = EntityPkg()
        value = "value"
        tested.set_name(value)
        pass

    def test_EntityPkg_summary_getter(self):
        tested = EntityPkg()
        tested.get_summary()
        pass

    def test_EntityPkg_summary_setter(self):
        tested = EntityPkg()
        value = "value"
        tested.set_summary(value)
        pass

    def test_EntityPkg_description_getter(self):
        tested = EntityPkg()
        tested.get_description()
        pass

    def test_EntityPkg_description_setter(self):
        tested = EntityPkg()
        value = "value"
        tested.set_description(value)
        pass

    def test_EntityPkg_status_getter(self):
        tested = EntityPkg()
        tested.get_status()
        pass

    def test_EntityPkg_status_setter(self):
        tested = EntityPkg()
        value = "value"
        tested.set_status(value)
        pass

    def test_EntityPkg_review_getter(self):
        tested = EntityPkg()
        tested.get_review()
        pass

    def test_EntityPkg_review_setter(self):
        tested = EntityPkg()
        value = "value"
        tested.set_review(value)
        pass

    def test_EntityPkg_visible_in_documentation_getter(self):
        tested = EntityPkg()
        tested.get_visible_in_documentation()
        pass

    def test_EntityPkg_visible_in_documentation_setter(self):
        tested = EntityPkg()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_EntityPkg_visible_for_traceability_getter(self):
        tested = EntityPkg()
        tested.get_visible_for_traceability()
        pass

    def test_EntityPkg_visible_for_traceability_setter(self):
        tested = EntityPkg()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_EntityPkg_owned_constraints_getter(self):
        tested = EntityPkg()
        tested.get_owned_constraints()
        pass

    def test_EntityPkg_constraints_getter(self):
        tested = EntityPkg()
        tested.get_constraints()
        pass

    def test_EntityPkg_constraints_setter(self):
        tested = EntityPkg()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_EntityPkg_owned_property_values_getter(self):
        tested = EntityPkg()
        tested.get_owned_property_values()
        pass

    def test_EntityPkg_applied_property_values_getter(self):
        tested = EntityPkg()
        tested.get_applied_property_values()
        pass

    def test_EntityPkg_applied_property_values_setter(self):
        tested = EntityPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_EntityPkg_owned_property_value_groups_getter(self):
        tested = EntityPkg()
        tested.get_owned_property_value_groups()
        pass

    def test_EntityPkg_applied_property_value_groups_getter(self):
        tested = EntityPkg()
        tested.get_applied_property_value_groups()
        pass

    def test_EntityPkg_applied_property_value_groups_setter(self):
        tested = EntityPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_EntityPkg_owned_enumeration_property_types_getter(self):
        tested = EntityPkg()
        tested.get_owned_enumeration_property_types()
        pass

    def test_EntityPkg_owned_diagrams_getter(self):
        tested = EntityPkg()
        tested.get_owned_diagrams()
        pass

    def test_EntityPkg_element_of_interest_for_diagrams_getter(self):
        tested = EntityPkg()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_EntityPkg_element_of_interest_for_diagrams_setter(self):
        tested = EntityPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_EntityPkg_contextual_element_for_diagrams_getter(self):
        tested = EntityPkg()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_EntityPkg_contextual_element_for_diagrams_setter(self):
        tested = EntityPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_EntityPkg_representing_diagrams_getter(self):
        tested = EntityPkg()
        tested.get_representing_diagrams()
        pass

    def test_EntityPkg__r_e_cs_getter(self):
        tested = EntityPkg()
        tested.get__r_e_cs()
        pass

    def test_EntityPkg__r_e_cs_setter(self):
        tested = EntityPkg()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_EntityPkg__r_p_ls_getter(self):
        tested = EntityPkg()
        tested.get__r_p_ls()
        pass

    def test_EntityPkg__r_p_ls_setter(self):
        tested = EntityPkg()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_EntityPkg_get_label(self):
        tested = EntityPkg()
        tested.get_label()
        pass

    def test_EntityPkg_get_element_type(self):
        tested = EntityPkg()
        tested.get_element_type()
        pass

    def test_EntityPkg_get_container(self):
        tested = EntityPkg()
        tested.get_container()
        pass

    def test_EntityPkg_get_contents(self):
        tested = EntityPkg()
        tested.get_contents()
        pass

    def test_EntityPkg_get_all_contents(self):
        tested = EntityPkg()
        tested.get_all_contents()
        pass

    def test_EntityPkg_get_all_contents_by_type(self):
        tested = EntityPkg()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_EntityPkg_get_available_s_b_queries(self):
        tested = EntityPkg()
        tested.get_available_s_b_queries()
        pass

    def test_EntityPkg_get_query_result(self):
        tested = EntityPkg()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_EntityPkg_owned_entity_pkgs_getter(self):
        tested = EntityPkg()
        tested.get_owned_entity_pkgs()
        pass

    def test_EntityPkg_owned_entities_getter(self):
        tested = EntityPkg()
        tested.get_owned_entities()
        pass

    def test_OperationalEntity_incoming_communication_means_getter(self):
        tested = OperationalEntity()
        tested.get_incoming_communication_means()
        pass

    def test_OperationalEntity_incoming_communication_means_setter(self):
        tested = OperationalEntity()
        value = CommunicationMean()
        tested.get_incoming_communication_means().add(value)
        pass

    def test_OperationalEntity_outgoing_communication_means_getter(self):
        tested = OperationalEntity()
        tested.get_outgoing_communication_means()
        pass

    def test_OperationalEntity_outgoing_communication_means_setter(self):
        tested = OperationalEntity()
        value = CommunicationMean()
        tested.get_outgoing_communication_means().add(value)
        pass

    def test_OperationalEntity_allocated_operational_activities_getter(self):
        tested = OperationalEntity()
        tested.get_allocated_operational_activities()
        pass

    def test_OperationalEntity_allocated_operational_activities_setter(self):
        tested = OperationalEntity()
        value = OperationalActivity()
        tested.get_allocated_operational_activities().add(value)
        pass

    def test_OperationalEntity_involving_operational_capabilities_getter(self):
        tested = OperationalEntity()
        tested.get_involving_operational_capabilities()
        pass

    def test_OperationalEntity_involving_operational_capabilities_setter(self):
        tested = OperationalEntity()
        value = OperationalCapability()
        tested.get_involving_operational_capabilities().add(value)
        pass

    def test_OperationalEntity_owned_state_machines_getter(self):
        tested = OperationalEntity()
        tested.get_owned_state_machines()
        pass

    def test_OperationalEntity_realizing_system_actors_getter(self):
        tested = OperationalEntity()
        tested.get_realizing_system_actors()
        pass

    def test_OperationalEntity_realizing_system_actors_setter(self):
        tested = OperationalEntity()
        value = SystemActor()
        tested.get_realizing_system_actors().add(value)
        pass

    def test_OperationalEntity_id_getter(self):
        tested = OperationalEntity()
        tested.get_id()
        pass

    def test_OperationalEntity_id_setter(self):
        tested = OperationalEntity()
        value = "value"
        tested.set_id(value)
        pass

    def test_OperationalEntity_sid_getter(self):
        tested = OperationalEntity()
        tested.get_sid()
        pass

    def test_OperationalEntity_sid_setter(self):
        tested = OperationalEntity()
        value = "value"
        tested.set_sid(value)
        pass

    def test_OperationalEntity_name_getter(self):
        tested = OperationalEntity()
        tested.get_name()
        pass

    def test_OperationalEntity_name_setter(self):
        tested = OperationalEntity()
        value = "value"
        tested.set_name(value)
        pass

    def test_OperationalEntity_summary_getter(self):
        tested = OperationalEntity()
        tested.get_summary()
        pass

    def test_OperationalEntity_summary_setter(self):
        tested = OperationalEntity()
        value = "value"
        tested.set_summary(value)
        pass

    def test_OperationalEntity_description_getter(self):
        tested = OperationalEntity()
        tested.get_description()
        pass

    def test_OperationalEntity_description_setter(self):
        tested = OperationalEntity()
        value = "value"
        tested.set_description(value)
        pass

    def test_OperationalEntity_status_getter(self):
        tested = OperationalEntity()
        tested.get_status()
        pass

    def test_OperationalEntity_status_setter(self):
        tested = OperationalEntity()
        value = "value"
        tested.set_status(value)
        pass

    def test_OperationalEntity_review_getter(self):
        tested = OperationalEntity()
        tested.get_review()
        pass

    def test_OperationalEntity_review_setter(self):
        tested = OperationalEntity()
        value = "value"
        tested.set_review(value)
        pass

    def test_OperationalEntity_visible_in_documentation_getter(self):
        tested = OperationalEntity()
        tested.get_visible_in_documentation()
        pass

    def test_OperationalEntity_visible_in_documentation_setter(self):
        tested = OperationalEntity()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_OperationalEntity_visible_for_traceability_getter(self):
        tested = OperationalEntity()
        tested.get_visible_for_traceability()
        pass

    def test_OperationalEntity_visible_for_traceability_setter(self):
        tested = OperationalEntity()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_OperationalEntity_owned_constraints_getter(self):
        tested = OperationalEntity()
        tested.get_owned_constraints()
        pass

    def test_OperationalEntity_constraints_getter(self):
        tested = OperationalEntity()
        tested.get_constraints()
        pass

    def test_OperationalEntity_constraints_setter(self):
        tested = OperationalEntity()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_OperationalEntity_owned_property_values_getter(self):
        tested = OperationalEntity()
        tested.get_owned_property_values()
        pass

    def test_OperationalEntity_applied_property_values_getter(self):
        tested = OperationalEntity()
        tested.get_applied_property_values()
        pass

    def test_OperationalEntity_applied_property_values_setter(self):
        tested = OperationalEntity()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_OperationalEntity_owned_property_value_groups_getter(self):
        tested = OperationalEntity()
        tested.get_owned_property_value_groups()
        pass

    def test_OperationalEntity_applied_property_value_groups_getter(self):
        tested = OperationalEntity()
        tested.get_applied_property_value_groups()
        pass

    def test_OperationalEntity_applied_property_value_groups_setter(self):
        tested = OperationalEntity()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_OperationalEntity_owned_enumeration_property_types_getter(self):
        tested = OperationalEntity()
        tested.get_owned_enumeration_property_types()
        pass

    def test_OperationalEntity_owned_diagrams_getter(self):
        tested = OperationalEntity()
        tested.get_owned_diagrams()
        pass

    def test_OperationalEntity_element_of_interest_for_diagrams_getter(self):
        tested = OperationalEntity()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_OperationalEntity_element_of_interest_for_diagrams_setter(self):
        tested = OperationalEntity()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_OperationalEntity_contextual_element_for_diagrams_getter(self):
        tested = OperationalEntity()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_OperationalEntity_contextual_element_for_diagrams_setter(self):
        tested = OperationalEntity()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_OperationalEntity_representing_diagrams_getter(self):
        tested = OperationalEntity()
        tested.get_representing_diagrams()
        pass

    def test_OperationalEntity__r_e_cs_getter(self):
        tested = OperationalEntity()
        tested.get__r_e_cs()
        pass

    def test_OperationalEntity__r_e_cs_setter(self):
        tested = OperationalEntity()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_OperationalEntity__r_p_ls_getter(self):
        tested = OperationalEntity()
        tested.get__r_p_ls()
        pass

    def test_OperationalEntity__r_p_ls_setter(self):
        tested = OperationalEntity()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_OperationalEntity_get_label(self):
        tested = OperationalEntity()
        tested.get_label()
        pass

    def test_OperationalEntity_get_element_type(self):
        tested = OperationalEntity()
        tested.get_element_type()
        pass

    def test_OperationalEntity_get_container(self):
        tested = OperationalEntity()
        tested.get_container()
        pass

    def test_OperationalEntity_get_contents(self):
        tested = OperationalEntity()
        tested.get_contents()
        pass

    def test_OperationalEntity_get_all_contents(self):
        tested = OperationalEntity()
        tested.get_all_contents()
        pass

    def test_OperationalEntity_get_all_contents_by_type(self):
        tested = OperationalEntity()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_OperationalEntity_get_available_s_b_queries(self):
        tested = OperationalEntity()
        tested.get_available_s_b_queries()
        pass

    def test_OperationalEntity_get_query_result(self):
        tested = OperationalEntity()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_OperationalEntity_owned_entities_getter(self):
        tested = OperationalEntity()
        tested.get_owned_entities()
        pass

    def test_OperationalActor_id_getter(self):
        tested = OperationalActor()
        tested.get_id()
        pass

    def test_OperationalActor_id_setter(self):
        tested = OperationalActor()
        value = "value"
        tested.set_id(value)
        pass

    def test_OperationalActor_sid_getter(self):
        tested = OperationalActor()
        tested.get_sid()
        pass

    def test_OperationalActor_sid_setter(self):
        tested = OperationalActor()
        value = "value"
        tested.set_sid(value)
        pass

    def test_OperationalActor_name_getter(self):
        tested = OperationalActor()
        tested.get_name()
        pass

    def test_OperationalActor_name_setter(self):
        tested = OperationalActor()
        value = "value"
        tested.set_name(value)
        pass

    def test_OperationalActor_summary_getter(self):
        tested = OperationalActor()
        tested.get_summary()
        pass

    def test_OperationalActor_summary_setter(self):
        tested = OperationalActor()
        value = "value"
        tested.set_summary(value)
        pass

    def test_OperationalActor_description_getter(self):
        tested = OperationalActor()
        tested.get_description()
        pass

    def test_OperationalActor_description_setter(self):
        tested = OperationalActor()
        value = "value"
        tested.set_description(value)
        pass

    def test_OperationalActor_status_getter(self):
        tested = OperationalActor()
        tested.get_status()
        pass

    def test_OperationalActor_status_setter(self):
        tested = OperationalActor()
        value = "value"
        tested.set_status(value)
        pass

    def test_OperationalActor_review_getter(self):
        tested = OperationalActor()
        tested.get_review()
        pass

    def test_OperationalActor_review_setter(self):
        tested = OperationalActor()
        value = "value"
        tested.set_review(value)
        pass

    def test_OperationalActor_visible_in_documentation_getter(self):
        tested = OperationalActor()
        tested.get_visible_in_documentation()
        pass

    def test_OperationalActor_visible_in_documentation_setter(self):
        tested = OperationalActor()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_OperationalActor_visible_for_traceability_getter(self):
        tested = OperationalActor()
        tested.get_visible_for_traceability()
        pass

    def test_OperationalActor_visible_for_traceability_setter(self):
        tested = OperationalActor()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_OperationalActor_owned_constraints_getter(self):
        tested = OperationalActor()
        tested.get_owned_constraints()
        pass

    def test_OperationalActor_constraints_getter(self):
        tested = OperationalActor()
        tested.get_constraints()
        pass

    def test_OperationalActor_constraints_setter(self):
        tested = OperationalActor()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_OperationalActor_owned_property_values_getter(self):
        tested = OperationalActor()
        tested.get_owned_property_values()
        pass

    def test_OperationalActor_applied_property_values_getter(self):
        tested = OperationalActor()
        tested.get_applied_property_values()
        pass

    def test_OperationalActor_applied_property_values_setter(self):
        tested = OperationalActor()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_OperationalActor_owned_property_value_groups_getter(self):
        tested = OperationalActor()
        tested.get_owned_property_value_groups()
        pass

    def test_OperationalActor_applied_property_value_groups_getter(self):
        tested = OperationalActor()
        tested.get_applied_property_value_groups()
        pass

    def test_OperationalActor_applied_property_value_groups_setter(self):
        tested = OperationalActor()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_OperationalActor_owned_enumeration_property_types_getter(self):
        tested = OperationalActor()
        tested.get_owned_enumeration_property_types()
        pass

    def test_OperationalActor_owned_diagrams_getter(self):
        tested = OperationalActor()
        tested.get_owned_diagrams()
        pass

    def test_OperationalActor_element_of_interest_for_diagrams_getter(self):
        tested = OperationalActor()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_OperationalActor_element_of_interest_for_diagrams_setter(self):
        tested = OperationalActor()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_OperationalActor_contextual_element_for_diagrams_getter(self):
        tested = OperationalActor()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_OperationalActor_contextual_element_for_diagrams_setter(self):
        tested = OperationalActor()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_OperationalActor_representing_diagrams_getter(self):
        tested = OperationalActor()
        tested.get_representing_diagrams()
        pass

    def test_OperationalActor__r_e_cs_getter(self):
        tested = OperationalActor()
        tested.get__r_e_cs()
        pass

    def test_OperationalActor__r_e_cs_setter(self):
        tested = OperationalActor()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_OperationalActor__r_p_ls_getter(self):
        tested = OperationalActor()
        tested.get__r_p_ls()
        pass

    def test_OperationalActor__r_p_ls_setter(self):
        tested = OperationalActor()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_OperationalActor_get_label(self):
        tested = OperationalActor()
        tested.get_label()
        pass

    def test_OperationalActor_get_element_type(self):
        tested = OperationalActor()
        tested.get_element_type()
        pass

    def test_OperationalActor_get_container(self):
        tested = OperationalActor()
        tested.get_container()
        pass

    def test_OperationalActor_get_contents(self):
        tested = OperationalActor()
        tested.get_contents()
        pass

    def test_OperationalActor_get_all_contents(self):
        tested = OperationalActor()
        tested.get_all_contents()
        pass

    def test_OperationalActor_get_all_contents_by_type(self):
        tested = OperationalActor()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_OperationalActor_get_available_s_b_queries(self):
        tested = OperationalActor()
        tested.get_available_s_b_queries()
        pass

    def test_OperationalActor_get_query_result(self):
        tested = OperationalActor()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_OperationalActor_incoming_communication_means_getter(self):
        tested = OperationalActor()
        tested.get_incoming_communication_means()
        pass

    def test_OperationalActor_incoming_communication_means_setter(self):
        tested = OperationalActor()
        value = CommunicationMean()
        tested.get_incoming_communication_means().add(value)
        pass

    def test_OperationalActor_outgoing_communication_means_getter(self):
        tested = OperationalActor()
        tested.get_outgoing_communication_means()
        pass

    def test_OperationalActor_outgoing_communication_means_setter(self):
        tested = OperationalActor()
        value = CommunicationMean()
        tested.get_outgoing_communication_means().add(value)
        pass

    def test_OperationalActor_allocated_operational_activities_getter(self):
        tested = OperationalActor()
        tested.get_allocated_operational_activities()
        pass

    def test_OperationalActor_allocated_operational_activities_setter(self):
        tested = OperationalActor()
        value = OperationalActivity()
        tested.get_allocated_operational_activities().add(value)
        pass

    def test_OperationalActor_involving_operational_capabilities_getter(self):
        tested = OperationalActor()
        tested.get_involving_operational_capabilities()
        pass

    def test_OperationalActor_involving_operational_capabilities_setter(self):
        tested = OperationalActor()
        value = OperationalCapability()
        tested.get_involving_operational_capabilities().add(value)
        pass

    def test_OperationalActor_owned_state_machines_getter(self):
        tested = OperationalActor()
        tested.get_owned_state_machines()
        pass

    def test_OperationalActor_realizing_system_actors_getter(self):
        tested = OperationalActor()
        tested.get_realizing_system_actors()
        pass

    def test_OperationalActor_realizing_system_actors_setter(self):
        tested = OperationalActor()
        value = SystemActor()
        tested.get_realizing_system_actors().add(value)
        pass

    def test_CommunicationMean_id_getter(self):
        tested = CommunicationMean()
        tested.get_id()
        pass

    def test_CommunicationMean_id_setter(self):
        tested = CommunicationMean()
        value = "value"
        tested.set_id(value)
        pass

    def test_CommunicationMean_sid_getter(self):
        tested = CommunicationMean()
        tested.get_sid()
        pass

    def test_CommunicationMean_sid_setter(self):
        tested = CommunicationMean()
        value = "value"
        tested.set_sid(value)
        pass

    def test_CommunicationMean_name_getter(self):
        tested = CommunicationMean()
        tested.get_name()
        pass

    def test_CommunicationMean_name_setter(self):
        tested = CommunicationMean()
        value = "value"
        tested.set_name(value)
        pass

    def test_CommunicationMean_summary_getter(self):
        tested = CommunicationMean()
        tested.get_summary()
        pass

    def test_CommunicationMean_summary_setter(self):
        tested = CommunicationMean()
        value = "value"
        tested.set_summary(value)
        pass

    def test_CommunicationMean_description_getter(self):
        tested = CommunicationMean()
        tested.get_description()
        pass

    def test_CommunicationMean_description_setter(self):
        tested = CommunicationMean()
        value = "value"
        tested.set_description(value)
        pass

    def test_CommunicationMean_status_getter(self):
        tested = CommunicationMean()
        tested.get_status()
        pass

    def test_CommunicationMean_status_setter(self):
        tested = CommunicationMean()
        value = "value"
        tested.set_status(value)
        pass

    def test_CommunicationMean_review_getter(self):
        tested = CommunicationMean()
        tested.get_review()
        pass

    def test_CommunicationMean_review_setter(self):
        tested = CommunicationMean()
        value = "value"
        tested.set_review(value)
        pass

    def test_CommunicationMean_visible_in_documentation_getter(self):
        tested = CommunicationMean()
        tested.get_visible_in_documentation()
        pass

    def test_CommunicationMean_visible_in_documentation_setter(self):
        tested = CommunicationMean()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_CommunicationMean_visible_for_traceability_getter(self):
        tested = CommunicationMean()
        tested.get_visible_for_traceability()
        pass

    def test_CommunicationMean_visible_for_traceability_setter(self):
        tested = CommunicationMean()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_CommunicationMean_owned_constraints_getter(self):
        tested = CommunicationMean()
        tested.get_owned_constraints()
        pass

    def test_CommunicationMean_constraints_getter(self):
        tested = CommunicationMean()
        tested.get_constraints()
        pass

    def test_CommunicationMean_constraints_setter(self):
        tested = CommunicationMean()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_CommunicationMean_owned_property_values_getter(self):
        tested = CommunicationMean()
        tested.get_owned_property_values()
        pass

    def test_CommunicationMean_applied_property_values_getter(self):
        tested = CommunicationMean()
        tested.get_applied_property_values()
        pass

    def test_CommunicationMean_applied_property_values_setter(self):
        tested = CommunicationMean()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_CommunicationMean_owned_property_value_groups_getter(self):
        tested = CommunicationMean()
        tested.get_owned_property_value_groups()
        pass

    def test_CommunicationMean_applied_property_value_groups_getter(self):
        tested = CommunicationMean()
        tested.get_applied_property_value_groups()
        pass

    def test_CommunicationMean_applied_property_value_groups_setter(self):
        tested = CommunicationMean()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_CommunicationMean_owned_enumeration_property_types_getter(self):
        tested = CommunicationMean()
        tested.get_owned_enumeration_property_types()
        pass

    def test_CommunicationMean_owned_diagrams_getter(self):
        tested = CommunicationMean()
        tested.get_owned_diagrams()
        pass

    def test_CommunicationMean_element_of_interest_for_diagrams_getter(self):
        tested = CommunicationMean()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_CommunicationMean_element_of_interest_for_diagrams_setter(self):
        tested = CommunicationMean()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_CommunicationMean_contextual_element_for_diagrams_getter(self):
        tested = CommunicationMean()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_CommunicationMean_contextual_element_for_diagrams_setter(self):
        tested = CommunicationMean()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_CommunicationMean_representing_diagrams_getter(self):
        tested = CommunicationMean()
        tested.get_representing_diagrams()
        pass

    def test_CommunicationMean__r_e_cs_getter(self):
        tested = CommunicationMean()
        tested.get__r_e_cs()
        pass

    def test_CommunicationMean__r_e_cs_setter(self):
        tested = CommunicationMean()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_CommunicationMean__r_p_ls_getter(self):
        tested = CommunicationMean()
        tested.get__r_p_ls()
        pass

    def test_CommunicationMean__r_p_ls_setter(self):
        tested = CommunicationMean()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_CommunicationMean_get_label(self):
        tested = CommunicationMean()
        tested.get_label()
        pass

    def test_CommunicationMean_get_element_type(self):
        tested = CommunicationMean()
        tested.get_element_type()
        pass

    def test_CommunicationMean_get_container(self):
        tested = CommunicationMean()
        tested.get_container()
        pass

    def test_CommunicationMean_get_contents(self):
        tested = CommunicationMean()
        tested.get_contents()
        pass

    def test_CommunicationMean_get_all_contents(self):
        tested = CommunicationMean()
        tested.get_all_contents()
        pass

    def test_CommunicationMean_get_all_contents_by_type(self):
        tested = CommunicationMean()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_CommunicationMean_get_available_s_b_queries(self):
        tested = CommunicationMean()
        tested.get_available_s_b_queries()
        pass

    def test_CommunicationMean_get_query_result(self):
        tested = CommunicationMean()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_CommunicationMean_source_entity_getter(self):
        tested = CommunicationMean()
        tested.get_source_entity()
        pass

    def test_CommunicationMean_source_entity_setter(self):
        tested = CommunicationMean()
        value = OperationalActor()
        tested.set_source_entity(value)
        pass

    def test_CommunicationMean_target_entity_getter(self):
        tested = CommunicationMean()
        tested.get_target_entity()
        pass

    def test_CommunicationMean_target_entity_setter(self):
        tested = CommunicationMean()
        value = OperationalActor()
        tested.set_target_entity(value)
        pass

    def test_CommunicationMean_allocated_interactions_getter(self):
        tested = CommunicationMean()
        tested.get_allocated_interactions()
        pass

    def test_CommunicationMean_allocated_interactions_setter(self):
        tested = CommunicationMean()
        value = Interaction()
        tested.get_allocated_interactions().add(value)
        pass

    def test_CommunicationMean_convoyed_informations_getter(self):
        tested = CommunicationMean()
        tested.get_convoyed_informations()
        pass

    def test_CommunicationMean_convoyed_informations_setter(self):
        tested = CommunicationMean()
        value = ExchangeItem()
        tested.get_convoyed_informations().add(value)
        pass

    def test_CommunicationMean_realizing_component_exchanges_getter(self):
        tested = CommunicationMean()
        tested.get_realizing_component_exchanges()
        pass

    def test_CommunicationMean_realizing_component_exchanges_setter(self):
        tested = CommunicationMean()
        value = ComponentExchange()
        tested.get_realizing_component_exchanges().add(value)
        pass

    def test_SystemAnalysis_owned_property_value_pkgs_getter(self):
        tested = SystemAnalysis()
        tested.get_owned_property_value_pkgs()
        pass

    def test_SystemAnalysis_id_getter(self):
        tested = SystemAnalysis()
        tested.get_id()
        pass

    def test_SystemAnalysis_id_setter(self):
        tested = SystemAnalysis()
        value = "value"
        tested.set_id(value)
        pass

    def test_SystemAnalysis_sid_getter(self):
        tested = SystemAnalysis()
        tested.get_sid()
        pass

    def test_SystemAnalysis_sid_setter(self):
        tested = SystemAnalysis()
        value = "value"
        tested.set_sid(value)
        pass

    def test_SystemAnalysis_name_getter(self):
        tested = SystemAnalysis()
        tested.get_name()
        pass

    def test_SystemAnalysis_name_setter(self):
        tested = SystemAnalysis()
        value = "value"
        tested.set_name(value)
        pass

    def test_SystemAnalysis_summary_getter(self):
        tested = SystemAnalysis()
        tested.get_summary()
        pass

    def test_SystemAnalysis_summary_setter(self):
        tested = SystemAnalysis()
        value = "value"
        tested.set_summary(value)
        pass

    def test_SystemAnalysis_description_getter(self):
        tested = SystemAnalysis()
        tested.get_description()
        pass

    def test_SystemAnalysis_description_setter(self):
        tested = SystemAnalysis()
        value = "value"
        tested.set_description(value)
        pass

    def test_SystemAnalysis_status_getter(self):
        tested = SystemAnalysis()
        tested.get_status()
        pass

    def test_SystemAnalysis_status_setter(self):
        tested = SystemAnalysis()
        value = "value"
        tested.set_status(value)
        pass

    def test_SystemAnalysis_review_getter(self):
        tested = SystemAnalysis()
        tested.get_review()
        pass

    def test_SystemAnalysis_review_setter(self):
        tested = SystemAnalysis()
        value = "value"
        tested.set_review(value)
        pass

    def test_SystemAnalysis_visible_in_documentation_getter(self):
        tested = SystemAnalysis()
        tested.get_visible_in_documentation()
        pass

    def test_SystemAnalysis_visible_in_documentation_setter(self):
        tested = SystemAnalysis()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_SystemAnalysis_visible_for_traceability_getter(self):
        tested = SystemAnalysis()
        tested.get_visible_for_traceability()
        pass

    def test_SystemAnalysis_visible_for_traceability_setter(self):
        tested = SystemAnalysis()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_SystemAnalysis_owned_constraints_getter(self):
        tested = SystemAnalysis()
        tested.get_owned_constraints()
        pass

    def test_SystemAnalysis_constraints_getter(self):
        tested = SystemAnalysis()
        tested.get_constraints()
        pass

    def test_SystemAnalysis_constraints_setter(self):
        tested = SystemAnalysis()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_SystemAnalysis_owned_property_values_getter(self):
        tested = SystemAnalysis()
        tested.get_owned_property_values()
        pass

    def test_SystemAnalysis_applied_property_values_getter(self):
        tested = SystemAnalysis()
        tested.get_applied_property_values()
        pass

    def test_SystemAnalysis_applied_property_values_setter(self):
        tested = SystemAnalysis()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_SystemAnalysis_owned_property_value_groups_getter(self):
        tested = SystemAnalysis()
        tested.get_owned_property_value_groups()
        pass

    def test_SystemAnalysis_applied_property_value_groups_getter(self):
        tested = SystemAnalysis()
        tested.get_applied_property_value_groups()
        pass

    def test_SystemAnalysis_applied_property_value_groups_setter(self):
        tested = SystemAnalysis()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_SystemAnalysis_owned_enumeration_property_types_getter(self):
        tested = SystemAnalysis()
        tested.get_owned_enumeration_property_types()
        pass

    def test_SystemAnalysis_owned_diagrams_getter(self):
        tested = SystemAnalysis()
        tested.get_owned_diagrams()
        pass

    def test_SystemAnalysis_element_of_interest_for_diagrams_getter(self):
        tested = SystemAnalysis()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_SystemAnalysis_element_of_interest_for_diagrams_setter(self):
        tested = SystemAnalysis()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_SystemAnalysis_contextual_element_for_diagrams_getter(self):
        tested = SystemAnalysis()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_SystemAnalysis_contextual_element_for_diagrams_setter(self):
        tested = SystemAnalysis()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_SystemAnalysis_representing_diagrams_getter(self):
        tested = SystemAnalysis()
        tested.get_representing_diagrams()
        pass

    def test_SystemAnalysis__r_e_cs_getter(self):
        tested = SystemAnalysis()
        tested.get__r_e_cs()
        pass

    def test_SystemAnalysis__r_e_cs_setter(self):
        tested = SystemAnalysis()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_SystemAnalysis__r_p_ls_getter(self):
        tested = SystemAnalysis()
        tested.get__r_p_ls()
        pass

    def test_SystemAnalysis__r_p_ls_setter(self):
        tested = SystemAnalysis()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_SystemAnalysis_get_label(self):
        tested = SystemAnalysis()
        tested.get_label()
        pass

    def test_SystemAnalysis_get_element_type(self):
        tested = SystemAnalysis()
        tested.get_element_type()
        pass

    def test_SystemAnalysis_get_container(self):
        tested = SystemAnalysis()
        tested.get_container()
        pass

    def test_SystemAnalysis_get_contents(self):
        tested = SystemAnalysis()
        tested.get_contents()
        pass

    def test_SystemAnalysis_get_all_contents(self):
        tested = SystemAnalysis()
        tested.get_all_contents()
        pass

    def test_SystemAnalysis_get_all_contents_by_type(self):
        tested = SystemAnalysis()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_SystemAnalysis_get_available_s_b_queries(self):
        tested = SystemAnalysis()
        tested.get_available_s_b_queries()
        pass

    def test_SystemAnalysis_get_query_result(self):
        tested = SystemAnalysis()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_SystemAnalysis_system_function_pkg_getter(self):
        tested = SystemAnalysis()
        tested.get_system_function_pkg()
        pass

    def test_SystemAnalysis_capability_pkg_getter(self):
        tested = SystemAnalysis()
        tested.get_capability_pkg()
        pass

    def test_SystemAnalysis_interface_pkg_getter(self):
        tested = SystemAnalysis()
        tested.get_interface_pkg()
        pass

    def test_SystemAnalysis_data_pkg_getter(self):
        tested = SystemAnalysis()
        tested.get_data_pkg()
        pass

    def test_SystemAnalysis_system_component_pkg_getter(self):
        tested = SystemAnalysis()
        tested.get_system_component_pkg()
        pass

    def test_SystemAnalysis_mission_pkg_getter(self):
        tested = SystemAnalysis()
        tested.get_mission_pkg()
        pass

    def test_SystemAnalysis_system_getter(self):
        tested = SystemAnalysis()
        tested.get_system()
        pass

    def test_SystemFunctionPkg_owned_property_value_pkgs_getter(self):
        tested = SystemFunctionPkg()
        tested.get_owned_property_value_pkgs()
        pass

    def test_SystemFunctionPkg_id_getter(self):
        tested = SystemFunctionPkg()
        tested.get_id()
        pass

    def test_SystemFunctionPkg_id_setter(self):
        tested = SystemFunctionPkg()
        value = "value"
        tested.set_id(value)
        pass

    def test_SystemFunctionPkg_sid_getter(self):
        tested = SystemFunctionPkg()
        tested.get_sid()
        pass

    def test_SystemFunctionPkg_sid_setter(self):
        tested = SystemFunctionPkg()
        value = "value"
        tested.set_sid(value)
        pass

    def test_SystemFunctionPkg_name_getter(self):
        tested = SystemFunctionPkg()
        tested.get_name()
        pass

    def test_SystemFunctionPkg_name_setter(self):
        tested = SystemFunctionPkg()
        value = "value"
        tested.set_name(value)
        pass

    def test_SystemFunctionPkg_summary_getter(self):
        tested = SystemFunctionPkg()
        tested.get_summary()
        pass

    def test_SystemFunctionPkg_summary_setter(self):
        tested = SystemFunctionPkg()
        value = "value"
        tested.set_summary(value)
        pass

    def test_SystemFunctionPkg_description_getter(self):
        tested = SystemFunctionPkg()
        tested.get_description()
        pass

    def test_SystemFunctionPkg_description_setter(self):
        tested = SystemFunctionPkg()
        value = "value"
        tested.set_description(value)
        pass

    def test_SystemFunctionPkg_status_getter(self):
        tested = SystemFunctionPkg()
        tested.get_status()
        pass

    def test_SystemFunctionPkg_status_setter(self):
        tested = SystemFunctionPkg()
        value = "value"
        tested.set_status(value)
        pass

    def test_SystemFunctionPkg_review_getter(self):
        tested = SystemFunctionPkg()
        tested.get_review()
        pass

    def test_SystemFunctionPkg_review_setter(self):
        tested = SystemFunctionPkg()
        value = "value"
        tested.set_review(value)
        pass

    def test_SystemFunctionPkg_visible_in_documentation_getter(self):
        tested = SystemFunctionPkg()
        tested.get_visible_in_documentation()
        pass

    def test_SystemFunctionPkg_visible_in_documentation_setter(self):
        tested = SystemFunctionPkg()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_SystemFunctionPkg_visible_for_traceability_getter(self):
        tested = SystemFunctionPkg()
        tested.get_visible_for_traceability()
        pass

    def test_SystemFunctionPkg_visible_for_traceability_setter(self):
        tested = SystemFunctionPkg()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_SystemFunctionPkg_owned_constraints_getter(self):
        tested = SystemFunctionPkg()
        tested.get_owned_constraints()
        pass

    def test_SystemFunctionPkg_constraints_getter(self):
        tested = SystemFunctionPkg()
        tested.get_constraints()
        pass

    def test_SystemFunctionPkg_constraints_setter(self):
        tested = SystemFunctionPkg()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_SystemFunctionPkg_owned_property_values_getter(self):
        tested = SystemFunctionPkg()
        tested.get_owned_property_values()
        pass

    def test_SystemFunctionPkg_applied_property_values_getter(self):
        tested = SystemFunctionPkg()
        tested.get_applied_property_values()
        pass

    def test_SystemFunctionPkg_applied_property_values_setter(self):
        tested = SystemFunctionPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_SystemFunctionPkg_owned_property_value_groups_getter(self):
        tested = SystemFunctionPkg()
        tested.get_owned_property_value_groups()
        pass

    def test_SystemFunctionPkg_applied_property_value_groups_getter(self):
        tested = SystemFunctionPkg()
        tested.get_applied_property_value_groups()
        pass

    def test_SystemFunctionPkg_applied_property_value_groups_setter(self):
        tested = SystemFunctionPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_SystemFunctionPkg_owned_enumeration_property_types_getter(self):
        tested = SystemFunctionPkg()
        tested.get_owned_enumeration_property_types()
        pass

    def test_SystemFunctionPkg_owned_diagrams_getter(self):
        tested = SystemFunctionPkg()
        tested.get_owned_diagrams()
        pass

    def test_SystemFunctionPkg_element_of_interest_for_diagrams_getter(self):
        tested = SystemFunctionPkg()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_SystemFunctionPkg_element_of_interest_for_diagrams_setter(self):
        tested = SystemFunctionPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_SystemFunctionPkg_contextual_element_for_diagrams_getter(self):
        tested = SystemFunctionPkg()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_SystemFunctionPkg_contextual_element_for_diagrams_setter(self):
        tested = SystemFunctionPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_SystemFunctionPkg_representing_diagrams_getter(self):
        tested = SystemFunctionPkg()
        tested.get_representing_diagrams()
        pass

    def test_SystemFunctionPkg__r_e_cs_getter(self):
        tested = SystemFunctionPkg()
        tested.get__r_e_cs()
        pass

    def test_SystemFunctionPkg__r_e_cs_setter(self):
        tested = SystemFunctionPkg()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_SystemFunctionPkg__r_p_ls_getter(self):
        tested = SystemFunctionPkg()
        tested.get__r_p_ls()
        pass

    def test_SystemFunctionPkg__r_p_ls_setter(self):
        tested = SystemFunctionPkg()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_SystemFunctionPkg_get_label(self):
        tested = SystemFunctionPkg()
        tested.get_label()
        pass

    def test_SystemFunctionPkg_get_element_type(self):
        tested = SystemFunctionPkg()
        tested.get_element_type()
        pass

    def test_SystemFunctionPkg_get_container(self):
        tested = SystemFunctionPkg()
        tested.get_container()
        pass

    def test_SystemFunctionPkg_get_contents(self):
        tested = SystemFunctionPkg()
        tested.get_contents()
        pass

    def test_SystemFunctionPkg_get_all_contents(self):
        tested = SystemFunctionPkg()
        tested.get_all_contents()
        pass

    def test_SystemFunctionPkg_get_all_contents_by_type(self):
        tested = SystemFunctionPkg()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_SystemFunctionPkg_get_available_s_b_queries(self):
        tested = SystemFunctionPkg()
        tested.get_available_s_b_queries()
        pass

    def test_SystemFunctionPkg_get_query_result(self):
        tested = SystemFunctionPkg()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_SystemFunctionPkg_owned_system_function_pkgs_getter(self):
        tested = SystemFunctionPkg()
        tested.get_owned_system_function_pkgs()
        pass

    def test_SystemFunctionPkg_owned_system_functions_getter(self):
        tested = SystemFunctionPkg()
        tested.get_owned_system_functions()
        pass

    def test_SystemFunctionPkg_owned_categories_getter(self):
        tested = SystemFunctionPkg()
        tested.get_owned_categories()
        pass

    def test_SystemFunction_kind_getter(self):
        tested = SystemFunction()
        tested.get_kind()
        pass

    def test_SystemFunction_kind_setter(self):
        tested = SystemFunction()
        value = FunctionKind()
        tested.set_kind(value)
        pass

    def test_SystemFunction_condition_getter(self):
        tested = SystemFunction()
        tested.get_condition()
        pass

    def test_SystemFunction_condition_setter(self):
        tested = SystemFunction()
        value = "value"
        tested.set_condition(value)
        pass

    def test_SystemFunction_inputs_getter(self):
        tested = SystemFunction()
        tested.get_inputs()
        pass

    def test_SystemFunction_outputs_getter(self):
        tested = SystemFunction()
        tested.get_outputs()
        pass

    def test_SystemFunction_incoming_getter(self):
        tested = SystemFunction()
        tested.get_incoming()
        pass

    def test_SystemFunction_incoming_setter(self):
        tested = SystemFunction()
        value = FunctionalExchange()
        tested.get_incoming().add(value)
        pass

    def test_SystemFunction_outgoing_getter(self):
        tested = SystemFunction()
        tested.get_outgoing()
        pass

    def test_SystemFunction_outgoing_setter(self):
        tested = SystemFunction()
        value = FunctionalExchange()
        tested.get_outgoing().add(value)
        pass

    def test_SystemFunction_allocating_component_getter(self):
        tested = SystemFunction()
        tested.get_allocating_component()
        pass

    def test_SystemFunction_allocating_component_setter(self):
        tested = SystemFunction()
        value = PhysicalActor()
        tested.set_allocating_component(value)
        pass

    def test_SystemFunction_owned_functional_chains_getter(self):
        tested = SystemFunction()
        tested.get_owned_functional_chains()
        pass

    def test_SystemFunction_involving_functional_chains_getter(self):
        tested = SystemFunction()
        tested.get_involving_functional_chains()
        pass

    def test_SystemFunction_involving_capabilities_getter(self):
        tested = SystemFunction()
        tested.get_involving_capabilities()
        pass

    def test_SystemFunction_involving_capabilities_setter(self):
        tested = SystemFunction()
        value = CapabilityRealization()
        tested.get_involving_capabilities().add(value)
        pass

    def test_SystemFunction_available_in_states_getter(self):
        tested = SystemFunction()
        tested.get_available_in_states()
        pass

    def test_SystemFunction_available_in_states_setter(self):
        tested = SystemFunction()
        value = State()
        tested.get_available_in_states().add(value)
        pass

    def test_SystemFunction_id_getter(self):
        tested = SystemFunction()
        tested.get_id()
        pass

    def test_SystemFunction_id_setter(self):
        tested = SystemFunction()
        value = "value"
        tested.set_id(value)
        pass

    def test_SystemFunction_sid_getter(self):
        tested = SystemFunction()
        tested.get_sid()
        pass

    def test_SystemFunction_sid_setter(self):
        tested = SystemFunction()
        value = "value"
        tested.set_sid(value)
        pass

    def test_SystemFunction_name_getter(self):
        tested = SystemFunction()
        tested.get_name()
        pass

    def test_SystemFunction_name_setter(self):
        tested = SystemFunction()
        value = "value"
        tested.set_name(value)
        pass

    def test_SystemFunction_summary_getter(self):
        tested = SystemFunction()
        tested.get_summary()
        pass

    def test_SystemFunction_summary_setter(self):
        tested = SystemFunction()
        value = "value"
        tested.set_summary(value)
        pass

    def test_SystemFunction_description_getter(self):
        tested = SystemFunction()
        tested.get_description()
        pass

    def test_SystemFunction_description_setter(self):
        tested = SystemFunction()
        value = "value"
        tested.set_description(value)
        pass

    def test_SystemFunction_status_getter(self):
        tested = SystemFunction()
        tested.get_status()
        pass

    def test_SystemFunction_status_setter(self):
        tested = SystemFunction()
        value = "value"
        tested.set_status(value)
        pass

    def test_SystemFunction_review_getter(self):
        tested = SystemFunction()
        tested.get_review()
        pass

    def test_SystemFunction_review_setter(self):
        tested = SystemFunction()
        value = "value"
        tested.set_review(value)
        pass

    def test_SystemFunction_visible_in_documentation_getter(self):
        tested = SystemFunction()
        tested.get_visible_in_documentation()
        pass

    def test_SystemFunction_visible_in_documentation_setter(self):
        tested = SystemFunction()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_SystemFunction_visible_for_traceability_getter(self):
        tested = SystemFunction()
        tested.get_visible_for_traceability()
        pass

    def test_SystemFunction_visible_for_traceability_setter(self):
        tested = SystemFunction()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_SystemFunction_owned_constraints_getter(self):
        tested = SystemFunction()
        tested.get_owned_constraints()
        pass

    def test_SystemFunction_constraints_getter(self):
        tested = SystemFunction()
        tested.get_constraints()
        pass

    def test_SystemFunction_constraints_setter(self):
        tested = SystemFunction()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_SystemFunction_owned_property_values_getter(self):
        tested = SystemFunction()
        tested.get_owned_property_values()
        pass

    def test_SystemFunction_applied_property_values_getter(self):
        tested = SystemFunction()
        tested.get_applied_property_values()
        pass

    def test_SystemFunction_applied_property_values_setter(self):
        tested = SystemFunction()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_SystemFunction_owned_property_value_groups_getter(self):
        tested = SystemFunction()
        tested.get_owned_property_value_groups()
        pass

    def test_SystemFunction_applied_property_value_groups_getter(self):
        tested = SystemFunction()
        tested.get_applied_property_value_groups()
        pass

    def test_SystemFunction_applied_property_value_groups_setter(self):
        tested = SystemFunction()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_SystemFunction_owned_enumeration_property_types_getter(self):
        tested = SystemFunction()
        tested.get_owned_enumeration_property_types()
        pass

    def test_SystemFunction_owned_diagrams_getter(self):
        tested = SystemFunction()
        tested.get_owned_diagrams()
        pass

    def test_SystemFunction_element_of_interest_for_diagrams_getter(self):
        tested = SystemFunction()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_SystemFunction_element_of_interest_for_diagrams_setter(self):
        tested = SystemFunction()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_SystemFunction_contextual_element_for_diagrams_getter(self):
        tested = SystemFunction()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_SystemFunction_contextual_element_for_diagrams_setter(self):
        tested = SystemFunction()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_SystemFunction_representing_diagrams_getter(self):
        tested = SystemFunction()
        tested.get_representing_diagrams()
        pass

    def test_SystemFunction__r_e_cs_getter(self):
        tested = SystemFunction()
        tested.get__r_e_cs()
        pass

    def test_SystemFunction__r_e_cs_setter(self):
        tested = SystemFunction()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_SystemFunction__r_p_ls_getter(self):
        tested = SystemFunction()
        tested.get__r_p_ls()
        pass

    def test_SystemFunction__r_p_ls_setter(self):
        tested = SystemFunction()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_SystemFunction_get_label(self):
        tested = SystemFunction()
        tested.get_label()
        pass

    def test_SystemFunction_get_element_type(self):
        tested = SystemFunction()
        tested.get_element_type()
        pass

    def test_SystemFunction_get_container(self):
        tested = SystemFunction()
        tested.get_container()
        pass

    def test_SystemFunction_get_contents(self):
        tested = SystemFunction()
        tested.get_contents()
        pass

    def test_SystemFunction_get_all_contents(self):
        tested = SystemFunction()
        tested.get_all_contents()
        pass

    def test_SystemFunction_get_all_contents_by_type(self):
        tested = SystemFunction()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_SystemFunction_get_available_s_b_queries(self):
        tested = SystemFunction()
        tested.get_available_s_b_queries()
        pass

    def test_SystemFunction_get_query_result(self):
        tested = SystemFunction()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_SystemFunction_contained_system_functions_getter(self):
        tested = SystemFunction()
        tested.get_contained_system_functions()
        pass

    def test_SystemFunction_owned_system_function_pkgs_getter(self):
        tested = SystemFunction()
        tested.get_owned_system_function_pkgs()
        pass

    def test_SystemFunction_realized_operational_activities_getter(self):
        tested = SystemFunction()
        tested.get_realized_operational_activities()
        pass

    def test_SystemFunction_realized_operational_activities_setter(self):
        tested = SystemFunction()
        value = OperationalActivity()
        tested.get_realized_operational_activities().add(value)
        pass

    def test_SystemFunction_realizing_logical_functions_getter(self):
        tested = SystemFunction()
        tested.get_realizing_logical_functions()
        pass

    def test_SystemFunction_realizing_logical_functions_setter(self):
        tested = SystemFunction()
        value = LogicalFunction()
        tested.get_realizing_logical_functions().add(value)
        pass

    def test_CapabilityPkg_owned_property_value_pkgs_getter(self):
        tested = CapabilityPkg()
        tested.get_owned_property_value_pkgs()
        pass

    def test_CapabilityPkg_id_getter(self):
        tested = CapabilityPkg()
        tested.get_id()
        pass

    def test_CapabilityPkg_id_setter(self):
        tested = CapabilityPkg()
        value = "value"
        tested.set_id(value)
        pass

    def test_CapabilityPkg_sid_getter(self):
        tested = CapabilityPkg()
        tested.get_sid()
        pass

    def test_CapabilityPkg_sid_setter(self):
        tested = CapabilityPkg()
        value = "value"
        tested.set_sid(value)
        pass

    def test_CapabilityPkg_name_getter(self):
        tested = CapabilityPkg()
        tested.get_name()
        pass

    def test_CapabilityPkg_name_setter(self):
        tested = CapabilityPkg()
        value = "value"
        tested.set_name(value)
        pass

    def test_CapabilityPkg_summary_getter(self):
        tested = CapabilityPkg()
        tested.get_summary()
        pass

    def test_CapabilityPkg_summary_setter(self):
        tested = CapabilityPkg()
        value = "value"
        tested.set_summary(value)
        pass

    def test_CapabilityPkg_description_getter(self):
        tested = CapabilityPkg()
        tested.get_description()
        pass

    def test_CapabilityPkg_description_setter(self):
        tested = CapabilityPkg()
        value = "value"
        tested.set_description(value)
        pass

    def test_CapabilityPkg_status_getter(self):
        tested = CapabilityPkg()
        tested.get_status()
        pass

    def test_CapabilityPkg_status_setter(self):
        tested = CapabilityPkg()
        value = "value"
        tested.set_status(value)
        pass

    def test_CapabilityPkg_review_getter(self):
        tested = CapabilityPkg()
        tested.get_review()
        pass

    def test_CapabilityPkg_review_setter(self):
        tested = CapabilityPkg()
        value = "value"
        tested.set_review(value)
        pass

    def test_CapabilityPkg_visible_in_documentation_getter(self):
        tested = CapabilityPkg()
        tested.get_visible_in_documentation()
        pass

    def test_CapabilityPkg_visible_in_documentation_setter(self):
        tested = CapabilityPkg()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_CapabilityPkg_visible_for_traceability_getter(self):
        tested = CapabilityPkg()
        tested.get_visible_for_traceability()
        pass

    def test_CapabilityPkg_visible_for_traceability_setter(self):
        tested = CapabilityPkg()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_CapabilityPkg_owned_constraints_getter(self):
        tested = CapabilityPkg()
        tested.get_owned_constraints()
        pass

    def test_CapabilityPkg_constraints_getter(self):
        tested = CapabilityPkg()
        tested.get_constraints()
        pass

    def test_CapabilityPkg_constraints_setter(self):
        tested = CapabilityPkg()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_CapabilityPkg_owned_property_values_getter(self):
        tested = CapabilityPkg()
        tested.get_owned_property_values()
        pass

    def test_CapabilityPkg_applied_property_values_getter(self):
        tested = CapabilityPkg()
        tested.get_applied_property_values()
        pass

    def test_CapabilityPkg_applied_property_values_setter(self):
        tested = CapabilityPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_CapabilityPkg_owned_property_value_groups_getter(self):
        tested = CapabilityPkg()
        tested.get_owned_property_value_groups()
        pass

    def test_CapabilityPkg_applied_property_value_groups_getter(self):
        tested = CapabilityPkg()
        tested.get_applied_property_value_groups()
        pass

    def test_CapabilityPkg_applied_property_value_groups_setter(self):
        tested = CapabilityPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_CapabilityPkg_owned_enumeration_property_types_getter(self):
        tested = CapabilityPkg()
        tested.get_owned_enumeration_property_types()
        pass

    def test_CapabilityPkg_owned_diagrams_getter(self):
        tested = CapabilityPkg()
        tested.get_owned_diagrams()
        pass

    def test_CapabilityPkg_element_of_interest_for_diagrams_getter(self):
        tested = CapabilityPkg()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_CapabilityPkg_element_of_interest_for_diagrams_setter(self):
        tested = CapabilityPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_CapabilityPkg_contextual_element_for_diagrams_getter(self):
        tested = CapabilityPkg()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_CapabilityPkg_contextual_element_for_diagrams_setter(self):
        tested = CapabilityPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_CapabilityPkg_representing_diagrams_getter(self):
        tested = CapabilityPkg()
        tested.get_representing_diagrams()
        pass

    def test_CapabilityPkg__r_e_cs_getter(self):
        tested = CapabilityPkg()
        tested.get__r_e_cs()
        pass

    def test_CapabilityPkg__r_e_cs_setter(self):
        tested = CapabilityPkg()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_CapabilityPkg__r_p_ls_getter(self):
        tested = CapabilityPkg()
        tested.get__r_p_ls()
        pass

    def test_CapabilityPkg__r_p_ls_setter(self):
        tested = CapabilityPkg()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_CapabilityPkg_get_label(self):
        tested = CapabilityPkg()
        tested.get_label()
        pass

    def test_CapabilityPkg_get_element_type(self):
        tested = CapabilityPkg()
        tested.get_element_type()
        pass

    def test_CapabilityPkg_get_container(self):
        tested = CapabilityPkg()
        tested.get_container()
        pass

    def test_CapabilityPkg_get_contents(self):
        tested = CapabilityPkg()
        tested.get_contents()
        pass

    def test_CapabilityPkg_get_all_contents(self):
        tested = CapabilityPkg()
        tested.get_all_contents()
        pass

    def test_CapabilityPkg_get_all_contents_by_type(self):
        tested = CapabilityPkg()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_CapabilityPkg_get_available_s_b_queries(self):
        tested = CapabilityPkg()
        tested.get_available_s_b_queries()
        pass

    def test_CapabilityPkg_get_query_result(self):
        tested = CapabilityPkg()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_CapabilityPkg_owned_capability_pkgs_getter(self):
        tested = CapabilityPkg()
        tested.get_owned_capability_pkgs()
        pass

    def test_CapabilityPkg_owned_capabilities_getter(self):
        tested = CapabilityPkg()
        tested.get_owned_capabilities()
        pass

    def test_Capability_owned_functional_chains_getter(self):
        tested = Capability()
        tested.get_owned_functional_chains()
        pass

    def test_Capability_involved_functional_chains_getter(self):
        tested = Capability()
        tested.get_involved_functional_chains()
        pass

    def test_Capability_involved_functional_chains_setter(self):
        tested = Capability()
        value = FunctionalChain()
        tested.get_involved_functional_chains().add(value)
        pass

    def test_Capability_involved_functions_getter(self):
        tested = Capability()
        tested.get_involved_functions()
        pass

    def test_Capability_involved_functions_setter(self):
        tested = Capability()
        value = PhysicalFunction()
        tested.get_involved_functions().add(value)
        pass

    def test_Capability_pre_condition_getter(self):
        tested = Capability()
        tested.get_pre_condition()
        pass

    def test_Capability_pre_condition_setter(self):
        tested = Capability()
        value = Constraint()
        tested.set_pre_condition(value)
        pass

    def test_Capability_post_condition_getter(self):
        tested = Capability()
        tested.get_post_condition()
        pass

    def test_Capability_post_condition_setter(self):
        tested = Capability()
        value = Constraint()
        tested.set_post_condition(value)
        pass

    def test_Capability_owned_scenarios_getter(self):
        tested = Capability()
        tested.get_owned_scenarios()
        pass

    def test_Capability_super_getter(self):
        tested = Capability()
        tested.get_super()
        pass

    def test_Capability_super_setter(self):
        tested = Capability()
        value = CapabilityRealization()
        tested.get_super().add(value)
        pass

    def test_Capability_sub_getter(self):
        tested = Capability()
        tested.get_sub()
        pass

    def test_Capability_sub_setter(self):
        tested = Capability()
        value = CapabilityRealization()
        tested.get_sub().add(value)
        pass

    def test_Capability_included_capabilities_getter(self):
        tested = Capability()
        tested.get_included_capabilities()
        pass

    def test_Capability_included_capabilities_setter(self):
        tested = Capability()
        value = CapabilityRealization()
        tested.get_included_capabilities().add(value)
        pass

    def test_Capability_including_capabilities_getter(self):
        tested = Capability()
        tested.get_including_capabilities()
        pass

    def test_Capability_including_capabilities_setter(self):
        tested = Capability()
        value = CapabilityRealization()
        tested.get_including_capabilities().add(value)
        pass

    def test_Capability_extended_capabilities_getter(self):
        tested = Capability()
        tested.get_extended_capabilities()
        pass

    def test_Capability_extended_capabilities_setter(self):
        tested = Capability()
        value = CapabilityRealization()
        tested.get_extended_capabilities().add(value)
        pass

    def test_Capability_extending_capabilities_getter(self):
        tested = Capability()
        tested.get_extending_capabilities()
        pass

    def test_Capability_extending_capabilities_setter(self):
        tested = Capability()
        value = CapabilityRealization()
        tested.get_extending_capabilities().add(value)
        pass

    def test_Capability_available_in_states_getter(self):
        tested = Capability()
        tested.get_available_in_states()
        pass

    def test_Capability_available_in_states_setter(self):
        tested = Capability()
        value = State()
        tested.get_available_in_states().add(value)
        pass

    def test_Capability_owned_property_value_pkgs_getter(self):
        tested = Capability()
        tested.get_owned_property_value_pkgs()
        pass

    def test_Capability_id_getter(self):
        tested = Capability()
        tested.get_id()
        pass

    def test_Capability_id_setter(self):
        tested = Capability()
        value = "value"
        tested.set_id(value)
        pass

    def test_Capability_sid_getter(self):
        tested = Capability()
        tested.get_sid()
        pass

    def test_Capability_sid_setter(self):
        tested = Capability()
        value = "value"
        tested.set_sid(value)
        pass

    def test_Capability_name_getter(self):
        tested = Capability()
        tested.get_name()
        pass

    def test_Capability_name_setter(self):
        tested = Capability()
        value = "value"
        tested.set_name(value)
        pass

    def test_Capability_summary_getter(self):
        tested = Capability()
        tested.get_summary()
        pass

    def test_Capability_summary_setter(self):
        tested = Capability()
        value = "value"
        tested.set_summary(value)
        pass

    def test_Capability_description_getter(self):
        tested = Capability()
        tested.get_description()
        pass

    def test_Capability_description_setter(self):
        tested = Capability()
        value = "value"
        tested.set_description(value)
        pass

    def test_Capability_status_getter(self):
        tested = Capability()
        tested.get_status()
        pass

    def test_Capability_status_setter(self):
        tested = Capability()
        value = "value"
        tested.set_status(value)
        pass

    def test_Capability_review_getter(self):
        tested = Capability()
        tested.get_review()
        pass

    def test_Capability_review_setter(self):
        tested = Capability()
        value = "value"
        tested.set_review(value)
        pass

    def test_Capability_visible_in_documentation_getter(self):
        tested = Capability()
        tested.get_visible_in_documentation()
        pass

    def test_Capability_visible_in_documentation_setter(self):
        tested = Capability()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_Capability_visible_for_traceability_getter(self):
        tested = Capability()
        tested.get_visible_for_traceability()
        pass

    def test_Capability_visible_for_traceability_setter(self):
        tested = Capability()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_Capability_owned_constraints_getter(self):
        tested = Capability()
        tested.get_owned_constraints()
        pass

    def test_Capability_constraints_getter(self):
        tested = Capability()
        tested.get_constraints()
        pass

    def test_Capability_constraints_setter(self):
        tested = Capability()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_Capability_owned_property_values_getter(self):
        tested = Capability()
        tested.get_owned_property_values()
        pass

    def test_Capability_applied_property_values_getter(self):
        tested = Capability()
        tested.get_applied_property_values()
        pass

    def test_Capability_applied_property_values_setter(self):
        tested = Capability()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_Capability_owned_property_value_groups_getter(self):
        tested = Capability()
        tested.get_owned_property_value_groups()
        pass

    def test_Capability_applied_property_value_groups_getter(self):
        tested = Capability()
        tested.get_applied_property_value_groups()
        pass

    def test_Capability_applied_property_value_groups_setter(self):
        tested = Capability()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_Capability_owned_enumeration_property_types_getter(self):
        tested = Capability()
        tested.get_owned_enumeration_property_types()
        pass

    def test_Capability_owned_diagrams_getter(self):
        tested = Capability()
        tested.get_owned_diagrams()
        pass

    def test_Capability_element_of_interest_for_diagrams_getter(self):
        tested = Capability()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_Capability_element_of_interest_for_diagrams_setter(self):
        tested = Capability()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_Capability_contextual_element_for_diagrams_getter(self):
        tested = Capability()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_Capability_contextual_element_for_diagrams_setter(self):
        tested = Capability()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_Capability_representing_diagrams_getter(self):
        tested = Capability()
        tested.get_representing_diagrams()
        pass

    def test_Capability__r_e_cs_getter(self):
        tested = Capability()
        tested.get__r_e_cs()
        pass

    def test_Capability__r_e_cs_setter(self):
        tested = Capability()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_Capability__r_p_ls_getter(self):
        tested = Capability()
        tested.get__r_p_ls()
        pass

    def test_Capability__r_p_ls_setter(self):
        tested = Capability()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_Capability_get_label(self):
        tested = Capability()
        tested.get_label()
        pass

    def test_Capability_get_element_type(self):
        tested = Capability()
        tested.get_element_type()
        pass

    def test_Capability_get_container(self):
        tested = Capability()
        tested.get_container()
        pass

    def test_Capability_get_contents(self):
        tested = Capability()
        tested.get_contents()
        pass

    def test_Capability_get_all_contents(self):
        tested = Capability()
        tested.get_all_contents()
        pass

    def test_Capability_get_all_contents_by_type(self):
        tested = Capability()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_Capability_get_available_s_b_queries(self):
        tested = Capability()
        tested.get_available_s_b_queries()
        pass

    def test_Capability_get_query_result(self):
        tested = Capability()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_Capability_purpose_missions_getter(self):
        tested = Capability()
        tested.get_purpose_missions()
        pass

    def test_Capability_purpose_missions_setter(self):
        tested = Capability()
        value = Mission()
        tested.get_purpose_missions().add(value)
        pass

    def test_Capability_realized_operational_capabilities_getter(self):
        tested = Capability()
        tested.get_realized_operational_capabilities()
        pass

    def test_Capability_realized_operational_capabilities_setter(self):
        tested = Capability()
        value = OperationalCapability()
        tested.get_realized_operational_capabilities().add(value)
        pass

    def test_Capability_realizing_capability_realizations_getter(self):
        tested = Capability()
        tested.get_realizing_capability_realizations()
        pass

    def test_Capability_realizing_capability_realizations_setter(self):
        tested = Capability()
        value = CapabilityRealization()
        tested.get_realizing_capability_realizations().add(value)
        pass

    def test_Capability_involved_system_actors_getter(self):
        tested = Capability()
        tested.get_involved_system_actors()
        pass

    def test_Capability_involved_system_actors_setter(self):
        tested = Capability()
        value = SystemActor()
        tested.get_involved_system_actors().add(value)
        pass

    def test_SystemComponentPkg_owned_property_value_pkgs_getter(self):
        tested = SystemComponentPkg()
        tested.get_owned_property_value_pkgs()
        pass

    def test_SystemComponentPkg_id_getter(self):
        tested = SystemComponentPkg()
        tested.get_id()
        pass

    def test_SystemComponentPkg_id_setter(self):
        tested = SystemComponentPkg()
        value = "value"
        tested.set_id(value)
        pass

    def test_SystemComponentPkg_sid_getter(self):
        tested = SystemComponentPkg()
        tested.get_sid()
        pass

    def test_SystemComponentPkg_sid_setter(self):
        tested = SystemComponentPkg()
        value = "value"
        tested.set_sid(value)
        pass

    def test_SystemComponentPkg_name_getter(self):
        tested = SystemComponentPkg()
        tested.get_name()
        pass

    def test_SystemComponentPkg_name_setter(self):
        tested = SystemComponentPkg()
        value = "value"
        tested.set_name(value)
        pass

    def test_SystemComponentPkg_summary_getter(self):
        tested = SystemComponentPkg()
        tested.get_summary()
        pass

    def test_SystemComponentPkg_summary_setter(self):
        tested = SystemComponentPkg()
        value = "value"
        tested.set_summary(value)
        pass

    def test_SystemComponentPkg_description_getter(self):
        tested = SystemComponentPkg()
        tested.get_description()
        pass

    def test_SystemComponentPkg_description_setter(self):
        tested = SystemComponentPkg()
        value = "value"
        tested.set_description(value)
        pass

    def test_SystemComponentPkg_status_getter(self):
        tested = SystemComponentPkg()
        tested.get_status()
        pass

    def test_SystemComponentPkg_status_setter(self):
        tested = SystemComponentPkg()
        value = "value"
        tested.set_status(value)
        pass

    def test_SystemComponentPkg_review_getter(self):
        tested = SystemComponentPkg()
        tested.get_review()
        pass

    def test_SystemComponentPkg_review_setter(self):
        tested = SystemComponentPkg()
        value = "value"
        tested.set_review(value)
        pass

    def test_SystemComponentPkg_visible_in_documentation_getter(self):
        tested = SystemComponentPkg()
        tested.get_visible_in_documentation()
        pass

    def test_SystemComponentPkg_visible_in_documentation_setter(self):
        tested = SystemComponentPkg()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_SystemComponentPkg_visible_for_traceability_getter(self):
        tested = SystemComponentPkg()
        tested.get_visible_for_traceability()
        pass

    def test_SystemComponentPkg_visible_for_traceability_setter(self):
        tested = SystemComponentPkg()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_SystemComponentPkg_owned_constraints_getter(self):
        tested = SystemComponentPkg()
        tested.get_owned_constraints()
        pass

    def test_SystemComponentPkg_constraints_getter(self):
        tested = SystemComponentPkg()
        tested.get_constraints()
        pass

    def test_SystemComponentPkg_constraints_setter(self):
        tested = SystemComponentPkg()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_SystemComponentPkg_owned_property_values_getter(self):
        tested = SystemComponentPkg()
        tested.get_owned_property_values()
        pass

    def test_SystemComponentPkg_applied_property_values_getter(self):
        tested = SystemComponentPkg()
        tested.get_applied_property_values()
        pass

    def test_SystemComponentPkg_applied_property_values_setter(self):
        tested = SystemComponentPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_SystemComponentPkg_owned_property_value_groups_getter(self):
        tested = SystemComponentPkg()
        tested.get_owned_property_value_groups()
        pass

    def test_SystemComponentPkg_applied_property_value_groups_getter(self):
        tested = SystemComponentPkg()
        tested.get_applied_property_value_groups()
        pass

    def test_SystemComponentPkg_applied_property_value_groups_setter(self):
        tested = SystemComponentPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_SystemComponentPkg_owned_enumeration_property_types_getter(self):
        tested = SystemComponentPkg()
        tested.get_owned_enumeration_property_types()
        pass

    def test_SystemComponentPkg_owned_diagrams_getter(self):
        tested = SystemComponentPkg()
        tested.get_owned_diagrams()
        pass

    def test_SystemComponentPkg_element_of_interest_for_diagrams_getter(self):
        tested = SystemComponentPkg()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_SystemComponentPkg_element_of_interest_for_diagrams_setter(self):
        tested = SystemComponentPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_SystemComponentPkg_contextual_element_for_diagrams_getter(self):
        tested = SystemComponentPkg()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_SystemComponentPkg_contextual_element_for_diagrams_setter(self):
        tested = SystemComponentPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_SystemComponentPkg_representing_diagrams_getter(self):
        tested = SystemComponentPkg()
        tested.get_representing_diagrams()
        pass

    def test_SystemComponentPkg__r_e_cs_getter(self):
        tested = SystemComponentPkg()
        tested.get__r_e_cs()
        pass

    def test_SystemComponentPkg__r_e_cs_setter(self):
        tested = SystemComponentPkg()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_SystemComponentPkg__r_p_ls_getter(self):
        tested = SystemComponentPkg()
        tested.get__r_p_ls()
        pass

    def test_SystemComponentPkg__r_p_ls_setter(self):
        tested = SystemComponentPkg()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_SystemComponentPkg_get_label(self):
        tested = SystemComponentPkg()
        tested.get_label()
        pass

    def test_SystemComponentPkg_get_element_type(self):
        tested = SystemComponentPkg()
        tested.get_element_type()
        pass

    def test_SystemComponentPkg_get_container(self):
        tested = SystemComponentPkg()
        tested.get_container()
        pass

    def test_SystemComponentPkg_get_contents(self):
        tested = SystemComponentPkg()
        tested.get_contents()
        pass

    def test_SystemComponentPkg_get_all_contents(self):
        tested = SystemComponentPkg()
        tested.get_all_contents()
        pass

    def test_SystemComponentPkg_get_all_contents_by_type(self):
        tested = SystemComponentPkg()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_SystemComponentPkg_get_available_s_b_queries(self):
        tested = SystemComponentPkg()
        tested.get_available_s_b_queries()
        pass

    def test_SystemComponentPkg_get_query_result(self):
        tested = SystemComponentPkg()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_SystemComponentPkg_owned_system_component_pkgs_getter(self):
        tested = SystemComponentPkg()
        tested.get_owned_system_component_pkgs()
        pass

    def test_SystemComponentPkg_owned_system_getter(self):
        tested = SystemComponentPkg()
        tested.get_owned_system()
        pass

    def test_SystemComponentPkg_owned_actors_getter(self):
        tested = SystemComponentPkg()
        tested.get_owned_actors()
        pass

    def test_SystemComponentPkg_owned_component_exchange_categories_getter(self):
        tested = SystemComponentPkg()
        tested.get_owned_component_exchange_categories()
        pass

    def test_SystemComponentPkg_owned_physical_link_categories_getter(self):
        tested = SystemComponentPkg()
        tested.get_owned_physical_link_categories()
        pass

    def test_System_contained_component_ports_getter(self):
        tested = System()
        tested.get_contained_component_ports()
        pass

    def test_System_incoming_component_exchanges_getter(self):
        tested = System()
        tested.get_incoming_component_exchanges()
        pass

    def test_System_incoming_component_exchanges_setter(self):
        tested = System()
        value = ComponentExchange()
        tested.get_incoming_component_exchanges().add(value)
        pass

    def test_System_outgoing_component_exchanges_getter(self):
        tested = System()
        tested.get_outgoing_component_exchanges()
        pass

    def test_System_outgoing_component_exchanges_setter(self):
        tested = System()
        value = ComponentExchange()
        tested.get_outgoing_component_exchanges().add(value)
        pass

    def test_System_inout_component_exchanges_getter(self):
        tested = System()
        tested.get_inout_component_exchanges()
        pass

    def test_System_inout_component_exchanges_setter(self):
        tested = System()
        value = ComponentExchange()
        tested.get_inout_component_exchanges().add(value)
        pass

    def test_System_allocated_functions_getter(self):
        tested = System()
        tested.get_allocated_functions()
        pass

    def test_System_allocated_functions_setter(self):
        tested = System()
        value = PhysicalFunction()
        tested.get_allocated_functions().add(value)
        pass

    def test_System_used_interfaces_getter(self):
        tested = System()
        tested.get_used_interfaces()
        pass

    def test_System_used_interfaces_setter(self):
        tested = System()
        value = Interface()
        tested.get_used_interfaces().add(value)
        pass

    def test_System_implemented_interfaces_getter(self):
        tested = System()
        tested.get_implemented_interfaces()
        pass

    def test_System_implemented_interfaces_setter(self):
        tested = System()
        value = Interface()
        tested.get_implemented_interfaces().add(value)
        pass

    def test_System_owned_state_machines_getter(self):
        tested = System()
        tested.get_owned_state_machines()
        pass

    def test_System_owned_component_exchange_categories_getter(self):
        tested = System()
        tested.get_owned_component_exchange_categories()
        pass

    def test_System_id_getter(self):
        tested = System()
        tested.get_id()
        pass

    def test_System_id_setter(self):
        tested = System()
        value = "value"
        tested.set_id(value)
        pass

    def test_System_sid_getter(self):
        tested = System()
        tested.get_sid()
        pass

    def test_System_sid_setter(self):
        tested = System()
        value = "value"
        tested.set_sid(value)
        pass

    def test_System_name_getter(self):
        tested = System()
        tested.get_name()
        pass

    def test_System_name_setter(self):
        tested = System()
        value = "value"
        tested.set_name(value)
        pass

    def test_System_summary_getter(self):
        tested = System()
        tested.get_summary()
        pass

    def test_System_summary_setter(self):
        tested = System()
        value = "value"
        tested.set_summary(value)
        pass

    def test_System_description_getter(self):
        tested = System()
        tested.get_description()
        pass

    def test_System_description_setter(self):
        tested = System()
        value = "value"
        tested.set_description(value)
        pass

    def test_System_status_getter(self):
        tested = System()
        tested.get_status()
        pass

    def test_System_status_setter(self):
        tested = System()
        value = "value"
        tested.set_status(value)
        pass

    def test_System_review_getter(self):
        tested = System()
        tested.get_review()
        pass

    def test_System_review_setter(self):
        tested = System()
        value = "value"
        tested.set_review(value)
        pass

    def test_System_visible_in_documentation_getter(self):
        tested = System()
        tested.get_visible_in_documentation()
        pass

    def test_System_visible_in_documentation_setter(self):
        tested = System()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_System_visible_for_traceability_getter(self):
        tested = System()
        tested.get_visible_for_traceability()
        pass

    def test_System_visible_for_traceability_setter(self):
        tested = System()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_System_owned_constraints_getter(self):
        tested = System()
        tested.get_owned_constraints()
        pass

    def test_System_constraints_getter(self):
        tested = System()
        tested.get_constraints()
        pass

    def test_System_constraints_setter(self):
        tested = System()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_System_owned_property_values_getter(self):
        tested = System()
        tested.get_owned_property_values()
        pass

    def test_System_applied_property_values_getter(self):
        tested = System()
        tested.get_applied_property_values()
        pass

    def test_System_applied_property_values_setter(self):
        tested = System()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_System_owned_property_value_groups_getter(self):
        tested = System()
        tested.get_owned_property_value_groups()
        pass

    def test_System_applied_property_value_groups_getter(self):
        tested = System()
        tested.get_applied_property_value_groups()
        pass

    def test_System_applied_property_value_groups_setter(self):
        tested = System()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_System_owned_enumeration_property_types_getter(self):
        tested = System()
        tested.get_owned_enumeration_property_types()
        pass

    def test_System_owned_diagrams_getter(self):
        tested = System()
        tested.get_owned_diagrams()
        pass

    def test_System_element_of_interest_for_diagrams_getter(self):
        tested = System()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_System_element_of_interest_for_diagrams_setter(self):
        tested = System()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_System_contextual_element_for_diagrams_getter(self):
        tested = System()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_System_contextual_element_for_diagrams_setter(self):
        tested = System()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_System_representing_diagrams_getter(self):
        tested = System()
        tested.get_representing_diagrams()
        pass

    def test_System__r_e_cs_getter(self):
        tested = System()
        tested.get__r_e_cs()
        pass

    def test_System__r_e_cs_setter(self):
        tested = System()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_System__r_p_ls_getter(self):
        tested = System()
        tested.get__r_p_ls()
        pass

    def test_System__r_p_ls_setter(self):
        tested = System()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_System_get_label(self):
        tested = System()
        tested.get_label()
        pass

    def test_System_get_element_type(self):
        tested = System()
        tested.get_element_type()
        pass

    def test_System_get_container(self):
        tested = System()
        tested.get_container()
        pass

    def test_System_get_contents(self):
        tested = System()
        tested.get_contents()
        pass

    def test_System_get_all_contents(self):
        tested = System()
        tested.get_all_contents()
        pass

    def test_System_get_all_contents_by_type(self):
        tested = System()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_System_get_available_s_b_queries(self):
        tested = System()
        tested.get_available_s_b_queries()
        pass

    def test_System_get_query_result(self):
        tested = System()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_System_contained_physical_ports_getter(self):
        tested = System()
        tested.get_contained_physical_ports()
        pass

    def test_System_physical_links_getter(self):
        tested = System()
        tested.get_physical_links()
        pass

    def test_System_physical_links_setter(self):
        tested = System()
        value = PhysicalLink()
        tested.get_physical_links().add(value)
        pass

    def test_System_involving_physical_paths_getter(self):
        tested = System()
        tested.get_involving_physical_paths()
        pass

    def test_System_owned_physical_link_categories_getter(self):
        tested = System()
        tested.get_owned_physical_link_categories()
        pass

    def test_System_owned_physical_paths_getter(self):
        tested = System()
        tested.get_owned_physical_paths()
        pass

    def test_SystemActor_contained_component_ports_getter(self):
        tested = SystemActor()
        tested.get_contained_component_ports()
        pass

    def test_SystemActor_incoming_component_exchanges_getter(self):
        tested = SystemActor()
        tested.get_incoming_component_exchanges()
        pass

    def test_SystemActor_incoming_component_exchanges_setter(self):
        tested = SystemActor()
        value = ComponentExchange()
        tested.get_incoming_component_exchanges().add(value)
        pass

    def test_SystemActor_outgoing_component_exchanges_getter(self):
        tested = SystemActor()
        tested.get_outgoing_component_exchanges()
        pass

    def test_SystemActor_outgoing_component_exchanges_setter(self):
        tested = SystemActor()
        value = ComponentExchange()
        tested.get_outgoing_component_exchanges().add(value)
        pass

    def test_SystemActor_inout_component_exchanges_getter(self):
        tested = SystemActor()
        tested.get_inout_component_exchanges()
        pass

    def test_SystemActor_inout_component_exchanges_setter(self):
        tested = SystemActor()
        value = ComponentExchange()
        tested.get_inout_component_exchanges().add(value)
        pass

    def test_SystemActor_allocated_functions_getter(self):
        tested = SystemActor()
        tested.get_allocated_functions()
        pass

    def test_SystemActor_allocated_functions_setter(self):
        tested = SystemActor()
        value = PhysicalFunction()
        tested.get_allocated_functions().add(value)
        pass

    def test_SystemActor_used_interfaces_getter(self):
        tested = SystemActor()
        tested.get_used_interfaces()
        pass

    def test_SystemActor_used_interfaces_setter(self):
        tested = SystemActor()
        value = Interface()
        tested.get_used_interfaces().add(value)
        pass

    def test_SystemActor_implemented_interfaces_getter(self):
        tested = SystemActor()
        tested.get_implemented_interfaces()
        pass

    def test_SystemActor_implemented_interfaces_setter(self):
        tested = SystemActor()
        value = Interface()
        tested.get_implemented_interfaces().add(value)
        pass

    def test_SystemActor_owned_state_machines_getter(self):
        tested = SystemActor()
        tested.get_owned_state_machines()
        pass

    def test_SystemActor_owned_component_exchange_categories_getter(self):
        tested = SystemActor()
        tested.get_owned_component_exchange_categories()
        pass

    def test_SystemActor_id_getter(self):
        tested = SystemActor()
        tested.get_id()
        pass

    def test_SystemActor_id_setter(self):
        tested = SystemActor()
        value = "value"
        tested.set_id(value)
        pass

    def test_SystemActor_sid_getter(self):
        tested = SystemActor()
        tested.get_sid()
        pass

    def test_SystemActor_sid_setter(self):
        tested = SystemActor()
        value = "value"
        tested.set_sid(value)
        pass

    def test_SystemActor_name_getter(self):
        tested = SystemActor()
        tested.get_name()
        pass

    def test_SystemActor_name_setter(self):
        tested = SystemActor()
        value = "value"
        tested.set_name(value)
        pass

    def test_SystemActor_summary_getter(self):
        tested = SystemActor()
        tested.get_summary()
        pass

    def test_SystemActor_summary_setter(self):
        tested = SystemActor()
        value = "value"
        tested.set_summary(value)
        pass

    def test_SystemActor_description_getter(self):
        tested = SystemActor()
        tested.get_description()
        pass

    def test_SystemActor_description_setter(self):
        tested = SystemActor()
        value = "value"
        tested.set_description(value)
        pass

    def test_SystemActor_status_getter(self):
        tested = SystemActor()
        tested.get_status()
        pass

    def test_SystemActor_status_setter(self):
        tested = SystemActor()
        value = "value"
        tested.set_status(value)
        pass

    def test_SystemActor_review_getter(self):
        tested = SystemActor()
        tested.get_review()
        pass

    def test_SystemActor_review_setter(self):
        tested = SystemActor()
        value = "value"
        tested.set_review(value)
        pass

    def test_SystemActor_visible_in_documentation_getter(self):
        tested = SystemActor()
        tested.get_visible_in_documentation()
        pass

    def test_SystemActor_visible_in_documentation_setter(self):
        tested = SystemActor()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_SystemActor_visible_for_traceability_getter(self):
        tested = SystemActor()
        tested.get_visible_for_traceability()
        pass

    def test_SystemActor_visible_for_traceability_setter(self):
        tested = SystemActor()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_SystemActor_owned_constraints_getter(self):
        tested = SystemActor()
        tested.get_owned_constraints()
        pass

    def test_SystemActor_constraints_getter(self):
        tested = SystemActor()
        tested.get_constraints()
        pass

    def test_SystemActor_constraints_setter(self):
        tested = SystemActor()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_SystemActor_owned_property_values_getter(self):
        tested = SystemActor()
        tested.get_owned_property_values()
        pass

    def test_SystemActor_applied_property_values_getter(self):
        tested = SystemActor()
        tested.get_applied_property_values()
        pass

    def test_SystemActor_applied_property_values_setter(self):
        tested = SystemActor()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_SystemActor_owned_property_value_groups_getter(self):
        tested = SystemActor()
        tested.get_owned_property_value_groups()
        pass

    def test_SystemActor_applied_property_value_groups_getter(self):
        tested = SystemActor()
        tested.get_applied_property_value_groups()
        pass

    def test_SystemActor_applied_property_value_groups_setter(self):
        tested = SystemActor()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_SystemActor_owned_enumeration_property_types_getter(self):
        tested = SystemActor()
        tested.get_owned_enumeration_property_types()
        pass

    def test_SystemActor_owned_diagrams_getter(self):
        tested = SystemActor()
        tested.get_owned_diagrams()
        pass

    def test_SystemActor_element_of_interest_for_diagrams_getter(self):
        tested = SystemActor()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_SystemActor_element_of_interest_for_diagrams_setter(self):
        tested = SystemActor()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_SystemActor_contextual_element_for_diagrams_getter(self):
        tested = SystemActor()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_SystemActor_contextual_element_for_diagrams_setter(self):
        tested = SystemActor()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_SystemActor_representing_diagrams_getter(self):
        tested = SystemActor()
        tested.get_representing_diagrams()
        pass

    def test_SystemActor__r_e_cs_getter(self):
        tested = SystemActor()
        tested.get__r_e_cs()
        pass

    def test_SystemActor__r_e_cs_setter(self):
        tested = SystemActor()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_SystemActor__r_p_ls_getter(self):
        tested = SystemActor()
        tested.get__r_p_ls()
        pass

    def test_SystemActor__r_p_ls_setter(self):
        tested = SystemActor()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_SystemActor_get_label(self):
        tested = SystemActor()
        tested.get_label()
        pass

    def test_SystemActor_get_element_type(self):
        tested = SystemActor()
        tested.get_element_type()
        pass

    def test_SystemActor_get_container(self):
        tested = SystemActor()
        tested.get_container()
        pass

    def test_SystemActor_get_contents(self):
        tested = SystemActor()
        tested.get_contents()
        pass

    def test_SystemActor_get_all_contents(self):
        tested = SystemActor()
        tested.get_all_contents()
        pass

    def test_SystemActor_get_all_contents_by_type(self):
        tested = SystemActor()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_SystemActor_get_available_s_b_queries(self):
        tested = SystemActor()
        tested.get_available_s_b_queries()
        pass

    def test_SystemActor_get_query_result(self):
        tested = SystemActor()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_SystemActor_contained_physical_ports_getter(self):
        tested = SystemActor()
        tested.get_contained_physical_ports()
        pass

    def test_SystemActor_physical_links_getter(self):
        tested = SystemActor()
        tested.get_physical_links()
        pass

    def test_SystemActor_physical_links_setter(self):
        tested = SystemActor()
        value = PhysicalLink()
        tested.get_physical_links().add(value)
        pass

    def test_SystemActor_involving_physical_paths_getter(self):
        tested = SystemActor()
        tested.get_involving_physical_paths()
        pass

    def test_SystemActor_owned_physical_link_categories_getter(self):
        tested = SystemActor()
        tested.get_owned_physical_link_categories()
        pass

    def test_SystemActor_owned_physical_paths_getter(self):
        tested = SystemActor()
        tested.get_owned_physical_paths()
        pass

    def test_SystemActor_is_human_getter(self):
        tested = SystemActor()
        tested.get_is_human()
        pass

    def test_SystemActor_is_human_setter(self):
        tested = SystemActor()
        value = True
        tested.set_is_human(value)
        pass

    def test_SystemActor_owned_actors_getter(self):
        tested = SystemActor()
        tested.get_owned_actors()
        pass

    def test_SystemActor_owned_system_component_pkgs_getter(self):
        tested = SystemActor()
        tested.get_owned_system_component_pkgs()
        pass

    def test_SystemActor_involving_missions_getter(self):
        tested = SystemActor()
        tested.get_involving_missions()
        pass

    def test_SystemActor_involving_missions_setter(self):
        tested = SystemActor()
        value = Mission()
        tested.get_involving_missions().add(value)
        pass

    def test_SystemActor_realized_operational_entities_getter(self):
        tested = SystemActor()
        tested.get_realized_operational_entities()
        pass

    def test_SystemActor_realized_operational_entities_setter(self):
        tested = SystemActor()
        value = OperationalActor()
        tested.get_realized_operational_entities().add(value)
        pass

    def test_SystemActor_involving_capabilities_getter(self):
        tested = SystemActor()
        tested.get_involving_capabilities()
        pass

    def test_SystemActor_involving_capabilities_setter(self):
        tested = SystemActor()
        value = Capability()
        tested.get_involving_capabilities().add(value)
        pass

    def test_SystemActor_realizing_logical_actors_getter(self):
        tested = SystemActor()
        tested.get_realizing_logical_actors()
        pass

    def test_SystemActor_realizing_logical_actors_setter(self):
        tested = SystemActor()
        value = LogicalActor()
        tested.get_realizing_logical_actors().add(value)
        pass

    def test_MissionPkg_owned_property_value_pkgs_getter(self):
        tested = MissionPkg()
        tested.get_owned_property_value_pkgs()
        pass

    def test_MissionPkg_id_getter(self):
        tested = MissionPkg()
        tested.get_id()
        pass

    def test_MissionPkg_id_setter(self):
        tested = MissionPkg()
        value = "value"
        tested.set_id(value)
        pass

    def test_MissionPkg_sid_getter(self):
        tested = MissionPkg()
        tested.get_sid()
        pass

    def test_MissionPkg_sid_setter(self):
        tested = MissionPkg()
        value = "value"
        tested.set_sid(value)
        pass

    def test_MissionPkg_name_getter(self):
        tested = MissionPkg()
        tested.get_name()
        pass

    def test_MissionPkg_name_setter(self):
        tested = MissionPkg()
        value = "value"
        tested.set_name(value)
        pass

    def test_MissionPkg_summary_getter(self):
        tested = MissionPkg()
        tested.get_summary()
        pass

    def test_MissionPkg_summary_setter(self):
        tested = MissionPkg()
        value = "value"
        tested.set_summary(value)
        pass

    def test_MissionPkg_description_getter(self):
        tested = MissionPkg()
        tested.get_description()
        pass

    def test_MissionPkg_description_setter(self):
        tested = MissionPkg()
        value = "value"
        tested.set_description(value)
        pass

    def test_MissionPkg_status_getter(self):
        tested = MissionPkg()
        tested.get_status()
        pass

    def test_MissionPkg_status_setter(self):
        tested = MissionPkg()
        value = "value"
        tested.set_status(value)
        pass

    def test_MissionPkg_review_getter(self):
        tested = MissionPkg()
        tested.get_review()
        pass

    def test_MissionPkg_review_setter(self):
        tested = MissionPkg()
        value = "value"
        tested.set_review(value)
        pass

    def test_MissionPkg_visible_in_documentation_getter(self):
        tested = MissionPkg()
        tested.get_visible_in_documentation()
        pass

    def test_MissionPkg_visible_in_documentation_setter(self):
        tested = MissionPkg()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_MissionPkg_visible_for_traceability_getter(self):
        tested = MissionPkg()
        tested.get_visible_for_traceability()
        pass

    def test_MissionPkg_visible_for_traceability_setter(self):
        tested = MissionPkg()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_MissionPkg_owned_constraints_getter(self):
        tested = MissionPkg()
        tested.get_owned_constraints()
        pass

    def test_MissionPkg_constraints_getter(self):
        tested = MissionPkg()
        tested.get_constraints()
        pass

    def test_MissionPkg_constraints_setter(self):
        tested = MissionPkg()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_MissionPkg_owned_property_values_getter(self):
        tested = MissionPkg()
        tested.get_owned_property_values()
        pass

    def test_MissionPkg_applied_property_values_getter(self):
        tested = MissionPkg()
        tested.get_applied_property_values()
        pass

    def test_MissionPkg_applied_property_values_setter(self):
        tested = MissionPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_MissionPkg_owned_property_value_groups_getter(self):
        tested = MissionPkg()
        tested.get_owned_property_value_groups()
        pass

    def test_MissionPkg_applied_property_value_groups_getter(self):
        tested = MissionPkg()
        tested.get_applied_property_value_groups()
        pass

    def test_MissionPkg_applied_property_value_groups_setter(self):
        tested = MissionPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_MissionPkg_owned_enumeration_property_types_getter(self):
        tested = MissionPkg()
        tested.get_owned_enumeration_property_types()
        pass

    def test_MissionPkg_owned_diagrams_getter(self):
        tested = MissionPkg()
        tested.get_owned_diagrams()
        pass

    def test_MissionPkg_element_of_interest_for_diagrams_getter(self):
        tested = MissionPkg()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_MissionPkg_element_of_interest_for_diagrams_setter(self):
        tested = MissionPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_MissionPkg_contextual_element_for_diagrams_getter(self):
        tested = MissionPkg()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_MissionPkg_contextual_element_for_diagrams_setter(self):
        tested = MissionPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_MissionPkg_representing_diagrams_getter(self):
        tested = MissionPkg()
        tested.get_representing_diagrams()
        pass

    def test_MissionPkg__r_e_cs_getter(self):
        tested = MissionPkg()
        tested.get__r_e_cs()
        pass

    def test_MissionPkg__r_e_cs_setter(self):
        tested = MissionPkg()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_MissionPkg__r_p_ls_getter(self):
        tested = MissionPkg()
        tested.get__r_p_ls()
        pass

    def test_MissionPkg__r_p_ls_setter(self):
        tested = MissionPkg()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_MissionPkg_get_label(self):
        tested = MissionPkg()
        tested.get_label()
        pass

    def test_MissionPkg_get_element_type(self):
        tested = MissionPkg()
        tested.get_element_type()
        pass

    def test_MissionPkg_get_container(self):
        tested = MissionPkg()
        tested.get_container()
        pass

    def test_MissionPkg_get_contents(self):
        tested = MissionPkg()
        tested.get_contents()
        pass

    def test_MissionPkg_get_all_contents(self):
        tested = MissionPkg()
        tested.get_all_contents()
        pass

    def test_MissionPkg_get_all_contents_by_type(self):
        tested = MissionPkg()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_MissionPkg_get_available_s_b_queries(self):
        tested = MissionPkg()
        tested.get_available_s_b_queries()
        pass

    def test_MissionPkg_get_query_result(self):
        tested = MissionPkg()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_MissionPkg_owned_mission_pkgs_getter(self):
        tested = MissionPkg()
        tested.get_owned_mission_pkgs()
        pass

    def test_MissionPkg_owned_missions_getter(self):
        tested = MissionPkg()
        tested.get_owned_missions()
        pass

    def test_Mission_id_getter(self):
        tested = Mission()
        tested.get_id()
        pass

    def test_Mission_id_setter(self):
        tested = Mission()
        value = "value"
        tested.set_id(value)
        pass

    def test_Mission_sid_getter(self):
        tested = Mission()
        tested.get_sid()
        pass

    def test_Mission_sid_setter(self):
        tested = Mission()
        value = "value"
        tested.set_sid(value)
        pass

    def test_Mission_name_getter(self):
        tested = Mission()
        tested.get_name()
        pass

    def test_Mission_name_setter(self):
        tested = Mission()
        value = "value"
        tested.set_name(value)
        pass

    def test_Mission_summary_getter(self):
        tested = Mission()
        tested.get_summary()
        pass

    def test_Mission_summary_setter(self):
        tested = Mission()
        value = "value"
        tested.set_summary(value)
        pass

    def test_Mission_description_getter(self):
        tested = Mission()
        tested.get_description()
        pass

    def test_Mission_description_setter(self):
        tested = Mission()
        value = "value"
        tested.set_description(value)
        pass

    def test_Mission_status_getter(self):
        tested = Mission()
        tested.get_status()
        pass

    def test_Mission_status_setter(self):
        tested = Mission()
        value = "value"
        tested.set_status(value)
        pass

    def test_Mission_review_getter(self):
        tested = Mission()
        tested.get_review()
        pass

    def test_Mission_review_setter(self):
        tested = Mission()
        value = "value"
        tested.set_review(value)
        pass

    def test_Mission_visible_in_documentation_getter(self):
        tested = Mission()
        tested.get_visible_in_documentation()
        pass

    def test_Mission_visible_in_documentation_setter(self):
        tested = Mission()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_Mission_visible_for_traceability_getter(self):
        tested = Mission()
        tested.get_visible_for_traceability()
        pass

    def test_Mission_visible_for_traceability_setter(self):
        tested = Mission()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_Mission_owned_constraints_getter(self):
        tested = Mission()
        tested.get_owned_constraints()
        pass

    def test_Mission_constraints_getter(self):
        tested = Mission()
        tested.get_constraints()
        pass

    def test_Mission_constraints_setter(self):
        tested = Mission()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_Mission_owned_property_values_getter(self):
        tested = Mission()
        tested.get_owned_property_values()
        pass

    def test_Mission_applied_property_values_getter(self):
        tested = Mission()
        tested.get_applied_property_values()
        pass

    def test_Mission_applied_property_values_setter(self):
        tested = Mission()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_Mission_owned_property_value_groups_getter(self):
        tested = Mission()
        tested.get_owned_property_value_groups()
        pass

    def test_Mission_applied_property_value_groups_getter(self):
        tested = Mission()
        tested.get_applied_property_value_groups()
        pass

    def test_Mission_applied_property_value_groups_setter(self):
        tested = Mission()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_Mission_owned_enumeration_property_types_getter(self):
        tested = Mission()
        tested.get_owned_enumeration_property_types()
        pass

    def test_Mission_owned_diagrams_getter(self):
        tested = Mission()
        tested.get_owned_diagrams()
        pass

    def test_Mission_element_of_interest_for_diagrams_getter(self):
        tested = Mission()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_Mission_element_of_interest_for_diagrams_setter(self):
        tested = Mission()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_Mission_contextual_element_for_diagrams_getter(self):
        tested = Mission()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_Mission_contextual_element_for_diagrams_setter(self):
        tested = Mission()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_Mission_representing_diagrams_getter(self):
        tested = Mission()
        tested.get_representing_diagrams()
        pass

    def test_Mission__r_e_cs_getter(self):
        tested = Mission()
        tested.get__r_e_cs()
        pass

    def test_Mission__r_e_cs_setter(self):
        tested = Mission()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_Mission__r_p_ls_getter(self):
        tested = Mission()
        tested.get__r_p_ls()
        pass

    def test_Mission__r_p_ls_setter(self):
        tested = Mission()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_Mission_get_label(self):
        tested = Mission()
        tested.get_label()
        pass

    def test_Mission_get_element_type(self):
        tested = Mission()
        tested.get_element_type()
        pass

    def test_Mission_get_container(self):
        tested = Mission()
        tested.get_container()
        pass

    def test_Mission_get_contents(self):
        tested = Mission()
        tested.get_contents()
        pass

    def test_Mission_get_all_contents(self):
        tested = Mission()
        tested.get_all_contents()
        pass

    def test_Mission_get_all_contents_by_type(self):
        tested = Mission()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_Mission_get_available_s_b_queries(self):
        tested = Mission()
        tested.get_available_s_b_queries()
        pass

    def test_Mission_get_query_result(self):
        tested = Mission()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_Mission_exploited_capabilities_getter(self):
        tested = Mission()
        tested.get_exploited_capabilities()
        pass

    def test_Mission_exploited_capabilities_setter(self):
        tested = Mission()
        value = Capability()
        tested.get_exploited_capabilities().add(value)
        pass

    def test_Mission_involved_actors_getter(self):
        tested = Mission()
        tested.get_involved_actors()
        pass

    def test_Mission_involved_actors_setter(self):
        tested = Mission()
        value = SystemActor()
        tested.get_involved_actors().add(value)
        pass

    def test_LogicalArchitecture_owned_property_value_pkgs_getter(self):
        tested = LogicalArchitecture()
        tested.get_owned_property_value_pkgs()
        pass

    def test_LogicalArchitecture_id_getter(self):
        tested = LogicalArchitecture()
        tested.get_id()
        pass

    def test_LogicalArchitecture_id_setter(self):
        tested = LogicalArchitecture()
        value = "value"
        tested.set_id(value)
        pass

    def test_LogicalArchitecture_sid_getter(self):
        tested = LogicalArchitecture()
        tested.get_sid()
        pass

    def test_LogicalArchitecture_sid_setter(self):
        tested = LogicalArchitecture()
        value = "value"
        tested.set_sid(value)
        pass

    def test_LogicalArchitecture_name_getter(self):
        tested = LogicalArchitecture()
        tested.get_name()
        pass

    def test_LogicalArchitecture_name_setter(self):
        tested = LogicalArchitecture()
        value = "value"
        tested.set_name(value)
        pass

    def test_LogicalArchitecture_summary_getter(self):
        tested = LogicalArchitecture()
        tested.get_summary()
        pass

    def test_LogicalArchitecture_summary_setter(self):
        tested = LogicalArchitecture()
        value = "value"
        tested.set_summary(value)
        pass

    def test_LogicalArchitecture_description_getter(self):
        tested = LogicalArchitecture()
        tested.get_description()
        pass

    def test_LogicalArchitecture_description_setter(self):
        tested = LogicalArchitecture()
        value = "value"
        tested.set_description(value)
        pass

    def test_LogicalArchitecture_status_getter(self):
        tested = LogicalArchitecture()
        tested.get_status()
        pass

    def test_LogicalArchitecture_status_setter(self):
        tested = LogicalArchitecture()
        value = "value"
        tested.set_status(value)
        pass

    def test_LogicalArchitecture_review_getter(self):
        tested = LogicalArchitecture()
        tested.get_review()
        pass

    def test_LogicalArchitecture_review_setter(self):
        tested = LogicalArchitecture()
        value = "value"
        tested.set_review(value)
        pass

    def test_LogicalArchitecture_visible_in_documentation_getter(self):
        tested = LogicalArchitecture()
        tested.get_visible_in_documentation()
        pass

    def test_LogicalArchitecture_visible_in_documentation_setter(self):
        tested = LogicalArchitecture()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_LogicalArchitecture_visible_for_traceability_getter(self):
        tested = LogicalArchitecture()
        tested.get_visible_for_traceability()
        pass

    def test_LogicalArchitecture_visible_for_traceability_setter(self):
        tested = LogicalArchitecture()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_LogicalArchitecture_owned_constraints_getter(self):
        tested = LogicalArchitecture()
        tested.get_owned_constraints()
        pass

    def test_LogicalArchitecture_constraints_getter(self):
        tested = LogicalArchitecture()
        tested.get_constraints()
        pass

    def test_LogicalArchitecture_constraints_setter(self):
        tested = LogicalArchitecture()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_LogicalArchitecture_owned_property_values_getter(self):
        tested = LogicalArchitecture()
        tested.get_owned_property_values()
        pass

    def test_LogicalArchitecture_applied_property_values_getter(self):
        tested = LogicalArchitecture()
        tested.get_applied_property_values()
        pass

    def test_LogicalArchitecture_applied_property_values_setter(self):
        tested = LogicalArchitecture()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_LogicalArchitecture_owned_property_value_groups_getter(self):
        tested = LogicalArchitecture()
        tested.get_owned_property_value_groups()
        pass

    def test_LogicalArchitecture_applied_property_value_groups_getter(self):
        tested = LogicalArchitecture()
        tested.get_applied_property_value_groups()
        pass

    def test_LogicalArchitecture_applied_property_value_groups_setter(self):
        tested = LogicalArchitecture()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_LogicalArchitecture_owned_enumeration_property_types_getter(self):
        tested = LogicalArchitecture()
        tested.get_owned_enumeration_property_types()
        pass

    def test_LogicalArchitecture_owned_diagrams_getter(self):
        tested = LogicalArchitecture()
        tested.get_owned_diagrams()
        pass

    def test_LogicalArchitecture_element_of_interest_for_diagrams_getter(self):
        tested = LogicalArchitecture()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_LogicalArchitecture_element_of_interest_for_diagrams_setter(self):
        tested = LogicalArchitecture()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_LogicalArchitecture_contextual_element_for_diagrams_getter(self):
        tested = LogicalArchitecture()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_LogicalArchitecture_contextual_element_for_diagrams_setter(self):
        tested = LogicalArchitecture()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_LogicalArchitecture_representing_diagrams_getter(self):
        tested = LogicalArchitecture()
        tested.get_representing_diagrams()
        pass

    def test_LogicalArchitecture__r_e_cs_getter(self):
        tested = LogicalArchitecture()
        tested.get__r_e_cs()
        pass

    def test_LogicalArchitecture__r_e_cs_setter(self):
        tested = LogicalArchitecture()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_LogicalArchitecture__r_p_ls_getter(self):
        tested = LogicalArchitecture()
        tested.get__r_p_ls()
        pass

    def test_LogicalArchitecture__r_p_ls_setter(self):
        tested = LogicalArchitecture()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_LogicalArchitecture_get_label(self):
        tested = LogicalArchitecture()
        tested.get_label()
        pass

    def test_LogicalArchitecture_get_element_type(self):
        tested = LogicalArchitecture()
        tested.get_element_type()
        pass

    def test_LogicalArchitecture_get_container(self):
        tested = LogicalArchitecture()
        tested.get_container()
        pass

    def test_LogicalArchitecture_get_contents(self):
        tested = LogicalArchitecture()
        tested.get_contents()
        pass

    def test_LogicalArchitecture_get_all_contents(self):
        tested = LogicalArchitecture()
        tested.get_all_contents()
        pass

    def test_LogicalArchitecture_get_all_contents_by_type(self):
        tested = LogicalArchitecture()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_LogicalArchitecture_get_available_s_b_queries(self):
        tested = LogicalArchitecture()
        tested.get_available_s_b_queries()
        pass

    def test_LogicalArchitecture_get_query_result(self):
        tested = LogicalArchitecture()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_LogicalArchitecture_logical_function_pkg_getter(self):
        tested = LogicalArchitecture()
        tested.get_logical_function_pkg()
        pass

    def test_LogicalArchitecture_capability_realization_pkg_getter(self):
        tested = LogicalArchitecture()
        tested.get_capability_realization_pkg()
        pass

    def test_LogicalArchitecture_interface_pkg_getter(self):
        tested = LogicalArchitecture()
        tested.get_interface_pkg()
        pass

    def test_LogicalArchitecture_data_pkg_getter(self):
        tested = LogicalArchitecture()
        tested.get_data_pkg()
        pass

    def test_LogicalArchitecture_logical_component_pkg_getter(self):
        tested = LogicalArchitecture()
        tested.get_logical_component_pkg()
        pass

    def test_LogicalArchitecture_logical_system_getter(self):
        tested = LogicalArchitecture()
        tested.get_logical_system()
        pass

    def test_LogicalFunctionPkg_owned_property_value_pkgs_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_owned_property_value_pkgs()
        pass

    def test_LogicalFunctionPkg_id_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_id()
        pass

    def test_LogicalFunctionPkg_id_setter(self):
        tested = LogicalFunctionPkg()
        value = "value"
        tested.set_id(value)
        pass

    def test_LogicalFunctionPkg_sid_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_sid()
        pass

    def test_LogicalFunctionPkg_sid_setter(self):
        tested = LogicalFunctionPkg()
        value = "value"
        tested.set_sid(value)
        pass

    def test_LogicalFunctionPkg_name_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_name()
        pass

    def test_LogicalFunctionPkg_name_setter(self):
        tested = LogicalFunctionPkg()
        value = "value"
        tested.set_name(value)
        pass

    def test_LogicalFunctionPkg_summary_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_summary()
        pass

    def test_LogicalFunctionPkg_summary_setter(self):
        tested = LogicalFunctionPkg()
        value = "value"
        tested.set_summary(value)
        pass

    def test_LogicalFunctionPkg_description_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_description()
        pass

    def test_LogicalFunctionPkg_description_setter(self):
        tested = LogicalFunctionPkg()
        value = "value"
        tested.set_description(value)
        pass

    def test_LogicalFunctionPkg_status_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_status()
        pass

    def test_LogicalFunctionPkg_status_setter(self):
        tested = LogicalFunctionPkg()
        value = "value"
        tested.set_status(value)
        pass

    def test_LogicalFunctionPkg_review_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_review()
        pass

    def test_LogicalFunctionPkg_review_setter(self):
        tested = LogicalFunctionPkg()
        value = "value"
        tested.set_review(value)
        pass

    def test_LogicalFunctionPkg_visible_in_documentation_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_visible_in_documentation()
        pass

    def test_LogicalFunctionPkg_visible_in_documentation_setter(self):
        tested = LogicalFunctionPkg()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_LogicalFunctionPkg_visible_for_traceability_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_visible_for_traceability()
        pass

    def test_LogicalFunctionPkg_visible_for_traceability_setter(self):
        tested = LogicalFunctionPkg()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_LogicalFunctionPkg_owned_constraints_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_owned_constraints()
        pass

    def test_LogicalFunctionPkg_constraints_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_constraints()
        pass

    def test_LogicalFunctionPkg_constraints_setter(self):
        tested = LogicalFunctionPkg()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_LogicalFunctionPkg_owned_property_values_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_owned_property_values()
        pass

    def test_LogicalFunctionPkg_applied_property_values_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_applied_property_values()
        pass

    def test_LogicalFunctionPkg_applied_property_values_setter(self):
        tested = LogicalFunctionPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_LogicalFunctionPkg_owned_property_value_groups_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_owned_property_value_groups()
        pass

    def test_LogicalFunctionPkg_applied_property_value_groups_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_applied_property_value_groups()
        pass

    def test_LogicalFunctionPkg_applied_property_value_groups_setter(self):
        tested = LogicalFunctionPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_LogicalFunctionPkg_owned_enumeration_property_types_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_owned_enumeration_property_types()
        pass

    def test_LogicalFunctionPkg_owned_diagrams_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_owned_diagrams()
        pass

    def test_LogicalFunctionPkg_element_of_interest_for_diagrams_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_LogicalFunctionPkg_element_of_interest_for_diagrams_setter(self):
        tested = LogicalFunctionPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_LogicalFunctionPkg_contextual_element_for_diagrams_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_LogicalFunctionPkg_contextual_element_for_diagrams_setter(self):
        tested = LogicalFunctionPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_LogicalFunctionPkg_representing_diagrams_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_representing_diagrams()
        pass

    def test_LogicalFunctionPkg__r_e_cs_getter(self):
        tested = LogicalFunctionPkg()
        tested.get__r_e_cs()
        pass

    def test_LogicalFunctionPkg__r_e_cs_setter(self):
        tested = LogicalFunctionPkg()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_LogicalFunctionPkg__r_p_ls_getter(self):
        tested = LogicalFunctionPkg()
        tested.get__r_p_ls()
        pass

    def test_LogicalFunctionPkg__r_p_ls_setter(self):
        tested = LogicalFunctionPkg()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_LogicalFunctionPkg_get_label(self):
        tested = LogicalFunctionPkg()
        tested.get_label()
        pass

    def test_LogicalFunctionPkg_get_element_type(self):
        tested = LogicalFunctionPkg()
        tested.get_element_type()
        pass

    def test_LogicalFunctionPkg_get_container(self):
        tested = LogicalFunctionPkg()
        tested.get_container()
        pass

    def test_LogicalFunctionPkg_get_contents(self):
        tested = LogicalFunctionPkg()
        tested.get_contents()
        pass

    def test_LogicalFunctionPkg_get_all_contents(self):
        tested = LogicalFunctionPkg()
        tested.get_all_contents()
        pass

    def test_LogicalFunctionPkg_get_all_contents_by_type(self):
        tested = LogicalFunctionPkg()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_LogicalFunctionPkg_get_available_s_b_queries(self):
        tested = LogicalFunctionPkg()
        tested.get_available_s_b_queries()
        pass

    def test_LogicalFunctionPkg_get_query_result(self):
        tested = LogicalFunctionPkg()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_LogicalFunctionPkg_owned_logical_function_pkgs_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_owned_logical_function_pkgs()
        pass

    def test_LogicalFunctionPkg_owned_logical_functions_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_owned_logical_functions()
        pass

    def test_LogicalFunctionPkg_owned_categories_getter(self):
        tested = LogicalFunctionPkg()
        tested.get_owned_categories()
        pass

    def test_LogicalFunction_kind_getter(self):
        tested = LogicalFunction()
        tested.get_kind()
        pass

    def test_LogicalFunction_kind_setter(self):
        tested = LogicalFunction()
        value = FunctionKind()
        tested.set_kind(value)
        pass

    def test_LogicalFunction_condition_getter(self):
        tested = LogicalFunction()
        tested.get_condition()
        pass

    def test_LogicalFunction_condition_setter(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_condition(value)
        pass

    def test_LogicalFunction_inputs_getter(self):
        tested = LogicalFunction()
        tested.get_inputs()
        pass

    def test_LogicalFunction_outputs_getter(self):
        tested = LogicalFunction()
        tested.get_outputs()
        pass

    def test_LogicalFunction_incoming_getter(self):
        tested = LogicalFunction()
        tested.get_incoming()
        pass

    def test_LogicalFunction_incoming_setter(self):
        tested = LogicalFunction()
        value = FunctionalExchange()
        tested.get_incoming().add(value)
        pass

    def test_LogicalFunction_outgoing_getter(self):
        tested = LogicalFunction()
        tested.get_outgoing()
        pass

    def test_LogicalFunction_outgoing_setter(self):
        tested = LogicalFunction()
        value = FunctionalExchange()
        tested.get_outgoing().add(value)
        pass

    def test_LogicalFunction_allocating_component_getter(self):
        tested = LogicalFunction()
        tested.get_allocating_component()
        pass

    def test_LogicalFunction_allocating_component_setter(self):
        tested = LogicalFunction()
        value = PhysicalActor()
        tested.set_allocating_component(value)
        pass

    def test_LogicalFunction_owned_functional_chains_getter(self):
        tested = LogicalFunction()
        tested.get_owned_functional_chains()
        pass

    def test_LogicalFunction_involving_functional_chains_getter(self):
        tested = LogicalFunction()
        tested.get_involving_functional_chains()
        pass

    def test_LogicalFunction_involving_capabilities_getter(self):
        tested = LogicalFunction()
        tested.get_involving_capabilities()
        pass

    def test_LogicalFunction_involving_capabilities_setter(self):
        tested = LogicalFunction()
        value = CapabilityRealization()
        tested.get_involving_capabilities().add(value)
        pass

    def test_LogicalFunction_available_in_states_getter(self):
        tested = LogicalFunction()
        tested.get_available_in_states()
        pass

    def test_LogicalFunction_available_in_states_setter(self):
        tested = LogicalFunction()
        value = State()
        tested.get_available_in_states().add(value)
        pass

    def test_LogicalFunction_id_getter(self):
        tested = LogicalFunction()
        tested.get_id()
        pass

    def test_LogicalFunction_id_setter(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_id(value)
        pass

    def test_LogicalFunction_sid_getter(self):
        tested = LogicalFunction()
        tested.get_sid()
        pass

    def test_LogicalFunction_sid_setter(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_sid(value)
        pass

    def test_LogicalFunction_name_getter(self):
        tested = LogicalFunction()
        tested.get_name()
        pass

    def test_LogicalFunction_name_setter(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_name(value)
        pass

    def test_LogicalFunction_summary_getter(self):
        tested = LogicalFunction()
        tested.get_summary()
        pass

    def test_LogicalFunction_summary_setter(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_summary(value)
        pass

    def test_LogicalFunction_description_getter(self):
        tested = LogicalFunction()
        tested.get_description()
        pass

    def test_LogicalFunction_description_setter(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_description(value)
        pass

    def test_LogicalFunction_status_getter(self):
        tested = LogicalFunction()
        tested.get_status()
        pass

    def test_LogicalFunction_status_setter(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_status(value)
        pass

    def test_LogicalFunction_review_getter(self):
        tested = LogicalFunction()
        tested.get_review()
        pass

    def test_LogicalFunction_review_setter(self):
        tested = LogicalFunction()
        value = "value"
        tested.set_review(value)
        pass

    def test_LogicalFunction_visible_in_documentation_getter(self):
        tested = LogicalFunction()
        tested.get_visible_in_documentation()
        pass

    def test_LogicalFunction_visible_in_documentation_setter(self):
        tested = LogicalFunction()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_LogicalFunction_visible_for_traceability_getter(self):
        tested = LogicalFunction()
        tested.get_visible_for_traceability()
        pass

    def test_LogicalFunction_visible_for_traceability_setter(self):
        tested = LogicalFunction()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_LogicalFunction_owned_constraints_getter(self):
        tested = LogicalFunction()
        tested.get_owned_constraints()
        pass

    def test_LogicalFunction_constraints_getter(self):
        tested = LogicalFunction()
        tested.get_constraints()
        pass

    def test_LogicalFunction_constraints_setter(self):
        tested = LogicalFunction()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_LogicalFunction_owned_property_values_getter(self):
        tested = LogicalFunction()
        tested.get_owned_property_values()
        pass

    def test_LogicalFunction_applied_property_values_getter(self):
        tested = LogicalFunction()
        tested.get_applied_property_values()
        pass

    def test_LogicalFunction_applied_property_values_setter(self):
        tested = LogicalFunction()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_LogicalFunction_owned_property_value_groups_getter(self):
        tested = LogicalFunction()
        tested.get_owned_property_value_groups()
        pass

    def test_LogicalFunction_applied_property_value_groups_getter(self):
        tested = LogicalFunction()
        tested.get_applied_property_value_groups()
        pass

    def test_LogicalFunction_applied_property_value_groups_setter(self):
        tested = LogicalFunction()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_LogicalFunction_owned_enumeration_property_types_getter(self):
        tested = LogicalFunction()
        tested.get_owned_enumeration_property_types()
        pass

    def test_LogicalFunction_owned_diagrams_getter(self):
        tested = LogicalFunction()
        tested.get_owned_diagrams()
        pass

    def test_LogicalFunction_element_of_interest_for_diagrams_getter(self):
        tested = LogicalFunction()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_LogicalFunction_element_of_interest_for_diagrams_setter(self):
        tested = LogicalFunction()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_LogicalFunction_contextual_element_for_diagrams_getter(self):
        tested = LogicalFunction()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_LogicalFunction_contextual_element_for_diagrams_setter(self):
        tested = LogicalFunction()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_LogicalFunction_representing_diagrams_getter(self):
        tested = LogicalFunction()
        tested.get_representing_diagrams()
        pass

    def test_LogicalFunction__r_e_cs_getter(self):
        tested = LogicalFunction()
        tested.get__r_e_cs()
        pass

    def test_LogicalFunction__r_e_cs_setter(self):
        tested = LogicalFunction()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_LogicalFunction__r_p_ls_getter(self):
        tested = LogicalFunction()
        tested.get__r_p_ls()
        pass

    def test_LogicalFunction__r_p_ls_setter(self):
        tested = LogicalFunction()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_LogicalFunction_get_label(self):
        tested = LogicalFunction()
        tested.get_label()
        pass

    def test_LogicalFunction_get_element_type(self):
        tested = LogicalFunction()
        tested.get_element_type()
        pass

    def test_LogicalFunction_get_container(self):
        tested = LogicalFunction()
        tested.get_container()
        pass

    def test_LogicalFunction_get_contents(self):
        tested = LogicalFunction()
        tested.get_contents()
        pass

    def test_LogicalFunction_get_all_contents(self):
        tested = LogicalFunction()
        tested.get_all_contents()
        pass

    def test_LogicalFunction_get_all_contents_by_type(self):
        tested = LogicalFunction()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_LogicalFunction_get_available_s_b_queries(self):
        tested = LogicalFunction()
        tested.get_available_s_b_queries()
        pass

    def test_LogicalFunction_get_query_result(self):
        tested = LogicalFunction()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_LogicalFunction_contained_logical_functions_getter(self):
        tested = LogicalFunction()
        tested.get_contained_logical_functions()
        pass

    def test_LogicalFunction_owned_logical_function_pkgs_getter(self):
        tested = LogicalFunction()
        tested.get_owned_logical_function_pkgs()
        pass

    def test_LogicalFunction_realized_system_functions_getter(self):
        tested = LogicalFunction()
        tested.get_realized_system_functions()
        pass

    def test_LogicalFunction_realized_system_functions_setter(self):
        tested = LogicalFunction()
        value = SystemFunction()
        tested.get_realized_system_functions().add(value)
        pass

    def test_LogicalFunction_realizing_physical_functions_getter(self):
        tested = LogicalFunction()
        tested.get_realizing_physical_functions()
        pass

    def test_LogicalFunction_realizing_physical_functions_setter(self):
        tested = LogicalFunction()
        value = PhysicalFunction()
        tested.get_realizing_physical_functions().add(value)
        pass

    def test_CapabilityRealizationPkg_owned_property_value_pkgs_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_owned_property_value_pkgs()
        pass

    def test_CapabilityRealizationPkg_id_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_id()
        pass

    def test_CapabilityRealizationPkg_id_setter(self):
        tested = CapabilityRealizationPkg()
        value = "value"
        tested.set_id(value)
        pass

    def test_CapabilityRealizationPkg_sid_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_sid()
        pass

    def test_CapabilityRealizationPkg_sid_setter(self):
        tested = CapabilityRealizationPkg()
        value = "value"
        tested.set_sid(value)
        pass

    def test_CapabilityRealizationPkg_name_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_name()
        pass

    def test_CapabilityRealizationPkg_name_setter(self):
        tested = CapabilityRealizationPkg()
        value = "value"
        tested.set_name(value)
        pass

    def test_CapabilityRealizationPkg_summary_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_summary()
        pass

    def test_CapabilityRealizationPkg_summary_setter(self):
        tested = CapabilityRealizationPkg()
        value = "value"
        tested.set_summary(value)
        pass

    def test_CapabilityRealizationPkg_description_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_description()
        pass

    def test_CapabilityRealizationPkg_description_setter(self):
        tested = CapabilityRealizationPkg()
        value = "value"
        tested.set_description(value)
        pass

    def test_CapabilityRealizationPkg_status_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_status()
        pass

    def test_CapabilityRealizationPkg_status_setter(self):
        tested = CapabilityRealizationPkg()
        value = "value"
        tested.set_status(value)
        pass

    def test_CapabilityRealizationPkg_review_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_review()
        pass

    def test_CapabilityRealizationPkg_review_setter(self):
        tested = CapabilityRealizationPkg()
        value = "value"
        tested.set_review(value)
        pass

    def test_CapabilityRealizationPkg_visible_in_documentation_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_visible_in_documentation()
        pass

    def test_CapabilityRealizationPkg_visible_in_documentation_setter(self):
        tested = CapabilityRealizationPkg()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_CapabilityRealizationPkg_visible_for_traceability_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_visible_for_traceability()
        pass

    def test_CapabilityRealizationPkg_visible_for_traceability_setter(self):
        tested = CapabilityRealizationPkg()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_CapabilityRealizationPkg_owned_constraints_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_owned_constraints()
        pass

    def test_CapabilityRealizationPkg_constraints_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_constraints()
        pass

    def test_CapabilityRealizationPkg_constraints_setter(self):
        tested = CapabilityRealizationPkg()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_CapabilityRealizationPkg_owned_property_values_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_owned_property_values()
        pass

    def test_CapabilityRealizationPkg_applied_property_values_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_applied_property_values()
        pass

    def test_CapabilityRealizationPkg_applied_property_values_setter(self):
        tested = CapabilityRealizationPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_CapabilityRealizationPkg_owned_property_value_groups_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_owned_property_value_groups()
        pass

    def test_CapabilityRealizationPkg_applied_property_value_groups_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_applied_property_value_groups()
        pass

    def test_CapabilityRealizationPkg_applied_property_value_groups_setter(self):
        tested = CapabilityRealizationPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_CapabilityRealizationPkg_owned_enumeration_property_types_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_owned_enumeration_property_types()
        pass

    def test_CapabilityRealizationPkg_owned_diagrams_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_owned_diagrams()
        pass

    def test_CapabilityRealizationPkg_element_of_interest_for_diagrams_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_CapabilityRealizationPkg_element_of_interest_for_diagrams_setter(self):
        tested = CapabilityRealizationPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_CapabilityRealizationPkg_contextual_element_for_diagrams_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_CapabilityRealizationPkg_contextual_element_for_diagrams_setter(self):
        tested = CapabilityRealizationPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_CapabilityRealizationPkg_representing_diagrams_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_representing_diagrams()
        pass

    def test_CapabilityRealizationPkg__r_e_cs_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get__r_e_cs()
        pass

    def test_CapabilityRealizationPkg__r_e_cs_setter(self):
        tested = CapabilityRealizationPkg()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_CapabilityRealizationPkg__r_p_ls_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get__r_p_ls()
        pass

    def test_CapabilityRealizationPkg__r_p_ls_setter(self):
        tested = CapabilityRealizationPkg()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_CapabilityRealizationPkg_get_label(self):
        tested = CapabilityRealizationPkg()
        tested.get_label()
        pass

    def test_CapabilityRealizationPkg_get_element_type(self):
        tested = CapabilityRealizationPkg()
        tested.get_element_type()
        pass

    def test_CapabilityRealizationPkg_get_container(self):
        tested = CapabilityRealizationPkg()
        tested.get_container()
        pass

    def test_CapabilityRealizationPkg_get_contents(self):
        tested = CapabilityRealizationPkg()
        tested.get_contents()
        pass

    def test_CapabilityRealizationPkg_get_all_contents(self):
        tested = CapabilityRealizationPkg()
        tested.get_all_contents()
        pass

    def test_CapabilityRealizationPkg_get_all_contents_by_type(self):
        tested = CapabilityRealizationPkg()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_CapabilityRealizationPkg_get_available_s_b_queries(self):
        tested = CapabilityRealizationPkg()
        tested.get_available_s_b_queries()
        pass

    def test_CapabilityRealizationPkg_get_query_result(self):
        tested = CapabilityRealizationPkg()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_CapabilityRealizationPkg_owned_capability_realization_pkgs_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_owned_capability_realization_pkgs()
        pass

    def test_CapabilityRealizationPkg_owned_capability_realizations_getter(self):
        tested = CapabilityRealizationPkg()
        tested.get_owned_capability_realizations()
        pass

    def test_CapabilityRealization_owned_functional_chains_getter(self):
        tested = CapabilityRealization()
        tested.get_owned_functional_chains()
        pass

    def test_CapabilityRealization_involved_functional_chains_getter(self):
        tested = CapabilityRealization()
        tested.get_involved_functional_chains()
        pass

    def test_CapabilityRealization_involved_functional_chains_setter(self):
        tested = CapabilityRealization()
        value = FunctionalChain()
        tested.get_involved_functional_chains().add(value)
        pass

    def test_CapabilityRealization_involved_functions_getter(self):
        tested = CapabilityRealization()
        tested.get_involved_functions()
        pass

    def test_CapabilityRealization_involved_functions_setter(self):
        tested = CapabilityRealization()
        value = PhysicalFunction()
        tested.get_involved_functions().add(value)
        pass

    def test_CapabilityRealization_pre_condition_getter(self):
        tested = CapabilityRealization()
        tested.get_pre_condition()
        pass

    def test_CapabilityRealization_pre_condition_setter(self):
        tested = CapabilityRealization()
        value = Constraint()
        tested.set_pre_condition(value)
        pass

    def test_CapabilityRealization_post_condition_getter(self):
        tested = CapabilityRealization()
        tested.get_post_condition()
        pass

    def test_CapabilityRealization_post_condition_setter(self):
        tested = CapabilityRealization()
        value = Constraint()
        tested.set_post_condition(value)
        pass

    def test_CapabilityRealization_owned_scenarios_getter(self):
        tested = CapabilityRealization()
        tested.get_owned_scenarios()
        pass

    def test_CapabilityRealization_super_getter(self):
        tested = CapabilityRealization()
        tested.get_super()
        pass

    def test_CapabilityRealization_super_setter(self):
        tested = CapabilityRealization()
        value = CapabilityRealization()
        tested.get_super().add(value)
        pass

    def test_CapabilityRealization_sub_getter(self):
        tested = CapabilityRealization()
        tested.get_sub()
        pass

    def test_CapabilityRealization_sub_setter(self):
        tested = CapabilityRealization()
        value = CapabilityRealization()
        tested.get_sub().add(value)
        pass

    def test_CapabilityRealization_included_capabilities_getter(self):
        tested = CapabilityRealization()
        tested.get_included_capabilities()
        pass

    def test_CapabilityRealization_included_capabilities_setter(self):
        tested = CapabilityRealization()
        value = CapabilityRealization()
        tested.get_included_capabilities().add(value)
        pass

    def test_CapabilityRealization_including_capabilities_getter(self):
        tested = CapabilityRealization()
        tested.get_including_capabilities()
        pass

    def test_CapabilityRealization_including_capabilities_setter(self):
        tested = CapabilityRealization()
        value = CapabilityRealization()
        tested.get_including_capabilities().add(value)
        pass

    def test_CapabilityRealization_extended_capabilities_getter(self):
        tested = CapabilityRealization()
        tested.get_extended_capabilities()
        pass

    def test_CapabilityRealization_extended_capabilities_setter(self):
        tested = CapabilityRealization()
        value = CapabilityRealization()
        tested.get_extended_capabilities().add(value)
        pass

    def test_CapabilityRealization_extending_capabilities_getter(self):
        tested = CapabilityRealization()
        tested.get_extending_capabilities()
        pass

    def test_CapabilityRealization_extending_capabilities_setter(self):
        tested = CapabilityRealization()
        value = CapabilityRealization()
        tested.get_extending_capabilities().add(value)
        pass

    def test_CapabilityRealization_available_in_states_getter(self):
        tested = CapabilityRealization()
        tested.get_available_in_states()
        pass

    def test_CapabilityRealization_available_in_states_setter(self):
        tested = CapabilityRealization()
        value = State()
        tested.get_available_in_states().add(value)
        pass

    def test_CapabilityRealization_owned_property_value_pkgs_getter(self):
        tested = CapabilityRealization()
        tested.get_owned_property_value_pkgs()
        pass

    def test_CapabilityRealization_id_getter(self):
        tested = CapabilityRealization()
        tested.get_id()
        pass

    def test_CapabilityRealization_id_setter(self):
        tested = CapabilityRealization()
        value = "value"
        tested.set_id(value)
        pass

    def test_CapabilityRealization_sid_getter(self):
        tested = CapabilityRealization()
        tested.get_sid()
        pass

    def test_CapabilityRealization_sid_setter(self):
        tested = CapabilityRealization()
        value = "value"
        tested.set_sid(value)
        pass

    def test_CapabilityRealization_name_getter(self):
        tested = CapabilityRealization()
        tested.get_name()
        pass

    def test_CapabilityRealization_name_setter(self):
        tested = CapabilityRealization()
        value = "value"
        tested.set_name(value)
        pass

    def test_CapabilityRealization_summary_getter(self):
        tested = CapabilityRealization()
        tested.get_summary()
        pass

    def test_CapabilityRealization_summary_setter(self):
        tested = CapabilityRealization()
        value = "value"
        tested.set_summary(value)
        pass

    def test_CapabilityRealization_description_getter(self):
        tested = CapabilityRealization()
        tested.get_description()
        pass

    def test_CapabilityRealization_description_setter(self):
        tested = CapabilityRealization()
        value = "value"
        tested.set_description(value)
        pass

    def test_CapabilityRealization_status_getter(self):
        tested = CapabilityRealization()
        tested.get_status()
        pass

    def test_CapabilityRealization_status_setter(self):
        tested = CapabilityRealization()
        value = "value"
        tested.set_status(value)
        pass

    def test_CapabilityRealization_review_getter(self):
        tested = CapabilityRealization()
        tested.get_review()
        pass

    def test_CapabilityRealization_review_setter(self):
        tested = CapabilityRealization()
        value = "value"
        tested.set_review(value)
        pass

    def test_CapabilityRealization_visible_in_documentation_getter(self):
        tested = CapabilityRealization()
        tested.get_visible_in_documentation()
        pass

    def test_CapabilityRealization_visible_in_documentation_setter(self):
        tested = CapabilityRealization()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_CapabilityRealization_visible_for_traceability_getter(self):
        tested = CapabilityRealization()
        tested.get_visible_for_traceability()
        pass

    def test_CapabilityRealization_visible_for_traceability_setter(self):
        tested = CapabilityRealization()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_CapabilityRealization_owned_constraints_getter(self):
        tested = CapabilityRealization()
        tested.get_owned_constraints()
        pass

    def test_CapabilityRealization_constraints_getter(self):
        tested = CapabilityRealization()
        tested.get_constraints()
        pass

    def test_CapabilityRealization_constraints_setter(self):
        tested = CapabilityRealization()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_CapabilityRealization_owned_property_values_getter(self):
        tested = CapabilityRealization()
        tested.get_owned_property_values()
        pass

    def test_CapabilityRealization_applied_property_values_getter(self):
        tested = CapabilityRealization()
        tested.get_applied_property_values()
        pass

    def test_CapabilityRealization_applied_property_values_setter(self):
        tested = CapabilityRealization()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_CapabilityRealization_owned_property_value_groups_getter(self):
        tested = CapabilityRealization()
        tested.get_owned_property_value_groups()
        pass

    def test_CapabilityRealization_applied_property_value_groups_getter(self):
        tested = CapabilityRealization()
        tested.get_applied_property_value_groups()
        pass

    def test_CapabilityRealization_applied_property_value_groups_setter(self):
        tested = CapabilityRealization()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_CapabilityRealization_owned_enumeration_property_types_getter(self):
        tested = CapabilityRealization()
        tested.get_owned_enumeration_property_types()
        pass

    def test_CapabilityRealization_owned_diagrams_getter(self):
        tested = CapabilityRealization()
        tested.get_owned_diagrams()
        pass

    def test_CapabilityRealization_element_of_interest_for_diagrams_getter(self):
        tested = CapabilityRealization()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_CapabilityRealization_element_of_interest_for_diagrams_setter(self):
        tested = CapabilityRealization()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_CapabilityRealization_contextual_element_for_diagrams_getter(self):
        tested = CapabilityRealization()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_CapabilityRealization_contextual_element_for_diagrams_setter(self):
        tested = CapabilityRealization()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_CapabilityRealization_representing_diagrams_getter(self):
        tested = CapabilityRealization()
        tested.get_representing_diagrams()
        pass

    def test_CapabilityRealization__r_e_cs_getter(self):
        tested = CapabilityRealization()
        tested.get__r_e_cs()
        pass

    def test_CapabilityRealization__r_e_cs_setter(self):
        tested = CapabilityRealization()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_CapabilityRealization__r_p_ls_getter(self):
        tested = CapabilityRealization()
        tested.get__r_p_ls()
        pass

    def test_CapabilityRealization__r_p_ls_setter(self):
        tested = CapabilityRealization()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_CapabilityRealization_get_label(self):
        tested = CapabilityRealization()
        tested.get_label()
        pass

    def test_CapabilityRealization_get_element_type(self):
        tested = CapabilityRealization()
        tested.get_element_type()
        pass

    def test_CapabilityRealization_get_container(self):
        tested = CapabilityRealization()
        tested.get_container()
        pass

    def test_CapabilityRealization_get_contents(self):
        tested = CapabilityRealization()
        tested.get_contents()
        pass

    def test_CapabilityRealization_get_all_contents(self):
        tested = CapabilityRealization()
        tested.get_all_contents()
        pass

    def test_CapabilityRealization_get_all_contents_by_type(self):
        tested = CapabilityRealization()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_CapabilityRealization_get_available_s_b_queries(self):
        tested = CapabilityRealization()
        tested.get_available_s_b_queries()
        pass

    def test_CapabilityRealization_get_query_result(self):
        tested = CapabilityRealization()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_CapabilityRealization_realized_capabilities_getter(self):
        tested = CapabilityRealization()
        tested.get_realized_capabilities()
        pass

    def test_CapabilityRealization_realized_capabilities_setter(self):
        tested = CapabilityRealization()
        value = Capability()
        tested.get_realized_capabilities().add(value)
        pass

    def test_CapabilityRealization_realized_capability_realizations_getter(self):
        tested = CapabilityRealization()
        tested.get_realized_capability_realizations()
        pass

    def test_CapabilityRealization_realized_capability_realizations_setter(self):
        tested = CapabilityRealization()
        value = CapabilityRealization()
        tested.get_realized_capability_realizations().add(value)
        pass

    def test_CapabilityRealization_realizing_capability_realizations_getter(self):
        tested = CapabilityRealization()
        tested.get_realizing_capability_realizations()
        pass

    def test_CapabilityRealization_realizing_capability_realizations_setter(self):
        tested = CapabilityRealization()
        value = CapabilityRealization()
        tested.get_realizing_capability_realizations().add(value)
        pass

    def test_CapabilityRealization_involved_logical_actors_getter(self):
        tested = CapabilityRealization()
        tested.get_involved_logical_actors()
        pass

    def test_CapabilityRealization_involved_logical_actors_setter(self):
        tested = CapabilityRealization()
        value = LogicalActor()
        tested.get_involved_logical_actors().add(value)
        pass

    def test_CapabilityRealization_involved_logical_components_getter(self):
        tested = CapabilityRealization()
        tested.get_involved_logical_components()
        pass

    def test_CapabilityRealization_involved_logical_components_setter(self):
        tested = CapabilityRealization()
        value = LogicalComponent()
        tested.get_involved_logical_components().add(value)
        pass

    def test_CapabilityRealization_involved_physical_components_getter(self):
        tested = CapabilityRealization()
        tested.get_involved_physical_components()
        pass

    def test_CapabilityRealization_involved_physical_components_setter(self):
        tested = CapabilityRealization()
        value = NodePC()
        tested.get_involved_physical_components().add(value)
        pass

    def test_CapabilityRealization_involved_physical_actors_getter(self):
        tested = CapabilityRealization()
        tested.get_involved_physical_actors()
        pass

    def test_CapabilityRealization_involved_physical_actors_setter(self):
        tested = CapabilityRealization()
        value = PhysicalActor()
        tested.get_involved_physical_actors().add(value)
        pass

    def test_LogicalComponentPkg_owned_property_value_pkgs_getter(self):
        tested = LogicalComponentPkg()
        tested.get_owned_property_value_pkgs()
        pass

    def test_LogicalComponentPkg_id_getter(self):
        tested = LogicalComponentPkg()
        tested.get_id()
        pass

    def test_LogicalComponentPkg_id_setter(self):
        tested = LogicalComponentPkg()
        value = "value"
        tested.set_id(value)
        pass

    def test_LogicalComponentPkg_sid_getter(self):
        tested = LogicalComponentPkg()
        tested.get_sid()
        pass

    def test_LogicalComponentPkg_sid_setter(self):
        tested = LogicalComponentPkg()
        value = "value"
        tested.set_sid(value)
        pass

    def test_LogicalComponentPkg_name_getter(self):
        tested = LogicalComponentPkg()
        tested.get_name()
        pass

    def test_LogicalComponentPkg_name_setter(self):
        tested = LogicalComponentPkg()
        value = "value"
        tested.set_name(value)
        pass

    def test_LogicalComponentPkg_summary_getter(self):
        tested = LogicalComponentPkg()
        tested.get_summary()
        pass

    def test_LogicalComponentPkg_summary_setter(self):
        tested = LogicalComponentPkg()
        value = "value"
        tested.set_summary(value)
        pass

    def test_LogicalComponentPkg_description_getter(self):
        tested = LogicalComponentPkg()
        tested.get_description()
        pass

    def test_LogicalComponentPkg_description_setter(self):
        tested = LogicalComponentPkg()
        value = "value"
        tested.set_description(value)
        pass

    def test_LogicalComponentPkg_status_getter(self):
        tested = LogicalComponentPkg()
        tested.get_status()
        pass

    def test_LogicalComponentPkg_status_setter(self):
        tested = LogicalComponentPkg()
        value = "value"
        tested.set_status(value)
        pass

    def test_LogicalComponentPkg_review_getter(self):
        tested = LogicalComponentPkg()
        tested.get_review()
        pass

    def test_LogicalComponentPkg_review_setter(self):
        tested = LogicalComponentPkg()
        value = "value"
        tested.set_review(value)
        pass

    def test_LogicalComponentPkg_visible_in_documentation_getter(self):
        tested = LogicalComponentPkg()
        tested.get_visible_in_documentation()
        pass

    def test_LogicalComponentPkg_visible_in_documentation_setter(self):
        tested = LogicalComponentPkg()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_LogicalComponentPkg_visible_for_traceability_getter(self):
        tested = LogicalComponentPkg()
        tested.get_visible_for_traceability()
        pass

    def test_LogicalComponentPkg_visible_for_traceability_setter(self):
        tested = LogicalComponentPkg()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_LogicalComponentPkg_owned_constraints_getter(self):
        tested = LogicalComponentPkg()
        tested.get_owned_constraints()
        pass

    def test_LogicalComponentPkg_constraints_getter(self):
        tested = LogicalComponentPkg()
        tested.get_constraints()
        pass

    def test_LogicalComponentPkg_constraints_setter(self):
        tested = LogicalComponentPkg()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_LogicalComponentPkg_owned_property_values_getter(self):
        tested = LogicalComponentPkg()
        tested.get_owned_property_values()
        pass

    def test_LogicalComponentPkg_applied_property_values_getter(self):
        tested = LogicalComponentPkg()
        tested.get_applied_property_values()
        pass

    def test_LogicalComponentPkg_applied_property_values_setter(self):
        tested = LogicalComponentPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_LogicalComponentPkg_owned_property_value_groups_getter(self):
        tested = LogicalComponentPkg()
        tested.get_owned_property_value_groups()
        pass

    def test_LogicalComponentPkg_applied_property_value_groups_getter(self):
        tested = LogicalComponentPkg()
        tested.get_applied_property_value_groups()
        pass

    def test_LogicalComponentPkg_applied_property_value_groups_setter(self):
        tested = LogicalComponentPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_LogicalComponentPkg_owned_enumeration_property_types_getter(self):
        tested = LogicalComponentPkg()
        tested.get_owned_enumeration_property_types()
        pass

    def test_LogicalComponentPkg_owned_diagrams_getter(self):
        tested = LogicalComponentPkg()
        tested.get_owned_diagrams()
        pass

    def test_LogicalComponentPkg_element_of_interest_for_diagrams_getter(self):
        tested = LogicalComponentPkg()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_LogicalComponentPkg_element_of_interest_for_diagrams_setter(self):
        tested = LogicalComponentPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_LogicalComponentPkg_contextual_element_for_diagrams_getter(self):
        tested = LogicalComponentPkg()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_LogicalComponentPkg_contextual_element_for_diagrams_setter(self):
        tested = LogicalComponentPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_LogicalComponentPkg_representing_diagrams_getter(self):
        tested = LogicalComponentPkg()
        tested.get_representing_diagrams()
        pass

    def test_LogicalComponentPkg__r_e_cs_getter(self):
        tested = LogicalComponentPkg()
        tested.get__r_e_cs()
        pass

    def test_LogicalComponentPkg__r_e_cs_setter(self):
        tested = LogicalComponentPkg()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_LogicalComponentPkg__r_p_ls_getter(self):
        tested = LogicalComponentPkg()
        tested.get__r_p_ls()
        pass

    def test_LogicalComponentPkg__r_p_ls_setter(self):
        tested = LogicalComponentPkg()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_LogicalComponentPkg_get_label(self):
        tested = LogicalComponentPkg()
        tested.get_label()
        pass

    def test_LogicalComponentPkg_get_element_type(self):
        tested = LogicalComponentPkg()
        tested.get_element_type()
        pass

    def test_LogicalComponentPkg_get_container(self):
        tested = LogicalComponentPkg()
        tested.get_container()
        pass

    def test_LogicalComponentPkg_get_contents(self):
        tested = LogicalComponentPkg()
        tested.get_contents()
        pass

    def test_LogicalComponentPkg_get_all_contents(self):
        tested = LogicalComponentPkg()
        tested.get_all_contents()
        pass

    def test_LogicalComponentPkg_get_all_contents_by_type(self):
        tested = LogicalComponentPkg()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_LogicalComponentPkg_get_available_s_b_queries(self):
        tested = LogicalComponentPkg()
        tested.get_available_s_b_queries()
        pass

    def test_LogicalComponentPkg_get_query_result(self):
        tested = LogicalComponentPkg()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_LogicalComponentPkg_owned_logical_component_pkgs_getter(self):
        tested = LogicalComponentPkg()
        tested.get_owned_logical_component_pkgs()
        pass

    def test_LogicalComponentPkg_owned_logical_system_getter(self):
        tested = LogicalComponentPkg()
        tested.get_owned_logical_system()
        pass

    def test_LogicalComponentPkg_owned_logical_actors_getter(self):
        tested = LogicalComponentPkg()
        tested.get_owned_logical_actors()
        pass

    def test_LogicalComponentPkg_owned_logical_components_getter(self):
        tested = LogicalComponentPkg()
        tested.get_owned_logical_components()
        pass

    def test_LogicalComponentPkg_owned_component_exchange_categories_getter(self):
        tested = LogicalComponentPkg()
        tested.get_owned_component_exchange_categories()
        pass

    def test_LogicalComponentPkg_owned_physical_link_categories_getter(self):
        tested = LogicalComponentPkg()
        tested.get_owned_physical_link_categories()
        pass

    def test_LogicalSystem_contained_component_ports_getter(self):
        tested = LogicalSystem()
        tested.get_contained_component_ports()
        pass

    def test_LogicalSystem_incoming_component_exchanges_getter(self):
        tested = LogicalSystem()
        tested.get_incoming_component_exchanges()
        pass

    def test_LogicalSystem_incoming_component_exchanges_setter(self):
        tested = LogicalSystem()
        value = ComponentExchange()
        tested.get_incoming_component_exchanges().add(value)
        pass

    def test_LogicalSystem_outgoing_component_exchanges_getter(self):
        tested = LogicalSystem()
        tested.get_outgoing_component_exchanges()
        pass

    def test_LogicalSystem_outgoing_component_exchanges_setter(self):
        tested = LogicalSystem()
        value = ComponentExchange()
        tested.get_outgoing_component_exchanges().add(value)
        pass

    def test_LogicalSystem_inout_component_exchanges_getter(self):
        tested = LogicalSystem()
        tested.get_inout_component_exchanges()
        pass

    def test_LogicalSystem_inout_component_exchanges_setter(self):
        tested = LogicalSystem()
        value = ComponentExchange()
        tested.get_inout_component_exchanges().add(value)
        pass

    def test_LogicalSystem_allocated_functions_getter(self):
        tested = LogicalSystem()
        tested.get_allocated_functions()
        pass

    def test_LogicalSystem_allocated_functions_setter(self):
        tested = LogicalSystem()
        value = PhysicalFunction()
        tested.get_allocated_functions().add(value)
        pass

    def test_LogicalSystem_used_interfaces_getter(self):
        tested = LogicalSystem()
        tested.get_used_interfaces()
        pass

    def test_LogicalSystem_used_interfaces_setter(self):
        tested = LogicalSystem()
        value = Interface()
        tested.get_used_interfaces().add(value)
        pass

    def test_LogicalSystem_implemented_interfaces_getter(self):
        tested = LogicalSystem()
        tested.get_implemented_interfaces()
        pass

    def test_LogicalSystem_implemented_interfaces_setter(self):
        tested = LogicalSystem()
        value = Interface()
        tested.get_implemented_interfaces().add(value)
        pass

    def test_LogicalSystem_owned_state_machines_getter(self):
        tested = LogicalSystem()
        tested.get_owned_state_machines()
        pass

    def test_LogicalSystem_owned_component_exchange_categories_getter(self):
        tested = LogicalSystem()
        tested.get_owned_component_exchange_categories()
        pass

    def test_LogicalSystem_id_getter(self):
        tested = LogicalSystem()
        tested.get_id()
        pass

    def test_LogicalSystem_id_setter(self):
        tested = LogicalSystem()
        value = "value"
        tested.set_id(value)
        pass

    def test_LogicalSystem_sid_getter(self):
        tested = LogicalSystem()
        tested.get_sid()
        pass

    def test_LogicalSystem_sid_setter(self):
        tested = LogicalSystem()
        value = "value"
        tested.set_sid(value)
        pass

    def test_LogicalSystem_name_getter(self):
        tested = LogicalSystem()
        tested.get_name()
        pass

    def test_LogicalSystem_name_setter(self):
        tested = LogicalSystem()
        value = "value"
        tested.set_name(value)
        pass

    def test_LogicalSystem_summary_getter(self):
        tested = LogicalSystem()
        tested.get_summary()
        pass

    def test_LogicalSystem_summary_setter(self):
        tested = LogicalSystem()
        value = "value"
        tested.set_summary(value)
        pass

    def test_LogicalSystem_description_getter(self):
        tested = LogicalSystem()
        tested.get_description()
        pass

    def test_LogicalSystem_description_setter(self):
        tested = LogicalSystem()
        value = "value"
        tested.set_description(value)
        pass

    def test_LogicalSystem_status_getter(self):
        tested = LogicalSystem()
        tested.get_status()
        pass

    def test_LogicalSystem_status_setter(self):
        tested = LogicalSystem()
        value = "value"
        tested.set_status(value)
        pass

    def test_LogicalSystem_review_getter(self):
        tested = LogicalSystem()
        tested.get_review()
        pass

    def test_LogicalSystem_review_setter(self):
        tested = LogicalSystem()
        value = "value"
        tested.set_review(value)
        pass

    def test_LogicalSystem_visible_in_documentation_getter(self):
        tested = LogicalSystem()
        tested.get_visible_in_documentation()
        pass

    def test_LogicalSystem_visible_in_documentation_setter(self):
        tested = LogicalSystem()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_LogicalSystem_visible_for_traceability_getter(self):
        tested = LogicalSystem()
        tested.get_visible_for_traceability()
        pass

    def test_LogicalSystem_visible_for_traceability_setter(self):
        tested = LogicalSystem()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_LogicalSystem_owned_constraints_getter(self):
        tested = LogicalSystem()
        tested.get_owned_constraints()
        pass

    def test_LogicalSystem_constraints_getter(self):
        tested = LogicalSystem()
        tested.get_constraints()
        pass

    def test_LogicalSystem_constraints_setter(self):
        tested = LogicalSystem()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_LogicalSystem_owned_property_values_getter(self):
        tested = LogicalSystem()
        tested.get_owned_property_values()
        pass

    def test_LogicalSystem_applied_property_values_getter(self):
        tested = LogicalSystem()
        tested.get_applied_property_values()
        pass

    def test_LogicalSystem_applied_property_values_setter(self):
        tested = LogicalSystem()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_LogicalSystem_owned_property_value_groups_getter(self):
        tested = LogicalSystem()
        tested.get_owned_property_value_groups()
        pass

    def test_LogicalSystem_applied_property_value_groups_getter(self):
        tested = LogicalSystem()
        tested.get_applied_property_value_groups()
        pass

    def test_LogicalSystem_applied_property_value_groups_setter(self):
        tested = LogicalSystem()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_LogicalSystem_owned_enumeration_property_types_getter(self):
        tested = LogicalSystem()
        tested.get_owned_enumeration_property_types()
        pass

    def test_LogicalSystem_owned_diagrams_getter(self):
        tested = LogicalSystem()
        tested.get_owned_diagrams()
        pass

    def test_LogicalSystem_element_of_interest_for_diagrams_getter(self):
        tested = LogicalSystem()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_LogicalSystem_element_of_interest_for_diagrams_setter(self):
        tested = LogicalSystem()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_LogicalSystem_contextual_element_for_diagrams_getter(self):
        tested = LogicalSystem()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_LogicalSystem_contextual_element_for_diagrams_setter(self):
        tested = LogicalSystem()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_LogicalSystem_representing_diagrams_getter(self):
        tested = LogicalSystem()
        tested.get_representing_diagrams()
        pass

    def test_LogicalSystem__r_e_cs_getter(self):
        tested = LogicalSystem()
        tested.get__r_e_cs()
        pass

    def test_LogicalSystem__r_e_cs_setter(self):
        tested = LogicalSystem()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_LogicalSystem__r_p_ls_getter(self):
        tested = LogicalSystem()
        tested.get__r_p_ls()
        pass

    def test_LogicalSystem__r_p_ls_setter(self):
        tested = LogicalSystem()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_LogicalSystem_get_label(self):
        tested = LogicalSystem()
        tested.get_label()
        pass

    def test_LogicalSystem_get_element_type(self):
        tested = LogicalSystem()
        tested.get_element_type()
        pass

    def test_LogicalSystem_get_container(self):
        tested = LogicalSystem()
        tested.get_container()
        pass

    def test_LogicalSystem_get_contents(self):
        tested = LogicalSystem()
        tested.get_contents()
        pass

    def test_LogicalSystem_get_all_contents(self):
        tested = LogicalSystem()
        tested.get_all_contents()
        pass

    def test_LogicalSystem_get_all_contents_by_type(self):
        tested = LogicalSystem()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_LogicalSystem_get_available_s_b_queries(self):
        tested = LogicalSystem()
        tested.get_available_s_b_queries()
        pass

    def test_LogicalSystem_get_query_result(self):
        tested = LogicalSystem()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_LogicalSystem_contained_physical_ports_getter(self):
        tested = LogicalSystem()
        tested.get_contained_physical_ports()
        pass

    def test_LogicalSystem_physical_links_getter(self):
        tested = LogicalSystem()
        tested.get_physical_links()
        pass

    def test_LogicalSystem_physical_links_setter(self):
        tested = LogicalSystem()
        value = PhysicalLink()
        tested.get_physical_links().add(value)
        pass

    def test_LogicalSystem_involving_physical_paths_getter(self):
        tested = LogicalSystem()
        tested.get_involving_physical_paths()
        pass

    def test_LogicalSystem_owned_physical_link_categories_getter(self):
        tested = LogicalSystem()
        tested.get_owned_physical_link_categories()
        pass

    def test_LogicalSystem_owned_physical_paths_getter(self):
        tested = LogicalSystem()
        tested.get_owned_physical_paths()
        pass

    def test_LogicalSystem_owned_logical_components_getter(self):
        tested = LogicalSystem()
        tested.get_owned_logical_components()
        pass

    def test_LogicalSystem_owned_logical_component_pkgs_getter(self):
        tested = LogicalSystem()
        tested.get_owned_logical_component_pkgs()
        pass

    def test_LogicalComponent_contained_component_ports_getter(self):
        tested = LogicalComponent()
        tested.get_contained_component_ports()
        pass

    def test_LogicalComponent_incoming_component_exchanges_getter(self):
        tested = LogicalComponent()
        tested.get_incoming_component_exchanges()
        pass

    def test_LogicalComponent_incoming_component_exchanges_setter(self):
        tested = LogicalComponent()
        value = ComponentExchange()
        tested.get_incoming_component_exchanges().add(value)
        pass

    def test_LogicalComponent_outgoing_component_exchanges_getter(self):
        tested = LogicalComponent()
        tested.get_outgoing_component_exchanges()
        pass

    def test_LogicalComponent_outgoing_component_exchanges_setter(self):
        tested = LogicalComponent()
        value = ComponentExchange()
        tested.get_outgoing_component_exchanges().add(value)
        pass

    def test_LogicalComponent_inout_component_exchanges_getter(self):
        tested = LogicalComponent()
        tested.get_inout_component_exchanges()
        pass

    def test_LogicalComponent_inout_component_exchanges_setter(self):
        tested = LogicalComponent()
        value = ComponentExchange()
        tested.get_inout_component_exchanges().add(value)
        pass

    def test_LogicalComponent_allocated_functions_getter(self):
        tested = LogicalComponent()
        tested.get_allocated_functions()
        pass

    def test_LogicalComponent_allocated_functions_setter(self):
        tested = LogicalComponent()
        value = PhysicalFunction()
        tested.get_allocated_functions().add(value)
        pass

    def test_LogicalComponent_used_interfaces_getter(self):
        tested = LogicalComponent()
        tested.get_used_interfaces()
        pass

    def test_LogicalComponent_used_interfaces_setter(self):
        tested = LogicalComponent()
        value = Interface()
        tested.get_used_interfaces().add(value)
        pass

    def test_LogicalComponent_implemented_interfaces_getter(self):
        tested = LogicalComponent()
        tested.get_implemented_interfaces()
        pass

    def test_LogicalComponent_implemented_interfaces_setter(self):
        tested = LogicalComponent()
        value = Interface()
        tested.get_implemented_interfaces().add(value)
        pass

    def test_LogicalComponent_owned_state_machines_getter(self):
        tested = LogicalComponent()
        tested.get_owned_state_machines()
        pass

    def test_LogicalComponent_owned_component_exchange_categories_getter(self):
        tested = LogicalComponent()
        tested.get_owned_component_exchange_categories()
        pass

    def test_LogicalComponent_id_getter(self):
        tested = LogicalComponent()
        tested.get_id()
        pass

    def test_LogicalComponent_id_setter(self):
        tested = LogicalComponent()
        value = "value"
        tested.set_id(value)
        pass

    def test_LogicalComponent_sid_getter(self):
        tested = LogicalComponent()
        tested.get_sid()
        pass

    def test_LogicalComponent_sid_setter(self):
        tested = LogicalComponent()
        value = "value"
        tested.set_sid(value)
        pass

    def test_LogicalComponent_name_getter(self):
        tested = LogicalComponent()
        tested.get_name()
        pass

    def test_LogicalComponent_name_setter(self):
        tested = LogicalComponent()
        value = "value"
        tested.set_name(value)
        pass

    def test_LogicalComponent_summary_getter(self):
        tested = LogicalComponent()
        tested.get_summary()
        pass

    def test_LogicalComponent_summary_setter(self):
        tested = LogicalComponent()
        value = "value"
        tested.set_summary(value)
        pass

    def test_LogicalComponent_description_getter(self):
        tested = LogicalComponent()
        tested.get_description()
        pass

    def test_LogicalComponent_description_setter(self):
        tested = LogicalComponent()
        value = "value"
        tested.set_description(value)
        pass

    def test_LogicalComponent_status_getter(self):
        tested = LogicalComponent()
        tested.get_status()
        pass

    def test_LogicalComponent_status_setter(self):
        tested = LogicalComponent()
        value = "value"
        tested.set_status(value)
        pass

    def test_LogicalComponent_review_getter(self):
        tested = LogicalComponent()
        tested.get_review()
        pass

    def test_LogicalComponent_review_setter(self):
        tested = LogicalComponent()
        value = "value"
        tested.set_review(value)
        pass

    def test_LogicalComponent_visible_in_documentation_getter(self):
        tested = LogicalComponent()
        tested.get_visible_in_documentation()
        pass

    def test_LogicalComponent_visible_in_documentation_setter(self):
        tested = LogicalComponent()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_LogicalComponent_visible_for_traceability_getter(self):
        tested = LogicalComponent()
        tested.get_visible_for_traceability()
        pass

    def test_LogicalComponent_visible_for_traceability_setter(self):
        tested = LogicalComponent()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_LogicalComponent_owned_constraints_getter(self):
        tested = LogicalComponent()
        tested.get_owned_constraints()
        pass

    def test_LogicalComponent_constraints_getter(self):
        tested = LogicalComponent()
        tested.get_constraints()
        pass

    def test_LogicalComponent_constraints_setter(self):
        tested = LogicalComponent()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_LogicalComponent_owned_property_values_getter(self):
        tested = LogicalComponent()
        tested.get_owned_property_values()
        pass

    def test_LogicalComponent_applied_property_values_getter(self):
        tested = LogicalComponent()
        tested.get_applied_property_values()
        pass

    def test_LogicalComponent_applied_property_values_setter(self):
        tested = LogicalComponent()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_LogicalComponent_owned_property_value_groups_getter(self):
        tested = LogicalComponent()
        tested.get_owned_property_value_groups()
        pass

    def test_LogicalComponent_applied_property_value_groups_getter(self):
        tested = LogicalComponent()
        tested.get_applied_property_value_groups()
        pass

    def test_LogicalComponent_applied_property_value_groups_setter(self):
        tested = LogicalComponent()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_LogicalComponent_owned_enumeration_property_types_getter(self):
        tested = LogicalComponent()
        tested.get_owned_enumeration_property_types()
        pass

    def test_LogicalComponent_owned_diagrams_getter(self):
        tested = LogicalComponent()
        tested.get_owned_diagrams()
        pass

    def test_LogicalComponent_element_of_interest_for_diagrams_getter(self):
        tested = LogicalComponent()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_LogicalComponent_element_of_interest_for_diagrams_setter(self):
        tested = LogicalComponent()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_LogicalComponent_contextual_element_for_diagrams_getter(self):
        tested = LogicalComponent()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_LogicalComponent_contextual_element_for_diagrams_setter(self):
        tested = LogicalComponent()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_LogicalComponent_representing_diagrams_getter(self):
        tested = LogicalComponent()
        tested.get_representing_diagrams()
        pass

    def test_LogicalComponent__r_e_cs_getter(self):
        tested = LogicalComponent()
        tested.get__r_e_cs()
        pass

    def test_LogicalComponent__r_e_cs_setter(self):
        tested = LogicalComponent()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_LogicalComponent__r_p_ls_getter(self):
        tested = LogicalComponent()
        tested.get__r_p_ls()
        pass

    def test_LogicalComponent__r_p_ls_setter(self):
        tested = LogicalComponent()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_LogicalComponent_get_label(self):
        tested = LogicalComponent()
        tested.get_label()
        pass

    def test_LogicalComponent_get_element_type(self):
        tested = LogicalComponent()
        tested.get_element_type()
        pass

    def test_LogicalComponent_get_container(self):
        tested = LogicalComponent()
        tested.get_container()
        pass

    def test_LogicalComponent_get_contents(self):
        tested = LogicalComponent()
        tested.get_contents()
        pass

    def test_LogicalComponent_get_all_contents(self):
        tested = LogicalComponent()
        tested.get_all_contents()
        pass

    def test_LogicalComponent_get_all_contents_by_type(self):
        tested = LogicalComponent()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_LogicalComponent_get_available_s_b_queries(self):
        tested = LogicalComponent()
        tested.get_available_s_b_queries()
        pass

    def test_LogicalComponent_get_query_result(self):
        tested = LogicalComponent()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_LogicalComponent_owned_logical_components_getter(self):
        tested = LogicalComponent()
        tested.get_owned_logical_components()
        pass

    def test_LogicalComponent_owned_logical_component_pkgs_getter(self):
        tested = LogicalComponent()
        tested.get_owned_logical_component_pkgs()
        pass

    def test_LogicalComponent_is_human_getter(self):
        tested = LogicalComponent()
        tested.get_is_human()
        pass

    def test_LogicalComponent_is_human_setter(self):
        tested = LogicalComponent()
        value = True
        tested.set_is_human(value)
        pass

    def test_LogicalComponent_realizing_behavior_p_cs_getter(self):
        tested = LogicalComponent()
        tested.get_realizing_behavior_p_cs()
        pass

    def test_LogicalComponent_realizing_behavior_p_cs_setter(self):
        tested = LogicalComponent()
        value = BehaviorPC()
        tested.get_realizing_behavior_p_cs().add(value)
        pass

    def test_LogicalComponent_involving_capability_realizations_getter(self):
        tested = LogicalComponent()
        tested.get_involving_capability_realizations()
        pass

    def test_LogicalComponent_involving_capability_realizations_setter(self):
        tested = LogicalComponent()
        value = CapabilityRealization()
        tested.get_involving_capability_realizations().add(value)
        pass

    def test_LogicalActor_contained_component_ports_getter(self):
        tested = LogicalActor()
        tested.get_contained_component_ports()
        pass

    def test_LogicalActor_incoming_component_exchanges_getter(self):
        tested = LogicalActor()
        tested.get_incoming_component_exchanges()
        pass

    def test_LogicalActor_incoming_component_exchanges_setter(self):
        tested = LogicalActor()
        value = ComponentExchange()
        tested.get_incoming_component_exchanges().add(value)
        pass

    def test_LogicalActor_outgoing_component_exchanges_getter(self):
        tested = LogicalActor()
        tested.get_outgoing_component_exchanges()
        pass

    def test_LogicalActor_outgoing_component_exchanges_setter(self):
        tested = LogicalActor()
        value = ComponentExchange()
        tested.get_outgoing_component_exchanges().add(value)
        pass

    def test_LogicalActor_inout_component_exchanges_getter(self):
        tested = LogicalActor()
        tested.get_inout_component_exchanges()
        pass

    def test_LogicalActor_inout_component_exchanges_setter(self):
        tested = LogicalActor()
        value = ComponentExchange()
        tested.get_inout_component_exchanges().add(value)
        pass

    def test_LogicalActor_allocated_functions_getter(self):
        tested = LogicalActor()
        tested.get_allocated_functions()
        pass

    def test_LogicalActor_allocated_functions_setter(self):
        tested = LogicalActor()
        value = PhysicalFunction()
        tested.get_allocated_functions().add(value)
        pass

    def test_LogicalActor_used_interfaces_getter(self):
        tested = LogicalActor()
        tested.get_used_interfaces()
        pass

    def test_LogicalActor_used_interfaces_setter(self):
        tested = LogicalActor()
        value = Interface()
        tested.get_used_interfaces().add(value)
        pass

    def test_LogicalActor_implemented_interfaces_getter(self):
        tested = LogicalActor()
        tested.get_implemented_interfaces()
        pass

    def test_LogicalActor_implemented_interfaces_setter(self):
        tested = LogicalActor()
        value = Interface()
        tested.get_implemented_interfaces().add(value)
        pass

    def test_LogicalActor_owned_state_machines_getter(self):
        tested = LogicalActor()
        tested.get_owned_state_machines()
        pass

    def test_LogicalActor_owned_component_exchange_categories_getter(self):
        tested = LogicalActor()
        tested.get_owned_component_exchange_categories()
        pass

    def test_LogicalActor_id_getter(self):
        tested = LogicalActor()
        tested.get_id()
        pass

    def test_LogicalActor_id_setter(self):
        tested = LogicalActor()
        value = "value"
        tested.set_id(value)
        pass

    def test_LogicalActor_sid_getter(self):
        tested = LogicalActor()
        tested.get_sid()
        pass

    def test_LogicalActor_sid_setter(self):
        tested = LogicalActor()
        value = "value"
        tested.set_sid(value)
        pass

    def test_LogicalActor_name_getter(self):
        tested = LogicalActor()
        tested.get_name()
        pass

    def test_LogicalActor_name_setter(self):
        tested = LogicalActor()
        value = "value"
        tested.set_name(value)
        pass

    def test_LogicalActor_summary_getter(self):
        tested = LogicalActor()
        tested.get_summary()
        pass

    def test_LogicalActor_summary_setter(self):
        tested = LogicalActor()
        value = "value"
        tested.set_summary(value)
        pass

    def test_LogicalActor_description_getter(self):
        tested = LogicalActor()
        tested.get_description()
        pass

    def test_LogicalActor_description_setter(self):
        tested = LogicalActor()
        value = "value"
        tested.set_description(value)
        pass

    def test_LogicalActor_status_getter(self):
        tested = LogicalActor()
        tested.get_status()
        pass

    def test_LogicalActor_status_setter(self):
        tested = LogicalActor()
        value = "value"
        tested.set_status(value)
        pass

    def test_LogicalActor_review_getter(self):
        tested = LogicalActor()
        tested.get_review()
        pass

    def test_LogicalActor_review_setter(self):
        tested = LogicalActor()
        value = "value"
        tested.set_review(value)
        pass

    def test_LogicalActor_visible_in_documentation_getter(self):
        tested = LogicalActor()
        tested.get_visible_in_documentation()
        pass

    def test_LogicalActor_visible_in_documentation_setter(self):
        tested = LogicalActor()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_LogicalActor_visible_for_traceability_getter(self):
        tested = LogicalActor()
        tested.get_visible_for_traceability()
        pass

    def test_LogicalActor_visible_for_traceability_setter(self):
        tested = LogicalActor()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_LogicalActor_owned_constraints_getter(self):
        tested = LogicalActor()
        tested.get_owned_constraints()
        pass

    def test_LogicalActor_constraints_getter(self):
        tested = LogicalActor()
        tested.get_constraints()
        pass

    def test_LogicalActor_constraints_setter(self):
        tested = LogicalActor()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_LogicalActor_owned_property_values_getter(self):
        tested = LogicalActor()
        tested.get_owned_property_values()
        pass

    def test_LogicalActor_applied_property_values_getter(self):
        tested = LogicalActor()
        tested.get_applied_property_values()
        pass

    def test_LogicalActor_applied_property_values_setter(self):
        tested = LogicalActor()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_LogicalActor_owned_property_value_groups_getter(self):
        tested = LogicalActor()
        tested.get_owned_property_value_groups()
        pass

    def test_LogicalActor_applied_property_value_groups_getter(self):
        tested = LogicalActor()
        tested.get_applied_property_value_groups()
        pass

    def test_LogicalActor_applied_property_value_groups_setter(self):
        tested = LogicalActor()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_LogicalActor_owned_enumeration_property_types_getter(self):
        tested = LogicalActor()
        tested.get_owned_enumeration_property_types()
        pass

    def test_LogicalActor_owned_diagrams_getter(self):
        tested = LogicalActor()
        tested.get_owned_diagrams()
        pass

    def test_LogicalActor_element_of_interest_for_diagrams_getter(self):
        tested = LogicalActor()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_LogicalActor_element_of_interest_for_diagrams_setter(self):
        tested = LogicalActor()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_LogicalActor_contextual_element_for_diagrams_getter(self):
        tested = LogicalActor()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_LogicalActor_contextual_element_for_diagrams_setter(self):
        tested = LogicalActor()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_LogicalActor_representing_diagrams_getter(self):
        tested = LogicalActor()
        tested.get_representing_diagrams()
        pass

    def test_LogicalActor__r_e_cs_getter(self):
        tested = LogicalActor()
        tested.get__r_e_cs()
        pass

    def test_LogicalActor__r_e_cs_setter(self):
        tested = LogicalActor()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_LogicalActor__r_p_ls_getter(self):
        tested = LogicalActor()
        tested.get__r_p_ls()
        pass

    def test_LogicalActor__r_p_ls_setter(self):
        tested = LogicalActor()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_LogicalActor_get_label(self):
        tested = LogicalActor()
        tested.get_label()
        pass

    def test_LogicalActor_get_element_type(self):
        tested = LogicalActor()
        tested.get_element_type()
        pass

    def test_LogicalActor_get_container(self):
        tested = LogicalActor()
        tested.get_container()
        pass

    def test_LogicalActor_get_contents(self):
        tested = LogicalActor()
        tested.get_contents()
        pass

    def test_LogicalActor_get_all_contents(self):
        tested = LogicalActor()
        tested.get_all_contents()
        pass

    def test_LogicalActor_get_all_contents_by_type(self):
        tested = LogicalActor()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_LogicalActor_get_available_s_b_queries(self):
        tested = LogicalActor()
        tested.get_available_s_b_queries()
        pass

    def test_LogicalActor_get_query_result(self):
        tested = LogicalActor()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_LogicalActor_contained_physical_ports_getter(self):
        tested = LogicalActor()
        tested.get_contained_physical_ports()
        pass

    def test_LogicalActor_physical_links_getter(self):
        tested = LogicalActor()
        tested.get_physical_links()
        pass

    def test_LogicalActor_physical_links_setter(self):
        tested = LogicalActor()
        value = PhysicalLink()
        tested.get_physical_links().add(value)
        pass

    def test_LogicalActor_involving_physical_paths_getter(self):
        tested = LogicalActor()
        tested.get_involving_physical_paths()
        pass

    def test_LogicalActor_owned_physical_link_categories_getter(self):
        tested = LogicalActor()
        tested.get_owned_physical_link_categories()
        pass

    def test_LogicalActor_owned_physical_paths_getter(self):
        tested = LogicalActor()
        tested.get_owned_physical_paths()
        pass

    def test_LogicalActor_owned_logical_actors_getter(self):
        tested = LogicalActor()
        tested.get_owned_logical_actors()
        pass

    def test_LogicalActor_owned_logical_component_pkgs_getter(self):
        tested = LogicalActor()
        tested.get_owned_logical_component_pkgs()
        pass

    def test_LogicalActor_realized_system_actors_getter(self):
        tested = LogicalActor()
        tested.get_realized_system_actors()
        pass

    def test_LogicalActor_realized_system_actors_setter(self):
        tested = LogicalActor()
        value = SystemActor()
        tested.get_realized_system_actors().add(value)
        pass

    def test_LogicalActor_is_human_getter(self):
        tested = LogicalActor()
        tested.get_is_human()
        pass

    def test_LogicalActor_is_human_setter(self):
        tested = LogicalActor()
        value = True
        tested.set_is_human(value)
        pass

    def test_LogicalActor_realizing_physical_actors_getter(self):
        tested = LogicalActor()
        tested.get_realizing_physical_actors()
        pass

    def test_LogicalActor_realizing_physical_actors_setter(self):
        tested = LogicalActor()
        value = PhysicalActor()
        tested.get_realizing_physical_actors().add(value)
        pass

    def test_LogicalActor_involving_capability_realizations_getter(self):
        tested = LogicalActor()
        tested.get_involving_capability_realizations()
        pass

    def test_LogicalActor_involving_capability_realizations_setter(self):
        tested = LogicalActor()
        value = CapabilityRealization()
        tested.get_involving_capability_realizations().add(value)
        pass

    def test_PhysicalArchitecture_owned_property_value_pkgs_getter(self):
        tested = PhysicalArchitecture()
        tested.get_owned_property_value_pkgs()
        pass

    def test_PhysicalArchitecture_id_getter(self):
        tested = PhysicalArchitecture()
        tested.get_id()
        pass

    def test_PhysicalArchitecture_id_setter(self):
        tested = PhysicalArchitecture()
        value = "value"
        tested.set_id(value)
        pass

    def test_PhysicalArchitecture_sid_getter(self):
        tested = PhysicalArchitecture()
        tested.get_sid()
        pass

    def test_PhysicalArchitecture_sid_setter(self):
        tested = PhysicalArchitecture()
        value = "value"
        tested.set_sid(value)
        pass

    def test_PhysicalArchitecture_name_getter(self):
        tested = PhysicalArchitecture()
        tested.get_name()
        pass

    def test_PhysicalArchitecture_name_setter(self):
        tested = PhysicalArchitecture()
        value = "value"
        tested.set_name(value)
        pass

    def test_PhysicalArchitecture_summary_getter(self):
        tested = PhysicalArchitecture()
        tested.get_summary()
        pass

    def test_PhysicalArchitecture_summary_setter(self):
        tested = PhysicalArchitecture()
        value = "value"
        tested.set_summary(value)
        pass

    def test_PhysicalArchitecture_description_getter(self):
        tested = PhysicalArchitecture()
        tested.get_description()
        pass

    def test_PhysicalArchitecture_description_setter(self):
        tested = PhysicalArchitecture()
        value = "value"
        tested.set_description(value)
        pass

    def test_PhysicalArchitecture_status_getter(self):
        tested = PhysicalArchitecture()
        tested.get_status()
        pass

    def test_PhysicalArchitecture_status_setter(self):
        tested = PhysicalArchitecture()
        value = "value"
        tested.set_status(value)
        pass

    def test_PhysicalArchitecture_review_getter(self):
        tested = PhysicalArchitecture()
        tested.get_review()
        pass

    def test_PhysicalArchitecture_review_setter(self):
        tested = PhysicalArchitecture()
        value = "value"
        tested.set_review(value)
        pass

    def test_PhysicalArchitecture_visible_in_documentation_getter(self):
        tested = PhysicalArchitecture()
        tested.get_visible_in_documentation()
        pass

    def test_PhysicalArchitecture_visible_in_documentation_setter(self):
        tested = PhysicalArchitecture()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_PhysicalArchitecture_visible_for_traceability_getter(self):
        tested = PhysicalArchitecture()
        tested.get_visible_for_traceability()
        pass

    def test_PhysicalArchitecture_visible_for_traceability_setter(self):
        tested = PhysicalArchitecture()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_PhysicalArchitecture_owned_constraints_getter(self):
        tested = PhysicalArchitecture()
        tested.get_owned_constraints()
        pass

    def test_PhysicalArchitecture_constraints_getter(self):
        tested = PhysicalArchitecture()
        tested.get_constraints()
        pass

    def test_PhysicalArchitecture_constraints_setter(self):
        tested = PhysicalArchitecture()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_PhysicalArchitecture_owned_property_values_getter(self):
        tested = PhysicalArchitecture()
        tested.get_owned_property_values()
        pass

    def test_PhysicalArchitecture_applied_property_values_getter(self):
        tested = PhysicalArchitecture()
        tested.get_applied_property_values()
        pass

    def test_PhysicalArchitecture_applied_property_values_setter(self):
        tested = PhysicalArchitecture()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_PhysicalArchitecture_owned_property_value_groups_getter(self):
        tested = PhysicalArchitecture()
        tested.get_owned_property_value_groups()
        pass

    def test_PhysicalArchitecture_applied_property_value_groups_getter(self):
        tested = PhysicalArchitecture()
        tested.get_applied_property_value_groups()
        pass

    def test_PhysicalArchitecture_applied_property_value_groups_setter(self):
        tested = PhysicalArchitecture()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_PhysicalArchitecture_owned_enumeration_property_types_getter(self):
        tested = PhysicalArchitecture()
        tested.get_owned_enumeration_property_types()
        pass

    def test_PhysicalArchitecture_owned_diagrams_getter(self):
        tested = PhysicalArchitecture()
        tested.get_owned_diagrams()
        pass

    def test_PhysicalArchitecture_element_of_interest_for_diagrams_getter(self):
        tested = PhysicalArchitecture()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_PhysicalArchitecture_element_of_interest_for_diagrams_setter(self):
        tested = PhysicalArchitecture()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_PhysicalArchitecture_contextual_element_for_diagrams_getter(self):
        tested = PhysicalArchitecture()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_PhysicalArchitecture_contextual_element_for_diagrams_setter(self):
        tested = PhysicalArchitecture()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_PhysicalArchitecture_representing_diagrams_getter(self):
        tested = PhysicalArchitecture()
        tested.get_representing_diagrams()
        pass

    def test_PhysicalArchitecture__r_e_cs_getter(self):
        tested = PhysicalArchitecture()
        tested.get__r_e_cs()
        pass

    def test_PhysicalArchitecture__r_e_cs_setter(self):
        tested = PhysicalArchitecture()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_PhysicalArchitecture__r_p_ls_getter(self):
        tested = PhysicalArchitecture()
        tested.get__r_p_ls()
        pass

    def test_PhysicalArchitecture__r_p_ls_setter(self):
        tested = PhysicalArchitecture()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_PhysicalArchitecture_get_label(self):
        tested = PhysicalArchitecture()
        tested.get_label()
        pass

    def test_PhysicalArchitecture_get_element_type(self):
        tested = PhysicalArchitecture()
        tested.get_element_type()
        pass

    def test_PhysicalArchitecture_get_container(self):
        tested = PhysicalArchitecture()
        tested.get_container()
        pass

    def test_PhysicalArchitecture_get_contents(self):
        tested = PhysicalArchitecture()
        tested.get_contents()
        pass

    def test_PhysicalArchitecture_get_all_contents(self):
        tested = PhysicalArchitecture()
        tested.get_all_contents()
        pass

    def test_PhysicalArchitecture_get_all_contents_by_type(self):
        tested = PhysicalArchitecture()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_PhysicalArchitecture_get_available_s_b_queries(self):
        tested = PhysicalArchitecture()
        tested.get_available_s_b_queries()
        pass

    def test_PhysicalArchitecture_get_query_result(self):
        tested = PhysicalArchitecture()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_PhysicalArchitecture_physical_function_pkg_getter(self):
        tested = PhysicalArchitecture()
        tested.get_physical_function_pkg()
        pass

    def test_PhysicalArchitecture_capability_realization_pkg_getter(self):
        tested = PhysicalArchitecture()
        tested.get_capability_realization_pkg()
        pass

    def test_PhysicalArchitecture_interface_pkg_getter(self):
        tested = PhysicalArchitecture()
        tested.get_interface_pkg()
        pass

    def test_PhysicalArchitecture_data_pkg_getter(self):
        tested = PhysicalArchitecture()
        tested.get_data_pkg()
        pass

    def test_PhysicalArchitecture_physical_component_pkg_getter(self):
        tested = PhysicalArchitecture()
        tested.get_physical_component_pkg()
        pass

    def test_PhysicalArchitecture_physical_system_getter(self):
        tested = PhysicalArchitecture()
        tested.get_physical_system()
        pass

    def test_PhysicalFunctionPkg_owned_property_value_pkgs_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_owned_property_value_pkgs()
        pass

    def test_PhysicalFunctionPkg_id_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_id()
        pass

    def test_PhysicalFunctionPkg_id_setter(self):
        tested = PhysicalFunctionPkg()
        value = "value"
        tested.set_id(value)
        pass

    def test_PhysicalFunctionPkg_sid_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_sid()
        pass

    def test_PhysicalFunctionPkg_sid_setter(self):
        tested = PhysicalFunctionPkg()
        value = "value"
        tested.set_sid(value)
        pass

    def test_PhysicalFunctionPkg_name_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_name()
        pass

    def test_PhysicalFunctionPkg_name_setter(self):
        tested = PhysicalFunctionPkg()
        value = "value"
        tested.set_name(value)
        pass

    def test_PhysicalFunctionPkg_summary_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_summary()
        pass

    def test_PhysicalFunctionPkg_summary_setter(self):
        tested = PhysicalFunctionPkg()
        value = "value"
        tested.set_summary(value)
        pass

    def test_PhysicalFunctionPkg_description_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_description()
        pass

    def test_PhysicalFunctionPkg_description_setter(self):
        tested = PhysicalFunctionPkg()
        value = "value"
        tested.set_description(value)
        pass

    def test_PhysicalFunctionPkg_status_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_status()
        pass

    def test_PhysicalFunctionPkg_status_setter(self):
        tested = PhysicalFunctionPkg()
        value = "value"
        tested.set_status(value)
        pass

    def test_PhysicalFunctionPkg_review_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_review()
        pass

    def test_PhysicalFunctionPkg_review_setter(self):
        tested = PhysicalFunctionPkg()
        value = "value"
        tested.set_review(value)
        pass

    def test_PhysicalFunctionPkg_visible_in_documentation_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_visible_in_documentation()
        pass

    def test_PhysicalFunctionPkg_visible_in_documentation_setter(self):
        tested = PhysicalFunctionPkg()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_PhysicalFunctionPkg_visible_for_traceability_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_visible_for_traceability()
        pass

    def test_PhysicalFunctionPkg_visible_for_traceability_setter(self):
        tested = PhysicalFunctionPkg()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_PhysicalFunctionPkg_owned_constraints_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_owned_constraints()
        pass

    def test_PhysicalFunctionPkg_constraints_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_constraints()
        pass

    def test_PhysicalFunctionPkg_constraints_setter(self):
        tested = PhysicalFunctionPkg()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_PhysicalFunctionPkg_owned_property_values_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_owned_property_values()
        pass

    def test_PhysicalFunctionPkg_applied_property_values_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_applied_property_values()
        pass

    def test_PhysicalFunctionPkg_applied_property_values_setter(self):
        tested = PhysicalFunctionPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_PhysicalFunctionPkg_owned_property_value_groups_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_owned_property_value_groups()
        pass

    def test_PhysicalFunctionPkg_applied_property_value_groups_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_applied_property_value_groups()
        pass

    def test_PhysicalFunctionPkg_applied_property_value_groups_setter(self):
        tested = PhysicalFunctionPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_PhysicalFunctionPkg_owned_enumeration_property_types_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_owned_enumeration_property_types()
        pass

    def test_PhysicalFunctionPkg_owned_diagrams_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_owned_diagrams()
        pass

    def test_PhysicalFunctionPkg_element_of_interest_for_diagrams_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_PhysicalFunctionPkg_element_of_interest_for_diagrams_setter(self):
        tested = PhysicalFunctionPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_PhysicalFunctionPkg_contextual_element_for_diagrams_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_PhysicalFunctionPkg_contextual_element_for_diagrams_setter(self):
        tested = PhysicalFunctionPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_PhysicalFunctionPkg_representing_diagrams_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_representing_diagrams()
        pass

    def test_PhysicalFunctionPkg__r_e_cs_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get__r_e_cs()
        pass

    def test_PhysicalFunctionPkg__r_e_cs_setter(self):
        tested = PhysicalFunctionPkg()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_PhysicalFunctionPkg__r_p_ls_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get__r_p_ls()
        pass

    def test_PhysicalFunctionPkg__r_p_ls_setter(self):
        tested = PhysicalFunctionPkg()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_PhysicalFunctionPkg_get_label(self):
        tested = PhysicalFunctionPkg()
        tested.get_label()
        pass

    def test_PhysicalFunctionPkg_get_element_type(self):
        tested = PhysicalFunctionPkg()
        tested.get_element_type()
        pass

    def test_PhysicalFunctionPkg_get_container(self):
        tested = PhysicalFunctionPkg()
        tested.get_container()
        pass

    def test_PhysicalFunctionPkg_get_contents(self):
        tested = PhysicalFunctionPkg()
        tested.get_contents()
        pass

    def test_PhysicalFunctionPkg_get_all_contents(self):
        tested = PhysicalFunctionPkg()
        tested.get_all_contents()
        pass

    def test_PhysicalFunctionPkg_get_all_contents_by_type(self):
        tested = PhysicalFunctionPkg()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_PhysicalFunctionPkg_get_available_s_b_queries(self):
        tested = PhysicalFunctionPkg()
        tested.get_available_s_b_queries()
        pass

    def test_PhysicalFunctionPkg_get_query_result(self):
        tested = PhysicalFunctionPkg()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_PhysicalFunctionPkg_owned_physical_function_pkgs_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_owned_physical_function_pkgs()
        pass

    def test_PhysicalFunctionPkg_owned_physical_functions_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_owned_physical_functions()
        pass

    def test_PhysicalFunctionPkg_owned_categories_getter(self):
        tested = PhysicalFunctionPkg()
        tested.get_owned_categories()
        pass

    def test_PhysicalFunction_kind_getter(self):
        tested = PhysicalFunction()
        tested.get_kind()
        pass

    def test_PhysicalFunction_kind_setter(self):
        tested = PhysicalFunction()
        value = FunctionKind()
        tested.set_kind(value)
        pass

    def test_PhysicalFunction_condition_getter(self):
        tested = PhysicalFunction()
        tested.get_condition()
        pass

    def test_PhysicalFunction_condition_setter(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_condition(value)
        pass

    def test_PhysicalFunction_inputs_getter(self):
        tested = PhysicalFunction()
        tested.get_inputs()
        pass

    def test_PhysicalFunction_outputs_getter(self):
        tested = PhysicalFunction()
        tested.get_outputs()
        pass

    def test_PhysicalFunction_incoming_getter(self):
        tested = PhysicalFunction()
        tested.get_incoming()
        pass

    def test_PhysicalFunction_incoming_setter(self):
        tested = PhysicalFunction()
        value = FunctionalExchange()
        tested.get_incoming().add(value)
        pass

    def test_PhysicalFunction_outgoing_getter(self):
        tested = PhysicalFunction()
        tested.get_outgoing()
        pass

    def test_PhysicalFunction_outgoing_setter(self):
        tested = PhysicalFunction()
        value = FunctionalExchange()
        tested.get_outgoing().add(value)
        pass

    def test_PhysicalFunction_allocating_component_getter(self):
        tested = PhysicalFunction()
        tested.get_allocating_component()
        pass

    def test_PhysicalFunction_allocating_component_setter(self):
        tested = PhysicalFunction()
        value = PhysicalActor()
        tested.set_allocating_component(value)
        pass

    def test_PhysicalFunction_owned_functional_chains_getter(self):
        tested = PhysicalFunction()
        tested.get_owned_functional_chains()
        pass

    def test_PhysicalFunction_involving_functional_chains_getter(self):
        tested = PhysicalFunction()
        tested.get_involving_functional_chains()
        pass

    def test_PhysicalFunction_involving_capabilities_getter(self):
        tested = PhysicalFunction()
        tested.get_involving_capabilities()
        pass

    def test_PhysicalFunction_involving_capabilities_setter(self):
        tested = PhysicalFunction()
        value = CapabilityRealization()
        tested.get_involving_capabilities().add(value)
        pass

    def test_PhysicalFunction_available_in_states_getter(self):
        tested = PhysicalFunction()
        tested.get_available_in_states()
        pass

    def test_PhysicalFunction_available_in_states_setter(self):
        tested = PhysicalFunction()
        value = State()
        tested.get_available_in_states().add(value)
        pass

    def test_PhysicalFunction_id_getter(self):
        tested = PhysicalFunction()
        tested.get_id()
        pass

    def test_PhysicalFunction_id_setter(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_id(value)
        pass

    def test_PhysicalFunction_sid_getter(self):
        tested = PhysicalFunction()
        tested.get_sid()
        pass

    def test_PhysicalFunction_sid_setter(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_sid(value)
        pass

    def test_PhysicalFunction_name_getter(self):
        tested = PhysicalFunction()
        tested.get_name()
        pass

    def test_PhysicalFunction_name_setter(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_name(value)
        pass

    def test_PhysicalFunction_summary_getter(self):
        tested = PhysicalFunction()
        tested.get_summary()
        pass

    def test_PhysicalFunction_summary_setter(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_summary(value)
        pass

    def test_PhysicalFunction_description_getter(self):
        tested = PhysicalFunction()
        tested.get_description()
        pass

    def test_PhysicalFunction_description_setter(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_description(value)
        pass

    def test_PhysicalFunction_status_getter(self):
        tested = PhysicalFunction()
        tested.get_status()
        pass

    def test_PhysicalFunction_status_setter(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_status(value)
        pass

    def test_PhysicalFunction_review_getter(self):
        tested = PhysicalFunction()
        tested.get_review()
        pass

    def test_PhysicalFunction_review_setter(self):
        tested = PhysicalFunction()
        value = "value"
        tested.set_review(value)
        pass

    def test_PhysicalFunction_visible_in_documentation_getter(self):
        tested = PhysicalFunction()
        tested.get_visible_in_documentation()
        pass

    def test_PhysicalFunction_visible_in_documentation_setter(self):
        tested = PhysicalFunction()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_PhysicalFunction_visible_for_traceability_getter(self):
        tested = PhysicalFunction()
        tested.get_visible_for_traceability()
        pass

    def test_PhysicalFunction_visible_for_traceability_setter(self):
        tested = PhysicalFunction()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_PhysicalFunction_owned_constraints_getter(self):
        tested = PhysicalFunction()
        tested.get_owned_constraints()
        pass

    def test_PhysicalFunction_constraints_getter(self):
        tested = PhysicalFunction()
        tested.get_constraints()
        pass

    def test_PhysicalFunction_constraints_setter(self):
        tested = PhysicalFunction()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_PhysicalFunction_owned_property_values_getter(self):
        tested = PhysicalFunction()
        tested.get_owned_property_values()
        pass

    def test_PhysicalFunction_applied_property_values_getter(self):
        tested = PhysicalFunction()
        tested.get_applied_property_values()
        pass

    def test_PhysicalFunction_applied_property_values_setter(self):
        tested = PhysicalFunction()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_PhysicalFunction_owned_property_value_groups_getter(self):
        tested = PhysicalFunction()
        tested.get_owned_property_value_groups()
        pass

    def test_PhysicalFunction_applied_property_value_groups_getter(self):
        tested = PhysicalFunction()
        tested.get_applied_property_value_groups()
        pass

    def test_PhysicalFunction_applied_property_value_groups_setter(self):
        tested = PhysicalFunction()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_PhysicalFunction_owned_enumeration_property_types_getter(self):
        tested = PhysicalFunction()
        tested.get_owned_enumeration_property_types()
        pass

    def test_PhysicalFunction_owned_diagrams_getter(self):
        tested = PhysicalFunction()
        tested.get_owned_diagrams()
        pass

    def test_PhysicalFunction_element_of_interest_for_diagrams_getter(self):
        tested = PhysicalFunction()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_PhysicalFunction_element_of_interest_for_diagrams_setter(self):
        tested = PhysicalFunction()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_PhysicalFunction_contextual_element_for_diagrams_getter(self):
        tested = PhysicalFunction()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_PhysicalFunction_contextual_element_for_diagrams_setter(self):
        tested = PhysicalFunction()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_PhysicalFunction_representing_diagrams_getter(self):
        tested = PhysicalFunction()
        tested.get_representing_diagrams()
        pass

    def test_PhysicalFunction__r_e_cs_getter(self):
        tested = PhysicalFunction()
        tested.get__r_e_cs()
        pass

    def test_PhysicalFunction__r_e_cs_setter(self):
        tested = PhysicalFunction()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_PhysicalFunction__r_p_ls_getter(self):
        tested = PhysicalFunction()
        tested.get__r_p_ls()
        pass

    def test_PhysicalFunction__r_p_ls_setter(self):
        tested = PhysicalFunction()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_PhysicalFunction_get_label(self):
        tested = PhysicalFunction()
        tested.get_label()
        pass

    def test_PhysicalFunction_get_element_type(self):
        tested = PhysicalFunction()
        tested.get_element_type()
        pass

    def test_PhysicalFunction_get_container(self):
        tested = PhysicalFunction()
        tested.get_container()
        pass

    def test_PhysicalFunction_get_contents(self):
        tested = PhysicalFunction()
        tested.get_contents()
        pass

    def test_PhysicalFunction_get_all_contents(self):
        tested = PhysicalFunction()
        tested.get_all_contents()
        pass

    def test_PhysicalFunction_get_all_contents_by_type(self):
        tested = PhysicalFunction()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_PhysicalFunction_get_available_s_b_queries(self):
        tested = PhysicalFunction()
        tested.get_available_s_b_queries()
        pass

    def test_PhysicalFunction_get_query_result(self):
        tested = PhysicalFunction()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_PhysicalFunction_contained_physical_functions_getter(self):
        tested = PhysicalFunction()
        tested.get_contained_physical_functions()
        pass

    def test_PhysicalFunction_owned_physical_function_pkgs_getter(self):
        tested = PhysicalFunction()
        tested.get_owned_physical_function_pkgs()
        pass

    def test_PhysicalFunction_realized_logical_functions_getter(self):
        tested = PhysicalFunction()
        tested.get_realized_logical_functions()
        pass

    def test_PhysicalFunction_realized_logical_functions_setter(self):
        tested = PhysicalFunction()
        value = LogicalFunction()
        tested.get_realized_logical_functions().add(value)
        pass

    def test_PhysicalComponentPkg_owned_property_value_pkgs_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_owned_property_value_pkgs()
        pass

    def test_PhysicalComponentPkg_id_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_id()
        pass

    def test_PhysicalComponentPkg_id_setter(self):
        tested = PhysicalComponentPkg()
        value = "value"
        tested.set_id(value)
        pass

    def test_PhysicalComponentPkg_sid_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_sid()
        pass

    def test_PhysicalComponentPkg_sid_setter(self):
        tested = PhysicalComponentPkg()
        value = "value"
        tested.set_sid(value)
        pass

    def test_PhysicalComponentPkg_name_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_name()
        pass

    def test_PhysicalComponentPkg_name_setter(self):
        tested = PhysicalComponentPkg()
        value = "value"
        tested.set_name(value)
        pass

    def test_PhysicalComponentPkg_summary_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_summary()
        pass

    def test_PhysicalComponentPkg_summary_setter(self):
        tested = PhysicalComponentPkg()
        value = "value"
        tested.set_summary(value)
        pass

    def test_PhysicalComponentPkg_description_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_description()
        pass

    def test_PhysicalComponentPkg_description_setter(self):
        tested = PhysicalComponentPkg()
        value = "value"
        tested.set_description(value)
        pass

    def test_PhysicalComponentPkg_status_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_status()
        pass

    def test_PhysicalComponentPkg_status_setter(self):
        tested = PhysicalComponentPkg()
        value = "value"
        tested.set_status(value)
        pass

    def test_PhysicalComponentPkg_review_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_review()
        pass

    def test_PhysicalComponentPkg_review_setter(self):
        tested = PhysicalComponentPkg()
        value = "value"
        tested.set_review(value)
        pass

    def test_PhysicalComponentPkg_visible_in_documentation_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_visible_in_documentation()
        pass

    def test_PhysicalComponentPkg_visible_in_documentation_setter(self):
        tested = PhysicalComponentPkg()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_PhysicalComponentPkg_visible_for_traceability_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_visible_for_traceability()
        pass

    def test_PhysicalComponentPkg_visible_for_traceability_setter(self):
        tested = PhysicalComponentPkg()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_PhysicalComponentPkg_owned_constraints_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_owned_constraints()
        pass

    def test_PhysicalComponentPkg_constraints_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_constraints()
        pass

    def test_PhysicalComponentPkg_constraints_setter(self):
        tested = PhysicalComponentPkg()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_PhysicalComponentPkg_owned_property_values_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_owned_property_values()
        pass

    def test_PhysicalComponentPkg_applied_property_values_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_applied_property_values()
        pass

    def test_PhysicalComponentPkg_applied_property_values_setter(self):
        tested = PhysicalComponentPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_PhysicalComponentPkg_owned_property_value_groups_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_owned_property_value_groups()
        pass

    def test_PhysicalComponentPkg_applied_property_value_groups_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_applied_property_value_groups()
        pass

    def test_PhysicalComponentPkg_applied_property_value_groups_setter(self):
        tested = PhysicalComponentPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_PhysicalComponentPkg_owned_enumeration_property_types_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_owned_enumeration_property_types()
        pass

    def test_PhysicalComponentPkg_owned_diagrams_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_owned_diagrams()
        pass

    def test_PhysicalComponentPkg_element_of_interest_for_diagrams_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_PhysicalComponentPkg_element_of_interest_for_diagrams_setter(self):
        tested = PhysicalComponentPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_PhysicalComponentPkg_contextual_element_for_diagrams_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_PhysicalComponentPkg_contextual_element_for_diagrams_setter(self):
        tested = PhysicalComponentPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_PhysicalComponentPkg_representing_diagrams_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_representing_diagrams()
        pass

    def test_PhysicalComponentPkg__r_e_cs_getter(self):
        tested = PhysicalComponentPkg()
        tested.get__r_e_cs()
        pass

    def test_PhysicalComponentPkg__r_e_cs_setter(self):
        tested = PhysicalComponentPkg()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_PhysicalComponentPkg__r_p_ls_getter(self):
        tested = PhysicalComponentPkg()
        tested.get__r_p_ls()
        pass

    def test_PhysicalComponentPkg__r_p_ls_setter(self):
        tested = PhysicalComponentPkg()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_PhysicalComponentPkg_get_label(self):
        tested = PhysicalComponentPkg()
        tested.get_label()
        pass

    def test_PhysicalComponentPkg_get_element_type(self):
        tested = PhysicalComponentPkg()
        tested.get_element_type()
        pass

    def test_PhysicalComponentPkg_get_container(self):
        tested = PhysicalComponentPkg()
        tested.get_container()
        pass

    def test_PhysicalComponentPkg_get_contents(self):
        tested = PhysicalComponentPkg()
        tested.get_contents()
        pass

    def test_PhysicalComponentPkg_get_all_contents(self):
        tested = PhysicalComponentPkg()
        tested.get_all_contents()
        pass

    def test_PhysicalComponentPkg_get_all_contents_by_type(self):
        tested = PhysicalComponentPkg()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_PhysicalComponentPkg_get_available_s_b_queries(self):
        tested = PhysicalComponentPkg()
        tested.get_available_s_b_queries()
        pass

    def test_PhysicalComponentPkg_get_query_result(self):
        tested = PhysicalComponentPkg()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_PhysicalComponentPkg_owned_physical_component_pkgs_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_owned_physical_component_pkgs()
        pass

    def test_PhysicalComponentPkg_owned_physical_system_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_owned_physical_system()
        pass

    def test_PhysicalComponentPkg_owned_physical_actors_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_owned_physical_actors()
        pass

    def test_PhysicalComponentPkg_owned_physical_components_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_owned_physical_components()
        pass

    def test_PhysicalComponentPkg_owned_component_exchange_categories_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_owned_component_exchange_categories()
        pass

    def test_PhysicalComponentPkg_owned_physical_link_categories_getter(self):
        tested = PhysicalComponentPkg()
        tested.get_owned_physical_link_categories()
        pass

    def test_PhysicalSystem_id_getter(self):
        tested = PhysicalSystem()
        tested.get_id()
        pass

    def test_PhysicalSystem_id_setter(self):
        tested = PhysicalSystem()
        value = "value"
        tested.set_id(value)
        pass

    def test_PhysicalSystem_sid_getter(self):
        tested = PhysicalSystem()
        tested.get_sid()
        pass

    def test_PhysicalSystem_sid_setter(self):
        tested = PhysicalSystem()
        value = "value"
        tested.set_sid(value)
        pass

    def test_PhysicalSystem_name_getter(self):
        tested = PhysicalSystem()
        tested.get_name()
        pass

    def test_PhysicalSystem_name_setter(self):
        tested = PhysicalSystem()
        value = "value"
        tested.set_name(value)
        pass

    def test_PhysicalSystem_summary_getter(self):
        tested = PhysicalSystem()
        tested.get_summary()
        pass

    def test_PhysicalSystem_summary_setter(self):
        tested = PhysicalSystem()
        value = "value"
        tested.set_summary(value)
        pass

    def test_PhysicalSystem_description_getter(self):
        tested = PhysicalSystem()
        tested.get_description()
        pass

    def test_PhysicalSystem_description_setter(self):
        tested = PhysicalSystem()
        value = "value"
        tested.set_description(value)
        pass

    def test_PhysicalSystem_status_getter(self):
        tested = PhysicalSystem()
        tested.get_status()
        pass

    def test_PhysicalSystem_status_setter(self):
        tested = PhysicalSystem()
        value = "value"
        tested.set_status(value)
        pass

    def test_PhysicalSystem_review_getter(self):
        tested = PhysicalSystem()
        tested.get_review()
        pass

    def test_PhysicalSystem_review_setter(self):
        tested = PhysicalSystem()
        value = "value"
        tested.set_review(value)
        pass

    def test_PhysicalSystem_visible_in_documentation_getter(self):
        tested = PhysicalSystem()
        tested.get_visible_in_documentation()
        pass

    def test_PhysicalSystem_visible_in_documentation_setter(self):
        tested = PhysicalSystem()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_PhysicalSystem_visible_for_traceability_getter(self):
        tested = PhysicalSystem()
        tested.get_visible_for_traceability()
        pass

    def test_PhysicalSystem_visible_for_traceability_setter(self):
        tested = PhysicalSystem()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_PhysicalSystem_owned_constraints_getter(self):
        tested = PhysicalSystem()
        tested.get_owned_constraints()
        pass

    def test_PhysicalSystem_constraints_getter(self):
        tested = PhysicalSystem()
        tested.get_constraints()
        pass

    def test_PhysicalSystem_constraints_setter(self):
        tested = PhysicalSystem()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_PhysicalSystem_owned_property_values_getter(self):
        tested = PhysicalSystem()
        tested.get_owned_property_values()
        pass

    def test_PhysicalSystem_applied_property_values_getter(self):
        tested = PhysicalSystem()
        tested.get_applied_property_values()
        pass

    def test_PhysicalSystem_applied_property_values_setter(self):
        tested = PhysicalSystem()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_PhysicalSystem_owned_property_value_groups_getter(self):
        tested = PhysicalSystem()
        tested.get_owned_property_value_groups()
        pass

    def test_PhysicalSystem_applied_property_value_groups_getter(self):
        tested = PhysicalSystem()
        tested.get_applied_property_value_groups()
        pass

    def test_PhysicalSystem_applied_property_value_groups_setter(self):
        tested = PhysicalSystem()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_PhysicalSystem_owned_enumeration_property_types_getter(self):
        tested = PhysicalSystem()
        tested.get_owned_enumeration_property_types()
        pass

    def test_PhysicalSystem_owned_diagrams_getter(self):
        tested = PhysicalSystem()
        tested.get_owned_diagrams()
        pass

    def test_PhysicalSystem_element_of_interest_for_diagrams_getter(self):
        tested = PhysicalSystem()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_PhysicalSystem_element_of_interest_for_diagrams_setter(self):
        tested = PhysicalSystem()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_PhysicalSystem_contextual_element_for_diagrams_getter(self):
        tested = PhysicalSystem()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_PhysicalSystem_contextual_element_for_diagrams_setter(self):
        tested = PhysicalSystem()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_PhysicalSystem_representing_diagrams_getter(self):
        tested = PhysicalSystem()
        tested.get_representing_diagrams()
        pass

    def test_PhysicalSystem__r_e_cs_getter(self):
        tested = PhysicalSystem()
        tested.get__r_e_cs()
        pass

    def test_PhysicalSystem__r_e_cs_setter(self):
        tested = PhysicalSystem()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_PhysicalSystem__r_p_ls_getter(self):
        tested = PhysicalSystem()
        tested.get__r_p_ls()
        pass

    def test_PhysicalSystem__r_p_ls_setter(self):
        tested = PhysicalSystem()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_PhysicalSystem_get_label(self):
        tested = PhysicalSystem()
        tested.get_label()
        pass

    def test_PhysicalSystem_get_element_type(self):
        tested = PhysicalSystem()
        tested.get_element_type()
        pass

    def test_PhysicalSystem_get_container(self):
        tested = PhysicalSystem()
        tested.get_container()
        pass

    def test_PhysicalSystem_get_contents(self):
        tested = PhysicalSystem()
        tested.get_contents()
        pass

    def test_PhysicalSystem_get_all_contents(self):
        tested = PhysicalSystem()
        tested.get_all_contents()
        pass

    def test_PhysicalSystem_get_all_contents_by_type(self):
        tested = PhysicalSystem()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_PhysicalSystem_get_available_s_b_queries(self):
        tested = PhysicalSystem()
        tested.get_available_s_b_queries()
        pass

    def test_PhysicalSystem_get_query_result(self):
        tested = PhysicalSystem()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_PhysicalSystem_contained_physical_ports_getter(self):
        tested = PhysicalSystem()
        tested.get_contained_physical_ports()
        pass

    def test_PhysicalSystem_physical_links_getter(self):
        tested = PhysicalSystem()
        tested.get_physical_links()
        pass

    def test_PhysicalSystem_physical_links_setter(self):
        tested = PhysicalSystem()
        value = PhysicalLink()
        tested.get_physical_links().add(value)
        pass

    def test_PhysicalSystem_involving_physical_paths_getter(self):
        tested = PhysicalSystem()
        tested.get_involving_physical_paths()
        pass

    def test_PhysicalSystem_owned_physical_link_categories_getter(self):
        tested = PhysicalSystem()
        tested.get_owned_physical_link_categories()
        pass

    def test_PhysicalSystem_owned_physical_paths_getter(self):
        tested = PhysicalSystem()
        tested.get_owned_physical_paths()
        pass

    def test_PhysicalSystem_owned_physical_components_getter(self):
        tested = PhysicalSystem()
        tested.get_owned_physical_components()
        pass

    def test_PhysicalSystem_owned_physical_component_pkgs_getter(self):
        tested = PhysicalSystem()
        tested.get_owned_physical_component_pkgs()
        pass

    def test_BehaviorPC_kind_getter(self):
        tested = BehaviorPC()
        tested.get_kind()
        pass

    def test_BehaviorPC_kind_setter(self):
        tested = BehaviorPC()
        value = "HARDWARE"
        tested.set_kind(value)
        pass

    def test_BehaviorPC_owned_physical_components_getter(self):
        tested = BehaviorPC()
        tested.get_owned_physical_components()
        pass

    def test_BehaviorPC_owned_physical_component_pkgs_getter(self):
        tested = BehaviorPC()
        tested.get_owned_physical_component_pkgs()
        pass

    def test_BehaviorPC_is_human_getter(self):
        tested = BehaviorPC()
        tested.get_is_human()
        pass

    def test_BehaviorPC_is_human_setter(self):
        tested = BehaviorPC()
        value = True
        tested.set_is_human(value)
        pass

    def test_BehaviorPC_involving_capability_realizations_getter(self):
        tested = BehaviorPC()
        tested.get_involving_capability_realizations()
        pass

    def test_BehaviorPC_involving_capability_realizations_setter(self):
        tested = BehaviorPC()
        value = CapabilityRealization()
        tested.get_involving_capability_realizations().add(value)
        pass

    def test_BehaviorPC_allocator_configuration_items_getter(self):
        tested = BehaviorPC()
        tested.get_allocator_configuration_items()
        pass

    def test_BehaviorPC_allocator_configuration_items_setter(self):
        tested = BehaviorPC()
        value = ConfigurationItem()
        tested.get_allocator_configuration_items().add(value)
        pass

    def test_BehaviorPC_id_getter(self):
        tested = BehaviorPC()
        tested.get_id()
        pass

    def test_BehaviorPC_id_setter(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_id(value)
        pass

    def test_BehaviorPC_sid_getter(self):
        tested = BehaviorPC()
        tested.get_sid()
        pass

    def test_BehaviorPC_sid_setter(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_sid(value)
        pass

    def test_BehaviorPC_name_getter(self):
        tested = BehaviorPC()
        tested.get_name()
        pass

    def test_BehaviorPC_name_setter(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_name(value)
        pass

    def test_BehaviorPC_summary_getter(self):
        tested = BehaviorPC()
        tested.get_summary()
        pass

    def test_BehaviorPC_summary_setter(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_summary(value)
        pass

    def test_BehaviorPC_description_getter(self):
        tested = BehaviorPC()
        tested.get_description()
        pass

    def test_BehaviorPC_description_setter(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_description(value)
        pass

    def test_BehaviorPC_status_getter(self):
        tested = BehaviorPC()
        tested.get_status()
        pass

    def test_BehaviorPC_status_setter(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_status(value)
        pass

    def test_BehaviorPC_review_getter(self):
        tested = BehaviorPC()
        tested.get_review()
        pass

    def test_BehaviorPC_review_setter(self):
        tested = BehaviorPC()
        value = "value"
        tested.set_review(value)
        pass

    def test_BehaviorPC_visible_in_documentation_getter(self):
        tested = BehaviorPC()
        tested.get_visible_in_documentation()
        pass

    def test_BehaviorPC_visible_in_documentation_setter(self):
        tested = BehaviorPC()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_BehaviorPC_visible_for_traceability_getter(self):
        tested = BehaviorPC()
        tested.get_visible_for_traceability()
        pass

    def test_BehaviorPC_visible_for_traceability_setter(self):
        tested = BehaviorPC()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_BehaviorPC_owned_constraints_getter(self):
        tested = BehaviorPC()
        tested.get_owned_constraints()
        pass

    def test_BehaviorPC_constraints_getter(self):
        tested = BehaviorPC()
        tested.get_constraints()
        pass

    def test_BehaviorPC_constraints_setter(self):
        tested = BehaviorPC()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_BehaviorPC_owned_property_values_getter(self):
        tested = BehaviorPC()
        tested.get_owned_property_values()
        pass

    def test_BehaviorPC_applied_property_values_getter(self):
        tested = BehaviorPC()
        tested.get_applied_property_values()
        pass

    def test_BehaviorPC_applied_property_values_setter(self):
        tested = BehaviorPC()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_BehaviorPC_owned_property_value_groups_getter(self):
        tested = BehaviorPC()
        tested.get_owned_property_value_groups()
        pass

    def test_BehaviorPC_applied_property_value_groups_getter(self):
        tested = BehaviorPC()
        tested.get_applied_property_value_groups()
        pass

    def test_BehaviorPC_applied_property_value_groups_setter(self):
        tested = BehaviorPC()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_BehaviorPC_owned_enumeration_property_types_getter(self):
        tested = BehaviorPC()
        tested.get_owned_enumeration_property_types()
        pass

    def test_BehaviorPC_owned_diagrams_getter(self):
        tested = BehaviorPC()
        tested.get_owned_diagrams()
        pass

    def test_BehaviorPC_element_of_interest_for_diagrams_getter(self):
        tested = BehaviorPC()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_BehaviorPC_element_of_interest_for_diagrams_setter(self):
        tested = BehaviorPC()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_BehaviorPC_contextual_element_for_diagrams_getter(self):
        tested = BehaviorPC()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_BehaviorPC_contextual_element_for_diagrams_setter(self):
        tested = BehaviorPC()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_BehaviorPC_representing_diagrams_getter(self):
        tested = BehaviorPC()
        tested.get_representing_diagrams()
        pass

    def test_BehaviorPC__r_e_cs_getter(self):
        tested = BehaviorPC()
        tested.get__r_e_cs()
        pass

    def test_BehaviorPC__r_e_cs_setter(self):
        tested = BehaviorPC()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_BehaviorPC__r_p_ls_getter(self):
        tested = BehaviorPC()
        tested.get__r_p_ls()
        pass

    def test_BehaviorPC__r_p_ls_setter(self):
        tested = BehaviorPC()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_BehaviorPC_get_label(self):
        tested = BehaviorPC()
        tested.get_label()
        pass

    def test_BehaviorPC_get_element_type(self):
        tested = BehaviorPC()
        tested.get_element_type()
        pass

    def test_BehaviorPC_get_container(self):
        tested = BehaviorPC()
        tested.get_container()
        pass

    def test_BehaviorPC_get_contents(self):
        tested = BehaviorPC()
        tested.get_contents()
        pass

    def test_BehaviorPC_get_all_contents(self):
        tested = BehaviorPC()
        tested.get_all_contents()
        pass

    def test_BehaviorPC_get_all_contents_by_type(self):
        tested = BehaviorPC()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_BehaviorPC_get_available_s_b_queries(self):
        tested = BehaviorPC()
        tested.get_available_s_b_queries()
        pass

    def test_BehaviorPC_get_query_result(self):
        tested = BehaviorPC()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_BehaviorPC_contained_component_ports_getter(self):
        tested = BehaviorPC()
        tested.get_contained_component_ports()
        pass

    def test_BehaviorPC_incoming_component_exchanges_getter(self):
        tested = BehaviorPC()
        tested.get_incoming_component_exchanges()
        pass

    def test_BehaviorPC_incoming_component_exchanges_setter(self):
        tested = BehaviorPC()
        value = ComponentExchange()
        tested.get_incoming_component_exchanges().add(value)
        pass

    def test_BehaviorPC_outgoing_component_exchanges_getter(self):
        tested = BehaviorPC()
        tested.get_outgoing_component_exchanges()
        pass

    def test_BehaviorPC_outgoing_component_exchanges_setter(self):
        tested = BehaviorPC()
        value = ComponentExchange()
        tested.get_outgoing_component_exchanges().add(value)
        pass

    def test_BehaviorPC_inout_component_exchanges_getter(self):
        tested = BehaviorPC()
        tested.get_inout_component_exchanges()
        pass

    def test_BehaviorPC_inout_component_exchanges_setter(self):
        tested = BehaviorPC()
        value = ComponentExchange()
        tested.get_inout_component_exchanges().add(value)
        pass

    def test_BehaviorPC_allocated_functions_getter(self):
        tested = BehaviorPC()
        tested.get_allocated_functions()
        pass

    def test_BehaviorPC_allocated_functions_setter(self):
        tested = BehaviorPC()
        value = PhysicalFunction()
        tested.get_allocated_functions().add(value)
        pass

    def test_BehaviorPC_used_interfaces_getter(self):
        tested = BehaviorPC()
        tested.get_used_interfaces()
        pass

    def test_BehaviorPC_used_interfaces_setter(self):
        tested = BehaviorPC()
        value = Interface()
        tested.get_used_interfaces().add(value)
        pass

    def test_BehaviorPC_implemented_interfaces_getter(self):
        tested = BehaviorPC()
        tested.get_implemented_interfaces()
        pass

    def test_BehaviorPC_implemented_interfaces_setter(self):
        tested = BehaviorPC()
        value = Interface()
        tested.get_implemented_interfaces().add(value)
        pass

    def test_BehaviorPC_owned_state_machines_getter(self):
        tested = BehaviorPC()
        tested.get_owned_state_machines()
        pass

    def test_BehaviorPC_owned_component_exchange_categories_getter(self):
        tested = BehaviorPC()
        tested.get_owned_component_exchange_categories()
        pass

    def test_BehaviorPC_deploying_node_p_c_getter(self):
        tested = BehaviorPC()
        tested.get_deploying_node_p_c()
        pass

    def test_BehaviorPC_deploying_node_p_c_setter(self):
        tested = BehaviorPC()
        value = NodePC()
        tested.set_deploying_node_p_c(value)
        pass

    def test_BehaviorPC_realized_logical_components_getter(self):
        tested = BehaviorPC()
        tested.get_realized_logical_components()
        pass

    def test_BehaviorPC_realized_logical_components_setter(self):
        tested = BehaviorPC()
        value = LogicalComponent()
        tested.get_realized_logical_components().add(value)
        pass

    def test_NodePC_kind_getter(self):
        tested = NodePC()
        tested.get_kind()
        pass

    def test_NodePC_kind_setter(self):
        tested = NodePC()
        value = "HARDWARE"
        tested.set_kind(value)
        pass

    def test_NodePC_owned_physical_components_getter(self):
        tested = NodePC()
        tested.get_owned_physical_components()
        pass

    def test_NodePC_owned_physical_component_pkgs_getter(self):
        tested = NodePC()
        tested.get_owned_physical_component_pkgs()
        pass

    def test_NodePC_is_human_getter(self):
        tested = NodePC()
        tested.get_is_human()
        pass

    def test_NodePC_is_human_setter(self):
        tested = NodePC()
        value = True
        tested.set_is_human(value)
        pass

    def test_NodePC_involving_capability_realizations_getter(self):
        tested = NodePC()
        tested.get_involving_capability_realizations()
        pass

    def test_NodePC_involving_capability_realizations_setter(self):
        tested = NodePC()
        value = CapabilityRealization()
        tested.get_involving_capability_realizations().add(value)
        pass

    def test_NodePC_allocator_configuration_items_getter(self):
        tested = NodePC()
        tested.get_allocator_configuration_items()
        pass

    def test_NodePC_allocator_configuration_items_setter(self):
        tested = NodePC()
        value = ConfigurationItem()
        tested.get_allocator_configuration_items().add(value)
        pass

    def test_NodePC_id_getter(self):
        tested = NodePC()
        tested.get_id()
        pass

    def test_NodePC_id_setter(self):
        tested = NodePC()
        value = "value"
        tested.set_id(value)
        pass

    def test_NodePC_sid_getter(self):
        tested = NodePC()
        tested.get_sid()
        pass

    def test_NodePC_sid_setter(self):
        tested = NodePC()
        value = "value"
        tested.set_sid(value)
        pass

    def test_NodePC_name_getter(self):
        tested = NodePC()
        tested.get_name()
        pass

    def test_NodePC_name_setter(self):
        tested = NodePC()
        value = "value"
        tested.set_name(value)
        pass

    def test_NodePC_summary_getter(self):
        tested = NodePC()
        tested.get_summary()
        pass

    def test_NodePC_summary_setter(self):
        tested = NodePC()
        value = "value"
        tested.set_summary(value)
        pass

    def test_NodePC_description_getter(self):
        tested = NodePC()
        tested.get_description()
        pass

    def test_NodePC_description_setter(self):
        tested = NodePC()
        value = "value"
        tested.set_description(value)
        pass

    def test_NodePC_status_getter(self):
        tested = NodePC()
        tested.get_status()
        pass

    def test_NodePC_status_setter(self):
        tested = NodePC()
        value = "value"
        tested.set_status(value)
        pass

    def test_NodePC_review_getter(self):
        tested = NodePC()
        tested.get_review()
        pass

    def test_NodePC_review_setter(self):
        tested = NodePC()
        value = "value"
        tested.set_review(value)
        pass

    def test_NodePC_visible_in_documentation_getter(self):
        tested = NodePC()
        tested.get_visible_in_documentation()
        pass

    def test_NodePC_visible_in_documentation_setter(self):
        tested = NodePC()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_NodePC_visible_for_traceability_getter(self):
        tested = NodePC()
        tested.get_visible_for_traceability()
        pass

    def test_NodePC_visible_for_traceability_setter(self):
        tested = NodePC()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_NodePC_owned_constraints_getter(self):
        tested = NodePC()
        tested.get_owned_constraints()
        pass

    def test_NodePC_constraints_getter(self):
        tested = NodePC()
        tested.get_constraints()
        pass

    def test_NodePC_constraints_setter(self):
        tested = NodePC()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_NodePC_owned_property_values_getter(self):
        tested = NodePC()
        tested.get_owned_property_values()
        pass

    def test_NodePC_applied_property_values_getter(self):
        tested = NodePC()
        tested.get_applied_property_values()
        pass

    def test_NodePC_applied_property_values_setter(self):
        tested = NodePC()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_NodePC_owned_property_value_groups_getter(self):
        tested = NodePC()
        tested.get_owned_property_value_groups()
        pass

    def test_NodePC_applied_property_value_groups_getter(self):
        tested = NodePC()
        tested.get_applied_property_value_groups()
        pass

    def test_NodePC_applied_property_value_groups_setter(self):
        tested = NodePC()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_NodePC_owned_enumeration_property_types_getter(self):
        tested = NodePC()
        tested.get_owned_enumeration_property_types()
        pass

    def test_NodePC_owned_diagrams_getter(self):
        tested = NodePC()
        tested.get_owned_diagrams()
        pass

    def test_NodePC_element_of_interest_for_diagrams_getter(self):
        tested = NodePC()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_NodePC_element_of_interest_for_diagrams_setter(self):
        tested = NodePC()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_NodePC_contextual_element_for_diagrams_getter(self):
        tested = NodePC()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_NodePC_contextual_element_for_diagrams_setter(self):
        tested = NodePC()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_NodePC_representing_diagrams_getter(self):
        tested = NodePC()
        tested.get_representing_diagrams()
        pass

    def test_NodePC__r_e_cs_getter(self):
        tested = NodePC()
        tested.get__r_e_cs()
        pass

    def test_NodePC__r_e_cs_setter(self):
        tested = NodePC()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_NodePC__r_p_ls_getter(self):
        tested = NodePC()
        tested.get__r_p_ls()
        pass

    def test_NodePC__r_p_ls_setter(self):
        tested = NodePC()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_NodePC_get_label(self):
        tested = NodePC()
        tested.get_label()
        pass

    def test_NodePC_get_element_type(self):
        tested = NodePC()
        tested.get_element_type()
        pass

    def test_NodePC_get_container(self):
        tested = NodePC()
        tested.get_container()
        pass

    def test_NodePC_get_contents(self):
        tested = NodePC()
        tested.get_contents()
        pass

    def test_NodePC_get_all_contents(self):
        tested = NodePC()
        tested.get_all_contents()
        pass

    def test_NodePC_get_all_contents_by_type(self):
        tested = NodePC()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_NodePC_get_available_s_b_queries(self):
        tested = NodePC()
        tested.get_available_s_b_queries()
        pass

    def test_NodePC_get_query_result(self):
        tested = NodePC()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_NodePC_contained_physical_ports_getter(self):
        tested = NodePC()
        tested.get_contained_physical_ports()
        pass

    def test_NodePC_physical_links_getter(self):
        tested = NodePC()
        tested.get_physical_links()
        pass

    def test_NodePC_physical_links_setter(self):
        tested = NodePC()
        value = PhysicalLink()
        tested.get_physical_links().add(value)
        pass

    def test_NodePC_involving_physical_paths_getter(self):
        tested = NodePC()
        tested.get_involving_physical_paths()
        pass

    def test_NodePC_owned_physical_link_categories_getter(self):
        tested = NodePC()
        tested.get_owned_physical_link_categories()
        pass

    def test_NodePC_owned_physical_paths_getter(self):
        tested = NodePC()
        tested.get_owned_physical_paths()
        pass

    def test_NodePC_deployed_behavior_p_cs_getter(self):
        tested = NodePC()
        tested.get_deployed_behavior_p_cs()
        pass

    def test_NodePC_deployed_behavior_p_cs_setter(self):
        tested = NodePC()
        value = BehaviorPC()
        tested.get_deployed_behavior_p_cs().add(value)
        pass

    def test_NodePC_owned_state_machines_getter(self):
        tested = NodePC()
        tested.get_owned_state_machines()
        pass

    def test_PhysicalActor_contained_component_ports_getter(self):
        tested = PhysicalActor()
        tested.get_contained_component_ports()
        pass

    def test_PhysicalActor_incoming_component_exchanges_getter(self):
        tested = PhysicalActor()
        tested.get_incoming_component_exchanges()
        pass

    def test_PhysicalActor_incoming_component_exchanges_setter(self):
        tested = PhysicalActor()
        value = ComponentExchange()
        tested.get_incoming_component_exchanges().add(value)
        pass

    def test_PhysicalActor_outgoing_component_exchanges_getter(self):
        tested = PhysicalActor()
        tested.get_outgoing_component_exchanges()
        pass

    def test_PhysicalActor_outgoing_component_exchanges_setter(self):
        tested = PhysicalActor()
        value = ComponentExchange()
        tested.get_outgoing_component_exchanges().add(value)
        pass

    def test_PhysicalActor_inout_component_exchanges_getter(self):
        tested = PhysicalActor()
        tested.get_inout_component_exchanges()
        pass

    def test_PhysicalActor_inout_component_exchanges_setter(self):
        tested = PhysicalActor()
        value = ComponentExchange()
        tested.get_inout_component_exchanges().add(value)
        pass

    def test_PhysicalActor_allocated_functions_getter(self):
        tested = PhysicalActor()
        tested.get_allocated_functions()
        pass

    def test_PhysicalActor_allocated_functions_setter(self):
        tested = PhysicalActor()
        value = PhysicalFunction()
        tested.get_allocated_functions().add(value)
        pass

    def test_PhysicalActor_used_interfaces_getter(self):
        tested = PhysicalActor()
        tested.get_used_interfaces()
        pass

    def test_PhysicalActor_used_interfaces_setter(self):
        tested = PhysicalActor()
        value = Interface()
        tested.get_used_interfaces().add(value)
        pass

    def test_PhysicalActor_implemented_interfaces_getter(self):
        tested = PhysicalActor()
        tested.get_implemented_interfaces()
        pass

    def test_PhysicalActor_implemented_interfaces_setter(self):
        tested = PhysicalActor()
        value = Interface()
        tested.get_implemented_interfaces().add(value)
        pass

    def test_PhysicalActor_owned_state_machines_getter(self):
        tested = PhysicalActor()
        tested.get_owned_state_machines()
        pass

    def test_PhysicalActor_owned_component_exchange_categories_getter(self):
        tested = PhysicalActor()
        tested.get_owned_component_exchange_categories()
        pass

    def test_PhysicalActor_id_getter(self):
        tested = PhysicalActor()
        tested.get_id()
        pass

    def test_PhysicalActor_id_setter(self):
        tested = PhysicalActor()
        value = "value"
        tested.set_id(value)
        pass

    def test_PhysicalActor_sid_getter(self):
        tested = PhysicalActor()
        tested.get_sid()
        pass

    def test_PhysicalActor_sid_setter(self):
        tested = PhysicalActor()
        value = "value"
        tested.set_sid(value)
        pass

    def test_PhysicalActor_name_getter(self):
        tested = PhysicalActor()
        tested.get_name()
        pass

    def test_PhysicalActor_name_setter(self):
        tested = PhysicalActor()
        value = "value"
        tested.set_name(value)
        pass

    def test_PhysicalActor_summary_getter(self):
        tested = PhysicalActor()
        tested.get_summary()
        pass

    def test_PhysicalActor_summary_setter(self):
        tested = PhysicalActor()
        value = "value"
        tested.set_summary(value)
        pass

    def test_PhysicalActor_description_getter(self):
        tested = PhysicalActor()
        tested.get_description()
        pass

    def test_PhysicalActor_description_setter(self):
        tested = PhysicalActor()
        value = "value"
        tested.set_description(value)
        pass

    def test_PhysicalActor_status_getter(self):
        tested = PhysicalActor()
        tested.get_status()
        pass

    def test_PhysicalActor_status_setter(self):
        tested = PhysicalActor()
        value = "value"
        tested.set_status(value)
        pass

    def test_PhysicalActor_review_getter(self):
        tested = PhysicalActor()
        tested.get_review()
        pass

    def test_PhysicalActor_review_setter(self):
        tested = PhysicalActor()
        value = "value"
        tested.set_review(value)
        pass

    def test_PhysicalActor_visible_in_documentation_getter(self):
        tested = PhysicalActor()
        tested.get_visible_in_documentation()
        pass

    def test_PhysicalActor_visible_in_documentation_setter(self):
        tested = PhysicalActor()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_PhysicalActor_visible_for_traceability_getter(self):
        tested = PhysicalActor()
        tested.get_visible_for_traceability()
        pass

    def test_PhysicalActor_visible_for_traceability_setter(self):
        tested = PhysicalActor()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_PhysicalActor_owned_constraints_getter(self):
        tested = PhysicalActor()
        tested.get_owned_constraints()
        pass

    def test_PhysicalActor_constraints_getter(self):
        tested = PhysicalActor()
        tested.get_constraints()
        pass

    def test_PhysicalActor_constraints_setter(self):
        tested = PhysicalActor()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_PhysicalActor_owned_property_values_getter(self):
        tested = PhysicalActor()
        tested.get_owned_property_values()
        pass

    def test_PhysicalActor_applied_property_values_getter(self):
        tested = PhysicalActor()
        tested.get_applied_property_values()
        pass

    def test_PhysicalActor_applied_property_values_setter(self):
        tested = PhysicalActor()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_PhysicalActor_owned_property_value_groups_getter(self):
        tested = PhysicalActor()
        tested.get_owned_property_value_groups()
        pass

    def test_PhysicalActor_applied_property_value_groups_getter(self):
        tested = PhysicalActor()
        tested.get_applied_property_value_groups()
        pass

    def test_PhysicalActor_applied_property_value_groups_setter(self):
        tested = PhysicalActor()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_PhysicalActor_owned_enumeration_property_types_getter(self):
        tested = PhysicalActor()
        tested.get_owned_enumeration_property_types()
        pass

    def test_PhysicalActor_owned_diagrams_getter(self):
        tested = PhysicalActor()
        tested.get_owned_diagrams()
        pass

    def test_PhysicalActor_element_of_interest_for_diagrams_getter(self):
        tested = PhysicalActor()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_PhysicalActor_element_of_interest_for_diagrams_setter(self):
        tested = PhysicalActor()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_PhysicalActor_contextual_element_for_diagrams_getter(self):
        tested = PhysicalActor()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_PhysicalActor_contextual_element_for_diagrams_setter(self):
        tested = PhysicalActor()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_PhysicalActor_representing_diagrams_getter(self):
        tested = PhysicalActor()
        tested.get_representing_diagrams()
        pass

    def test_PhysicalActor__r_e_cs_getter(self):
        tested = PhysicalActor()
        tested.get__r_e_cs()
        pass

    def test_PhysicalActor__r_e_cs_setter(self):
        tested = PhysicalActor()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_PhysicalActor__r_p_ls_getter(self):
        tested = PhysicalActor()
        tested.get__r_p_ls()
        pass

    def test_PhysicalActor__r_p_ls_setter(self):
        tested = PhysicalActor()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_PhysicalActor_get_label(self):
        tested = PhysicalActor()
        tested.get_label()
        pass

    def test_PhysicalActor_get_element_type(self):
        tested = PhysicalActor()
        tested.get_element_type()
        pass

    def test_PhysicalActor_get_container(self):
        tested = PhysicalActor()
        tested.get_container()
        pass

    def test_PhysicalActor_get_contents(self):
        tested = PhysicalActor()
        tested.get_contents()
        pass

    def test_PhysicalActor_get_all_contents(self):
        tested = PhysicalActor()
        tested.get_all_contents()
        pass

    def test_PhysicalActor_get_all_contents_by_type(self):
        tested = PhysicalActor()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_PhysicalActor_get_available_s_b_queries(self):
        tested = PhysicalActor()
        tested.get_available_s_b_queries()
        pass

    def test_PhysicalActor_get_query_result(self):
        tested = PhysicalActor()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_PhysicalActor_contained_physical_ports_getter(self):
        tested = PhysicalActor()
        tested.get_contained_physical_ports()
        pass

    def test_PhysicalActor_physical_links_getter(self):
        tested = PhysicalActor()
        tested.get_physical_links()
        pass

    def test_PhysicalActor_physical_links_setter(self):
        tested = PhysicalActor()
        value = PhysicalLink()
        tested.get_physical_links().add(value)
        pass

    def test_PhysicalActor_involving_physical_paths_getter(self):
        tested = PhysicalActor()
        tested.get_involving_physical_paths()
        pass

    def test_PhysicalActor_owned_physical_link_categories_getter(self):
        tested = PhysicalActor()
        tested.get_owned_physical_link_categories()
        pass

    def test_PhysicalActor_owned_physical_paths_getter(self):
        tested = PhysicalActor()
        tested.get_owned_physical_paths()
        pass

    def test_PhysicalActor_owned_physical_actors_getter(self):
        tested = PhysicalActor()
        tested.get_owned_physical_actors()
        pass

    def test_PhysicalActor_owned_physical_component_pkgs_getter(self):
        tested = PhysicalActor()
        tested.get_owned_physical_component_pkgs()
        pass

    def test_PhysicalActor_realized_logical_actors_getter(self):
        tested = PhysicalActor()
        tested.get_realized_logical_actors()
        pass

    def test_PhysicalActor_realized_logical_actors_setter(self):
        tested = PhysicalActor()
        value = LogicalActor()
        tested.get_realized_logical_actors().add(value)
        pass

    def test_PhysicalActor_is_human_getter(self):
        tested = PhysicalActor()
        tested.get_is_human()
        pass

    def test_PhysicalActor_is_human_setter(self):
        tested = PhysicalActor()
        value = True
        tested.set_is_human(value)
        pass

    def test_PhysicalActor_involving_capability_realizations_getter(self):
        tested = PhysicalActor()
        tested.get_involving_capability_realizations()
        pass

    def test_PhysicalActor_involving_capability_realizations_setter(self):
        tested = PhysicalActor()
        value = CapabilityRealization()
        tested.get_involving_capability_realizations().add(value)
        pass

    def test_EPBSArchitecture_owned_property_value_pkgs_getter(self):
        tested = EPBSArchitecture()
        tested.get_owned_property_value_pkgs()
        pass

    def test_EPBSArchitecture_id_getter(self):
        tested = EPBSArchitecture()
        tested.get_id()
        pass

    def test_EPBSArchitecture_id_setter(self):
        tested = EPBSArchitecture()
        value = "value"
        tested.set_id(value)
        pass

    def test_EPBSArchitecture_sid_getter(self):
        tested = EPBSArchitecture()
        tested.get_sid()
        pass

    def test_EPBSArchitecture_sid_setter(self):
        tested = EPBSArchitecture()
        value = "value"
        tested.set_sid(value)
        pass

    def test_EPBSArchitecture_name_getter(self):
        tested = EPBSArchitecture()
        tested.get_name()
        pass

    def test_EPBSArchitecture_name_setter(self):
        tested = EPBSArchitecture()
        value = "value"
        tested.set_name(value)
        pass

    def test_EPBSArchitecture_summary_getter(self):
        tested = EPBSArchitecture()
        tested.get_summary()
        pass

    def test_EPBSArchitecture_summary_setter(self):
        tested = EPBSArchitecture()
        value = "value"
        tested.set_summary(value)
        pass

    def test_EPBSArchitecture_description_getter(self):
        tested = EPBSArchitecture()
        tested.get_description()
        pass

    def test_EPBSArchitecture_description_setter(self):
        tested = EPBSArchitecture()
        value = "value"
        tested.set_description(value)
        pass

    def test_EPBSArchitecture_status_getter(self):
        tested = EPBSArchitecture()
        tested.get_status()
        pass

    def test_EPBSArchitecture_status_setter(self):
        tested = EPBSArchitecture()
        value = "value"
        tested.set_status(value)
        pass

    def test_EPBSArchitecture_review_getter(self):
        tested = EPBSArchitecture()
        tested.get_review()
        pass

    def test_EPBSArchitecture_review_setter(self):
        tested = EPBSArchitecture()
        value = "value"
        tested.set_review(value)
        pass

    def test_EPBSArchitecture_visible_in_documentation_getter(self):
        tested = EPBSArchitecture()
        tested.get_visible_in_documentation()
        pass

    def test_EPBSArchitecture_visible_in_documentation_setter(self):
        tested = EPBSArchitecture()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_EPBSArchitecture_visible_for_traceability_getter(self):
        tested = EPBSArchitecture()
        tested.get_visible_for_traceability()
        pass

    def test_EPBSArchitecture_visible_for_traceability_setter(self):
        tested = EPBSArchitecture()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_EPBSArchitecture_owned_constraints_getter(self):
        tested = EPBSArchitecture()
        tested.get_owned_constraints()
        pass

    def test_EPBSArchitecture_constraints_getter(self):
        tested = EPBSArchitecture()
        tested.get_constraints()
        pass

    def test_EPBSArchitecture_constraints_setter(self):
        tested = EPBSArchitecture()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_EPBSArchitecture_owned_property_values_getter(self):
        tested = EPBSArchitecture()
        tested.get_owned_property_values()
        pass

    def test_EPBSArchitecture_applied_property_values_getter(self):
        tested = EPBSArchitecture()
        tested.get_applied_property_values()
        pass

    def test_EPBSArchitecture_applied_property_values_setter(self):
        tested = EPBSArchitecture()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_EPBSArchitecture_owned_property_value_groups_getter(self):
        tested = EPBSArchitecture()
        tested.get_owned_property_value_groups()
        pass

    def test_EPBSArchitecture_applied_property_value_groups_getter(self):
        tested = EPBSArchitecture()
        tested.get_applied_property_value_groups()
        pass

    def test_EPBSArchitecture_applied_property_value_groups_setter(self):
        tested = EPBSArchitecture()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_EPBSArchitecture_owned_enumeration_property_types_getter(self):
        tested = EPBSArchitecture()
        tested.get_owned_enumeration_property_types()
        pass

    def test_EPBSArchitecture_owned_diagrams_getter(self):
        tested = EPBSArchitecture()
        tested.get_owned_diagrams()
        pass

    def test_EPBSArchitecture_element_of_interest_for_diagrams_getter(self):
        tested = EPBSArchitecture()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_EPBSArchitecture_element_of_interest_for_diagrams_setter(self):
        tested = EPBSArchitecture()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_EPBSArchitecture_contextual_element_for_diagrams_getter(self):
        tested = EPBSArchitecture()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_EPBSArchitecture_contextual_element_for_diagrams_setter(self):
        tested = EPBSArchitecture()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_EPBSArchitecture_representing_diagrams_getter(self):
        tested = EPBSArchitecture()
        tested.get_representing_diagrams()
        pass

    def test_EPBSArchitecture__r_e_cs_getter(self):
        tested = EPBSArchitecture()
        tested.get__r_e_cs()
        pass

    def test_EPBSArchitecture__r_e_cs_setter(self):
        tested = EPBSArchitecture()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_EPBSArchitecture__r_p_ls_getter(self):
        tested = EPBSArchitecture()
        tested.get__r_p_ls()
        pass

    def test_EPBSArchitecture__r_p_ls_setter(self):
        tested = EPBSArchitecture()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_EPBSArchitecture_get_label(self):
        tested = EPBSArchitecture()
        tested.get_label()
        pass

    def test_EPBSArchitecture_get_element_type(self):
        tested = EPBSArchitecture()
        tested.get_element_type()
        pass

    def test_EPBSArchitecture_get_container(self):
        tested = EPBSArchitecture()
        tested.get_container()
        pass

    def test_EPBSArchitecture_get_contents(self):
        tested = EPBSArchitecture()
        tested.get_contents()
        pass

    def test_EPBSArchitecture_get_all_contents(self):
        tested = EPBSArchitecture()
        tested.get_all_contents()
        pass

    def test_EPBSArchitecture_get_all_contents_by_type(self):
        tested = EPBSArchitecture()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_EPBSArchitecture_get_available_s_b_queries(self):
        tested = EPBSArchitecture()
        tested.get_available_s_b_queries()
        pass

    def test_EPBSArchitecture_get_query_result(self):
        tested = EPBSArchitecture()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_EPBSArchitecture_capability_realization_pkg_getter(self):
        tested = EPBSArchitecture()
        tested.get_capability_realization_pkg()
        pass

    def test_EPBSArchitecture_configuration_item_pkg_getter(self):
        tested = EPBSArchitecture()
        tested.get_configuration_item_pkg()
        pass

    def test_EPBSArchitecture_data_pkg_getter(self):
        tested = EPBSArchitecture()
        tested.get_data_pkg()
        pass

    def test_ConfigurationItemPkg_owned_property_value_pkgs_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_owned_property_value_pkgs()
        pass

    def test_ConfigurationItemPkg_id_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_id()
        pass

    def test_ConfigurationItemPkg_id_setter(self):
        tested = ConfigurationItemPkg()
        value = "value"
        tested.set_id(value)
        pass

    def test_ConfigurationItemPkg_sid_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_sid()
        pass

    def test_ConfigurationItemPkg_sid_setter(self):
        tested = ConfigurationItemPkg()
        value = "value"
        tested.set_sid(value)
        pass

    def test_ConfigurationItemPkg_name_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_name()
        pass

    def test_ConfigurationItemPkg_name_setter(self):
        tested = ConfigurationItemPkg()
        value = "value"
        tested.set_name(value)
        pass

    def test_ConfigurationItemPkg_summary_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_summary()
        pass

    def test_ConfigurationItemPkg_summary_setter(self):
        tested = ConfigurationItemPkg()
        value = "value"
        tested.set_summary(value)
        pass

    def test_ConfigurationItemPkg_description_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_description()
        pass

    def test_ConfigurationItemPkg_description_setter(self):
        tested = ConfigurationItemPkg()
        value = "value"
        tested.set_description(value)
        pass

    def test_ConfigurationItemPkg_status_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_status()
        pass

    def test_ConfigurationItemPkg_status_setter(self):
        tested = ConfigurationItemPkg()
        value = "value"
        tested.set_status(value)
        pass

    def test_ConfigurationItemPkg_review_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_review()
        pass

    def test_ConfigurationItemPkg_review_setter(self):
        tested = ConfigurationItemPkg()
        value = "value"
        tested.set_review(value)
        pass

    def test_ConfigurationItemPkg_visible_in_documentation_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_visible_in_documentation()
        pass

    def test_ConfigurationItemPkg_visible_in_documentation_setter(self):
        tested = ConfigurationItemPkg()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_ConfigurationItemPkg_visible_for_traceability_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_visible_for_traceability()
        pass

    def test_ConfigurationItemPkg_visible_for_traceability_setter(self):
        tested = ConfigurationItemPkg()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_ConfigurationItemPkg_owned_constraints_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_owned_constraints()
        pass

    def test_ConfigurationItemPkg_constraints_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_constraints()
        pass

    def test_ConfigurationItemPkg_constraints_setter(self):
        tested = ConfigurationItemPkg()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_ConfigurationItemPkg_owned_property_values_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_owned_property_values()
        pass

    def test_ConfigurationItemPkg_applied_property_values_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_applied_property_values()
        pass

    def test_ConfigurationItemPkg_applied_property_values_setter(self):
        tested = ConfigurationItemPkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_ConfigurationItemPkg_owned_property_value_groups_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_owned_property_value_groups()
        pass

    def test_ConfigurationItemPkg_applied_property_value_groups_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_applied_property_value_groups()
        pass

    def test_ConfigurationItemPkg_applied_property_value_groups_setter(self):
        tested = ConfigurationItemPkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_ConfigurationItemPkg_owned_enumeration_property_types_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_owned_enumeration_property_types()
        pass

    def test_ConfigurationItemPkg_owned_diagrams_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_owned_diagrams()
        pass

    def test_ConfigurationItemPkg_element_of_interest_for_diagrams_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_ConfigurationItemPkg_element_of_interest_for_diagrams_setter(self):
        tested = ConfigurationItemPkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_ConfigurationItemPkg_contextual_element_for_diagrams_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_ConfigurationItemPkg_contextual_element_for_diagrams_setter(self):
        tested = ConfigurationItemPkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_ConfigurationItemPkg_representing_diagrams_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_representing_diagrams()
        pass

    def test_ConfigurationItemPkg__r_e_cs_getter(self):
        tested = ConfigurationItemPkg()
        tested.get__r_e_cs()
        pass

    def test_ConfigurationItemPkg__r_e_cs_setter(self):
        tested = ConfigurationItemPkg()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_ConfigurationItemPkg__r_p_ls_getter(self):
        tested = ConfigurationItemPkg()
        tested.get__r_p_ls()
        pass

    def test_ConfigurationItemPkg__r_p_ls_setter(self):
        tested = ConfigurationItemPkg()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_ConfigurationItemPkg_get_label(self):
        tested = ConfigurationItemPkg()
        tested.get_label()
        pass

    def test_ConfigurationItemPkg_get_element_type(self):
        tested = ConfigurationItemPkg()
        tested.get_element_type()
        pass

    def test_ConfigurationItemPkg_get_container(self):
        tested = ConfigurationItemPkg()
        tested.get_container()
        pass

    def test_ConfigurationItemPkg_get_contents(self):
        tested = ConfigurationItemPkg()
        tested.get_contents()
        pass

    def test_ConfigurationItemPkg_get_all_contents(self):
        tested = ConfigurationItemPkg()
        tested.get_all_contents()
        pass

    def test_ConfigurationItemPkg_get_all_contents_by_type(self):
        tested = ConfigurationItemPkg()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_ConfigurationItemPkg_get_available_s_b_queries(self):
        tested = ConfigurationItemPkg()
        tested.get_available_s_b_queries()
        pass

    def test_ConfigurationItemPkg_get_query_result(self):
        tested = ConfigurationItemPkg()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_ConfigurationItemPkg_owned_configuration_item_pkgs_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_owned_configuration_item_pkgs()
        pass

    def test_ConfigurationItemPkg_owned_configuration_items_getter(self):
        tested = ConfigurationItemPkg()
        tested.get_owned_configuration_items()
        pass

    def test_ConfigurationItem_id_getter(self):
        tested = ConfigurationItem()
        tested.get_id()
        pass

    def test_ConfigurationItem_id_setter(self):
        tested = ConfigurationItem()
        value = "value"
        tested.set_id(value)
        pass

    def test_ConfigurationItem_sid_getter(self):
        tested = ConfigurationItem()
        tested.get_sid()
        pass

    def test_ConfigurationItem_sid_setter(self):
        tested = ConfigurationItem()
        value = "value"
        tested.set_sid(value)
        pass

    def test_ConfigurationItem_name_getter(self):
        tested = ConfigurationItem()
        tested.get_name()
        pass

    def test_ConfigurationItem_name_setter(self):
        tested = ConfigurationItem()
        value = "value"
        tested.set_name(value)
        pass

    def test_ConfigurationItem_summary_getter(self):
        tested = ConfigurationItem()
        tested.get_summary()
        pass

    def test_ConfigurationItem_summary_setter(self):
        tested = ConfigurationItem()
        value = "value"
        tested.set_summary(value)
        pass

    def test_ConfigurationItem_description_getter(self):
        tested = ConfigurationItem()
        tested.get_description()
        pass

    def test_ConfigurationItem_description_setter(self):
        tested = ConfigurationItem()
        value = "value"
        tested.set_description(value)
        pass

    def test_ConfigurationItem_status_getter(self):
        tested = ConfigurationItem()
        tested.get_status()
        pass

    def test_ConfigurationItem_status_setter(self):
        tested = ConfigurationItem()
        value = "value"
        tested.set_status(value)
        pass

    def test_ConfigurationItem_review_getter(self):
        tested = ConfigurationItem()
        tested.get_review()
        pass

    def test_ConfigurationItem_review_setter(self):
        tested = ConfigurationItem()
        value = "value"
        tested.set_review(value)
        pass

    def test_ConfigurationItem_visible_in_documentation_getter(self):
        tested = ConfigurationItem()
        tested.get_visible_in_documentation()
        pass

    def test_ConfigurationItem_visible_in_documentation_setter(self):
        tested = ConfigurationItem()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_ConfigurationItem_visible_for_traceability_getter(self):
        tested = ConfigurationItem()
        tested.get_visible_for_traceability()
        pass

    def test_ConfigurationItem_visible_for_traceability_setter(self):
        tested = ConfigurationItem()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_ConfigurationItem_owned_constraints_getter(self):
        tested = ConfigurationItem()
        tested.get_owned_constraints()
        pass

    def test_ConfigurationItem_constraints_getter(self):
        tested = ConfigurationItem()
        tested.get_constraints()
        pass

    def test_ConfigurationItem_constraints_setter(self):
        tested = ConfigurationItem()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_ConfigurationItem_owned_property_values_getter(self):
        tested = ConfigurationItem()
        tested.get_owned_property_values()
        pass

    def test_ConfigurationItem_applied_property_values_getter(self):
        tested = ConfigurationItem()
        tested.get_applied_property_values()
        pass

    def test_ConfigurationItem_applied_property_values_setter(self):
        tested = ConfigurationItem()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_ConfigurationItem_owned_property_value_groups_getter(self):
        tested = ConfigurationItem()
        tested.get_owned_property_value_groups()
        pass

    def test_ConfigurationItem_applied_property_value_groups_getter(self):
        tested = ConfigurationItem()
        tested.get_applied_property_value_groups()
        pass

    def test_ConfigurationItem_applied_property_value_groups_setter(self):
        tested = ConfigurationItem()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_ConfigurationItem_owned_enumeration_property_types_getter(self):
        tested = ConfigurationItem()
        tested.get_owned_enumeration_property_types()
        pass

    def test_ConfigurationItem_owned_diagrams_getter(self):
        tested = ConfigurationItem()
        tested.get_owned_diagrams()
        pass

    def test_ConfigurationItem_element_of_interest_for_diagrams_getter(self):
        tested = ConfigurationItem()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_ConfigurationItem_element_of_interest_for_diagrams_setter(self):
        tested = ConfigurationItem()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_ConfigurationItem_contextual_element_for_diagrams_getter(self):
        tested = ConfigurationItem()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_ConfigurationItem_contextual_element_for_diagrams_setter(self):
        tested = ConfigurationItem()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_ConfigurationItem_representing_diagrams_getter(self):
        tested = ConfigurationItem()
        tested.get_representing_diagrams()
        pass

    def test_ConfigurationItem__r_e_cs_getter(self):
        tested = ConfigurationItem()
        tested.get__r_e_cs()
        pass

    def test_ConfigurationItem__r_e_cs_setter(self):
        tested = ConfigurationItem()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_ConfigurationItem__r_p_ls_getter(self):
        tested = ConfigurationItem()
        tested.get__r_p_ls()
        pass

    def test_ConfigurationItem__r_p_ls_setter(self):
        tested = ConfigurationItem()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_ConfigurationItem_get_label(self):
        tested = ConfigurationItem()
        tested.get_label()
        pass

    def test_ConfigurationItem_get_element_type(self):
        tested = ConfigurationItem()
        tested.get_element_type()
        pass

    def test_ConfigurationItem_get_container(self):
        tested = ConfigurationItem()
        tested.get_container()
        pass

    def test_ConfigurationItem_get_contents(self):
        tested = ConfigurationItem()
        tested.get_contents()
        pass

    def test_ConfigurationItem_get_all_contents(self):
        tested = ConfigurationItem()
        tested.get_all_contents()
        pass

    def test_ConfigurationItem_get_all_contents_by_type(self):
        tested = ConfigurationItem()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_ConfigurationItem_get_available_s_b_queries(self):
        tested = ConfigurationItem()
        tested.get_available_s_b_queries()
        pass

    def test_ConfigurationItem_get_query_result(self):
        tested = ConfigurationItem()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_ConfigurationItem_item_identifier_getter(self):
        tested = ConfigurationItem()
        tested.get_item_identifier()
        pass

    def test_ConfigurationItem_item_identifier_setter(self):
        tested = ConfigurationItem()
        value = "value"
        tested.set_item_identifier(value)
        pass

    def test_ConfigurationItem_kind_getter(self):
        tested = ConfigurationItem()
        tested.get_kind()
        pass

    def test_ConfigurationItem_kind_setter(self):
        tested = ConfigurationItem()
        value = ConfigurationItemKind()
        tested.set_kind(value)
        pass

    def test_ConfigurationItem_owned_configuration_items_getter(self):
        tested = ConfigurationItem()
        tested.get_owned_configuration_items()
        pass

    def test_ConfigurationItem_owned_configuration_item_pkgs_getter(self):
        tested = ConfigurationItem()
        tested.get_owned_configuration_item_pkgs()
        pass

    def test_ConfigurationItem_allocated_physical_artifacts_getter(self):
        tested = ConfigurationItem()
        tested.get_allocated_physical_artifacts()
        pass

    def test_ConfigurationItem_allocated_physical_artifacts_setter(self):
        tested = ConfigurationItem()
        value = PhysicalLink()
        tested.get_allocated_physical_artifacts().add(value)
        pass

    def test_StateMachine_id_getter(self):
        tested = StateMachine()
        tested.get_id()
        pass

    def test_StateMachine_id_setter(self):
        tested = StateMachine()
        value = "value"
        tested.set_id(value)
        pass

    def test_StateMachine_sid_getter(self):
        tested = StateMachine()
        tested.get_sid()
        pass

    def test_StateMachine_sid_setter(self):
        tested = StateMachine()
        value = "value"
        tested.set_sid(value)
        pass

    def test_StateMachine_name_getter(self):
        tested = StateMachine()
        tested.get_name()
        pass

    def test_StateMachine_name_setter(self):
        tested = StateMachine()
        value = "value"
        tested.set_name(value)
        pass

    def test_StateMachine_summary_getter(self):
        tested = StateMachine()
        tested.get_summary()
        pass

    def test_StateMachine_summary_setter(self):
        tested = StateMachine()
        value = "value"
        tested.set_summary(value)
        pass

    def test_StateMachine_description_getter(self):
        tested = StateMachine()
        tested.get_description()
        pass

    def test_StateMachine_description_setter(self):
        tested = StateMachine()
        value = "value"
        tested.set_description(value)
        pass

    def test_StateMachine_status_getter(self):
        tested = StateMachine()
        tested.get_status()
        pass

    def test_StateMachine_status_setter(self):
        tested = StateMachine()
        value = "value"
        tested.set_status(value)
        pass

    def test_StateMachine_review_getter(self):
        tested = StateMachine()
        tested.get_review()
        pass

    def test_StateMachine_review_setter(self):
        tested = StateMachine()
        value = "value"
        tested.set_review(value)
        pass

    def test_StateMachine_visible_in_documentation_getter(self):
        tested = StateMachine()
        tested.get_visible_in_documentation()
        pass

    def test_StateMachine_visible_in_documentation_setter(self):
        tested = StateMachine()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_StateMachine_visible_for_traceability_getter(self):
        tested = StateMachine()
        tested.get_visible_for_traceability()
        pass

    def test_StateMachine_visible_for_traceability_setter(self):
        tested = StateMachine()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_StateMachine_owned_constraints_getter(self):
        tested = StateMachine()
        tested.get_owned_constraints()
        pass

    def test_StateMachine_constraints_getter(self):
        tested = StateMachine()
        tested.get_constraints()
        pass

    def test_StateMachine_constraints_setter(self):
        tested = StateMachine()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_StateMachine_owned_property_values_getter(self):
        tested = StateMachine()
        tested.get_owned_property_values()
        pass

    def test_StateMachine_applied_property_values_getter(self):
        tested = StateMachine()
        tested.get_applied_property_values()
        pass

    def test_StateMachine_applied_property_values_setter(self):
        tested = StateMachine()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_StateMachine_owned_property_value_groups_getter(self):
        tested = StateMachine()
        tested.get_owned_property_value_groups()
        pass

    def test_StateMachine_applied_property_value_groups_getter(self):
        tested = StateMachine()
        tested.get_applied_property_value_groups()
        pass

    def test_StateMachine_applied_property_value_groups_setter(self):
        tested = StateMachine()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_StateMachine_owned_enumeration_property_types_getter(self):
        tested = StateMachine()
        tested.get_owned_enumeration_property_types()
        pass

    def test_StateMachine_owned_diagrams_getter(self):
        tested = StateMachine()
        tested.get_owned_diagrams()
        pass

    def test_StateMachine_element_of_interest_for_diagrams_getter(self):
        tested = StateMachine()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_StateMachine_element_of_interest_for_diagrams_setter(self):
        tested = StateMachine()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_StateMachine_contextual_element_for_diagrams_getter(self):
        tested = StateMachine()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_StateMachine_contextual_element_for_diagrams_setter(self):
        tested = StateMachine()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_StateMachine_representing_diagrams_getter(self):
        tested = StateMachine()
        tested.get_representing_diagrams()
        pass

    def test_StateMachine__r_e_cs_getter(self):
        tested = StateMachine()
        tested.get__r_e_cs()
        pass

    def test_StateMachine__r_e_cs_setter(self):
        tested = StateMachine()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_StateMachine__r_p_ls_getter(self):
        tested = StateMachine()
        tested.get__r_p_ls()
        pass

    def test_StateMachine__r_p_ls_setter(self):
        tested = StateMachine()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_StateMachine_get_label(self):
        tested = StateMachine()
        tested.get_label()
        pass

    def test_StateMachine_get_element_type(self):
        tested = StateMachine()
        tested.get_element_type()
        pass

    def test_StateMachine_get_container(self):
        tested = StateMachine()
        tested.get_container()
        pass

    def test_StateMachine_get_contents(self):
        tested = StateMachine()
        tested.get_contents()
        pass

    def test_StateMachine_get_all_contents(self):
        tested = StateMachine()
        tested.get_all_contents()
        pass

    def test_StateMachine_get_all_contents_by_type(self):
        tested = StateMachine()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_StateMachine_get_available_s_b_queries(self):
        tested = StateMachine()
        tested.get_available_s_b_queries()
        pass

    def test_StateMachine_get_query_result(self):
        tested = StateMachine()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_StateMachine_owned_regions_getter(self):
        tested = StateMachine()
        tested.get_owned_regions()
        pass

    def test_State_incoming_getter(self):
        tested = State()
        tested.get_incoming()
        pass

    def test_State_incoming_setter(self):
        tested = State()
        value = StateTransition()
        tested.get_incoming().add(value)
        pass

    def test_State_outgoing_getter(self):
        tested = State()
        tested.get_outgoing()
        pass

    def test_State_outgoing_setter(self):
        tested = State()
        value = StateTransition()
        tested.get_outgoing().add(value)
        pass

    def test_State_realized_states_getter(self):
        tested = State()
        tested.get_realized_states()
        pass

    def test_State_realized_states_setter(self):
        tested = State()
        value = Pseudostate()
        tested.get_realized_states().add(value)
        pass

    def test_State_realizing_states_getter(self):
        tested = State()
        tested.get_realizing_states()
        pass

    def test_State_realizing_states_setter(self):
        tested = State()
        value = Pseudostate()
        tested.get_realizing_states().add(value)
        pass

    def test_State_id_getter(self):
        tested = State()
        tested.get_id()
        pass

    def test_State_id_setter(self):
        tested = State()
        value = "value"
        tested.set_id(value)
        pass

    def test_State_sid_getter(self):
        tested = State()
        tested.get_sid()
        pass

    def test_State_sid_setter(self):
        tested = State()
        value = "value"
        tested.set_sid(value)
        pass

    def test_State_name_getter(self):
        tested = State()
        tested.get_name()
        pass

    def test_State_name_setter(self):
        tested = State()
        value = "value"
        tested.set_name(value)
        pass

    def test_State_summary_getter(self):
        tested = State()
        tested.get_summary()
        pass

    def test_State_summary_setter(self):
        tested = State()
        value = "value"
        tested.set_summary(value)
        pass

    def test_State_description_getter(self):
        tested = State()
        tested.get_description()
        pass

    def test_State_description_setter(self):
        tested = State()
        value = "value"
        tested.set_description(value)
        pass

    def test_State_status_getter(self):
        tested = State()
        tested.get_status()
        pass

    def test_State_status_setter(self):
        tested = State()
        value = "value"
        tested.set_status(value)
        pass

    def test_State_review_getter(self):
        tested = State()
        tested.get_review()
        pass

    def test_State_review_setter(self):
        tested = State()
        value = "value"
        tested.set_review(value)
        pass

    def test_State_visible_in_documentation_getter(self):
        tested = State()
        tested.get_visible_in_documentation()
        pass

    def test_State_visible_in_documentation_setter(self):
        tested = State()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_State_visible_for_traceability_getter(self):
        tested = State()
        tested.get_visible_for_traceability()
        pass

    def test_State_visible_for_traceability_setter(self):
        tested = State()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_State_owned_constraints_getter(self):
        tested = State()
        tested.get_owned_constraints()
        pass

    def test_State_constraints_getter(self):
        tested = State()
        tested.get_constraints()
        pass

    def test_State_constraints_setter(self):
        tested = State()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_State_owned_property_values_getter(self):
        tested = State()
        tested.get_owned_property_values()
        pass

    def test_State_applied_property_values_getter(self):
        tested = State()
        tested.get_applied_property_values()
        pass

    def test_State_applied_property_values_setter(self):
        tested = State()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_State_owned_property_value_groups_getter(self):
        tested = State()
        tested.get_owned_property_value_groups()
        pass

    def test_State_applied_property_value_groups_getter(self):
        tested = State()
        tested.get_applied_property_value_groups()
        pass

    def test_State_applied_property_value_groups_setter(self):
        tested = State()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_State_owned_enumeration_property_types_getter(self):
        tested = State()
        tested.get_owned_enumeration_property_types()
        pass

    def test_State_owned_diagrams_getter(self):
        tested = State()
        tested.get_owned_diagrams()
        pass

    def test_State_element_of_interest_for_diagrams_getter(self):
        tested = State()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_State_element_of_interest_for_diagrams_setter(self):
        tested = State()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_State_contextual_element_for_diagrams_getter(self):
        tested = State()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_State_contextual_element_for_diagrams_setter(self):
        tested = State()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_State_representing_diagrams_getter(self):
        tested = State()
        tested.get_representing_diagrams()
        pass

    def test_State__r_e_cs_getter(self):
        tested = State()
        tested.get__r_e_cs()
        pass

    def test_State__r_e_cs_setter(self):
        tested = State()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_State__r_p_ls_getter(self):
        tested = State()
        tested.get__r_p_ls()
        pass

    def test_State__r_p_ls_setter(self):
        tested = State()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_State_get_label(self):
        tested = State()
        tested.get_label()
        pass

    def test_State_get_element_type(self):
        tested = State()
        tested.get_element_type()
        pass

    def test_State_get_container(self):
        tested = State()
        tested.get_container()
        pass

    def test_State_get_contents(self):
        tested = State()
        tested.get_contents()
        pass

    def test_State_get_all_contents(self):
        tested = State()
        tested.get_all_contents()
        pass

    def test_State_get_all_contents_by_type(self):
        tested = State()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_State_get_available_s_b_queries(self):
        tested = State()
        tested.get_available_s_b_queries()
        pass

    def test_State_get_query_result(self):
        tested = State()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_State_owned_regions_getter(self):
        tested = State()
        tested.get_owned_regions()
        pass

    def test_State_available_activities_functions_getter(self):
        tested = State()
        tested.get_available_activities_functions()
        pass

    def test_State_available_activities_functions_setter(self):
        tested = State()
        value = PhysicalFunction()
        tested.get_available_activities_functions().add(value)
        pass

    def test_State_entry_getter(self):
        tested = State()
        tested.get_entry()
        pass

    def test_State_entry_setter(self):
        tested = State()
        value = FunctionalExchange()
        tested.get_entry().add(value)
        pass

    def test_State_do_getter(self):
        tested = State()
        tested.get_do()
        pass

    def test_State_do_setter(self):
        tested = State()
        value = FunctionalExchange()
        tested.get_do().add(value)
        pass

    def test_State_exit_getter(self):
        tested = State()
        tested.get_exit()
        pass

    def test_State_exit_setter(self):
        tested = State()
        value = FunctionalExchange()
        tested.get_exit().add(value)
        pass

    def test_State_available_functional_chains_getter(self):
        tested = State()
        tested.get_available_functional_chains()
        pass

    def test_State_available_functional_chains_setter(self):
        tested = State()
        value = FunctionalChain()
        tested.get_available_functional_chains().add(value)
        pass

    def test_State_available_operational_processes_getter(self):
        tested = State()
        tested.get_available_operational_processes()
        pass

    def test_State_available_operational_processes_setter(self):
        tested = State()
        value = OperationalProcess()
        tested.get_available_operational_processes().add(value)
        pass

    def test_State_available_capabilities_getter(self):
        tested = State()
        tested.get_available_capabilities()
        pass

    def test_State_available_capabilities_setter(self):
        tested = State()
        value = CapabilityRealization()
        tested.get_available_capabilities().add(value)
        pass

    def test_Mode_owned_regions_getter(self):
        tested = Mode()
        tested.get_owned_regions()
        pass

    def test_Mode_available_activities_functions_getter(self):
        tested = Mode()
        tested.get_available_activities_functions()
        pass

    def test_Mode_available_activities_functions_setter(self):
        tested = Mode()
        value = PhysicalFunction()
        tested.get_available_activities_functions().add(value)
        pass

    def test_Mode_entry_getter(self):
        tested = Mode()
        tested.get_entry()
        pass

    def test_Mode_entry_setter(self):
        tested = Mode()
        value = FunctionalExchange()
        tested.get_entry().add(value)
        pass

    def test_Mode_do_getter(self):
        tested = Mode()
        tested.get_do()
        pass

    def test_Mode_do_setter(self):
        tested = Mode()
        value = FunctionalExchange()
        tested.get_do().add(value)
        pass

    def test_Mode_exit_getter(self):
        tested = Mode()
        tested.get_exit()
        pass

    def test_Mode_exit_setter(self):
        tested = Mode()
        value = FunctionalExchange()
        tested.get_exit().add(value)
        pass

    def test_Mode_available_functional_chains_getter(self):
        tested = Mode()
        tested.get_available_functional_chains()
        pass

    def test_Mode_available_functional_chains_setter(self):
        tested = Mode()
        value = FunctionalChain()
        tested.get_available_functional_chains().add(value)
        pass

    def test_Mode_available_operational_processes_getter(self):
        tested = Mode()
        tested.get_available_operational_processes()
        pass

    def test_Mode_available_operational_processes_setter(self):
        tested = Mode()
        value = OperationalProcess()
        tested.get_available_operational_processes().add(value)
        pass

    def test_Mode_available_capabilities_getter(self):
        tested = Mode()
        tested.get_available_capabilities()
        pass

    def test_Mode_available_capabilities_setter(self):
        tested = Mode()
        value = CapabilityRealization()
        tested.get_available_capabilities().add(value)
        pass

    def test_Mode_incoming_getter(self):
        tested = Mode()
        tested.get_incoming()
        pass

    def test_Mode_incoming_setter(self):
        tested = Mode()
        value = StateTransition()
        tested.get_incoming().add(value)
        pass

    def test_Mode_outgoing_getter(self):
        tested = Mode()
        tested.get_outgoing()
        pass

    def test_Mode_outgoing_setter(self):
        tested = Mode()
        value = StateTransition()
        tested.get_outgoing().add(value)
        pass

    def test_Mode_realized_states_getter(self):
        tested = Mode()
        tested.get_realized_states()
        pass

    def test_Mode_realized_states_setter(self):
        tested = Mode()
        value = Pseudostate()
        tested.get_realized_states().add(value)
        pass

    def test_Mode_realizing_states_getter(self):
        tested = Mode()
        tested.get_realizing_states()
        pass

    def test_Mode_realizing_states_setter(self):
        tested = Mode()
        value = Pseudostate()
        tested.get_realizing_states().add(value)
        pass

    def test_Mode_id_getter(self):
        tested = Mode()
        tested.get_id()
        pass

    def test_Mode_id_setter(self):
        tested = Mode()
        value = "value"
        tested.set_id(value)
        pass

    def test_Mode_sid_getter(self):
        tested = Mode()
        tested.get_sid()
        pass

    def test_Mode_sid_setter(self):
        tested = Mode()
        value = "value"
        tested.set_sid(value)
        pass

    def test_Mode_name_getter(self):
        tested = Mode()
        tested.get_name()
        pass

    def test_Mode_name_setter(self):
        tested = Mode()
        value = "value"
        tested.set_name(value)
        pass

    def test_Mode_summary_getter(self):
        tested = Mode()
        tested.get_summary()
        pass

    def test_Mode_summary_setter(self):
        tested = Mode()
        value = "value"
        tested.set_summary(value)
        pass

    def test_Mode_description_getter(self):
        tested = Mode()
        tested.get_description()
        pass

    def test_Mode_description_setter(self):
        tested = Mode()
        value = "value"
        tested.set_description(value)
        pass

    def test_Mode_status_getter(self):
        tested = Mode()
        tested.get_status()
        pass

    def test_Mode_status_setter(self):
        tested = Mode()
        value = "value"
        tested.set_status(value)
        pass

    def test_Mode_review_getter(self):
        tested = Mode()
        tested.get_review()
        pass

    def test_Mode_review_setter(self):
        tested = Mode()
        value = "value"
        tested.set_review(value)
        pass

    def test_Mode_visible_in_documentation_getter(self):
        tested = Mode()
        tested.get_visible_in_documentation()
        pass

    def test_Mode_visible_in_documentation_setter(self):
        tested = Mode()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_Mode_visible_for_traceability_getter(self):
        tested = Mode()
        tested.get_visible_for_traceability()
        pass

    def test_Mode_visible_for_traceability_setter(self):
        tested = Mode()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_Mode_owned_constraints_getter(self):
        tested = Mode()
        tested.get_owned_constraints()
        pass

    def test_Mode_constraints_getter(self):
        tested = Mode()
        tested.get_constraints()
        pass

    def test_Mode_constraints_setter(self):
        tested = Mode()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_Mode_owned_property_values_getter(self):
        tested = Mode()
        tested.get_owned_property_values()
        pass

    def test_Mode_applied_property_values_getter(self):
        tested = Mode()
        tested.get_applied_property_values()
        pass

    def test_Mode_applied_property_values_setter(self):
        tested = Mode()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_Mode_owned_property_value_groups_getter(self):
        tested = Mode()
        tested.get_owned_property_value_groups()
        pass

    def test_Mode_applied_property_value_groups_getter(self):
        tested = Mode()
        tested.get_applied_property_value_groups()
        pass

    def test_Mode_applied_property_value_groups_setter(self):
        tested = Mode()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_Mode_owned_enumeration_property_types_getter(self):
        tested = Mode()
        tested.get_owned_enumeration_property_types()
        pass

    def test_Mode_owned_diagrams_getter(self):
        tested = Mode()
        tested.get_owned_diagrams()
        pass

    def test_Mode_element_of_interest_for_diagrams_getter(self):
        tested = Mode()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_Mode_element_of_interest_for_diagrams_setter(self):
        tested = Mode()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_Mode_contextual_element_for_diagrams_getter(self):
        tested = Mode()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_Mode_contextual_element_for_diagrams_setter(self):
        tested = Mode()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_Mode_representing_diagrams_getter(self):
        tested = Mode()
        tested.get_representing_diagrams()
        pass

    def test_Mode__r_e_cs_getter(self):
        tested = Mode()
        tested.get__r_e_cs()
        pass

    def test_Mode__r_e_cs_setter(self):
        tested = Mode()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_Mode__r_p_ls_getter(self):
        tested = Mode()
        tested.get__r_p_ls()
        pass

    def test_Mode__r_p_ls_setter(self):
        tested = Mode()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_Mode_get_label(self):
        tested = Mode()
        tested.get_label()
        pass

    def test_Mode_get_element_type(self):
        tested = Mode()
        tested.get_element_type()
        pass

    def test_Mode_get_container(self):
        tested = Mode()
        tested.get_container()
        pass

    def test_Mode_get_contents(self):
        tested = Mode()
        tested.get_contents()
        pass

    def test_Mode_get_all_contents(self):
        tested = Mode()
        tested.get_all_contents()
        pass

    def test_Mode_get_all_contents_by_type(self):
        tested = Mode()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_Mode_get_available_s_b_queries(self):
        tested = Mode()
        tested.get_available_s_b_queries()
        pass

    def test_Mode_get_query_result(self):
        tested = Mode()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_Pseudostate_incoming_getter(self):
        tested = Pseudostate()
        tested.get_incoming()
        pass

    def test_Pseudostate_incoming_setter(self):
        tested = Pseudostate()
        value = StateTransition()
        tested.get_incoming().add(value)
        pass

    def test_Pseudostate_outgoing_getter(self):
        tested = Pseudostate()
        tested.get_outgoing()
        pass

    def test_Pseudostate_outgoing_setter(self):
        tested = Pseudostate()
        value = StateTransition()
        tested.get_outgoing().add(value)
        pass

    def test_Pseudostate_realized_states_getter(self):
        tested = Pseudostate()
        tested.get_realized_states()
        pass

    def test_Pseudostate_realized_states_setter(self):
        tested = Pseudostate()
        value = Pseudostate()
        tested.get_realized_states().add(value)
        pass

    def test_Pseudostate_realizing_states_getter(self):
        tested = Pseudostate()
        tested.get_realizing_states()
        pass

    def test_Pseudostate_realizing_states_setter(self):
        tested = Pseudostate()
        value = Pseudostate()
        tested.get_realizing_states().add(value)
        pass

    def test_Pseudostate_id_getter(self):
        tested = Pseudostate()
        tested.get_id()
        pass

    def test_Pseudostate_id_setter(self):
        tested = Pseudostate()
        value = "value"
        tested.set_id(value)
        pass

    def test_Pseudostate_sid_getter(self):
        tested = Pseudostate()
        tested.get_sid()
        pass

    def test_Pseudostate_sid_setter(self):
        tested = Pseudostate()
        value = "value"
        tested.set_sid(value)
        pass

    def test_Pseudostate_name_getter(self):
        tested = Pseudostate()
        tested.get_name()
        pass

    def test_Pseudostate_name_setter(self):
        tested = Pseudostate()
        value = "value"
        tested.set_name(value)
        pass

    def test_Pseudostate_summary_getter(self):
        tested = Pseudostate()
        tested.get_summary()
        pass

    def test_Pseudostate_summary_setter(self):
        tested = Pseudostate()
        value = "value"
        tested.set_summary(value)
        pass

    def test_Pseudostate_description_getter(self):
        tested = Pseudostate()
        tested.get_description()
        pass

    def test_Pseudostate_description_setter(self):
        tested = Pseudostate()
        value = "value"
        tested.set_description(value)
        pass

    def test_Pseudostate_status_getter(self):
        tested = Pseudostate()
        tested.get_status()
        pass

    def test_Pseudostate_status_setter(self):
        tested = Pseudostate()
        value = "value"
        tested.set_status(value)
        pass

    def test_Pseudostate_review_getter(self):
        tested = Pseudostate()
        tested.get_review()
        pass

    def test_Pseudostate_review_setter(self):
        tested = Pseudostate()
        value = "value"
        tested.set_review(value)
        pass

    def test_Pseudostate_visible_in_documentation_getter(self):
        tested = Pseudostate()
        tested.get_visible_in_documentation()
        pass

    def test_Pseudostate_visible_in_documentation_setter(self):
        tested = Pseudostate()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_Pseudostate_visible_for_traceability_getter(self):
        tested = Pseudostate()
        tested.get_visible_for_traceability()
        pass

    def test_Pseudostate_visible_for_traceability_setter(self):
        tested = Pseudostate()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_Pseudostate_owned_constraints_getter(self):
        tested = Pseudostate()
        tested.get_owned_constraints()
        pass

    def test_Pseudostate_constraints_getter(self):
        tested = Pseudostate()
        tested.get_constraints()
        pass

    def test_Pseudostate_constraints_setter(self):
        tested = Pseudostate()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_Pseudostate_owned_property_values_getter(self):
        tested = Pseudostate()
        tested.get_owned_property_values()
        pass

    def test_Pseudostate_applied_property_values_getter(self):
        tested = Pseudostate()
        tested.get_applied_property_values()
        pass

    def test_Pseudostate_applied_property_values_setter(self):
        tested = Pseudostate()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_Pseudostate_owned_property_value_groups_getter(self):
        tested = Pseudostate()
        tested.get_owned_property_value_groups()
        pass

    def test_Pseudostate_applied_property_value_groups_getter(self):
        tested = Pseudostate()
        tested.get_applied_property_value_groups()
        pass

    def test_Pseudostate_applied_property_value_groups_setter(self):
        tested = Pseudostate()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_Pseudostate_owned_enumeration_property_types_getter(self):
        tested = Pseudostate()
        tested.get_owned_enumeration_property_types()
        pass

    def test_Pseudostate_owned_diagrams_getter(self):
        tested = Pseudostate()
        tested.get_owned_diagrams()
        pass

    def test_Pseudostate_element_of_interest_for_diagrams_getter(self):
        tested = Pseudostate()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_Pseudostate_element_of_interest_for_diagrams_setter(self):
        tested = Pseudostate()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_Pseudostate_contextual_element_for_diagrams_getter(self):
        tested = Pseudostate()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_Pseudostate_contextual_element_for_diagrams_setter(self):
        tested = Pseudostate()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_Pseudostate_representing_diagrams_getter(self):
        tested = Pseudostate()
        tested.get_representing_diagrams()
        pass

    def test_Pseudostate__r_e_cs_getter(self):
        tested = Pseudostate()
        tested.get__r_e_cs()
        pass

    def test_Pseudostate__r_e_cs_setter(self):
        tested = Pseudostate()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_Pseudostate__r_p_ls_getter(self):
        tested = Pseudostate()
        tested.get__r_p_ls()
        pass

    def test_Pseudostate__r_p_ls_setter(self):
        tested = Pseudostate()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_Pseudostate_get_label(self):
        tested = Pseudostate()
        tested.get_label()
        pass

    def test_Pseudostate_get_element_type(self):
        tested = Pseudostate()
        tested.get_element_type()
        pass

    def test_Pseudostate_get_container(self):
        tested = Pseudostate()
        tested.get_container()
        pass

    def test_Pseudostate_get_contents(self):
        tested = Pseudostate()
        tested.get_contents()
        pass

    def test_Pseudostate_get_all_contents(self):
        tested = Pseudostate()
        tested.get_all_contents()
        pass

    def test_Pseudostate_get_all_contents_by_type(self):
        tested = Pseudostate()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_Pseudostate_get_available_s_b_queries(self):
        tested = Pseudostate()
        tested.get_available_s_b_queries()
        pass

    def test_Pseudostate_get_query_result(self):
        tested = Pseudostate()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_Pseudostate_kind_getter(self):
        tested = Pseudostate()
        tested.get_kind()
        pass

    def test_Region_id_getter(self):
        tested = Region()
        tested.get_id()
        pass

    def test_Region_id_setter(self):
        tested = Region()
        value = "value"
        tested.set_id(value)
        pass

    def test_Region_sid_getter(self):
        tested = Region()
        tested.get_sid()
        pass

    def test_Region_sid_setter(self):
        tested = Region()
        value = "value"
        tested.set_sid(value)
        pass

    def test_Region_name_getter(self):
        tested = Region()
        tested.get_name()
        pass

    def test_Region_name_setter(self):
        tested = Region()
        value = "value"
        tested.set_name(value)
        pass

    def test_Region_summary_getter(self):
        tested = Region()
        tested.get_summary()
        pass

    def test_Region_summary_setter(self):
        tested = Region()
        value = "value"
        tested.set_summary(value)
        pass

    def test_Region_description_getter(self):
        tested = Region()
        tested.get_description()
        pass

    def test_Region_description_setter(self):
        tested = Region()
        value = "value"
        tested.set_description(value)
        pass

    def test_Region_status_getter(self):
        tested = Region()
        tested.get_status()
        pass

    def test_Region_status_setter(self):
        tested = Region()
        value = "value"
        tested.set_status(value)
        pass

    def test_Region_review_getter(self):
        tested = Region()
        tested.get_review()
        pass

    def test_Region_review_setter(self):
        tested = Region()
        value = "value"
        tested.set_review(value)
        pass

    def test_Region_visible_in_documentation_getter(self):
        tested = Region()
        tested.get_visible_in_documentation()
        pass

    def test_Region_visible_in_documentation_setter(self):
        tested = Region()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_Region_visible_for_traceability_getter(self):
        tested = Region()
        tested.get_visible_for_traceability()
        pass

    def test_Region_visible_for_traceability_setter(self):
        tested = Region()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_Region_owned_constraints_getter(self):
        tested = Region()
        tested.get_owned_constraints()
        pass

    def test_Region_constraints_getter(self):
        tested = Region()
        tested.get_constraints()
        pass

    def test_Region_constraints_setter(self):
        tested = Region()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_Region_owned_property_values_getter(self):
        tested = Region()
        tested.get_owned_property_values()
        pass

    def test_Region_applied_property_values_getter(self):
        tested = Region()
        tested.get_applied_property_values()
        pass

    def test_Region_applied_property_values_setter(self):
        tested = Region()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_Region_owned_property_value_groups_getter(self):
        tested = Region()
        tested.get_owned_property_value_groups()
        pass

    def test_Region_applied_property_value_groups_getter(self):
        tested = Region()
        tested.get_applied_property_value_groups()
        pass

    def test_Region_applied_property_value_groups_setter(self):
        tested = Region()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_Region_owned_enumeration_property_types_getter(self):
        tested = Region()
        tested.get_owned_enumeration_property_types()
        pass

    def test_Region_owned_diagrams_getter(self):
        tested = Region()
        tested.get_owned_diagrams()
        pass

    def test_Region_element_of_interest_for_diagrams_getter(self):
        tested = Region()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_Region_element_of_interest_for_diagrams_setter(self):
        tested = Region()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_Region_contextual_element_for_diagrams_getter(self):
        tested = Region()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_Region_contextual_element_for_diagrams_setter(self):
        tested = Region()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_Region_representing_diagrams_getter(self):
        tested = Region()
        tested.get_representing_diagrams()
        pass

    def test_Region__r_e_cs_getter(self):
        tested = Region()
        tested.get__r_e_cs()
        pass

    def test_Region__r_e_cs_setter(self):
        tested = Region()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_Region__r_p_ls_getter(self):
        tested = Region()
        tested.get__r_p_ls()
        pass

    def test_Region__r_p_ls_setter(self):
        tested = Region()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_Region_get_label(self):
        tested = Region()
        tested.get_label()
        pass

    def test_Region_get_element_type(self):
        tested = Region()
        tested.get_element_type()
        pass

    def test_Region_get_container(self):
        tested = Region()
        tested.get_container()
        pass

    def test_Region_get_contents(self):
        tested = Region()
        tested.get_contents()
        pass

    def test_Region_get_all_contents(self):
        tested = Region()
        tested.get_all_contents()
        pass

    def test_Region_get_all_contents_by_type(self):
        tested = Region()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_Region_get_available_s_b_queries(self):
        tested = Region()
        tested.get_available_s_b_queries()
        pass

    def test_Region_get_query_result(self):
        tested = Region()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_Region_owned_states_getter(self):
        tested = Region()
        tested.get_owned_states()
        pass

    def test_StateTransition_id_getter(self):
        tested = StateTransition()
        tested.get_id()
        pass

    def test_StateTransition_id_setter(self):
        tested = StateTransition()
        value = "value"
        tested.set_id(value)
        pass

    def test_StateTransition_sid_getter(self):
        tested = StateTransition()
        tested.get_sid()
        pass

    def test_StateTransition_sid_setter(self):
        tested = StateTransition()
        value = "value"
        tested.set_sid(value)
        pass

    def test_StateTransition_name_getter(self):
        tested = StateTransition()
        tested.get_name()
        pass

    def test_StateTransition_name_setter(self):
        tested = StateTransition()
        value = "value"
        tested.set_name(value)
        pass

    def test_StateTransition_summary_getter(self):
        tested = StateTransition()
        tested.get_summary()
        pass

    def test_StateTransition_summary_setter(self):
        tested = StateTransition()
        value = "value"
        tested.set_summary(value)
        pass

    def test_StateTransition_description_getter(self):
        tested = StateTransition()
        tested.get_description()
        pass

    def test_StateTransition_description_setter(self):
        tested = StateTransition()
        value = "value"
        tested.set_description(value)
        pass

    def test_StateTransition_status_getter(self):
        tested = StateTransition()
        tested.get_status()
        pass

    def test_StateTransition_status_setter(self):
        tested = StateTransition()
        value = "value"
        tested.set_status(value)
        pass

    def test_StateTransition_review_getter(self):
        tested = StateTransition()
        tested.get_review()
        pass

    def test_StateTransition_review_setter(self):
        tested = StateTransition()
        value = "value"
        tested.set_review(value)
        pass

    def test_StateTransition_visible_in_documentation_getter(self):
        tested = StateTransition()
        tested.get_visible_in_documentation()
        pass

    def test_StateTransition_visible_in_documentation_setter(self):
        tested = StateTransition()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_StateTransition_visible_for_traceability_getter(self):
        tested = StateTransition()
        tested.get_visible_for_traceability()
        pass

    def test_StateTransition_visible_for_traceability_setter(self):
        tested = StateTransition()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_StateTransition_owned_constraints_getter(self):
        tested = StateTransition()
        tested.get_owned_constraints()
        pass

    def test_StateTransition_constraints_getter(self):
        tested = StateTransition()
        tested.get_constraints()
        pass

    def test_StateTransition_constraints_setter(self):
        tested = StateTransition()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_StateTransition_owned_property_values_getter(self):
        tested = StateTransition()
        tested.get_owned_property_values()
        pass

    def test_StateTransition_applied_property_values_getter(self):
        tested = StateTransition()
        tested.get_applied_property_values()
        pass

    def test_StateTransition_applied_property_values_setter(self):
        tested = StateTransition()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_StateTransition_owned_property_value_groups_getter(self):
        tested = StateTransition()
        tested.get_owned_property_value_groups()
        pass

    def test_StateTransition_applied_property_value_groups_getter(self):
        tested = StateTransition()
        tested.get_applied_property_value_groups()
        pass

    def test_StateTransition_applied_property_value_groups_setter(self):
        tested = StateTransition()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_StateTransition_owned_enumeration_property_types_getter(self):
        tested = StateTransition()
        tested.get_owned_enumeration_property_types()
        pass

    def test_StateTransition_owned_diagrams_getter(self):
        tested = StateTransition()
        tested.get_owned_diagrams()
        pass

    def test_StateTransition_element_of_interest_for_diagrams_getter(self):
        tested = StateTransition()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_StateTransition_element_of_interest_for_diagrams_setter(self):
        tested = StateTransition()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_StateTransition_contextual_element_for_diagrams_getter(self):
        tested = StateTransition()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_StateTransition_contextual_element_for_diagrams_setter(self):
        tested = StateTransition()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_StateTransition_representing_diagrams_getter(self):
        tested = StateTransition()
        tested.get_representing_diagrams()
        pass

    def test_StateTransition__r_e_cs_getter(self):
        tested = StateTransition()
        tested.get__r_e_cs()
        pass

    def test_StateTransition__r_e_cs_setter(self):
        tested = StateTransition()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_StateTransition__r_p_ls_getter(self):
        tested = StateTransition()
        tested.get__r_p_ls()
        pass

    def test_StateTransition__r_p_ls_setter(self):
        tested = StateTransition()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_StateTransition_get_label(self):
        tested = StateTransition()
        tested.get_label()
        pass

    def test_StateTransition_get_element_type(self):
        tested = StateTransition()
        tested.get_element_type()
        pass

    def test_StateTransition_get_container(self):
        tested = StateTransition()
        tested.get_container()
        pass

    def test_StateTransition_get_contents(self):
        tested = StateTransition()
        tested.get_contents()
        pass

    def test_StateTransition_get_all_contents(self):
        tested = StateTransition()
        tested.get_all_contents()
        pass

    def test_StateTransition_get_all_contents_by_type(self):
        tested = StateTransition()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_StateTransition_get_available_s_b_queries(self):
        tested = StateTransition()
        tested.get_available_s_b_queries()
        pass

    def test_StateTransition_get_query_result(self):
        tested = StateTransition()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_StateTransition_trigger_description_getter(self):
        tested = StateTransition()
        tested.get_trigger_description()
        pass

    def test_StateTransition_trigger_description_setter(self):
        tested = StateTransition()
        value = "value"
        tested.set_trigger_description(value)
        pass

    def test_StateTransition_source_getter(self):
        tested = StateTransition()
        tested.get_source()
        pass

    def test_StateTransition_source_setter(self):
        tested = StateTransition()
        value = Pseudostate()
        tested.set_source(value)
        pass

    def test_StateTransition_target_getter(self):
        tested = StateTransition()
        tested.get_target()
        pass

    def test_StateTransition_target_setter(self):
        tested = StateTransition()
        value = Pseudostate()
        tested.set_target(value)
        pass

    def test_StateTransition_triggers_getter(self):
        tested = StateTransition()
        tested.get_triggers()
        pass

    def test_StateTransition_triggers_setter(self):
        tested = StateTransition()
        value = FunctionalExchange()
        tested.get_triggers().add(value)
        pass

    def test_StateTransition_guard_getter(self):
        tested = StateTransition()
        tested.get_guard()
        pass

    def test_StateTransition_guard_setter(self):
        tested = StateTransition()
        value = Constraint()
        tested.set_guard(value)
        pass

    def test_StateTransition_effects_getter(self):
        tested = StateTransition()
        tested.get_effects()
        pass

    def test_StateTransition_effects_setter(self):
        tested = StateTransition()
        value = ExchangeItem()
        tested.get_effects().add(value)
        pass

    def test_StateTransition_realized_state_transitions_getter(self):
        tested = StateTransition()
        tested.get_realized_state_transitions()
        pass

    def test_StateTransition_realized_state_transitions_setter(self):
        tested = StateTransition()
        value = StateTransition()
        tested.get_realized_state_transitions().add(value)
        pass

    def test_StateTransition_realizing_state_transitions_getter(self):
        tested = StateTransition()
        tested.get_realizing_state_transitions()
        pass

    def test_StateTransition_realizing_state_transitions_setter(self):
        tested = StateTransition()
        value = StateTransition()
        tested.get_realizing_state_transitions().add(value)
        pass

    def test_ChangeEvent_id_getter(self):
        tested = ChangeEvent()
        tested.get_id()
        pass

    def test_ChangeEvent_id_setter(self):
        tested = ChangeEvent()
        value = "value"
        tested.set_id(value)
        pass

    def test_ChangeEvent_sid_getter(self):
        tested = ChangeEvent()
        tested.get_sid()
        pass

    def test_ChangeEvent_sid_setter(self):
        tested = ChangeEvent()
        value = "value"
        tested.set_sid(value)
        pass

    def test_ChangeEvent_name_getter(self):
        tested = ChangeEvent()
        tested.get_name()
        pass

    def test_ChangeEvent_name_setter(self):
        tested = ChangeEvent()
        value = "value"
        tested.set_name(value)
        pass

    def test_ChangeEvent_summary_getter(self):
        tested = ChangeEvent()
        tested.get_summary()
        pass

    def test_ChangeEvent_summary_setter(self):
        tested = ChangeEvent()
        value = "value"
        tested.set_summary(value)
        pass

    def test_ChangeEvent_description_getter(self):
        tested = ChangeEvent()
        tested.get_description()
        pass

    def test_ChangeEvent_description_setter(self):
        tested = ChangeEvent()
        value = "value"
        tested.set_description(value)
        pass

    def test_ChangeEvent_status_getter(self):
        tested = ChangeEvent()
        tested.get_status()
        pass

    def test_ChangeEvent_status_setter(self):
        tested = ChangeEvent()
        value = "value"
        tested.set_status(value)
        pass

    def test_ChangeEvent_review_getter(self):
        tested = ChangeEvent()
        tested.get_review()
        pass

    def test_ChangeEvent_review_setter(self):
        tested = ChangeEvent()
        value = "value"
        tested.set_review(value)
        pass

    def test_ChangeEvent_visible_in_documentation_getter(self):
        tested = ChangeEvent()
        tested.get_visible_in_documentation()
        pass

    def test_ChangeEvent_visible_in_documentation_setter(self):
        tested = ChangeEvent()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_ChangeEvent_visible_for_traceability_getter(self):
        tested = ChangeEvent()
        tested.get_visible_for_traceability()
        pass

    def test_ChangeEvent_visible_for_traceability_setter(self):
        tested = ChangeEvent()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_ChangeEvent_owned_constraints_getter(self):
        tested = ChangeEvent()
        tested.get_owned_constraints()
        pass

    def test_ChangeEvent_constraints_getter(self):
        tested = ChangeEvent()
        tested.get_constraints()
        pass

    def test_ChangeEvent_constraints_setter(self):
        tested = ChangeEvent()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_ChangeEvent_owned_property_values_getter(self):
        tested = ChangeEvent()
        tested.get_owned_property_values()
        pass

    def test_ChangeEvent_applied_property_values_getter(self):
        tested = ChangeEvent()
        tested.get_applied_property_values()
        pass

    def test_ChangeEvent_applied_property_values_setter(self):
        tested = ChangeEvent()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_ChangeEvent_owned_property_value_groups_getter(self):
        tested = ChangeEvent()
        tested.get_owned_property_value_groups()
        pass

    def test_ChangeEvent_applied_property_value_groups_getter(self):
        tested = ChangeEvent()
        tested.get_applied_property_value_groups()
        pass

    def test_ChangeEvent_applied_property_value_groups_setter(self):
        tested = ChangeEvent()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_ChangeEvent_owned_enumeration_property_types_getter(self):
        tested = ChangeEvent()
        tested.get_owned_enumeration_property_types()
        pass

    def test_ChangeEvent_owned_diagrams_getter(self):
        tested = ChangeEvent()
        tested.get_owned_diagrams()
        pass

    def test_ChangeEvent_element_of_interest_for_diagrams_getter(self):
        tested = ChangeEvent()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_ChangeEvent_element_of_interest_for_diagrams_setter(self):
        tested = ChangeEvent()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_ChangeEvent_contextual_element_for_diagrams_getter(self):
        tested = ChangeEvent()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_ChangeEvent_contextual_element_for_diagrams_setter(self):
        tested = ChangeEvent()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_ChangeEvent_representing_diagrams_getter(self):
        tested = ChangeEvent()
        tested.get_representing_diagrams()
        pass

    def test_ChangeEvent__r_e_cs_getter(self):
        tested = ChangeEvent()
        tested.get__r_e_cs()
        pass

    def test_ChangeEvent__r_e_cs_setter(self):
        tested = ChangeEvent()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_ChangeEvent__r_p_ls_getter(self):
        tested = ChangeEvent()
        tested.get__r_p_ls()
        pass

    def test_ChangeEvent__r_p_ls_setter(self):
        tested = ChangeEvent()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_ChangeEvent_get_label(self):
        tested = ChangeEvent()
        tested.get_label()
        pass

    def test_ChangeEvent_get_element_type(self):
        tested = ChangeEvent()
        tested.get_element_type()
        pass

    def test_ChangeEvent_get_container(self):
        tested = ChangeEvent()
        tested.get_container()
        pass

    def test_ChangeEvent_get_contents(self):
        tested = ChangeEvent()
        tested.get_contents()
        pass

    def test_ChangeEvent_get_all_contents(self):
        tested = ChangeEvent()
        tested.get_all_contents()
        pass

    def test_ChangeEvent_get_all_contents_by_type(self):
        tested = ChangeEvent()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_ChangeEvent_get_available_s_b_queries(self):
        tested = ChangeEvent()
        tested.get_available_s_b_queries()
        pass

    def test_ChangeEvent_get_query_result(self):
        tested = ChangeEvent()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_ChangeEvent_expression_getter(self):
        tested = ChangeEvent()
        tested.get_expression()
        pass

    def test_ChangeEvent_expression_setter(self):
        tested = ChangeEvent()
        value = "value"
        tested.set_expression(value)
        pass

    def test_TimeEvent_id_getter(self):
        tested = TimeEvent()
        tested.get_id()
        pass

    def test_TimeEvent_id_setter(self):
        tested = TimeEvent()
        value = "value"
        tested.set_id(value)
        pass

    def test_TimeEvent_sid_getter(self):
        tested = TimeEvent()
        tested.get_sid()
        pass

    def test_TimeEvent_sid_setter(self):
        tested = TimeEvent()
        value = "value"
        tested.set_sid(value)
        pass

    def test_TimeEvent_name_getter(self):
        tested = TimeEvent()
        tested.get_name()
        pass

    def test_TimeEvent_name_setter(self):
        tested = TimeEvent()
        value = "value"
        tested.set_name(value)
        pass

    def test_TimeEvent_summary_getter(self):
        tested = TimeEvent()
        tested.get_summary()
        pass

    def test_TimeEvent_summary_setter(self):
        tested = TimeEvent()
        value = "value"
        tested.set_summary(value)
        pass

    def test_TimeEvent_description_getter(self):
        tested = TimeEvent()
        tested.get_description()
        pass

    def test_TimeEvent_description_setter(self):
        tested = TimeEvent()
        value = "value"
        tested.set_description(value)
        pass

    def test_TimeEvent_status_getter(self):
        tested = TimeEvent()
        tested.get_status()
        pass

    def test_TimeEvent_status_setter(self):
        tested = TimeEvent()
        value = "value"
        tested.set_status(value)
        pass

    def test_TimeEvent_review_getter(self):
        tested = TimeEvent()
        tested.get_review()
        pass

    def test_TimeEvent_review_setter(self):
        tested = TimeEvent()
        value = "value"
        tested.set_review(value)
        pass

    def test_TimeEvent_visible_in_documentation_getter(self):
        tested = TimeEvent()
        tested.get_visible_in_documentation()
        pass

    def test_TimeEvent_visible_in_documentation_setter(self):
        tested = TimeEvent()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_TimeEvent_visible_for_traceability_getter(self):
        tested = TimeEvent()
        tested.get_visible_for_traceability()
        pass

    def test_TimeEvent_visible_for_traceability_setter(self):
        tested = TimeEvent()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_TimeEvent_owned_constraints_getter(self):
        tested = TimeEvent()
        tested.get_owned_constraints()
        pass

    def test_TimeEvent_constraints_getter(self):
        tested = TimeEvent()
        tested.get_constraints()
        pass

    def test_TimeEvent_constraints_setter(self):
        tested = TimeEvent()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_TimeEvent_owned_property_values_getter(self):
        tested = TimeEvent()
        tested.get_owned_property_values()
        pass

    def test_TimeEvent_applied_property_values_getter(self):
        tested = TimeEvent()
        tested.get_applied_property_values()
        pass

    def test_TimeEvent_applied_property_values_setter(self):
        tested = TimeEvent()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_TimeEvent_owned_property_value_groups_getter(self):
        tested = TimeEvent()
        tested.get_owned_property_value_groups()
        pass

    def test_TimeEvent_applied_property_value_groups_getter(self):
        tested = TimeEvent()
        tested.get_applied_property_value_groups()
        pass

    def test_TimeEvent_applied_property_value_groups_setter(self):
        tested = TimeEvent()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_TimeEvent_owned_enumeration_property_types_getter(self):
        tested = TimeEvent()
        tested.get_owned_enumeration_property_types()
        pass

    def test_TimeEvent_owned_diagrams_getter(self):
        tested = TimeEvent()
        tested.get_owned_diagrams()
        pass

    def test_TimeEvent_element_of_interest_for_diagrams_getter(self):
        tested = TimeEvent()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_TimeEvent_element_of_interest_for_diagrams_setter(self):
        tested = TimeEvent()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_TimeEvent_contextual_element_for_diagrams_getter(self):
        tested = TimeEvent()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_TimeEvent_contextual_element_for_diagrams_setter(self):
        tested = TimeEvent()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_TimeEvent_representing_diagrams_getter(self):
        tested = TimeEvent()
        tested.get_representing_diagrams()
        pass

    def test_TimeEvent__r_e_cs_getter(self):
        tested = TimeEvent()
        tested.get__r_e_cs()
        pass

    def test_TimeEvent__r_e_cs_setter(self):
        tested = TimeEvent()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_TimeEvent__r_p_ls_getter(self):
        tested = TimeEvent()
        tested.get__r_p_ls()
        pass

    def test_TimeEvent__r_p_ls_setter(self):
        tested = TimeEvent()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_TimeEvent_get_label(self):
        tested = TimeEvent()
        tested.get_label()
        pass

    def test_TimeEvent_get_element_type(self):
        tested = TimeEvent()
        tested.get_element_type()
        pass

    def test_TimeEvent_get_container(self):
        tested = TimeEvent()
        tested.get_container()
        pass

    def test_TimeEvent_get_contents(self):
        tested = TimeEvent()
        tested.get_contents()
        pass

    def test_TimeEvent_get_all_contents(self):
        tested = TimeEvent()
        tested.get_all_contents()
        pass

    def test_TimeEvent_get_all_contents_by_type(self):
        tested = TimeEvent()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_TimeEvent_get_available_s_b_queries(self):
        tested = TimeEvent()
        tested.get_available_s_b_queries()
        pass

    def test_TimeEvent_get_query_result(self):
        tested = TimeEvent()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_TimeEvent_kind_getter(self):
        tested = TimeEvent()
        tested.get_kind()
        pass

    def test_TimeEvent_kind_setter(self):
        tested = TimeEvent()
        value = TimeEventKind()
        tested.set_kind(value)
        pass

    def test_TimeEvent_expression_getter(self):
        tested = TimeEvent()
        tested.get_expression()
        pass

    def test_TimeEvent_expression_setter(self):
        tested = TimeEvent()
        value = "value"
        tested.set_expression(value)
        pass

    def test_Scenario_id_getter(self):
        tested = Scenario()
        tested.get_id()
        pass

    def test_Scenario_id_setter(self):
        tested = Scenario()
        value = "value"
        tested.set_id(value)
        pass

    def test_Scenario_sid_getter(self):
        tested = Scenario()
        tested.get_sid()
        pass

    def test_Scenario_sid_setter(self):
        tested = Scenario()
        value = "value"
        tested.set_sid(value)
        pass

    def test_Scenario_name_getter(self):
        tested = Scenario()
        tested.get_name()
        pass

    def test_Scenario_name_setter(self):
        tested = Scenario()
        value = "value"
        tested.set_name(value)
        pass

    def test_Scenario_summary_getter(self):
        tested = Scenario()
        tested.get_summary()
        pass

    def test_Scenario_summary_setter(self):
        tested = Scenario()
        value = "value"
        tested.set_summary(value)
        pass

    def test_Scenario_description_getter(self):
        tested = Scenario()
        tested.get_description()
        pass

    def test_Scenario_description_setter(self):
        tested = Scenario()
        value = "value"
        tested.set_description(value)
        pass

    def test_Scenario_status_getter(self):
        tested = Scenario()
        tested.get_status()
        pass

    def test_Scenario_status_setter(self):
        tested = Scenario()
        value = "value"
        tested.set_status(value)
        pass

    def test_Scenario_review_getter(self):
        tested = Scenario()
        tested.get_review()
        pass

    def test_Scenario_review_setter(self):
        tested = Scenario()
        value = "value"
        tested.set_review(value)
        pass

    def test_Scenario_visible_in_documentation_getter(self):
        tested = Scenario()
        tested.get_visible_in_documentation()
        pass

    def test_Scenario_visible_in_documentation_setter(self):
        tested = Scenario()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_Scenario_visible_for_traceability_getter(self):
        tested = Scenario()
        tested.get_visible_for_traceability()
        pass

    def test_Scenario_visible_for_traceability_setter(self):
        tested = Scenario()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_Scenario_owned_constraints_getter(self):
        tested = Scenario()
        tested.get_owned_constraints()
        pass

    def test_Scenario_constraints_getter(self):
        tested = Scenario()
        tested.get_constraints()
        pass

    def test_Scenario_constraints_setter(self):
        tested = Scenario()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_Scenario_owned_property_values_getter(self):
        tested = Scenario()
        tested.get_owned_property_values()
        pass

    def test_Scenario_applied_property_values_getter(self):
        tested = Scenario()
        tested.get_applied_property_values()
        pass

    def test_Scenario_applied_property_values_setter(self):
        tested = Scenario()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_Scenario_owned_property_value_groups_getter(self):
        tested = Scenario()
        tested.get_owned_property_value_groups()
        pass

    def test_Scenario_applied_property_value_groups_getter(self):
        tested = Scenario()
        tested.get_applied_property_value_groups()
        pass

    def test_Scenario_applied_property_value_groups_setter(self):
        tested = Scenario()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_Scenario_owned_enumeration_property_types_getter(self):
        tested = Scenario()
        tested.get_owned_enumeration_property_types()
        pass

    def test_Scenario_owned_diagrams_getter(self):
        tested = Scenario()
        tested.get_owned_diagrams()
        pass

    def test_Scenario_element_of_interest_for_diagrams_getter(self):
        tested = Scenario()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_Scenario_element_of_interest_for_diagrams_setter(self):
        tested = Scenario()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_Scenario_contextual_element_for_diagrams_getter(self):
        tested = Scenario()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_Scenario_contextual_element_for_diagrams_setter(self):
        tested = Scenario()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_Scenario_representing_diagrams_getter(self):
        tested = Scenario()
        tested.get_representing_diagrams()
        pass

    def test_Scenario__r_e_cs_getter(self):
        tested = Scenario()
        tested.get__r_e_cs()
        pass

    def test_Scenario__r_e_cs_setter(self):
        tested = Scenario()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_Scenario__r_p_ls_getter(self):
        tested = Scenario()
        tested.get__r_p_ls()
        pass

    def test_Scenario__r_p_ls_setter(self):
        tested = Scenario()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_Scenario_get_label(self):
        tested = Scenario()
        tested.get_label()
        pass

    def test_Scenario_get_element_type(self):
        tested = Scenario()
        tested.get_element_type()
        pass

    def test_Scenario_get_container(self):
        tested = Scenario()
        tested.get_container()
        pass

    def test_Scenario_get_contents(self):
        tested = Scenario()
        tested.get_contents()
        pass

    def test_Scenario_get_all_contents(self):
        tested = Scenario()
        tested.get_all_contents()
        pass

    def test_Scenario_get_all_contents_by_type(self):
        tested = Scenario()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_Scenario_get_available_s_b_queries(self):
        tested = Scenario()
        tested.get_available_s_b_queries()
        pass

    def test_Scenario_get_query_result(self):
        tested = Scenario()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_Scenario_kind_getter(self):
        tested = Scenario()
        tested.get_kind()
        pass

    def test_Scenario_pre_condition_getter(self):
        tested = Scenario()
        tested.get_pre_condition()
        pass

    def test_Scenario_pre_condition_setter(self):
        tested = Scenario()
        value = Constraint()
        tested.set_pre_condition(value)
        pass

    def test_Scenario_post_condition_getter(self):
        tested = Scenario()
        tested.get_post_condition()
        pass

    def test_Scenario_post_condition_setter(self):
        tested = Scenario()
        value = Constraint()
        tested.set_post_condition(value)
        pass

    def test_Scenario_owned_instance_roles_getter(self):
        tested = Scenario()
        tested.get_owned_instance_roles()
        pass

    def test_Scenario_owned_messages_getter(self):
        tested = Scenario()
        tested.get_owned_messages()
        pass

    def test_Scenario_owned_state_fragments_getter(self):
        tested = Scenario()
        tested.get_owned_state_fragments()
        pass

    def test_Scenario_owned_combined_fragments_getter(self):
        tested = Scenario()
        tested.get_owned_combined_fragments()
        pass

    def test_Scenario_owned_constraint_durations_getter(self):
        tested = Scenario()
        tested.get_owned_constraint_durations()
        pass

    def test_Scenario_referenced_scenarios_getter(self):
        tested = Scenario()
        tested.get_referenced_scenarios()
        pass

    def test_Scenario_realized_scenarios_getter(self):
        tested = Scenario()
        tested.get_realized_scenarios()
        pass

    def test_Scenario_realized_scenarios_setter(self):
        tested = Scenario()
        value = Scenario()
        tested.get_realized_scenarios().add(value)
        pass

    def test_Scenario_realizing_scenarios_getter(self):
        tested = Scenario()
        tested.get_realizing_scenarios()
        pass

    def test_Scenario_realizing_scenarios_setter(self):
        tested = Scenario()
        value = Scenario()
        tested.get_realizing_scenarios().add(value)
        pass

    def test_InstanceRole_id_getter(self):
        tested = InstanceRole()
        tested.get_id()
        pass

    def test_InstanceRole_id_setter(self):
        tested = InstanceRole()
        value = "value"
        tested.set_id(value)
        pass

    def test_InstanceRole_sid_getter(self):
        tested = InstanceRole()
        tested.get_sid()
        pass

    def test_InstanceRole_sid_setter(self):
        tested = InstanceRole()
        value = "value"
        tested.set_sid(value)
        pass

    def test_InstanceRole_name_getter(self):
        tested = InstanceRole()
        tested.get_name()
        pass

    def test_InstanceRole_name_setter(self):
        tested = InstanceRole()
        value = "value"
        tested.set_name(value)
        pass

    def test_InstanceRole_summary_getter(self):
        tested = InstanceRole()
        tested.get_summary()
        pass

    def test_InstanceRole_summary_setter(self):
        tested = InstanceRole()
        value = "value"
        tested.set_summary(value)
        pass

    def test_InstanceRole_description_getter(self):
        tested = InstanceRole()
        tested.get_description()
        pass

    def test_InstanceRole_description_setter(self):
        tested = InstanceRole()
        value = "value"
        tested.set_description(value)
        pass

    def test_InstanceRole_status_getter(self):
        tested = InstanceRole()
        tested.get_status()
        pass

    def test_InstanceRole_status_setter(self):
        tested = InstanceRole()
        value = "value"
        tested.set_status(value)
        pass

    def test_InstanceRole_review_getter(self):
        tested = InstanceRole()
        tested.get_review()
        pass

    def test_InstanceRole_review_setter(self):
        tested = InstanceRole()
        value = "value"
        tested.set_review(value)
        pass

    def test_InstanceRole_visible_in_documentation_getter(self):
        tested = InstanceRole()
        tested.get_visible_in_documentation()
        pass

    def test_InstanceRole_visible_in_documentation_setter(self):
        tested = InstanceRole()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_InstanceRole_visible_for_traceability_getter(self):
        tested = InstanceRole()
        tested.get_visible_for_traceability()
        pass

    def test_InstanceRole_visible_for_traceability_setter(self):
        tested = InstanceRole()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_InstanceRole_owned_constraints_getter(self):
        tested = InstanceRole()
        tested.get_owned_constraints()
        pass

    def test_InstanceRole_constraints_getter(self):
        tested = InstanceRole()
        tested.get_constraints()
        pass

    def test_InstanceRole_constraints_setter(self):
        tested = InstanceRole()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_InstanceRole_owned_property_values_getter(self):
        tested = InstanceRole()
        tested.get_owned_property_values()
        pass

    def test_InstanceRole_applied_property_values_getter(self):
        tested = InstanceRole()
        tested.get_applied_property_values()
        pass

    def test_InstanceRole_applied_property_values_setter(self):
        tested = InstanceRole()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_InstanceRole_owned_property_value_groups_getter(self):
        tested = InstanceRole()
        tested.get_owned_property_value_groups()
        pass

    def test_InstanceRole_applied_property_value_groups_getter(self):
        tested = InstanceRole()
        tested.get_applied_property_value_groups()
        pass

    def test_InstanceRole_applied_property_value_groups_setter(self):
        tested = InstanceRole()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_InstanceRole_owned_enumeration_property_types_getter(self):
        tested = InstanceRole()
        tested.get_owned_enumeration_property_types()
        pass

    def test_InstanceRole_owned_diagrams_getter(self):
        tested = InstanceRole()
        tested.get_owned_diagrams()
        pass

    def test_InstanceRole_element_of_interest_for_diagrams_getter(self):
        tested = InstanceRole()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_InstanceRole_element_of_interest_for_diagrams_setter(self):
        tested = InstanceRole()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_InstanceRole_contextual_element_for_diagrams_getter(self):
        tested = InstanceRole()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_InstanceRole_contextual_element_for_diagrams_setter(self):
        tested = InstanceRole()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_InstanceRole_representing_diagrams_getter(self):
        tested = InstanceRole()
        tested.get_representing_diagrams()
        pass

    def test_InstanceRole__r_e_cs_getter(self):
        tested = InstanceRole()
        tested.get__r_e_cs()
        pass

    def test_InstanceRole__r_e_cs_setter(self):
        tested = InstanceRole()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_InstanceRole__r_p_ls_getter(self):
        tested = InstanceRole()
        tested.get__r_p_ls()
        pass

    def test_InstanceRole__r_p_ls_setter(self):
        tested = InstanceRole()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_InstanceRole_get_label(self):
        tested = InstanceRole()
        tested.get_label()
        pass

    def test_InstanceRole_get_element_type(self):
        tested = InstanceRole()
        tested.get_element_type()
        pass

    def test_InstanceRole_get_container(self):
        tested = InstanceRole()
        tested.get_container()
        pass

    def test_InstanceRole_get_contents(self):
        tested = InstanceRole()
        tested.get_contents()
        pass

    def test_InstanceRole_get_all_contents(self):
        tested = InstanceRole()
        tested.get_all_contents()
        pass

    def test_InstanceRole_get_all_contents_by_type(self):
        tested = InstanceRole()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_InstanceRole_get_available_s_b_queries(self):
        tested = InstanceRole()
        tested.get_available_s_b_queries()
        pass

    def test_InstanceRole_get_query_result(self):
        tested = InstanceRole()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_InstanceRole_represented_instance_getter(self):
        tested = InstanceRole()
        tested.get_represented_instance()
        pass

    def test_SequenceMessage_id_getter(self):
        tested = SequenceMessage()
        tested.get_id()
        pass

    def test_SequenceMessage_id_setter(self):
        tested = SequenceMessage()
        value = "value"
        tested.set_id(value)
        pass

    def test_SequenceMessage_sid_getter(self):
        tested = SequenceMessage()
        tested.get_sid()
        pass

    def test_SequenceMessage_sid_setter(self):
        tested = SequenceMessage()
        value = "value"
        tested.set_sid(value)
        pass

    def test_SequenceMessage_name_getter(self):
        tested = SequenceMessage()
        tested.get_name()
        pass

    def test_SequenceMessage_name_setter(self):
        tested = SequenceMessage()
        value = "value"
        tested.set_name(value)
        pass

    def test_SequenceMessage_summary_getter(self):
        tested = SequenceMessage()
        tested.get_summary()
        pass

    def test_SequenceMessage_summary_setter(self):
        tested = SequenceMessage()
        value = "value"
        tested.set_summary(value)
        pass

    def test_SequenceMessage_description_getter(self):
        tested = SequenceMessage()
        tested.get_description()
        pass

    def test_SequenceMessage_description_setter(self):
        tested = SequenceMessage()
        value = "value"
        tested.set_description(value)
        pass

    def test_SequenceMessage_status_getter(self):
        tested = SequenceMessage()
        tested.get_status()
        pass

    def test_SequenceMessage_status_setter(self):
        tested = SequenceMessage()
        value = "value"
        tested.set_status(value)
        pass

    def test_SequenceMessage_review_getter(self):
        tested = SequenceMessage()
        tested.get_review()
        pass

    def test_SequenceMessage_review_setter(self):
        tested = SequenceMessage()
        value = "value"
        tested.set_review(value)
        pass

    def test_SequenceMessage_visible_in_documentation_getter(self):
        tested = SequenceMessage()
        tested.get_visible_in_documentation()
        pass

    def test_SequenceMessage_visible_in_documentation_setter(self):
        tested = SequenceMessage()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_SequenceMessage_visible_for_traceability_getter(self):
        tested = SequenceMessage()
        tested.get_visible_for_traceability()
        pass

    def test_SequenceMessage_visible_for_traceability_setter(self):
        tested = SequenceMessage()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_SequenceMessage_owned_constraints_getter(self):
        tested = SequenceMessage()
        tested.get_owned_constraints()
        pass

    def test_SequenceMessage_constraints_getter(self):
        tested = SequenceMessage()
        tested.get_constraints()
        pass

    def test_SequenceMessage_constraints_setter(self):
        tested = SequenceMessage()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_SequenceMessage_owned_property_values_getter(self):
        tested = SequenceMessage()
        tested.get_owned_property_values()
        pass

    def test_SequenceMessage_applied_property_values_getter(self):
        tested = SequenceMessage()
        tested.get_applied_property_values()
        pass

    def test_SequenceMessage_applied_property_values_setter(self):
        tested = SequenceMessage()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_SequenceMessage_owned_property_value_groups_getter(self):
        tested = SequenceMessage()
        tested.get_owned_property_value_groups()
        pass

    def test_SequenceMessage_applied_property_value_groups_getter(self):
        tested = SequenceMessage()
        tested.get_applied_property_value_groups()
        pass

    def test_SequenceMessage_applied_property_value_groups_setter(self):
        tested = SequenceMessage()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_SequenceMessage_owned_enumeration_property_types_getter(self):
        tested = SequenceMessage()
        tested.get_owned_enumeration_property_types()
        pass

    def test_SequenceMessage_owned_diagrams_getter(self):
        tested = SequenceMessage()
        tested.get_owned_diagrams()
        pass

    def test_SequenceMessage_element_of_interest_for_diagrams_getter(self):
        tested = SequenceMessage()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_SequenceMessage_element_of_interest_for_diagrams_setter(self):
        tested = SequenceMessage()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_SequenceMessage_contextual_element_for_diagrams_getter(self):
        tested = SequenceMessage()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_SequenceMessage_contextual_element_for_diagrams_setter(self):
        tested = SequenceMessage()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_SequenceMessage_representing_diagrams_getter(self):
        tested = SequenceMessage()
        tested.get_representing_diagrams()
        pass

    def test_SequenceMessage__r_e_cs_getter(self):
        tested = SequenceMessage()
        tested.get__r_e_cs()
        pass

    def test_SequenceMessage__r_e_cs_setter(self):
        tested = SequenceMessage()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_SequenceMessage__r_p_ls_getter(self):
        tested = SequenceMessage()
        tested.get__r_p_ls()
        pass

    def test_SequenceMessage__r_p_ls_setter(self):
        tested = SequenceMessage()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_SequenceMessage_get_label(self):
        tested = SequenceMessage()
        tested.get_label()
        pass

    def test_SequenceMessage_get_element_type(self):
        tested = SequenceMessage()
        tested.get_element_type()
        pass

    def test_SequenceMessage_get_container(self):
        tested = SequenceMessage()
        tested.get_container()
        pass

    def test_SequenceMessage_get_contents(self):
        tested = SequenceMessage()
        tested.get_contents()
        pass

    def test_SequenceMessage_get_all_contents(self):
        tested = SequenceMessage()
        tested.get_all_contents()
        pass

    def test_SequenceMessage_get_all_contents_by_type(self):
        tested = SequenceMessage()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_SequenceMessage_get_available_s_b_queries(self):
        tested = SequenceMessage()
        tested.get_available_s_b_queries()
        pass

    def test_SequenceMessage_get_query_result(self):
        tested = SequenceMessage()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_SequenceMessage_kind_getter(self):
        tested = SequenceMessage()
        tested.get_kind()
        pass

    def test_SequenceMessage_sending_instance_role_getter(self):
        tested = SequenceMessage()
        tested.get_sending_instance_role()
        pass

    def test_SequenceMessage_receiving_instance_role_getter(self):
        tested = SequenceMessage()
        tested.get_receiving_instance_role()
        pass

    def test_SequenceMessage_invoked_exchange_getter(self):
        tested = SequenceMessage()
        tested.get_invoked_exchange()
        pass

    def test_SequenceMessage_exchanged_items_getter(self):
        tested = SequenceMessage()
        tested.get_exchanged_items()
        pass

    def test_SequenceMessage_invoked_operation_getter(self):
        tested = SequenceMessage()
        tested.get_invoked_operation()
        pass

    def test_SequenceMessage_exchange_context_getter(self):
        tested = SequenceMessage()
        tested.get_exchange_context()
        pass

    def test_StateFragment_id_getter(self):
        tested = StateFragment()
        tested.get_id()
        pass

    def test_StateFragment_id_setter(self):
        tested = StateFragment()
        value = "value"
        tested.set_id(value)
        pass

    def test_StateFragment_sid_getter(self):
        tested = StateFragment()
        tested.get_sid()
        pass

    def test_StateFragment_sid_setter(self):
        tested = StateFragment()
        value = "value"
        tested.set_sid(value)
        pass

    def test_StateFragment_name_getter(self):
        tested = StateFragment()
        tested.get_name()
        pass

    def test_StateFragment_name_setter(self):
        tested = StateFragment()
        value = "value"
        tested.set_name(value)
        pass

    def test_StateFragment_summary_getter(self):
        tested = StateFragment()
        tested.get_summary()
        pass

    def test_StateFragment_summary_setter(self):
        tested = StateFragment()
        value = "value"
        tested.set_summary(value)
        pass

    def test_StateFragment_description_getter(self):
        tested = StateFragment()
        tested.get_description()
        pass

    def test_StateFragment_description_setter(self):
        tested = StateFragment()
        value = "value"
        tested.set_description(value)
        pass

    def test_StateFragment_status_getter(self):
        tested = StateFragment()
        tested.get_status()
        pass

    def test_StateFragment_status_setter(self):
        tested = StateFragment()
        value = "value"
        tested.set_status(value)
        pass

    def test_StateFragment_review_getter(self):
        tested = StateFragment()
        tested.get_review()
        pass

    def test_StateFragment_review_setter(self):
        tested = StateFragment()
        value = "value"
        tested.set_review(value)
        pass

    def test_StateFragment_visible_in_documentation_getter(self):
        tested = StateFragment()
        tested.get_visible_in_documentation()
        pass

    def test_StateFragment_visible_in_documentation_setter(self):
        tested = StateFragment()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_StateFragment_visible_for_traceability_getter(self):
        tested = StateFragment()
        tested.get_visible_for_traceability()
        pass

    def test_StateFragment_visible_for_traceability_setter(self):
        tested = StateFragment()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_StateFragment_owned_constraints_getter(self):
        tested = StateFragment()
        tested.get_owned_constraints()
        pass

    def test_StateFragment_constraints_getter(self):
        tested = StateFragment()
        tested.get_constraints()
        pass

    def test_StateFragment_constraints_setter(self):
        tested = StateFragment()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_StateFragment_owned_property_values_getter(self):
        tested = StateFragment()
        tested.get_owned_property_values()
        pass

    def test_StateFragment_applied_property_values_getter(self):
        tested = StateFragment()
        tested.get_applied_property_values()
        pass

    def test_StateFragment_applied_property_values_setter(self):
        tested = StateFragment()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_StateFragment_owned_property_value_groups_getter(self):
        tested = StateFragment()
        tested.get_owned_property_value_groups()
        pass

    def test_StateFragment_applied_property_value_groups_getter(self):
        tested = StateFragment()
        tested.get_applied_property_value_groups()
        pass

    def test_StateFragment_applied_property_value_groups_setter(self):
        tested = StateFragment()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_StateFragment_owned_enumeration_property_types_getter(self):
        tested = StateFragment()
        tested.get_owned_enumeration_property_types()
        pass

    def test_StateFragment_owned_diagrams_getter(self):
        tested = StateFragment()
        tested.get_owned_diagrams()
        pass

    def test_StateFragment_element_of_interest_for_diagrams_getter(self):
        tested = StateFragment()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_StateFragment_element_of_interest_for_diagrams_setter(self):
        tested = StateFragment()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_StateFragment_contextual_element_for_diagrams_getter(self):
        tested = StateFragment()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_StateFragment_contextual_element_for_diagrams_setter(self):
        tested = StateFragment()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_StateFragment_representing_diagrams_getter(self):
        tested = StateFragment()
        tested.get_representing_diagrams()
        pass

    def test_StateFragment__r_e_cs_getter(self):
        tested = StateFragment()
        tested.get__r_e_cs()
        pass

    def test_StateFragment__r_e_cs_setter(self):
        tested = StateFragment()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_StateFragment__r_p_ls_getter(self):
        tested = StateFragment()
        tested.get__r_p_ls()
        pass

    def test_StateFragment__r_p_ls_setter(self):
        tested = StateFragment()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_StateFragment_get_label(self):
        tested = StateFragment()
        tested.get_label()
        pass

    def test_StateFragment_get_element_type(self):
        tested = StateFragment()
        tested.get_element_type()
        pass

    def test_StateFragment_get_container(self):
        tested = StateFragment()
        tested.get_container()
        pass

    def test_StateFragment_get_contents(self):
        tested = StateFragment()
        tested.get_contents()
        pass

    def test_StateFragment_get_all_contents(self):
        tested = StateFragment()
        tested.get_all_contents()
        pass

    def test_StateFragment_get_all_contents_by_type(self):
        tested = StateFragment()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_StateFragment_get_available_s_b_queries(self):
        tested = StateFragment()
        tested.get_available_s_b_queries()
        pass

    def test_StateFragment_get_query_result(self):
        tested = StateFragment()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_StateFragment_covered_instance_role_getter(self):
        tested = StateFragment()
        tested.get_covered_instance_role()
        pass

    def test_StateFragment_related_state_getter(self):
        tested = StateFragment()
        tested.get_related_state()
        pass

    def test_StateFragment_related_activity_function_getter(self):
        tested = StateFragment()
        tested.get_related_activity_function()
        pass

    def test_CombinedFragment_id_getter(self):
        tested = CombinedFragment()
        tested.get_id()
        pass

    def test_CombinedFragment_id_setter(self):
        tested = CombinedFragment()
        value = "value"
        tested.set_id(value)
        pass

    def test_CombinedFragment_sid_getter(self):
        tested = CombinedFragment()
        tested.get_sid()
        pass

    def test_CombinedFragment_sid_setter(self):
        tested = CombinedFragment()
        value = "value"
        tested.set_sid(value)
        pass

    def test_CombinedFragment_name_getter(self):
        tested = CombinedFragment()
        tested.get_name()
        pass

    def test_CombinedFragment_name_setter(self):
        tested = CombinedFragment()
        value = "value"
        tested.set_name(value)
        pass

    def test_CombinedFragment_summary_getter(self):
        tested = CombinedFragment()
        tested.get_summary()
        pass

    def test_CombinedFragment_summary_setter(self):
        tested = CombinedFragment()
        value = "value"
        tested.set_summary(value)
        pass

    def test_CombinedFragment_description_getter(self):
        tested = CombinedFragment()
        tested.get_description()
        pass

    def test_CombinedFragment_description_setter(self):
        tested = CombinedFragment()
        value = "value"
        tested.set_description(value)
        pass

    def test_CombinedFragment_status_getter(self):
        tested = CombinedFragment()
        tested.get_status()
        pass

    def test_CombinedFragment_status_setter(self):
        tested = CombinedFragment()
        value = "value"
        tested.set_status(value)
        pass

    def test_CombinedFragment_review_getter(self):
        tested = CombinedFragment()
        tested.get_review()
        pass

    def test_CombinedFragment_review_setter(self):
        tested = CombinedFragment()
        value = "value"
        tested.set_review(value)
        pass

    def test_CombinedFragment_visible_in_documentation_getter(self):
        tested = CombinedFragment()
        tested.get_visible_in_documentation()
        pass

    def test_CombinedFragment_visible_in_documentation_setter(self):
        tested = CombinedFragment()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_CombinedFragment_visible_for_traceability_getter(self):
        tested = CombinedFragment()
        tested.get_visible_for_traceability()
        pass

    def test_CombinedFragment_visible_for_traceability_setter(self):
        tested = CombinedFragment()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_CombinedFragment_owned_constraints_getter(self):
        tested = CombinedFragment()
        tested.get_owned_constraints()
        pass

    def test_CombinedFragment_constraints_getter(self):
        tested = CombinedFragment()
        tested.get_constraints()
        pass

    def test_CombinedFragment_constraints_setter(self):
        tested = CombinedFragment()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_CombinedFragment_owned_property_values_getter(self):
        tested = CombinedFragment()
        tested.get_owned_property_values()
        pass

    def test_CombinedFragment_applied_property_values_getter(self):
        tested = CombinedFragment()
        tested.get_applied_property_values()
        pass

    def test_CombinedFragment_applied_property_values_setter(self):
        tested = CombinedFragment()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_CombinedFragment_owned_property_value_groups_getter(self):
        tested = CombinedFragment()
        tested.get_owned_property_value_groups()
        pass

    def test_CombinedFragment_applied_property_value_groups_getter(self):
        tested = CombinedFragment()
        tested.get_applied_property_value_groups()
        pass

    def test_CombinedFragment_applied_property_value_groups_setter(self):
        tested = CombinedFragment()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_CombinedFragment_owned_enumeration_property_types_getter(self):
        tested = CombinedFragment()
        tested.get_owned_enumeration_property_types()
        pass

    def test_CombinedFragment_owned_diagrams_getter(self):
        tested = CombinedFragment()
        tested.get_owned_diagrams()
        pass

    def test_CombinedFragment_element_of_interest_for_diagrams_getter(self):
        tested = CombinedFragment()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_CombinedFragment_element_of_interest_for_diagrams_setter(self):
        tested = CombinedFragment()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_CombinedFragment_contextual_element_for_diagrams_getter(self):
        tested = CombinedFragment()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_CombinedFragment_contextual_element_for_diagrams_setter(self):
        tested = CombinedFragment()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_CombinedFragment_representing_diagrams_getter(self):
        tested = CombinedFragment()
        tested.get_representing_diagrams()
        pass

    def test_CombinedFragment__r_e_cs_getter(self):
        tested = CombinedFragment()
        tested.get__r_e_cs()
        pass

    def test_CombinedFragment__r_e_cs_setter(self):
        tested = CombinedFragment()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_CombinedFragment__r_p_ls_getter(self):
        tested = CombinedFragment()
        tested.get__r_p_ls()
        pass

    def test_CombinedFragment__r_p_ls_setter(self):
        tested = CombinedFragment()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_CombinedFragment_get_label(self):
        tested = CombinedFragment()
        tested.get_label()
        pass

    def test_CombinedFragment_get_element_type(self):
        tested = CombinedFragment()
        tested.get_element_type()
        pass

    def test_CombinedFragment_get_container(self):
        tested = CombinedFragment()
        tested.get_container()
        pass

    def test_CombinedFragment_get_contents(self):
        tested = CombinedFragment()
        tested.get_contents()
        pass

    def test_CombinedFragment_get_all_contents(self):
        tested = CombinedFragment()
        tested.get_all_contents()
        pass

    def test_CombinedFragment_get_all_contents_by_type(self):
        tested = CombinedFragment()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_CombinedFragment_get_available_s_b_queries(self):
        tested = CombinedFragment()
        tested.get_available_s_b_queries()
        pass

    def test_CombinedFragment_get_query_result(self):
        tested = CombinedFragment()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_CombinedFragment_operator_getter(self):
        tested = CombinedFragment()
        tested.get_operator()
        pass

    def test_CombinedFragment_operands_getter(self):
        tested = CombinedFragment()
        tested.get_operands()
        pass

    def test_CombinedFragment_covered_instance_roles_getter(self):
        tested = CombinedFragment()
        tested.get_covered_instance_roles()
        pass

    def test_Operand_id_getter(self):
        tested = Operand()
        tested.get_id()
        pass

    def test_Operand_id_setter(self):
        tested = Operand()
        value = "value"
        tested.set_id(value)
        pass

    def test_Operand_sid_getter(self):
        tested = Operand()
        tested.get_sid()
        pass

    def test_Operand_sid_setter(self):
        tested = Operand()
        value = "value"
        tested.set_sid(value)
        pass

    def test_Operand_name_getter(self):
        tested = Operand()
        tested.get_name()
        pass

    def test_Operand_name_setter(self):
        tested = Operand()
        value = "value"
        tested.set_name(value)
        pass

    def test_Operand_summary_getter(self):
        tested = Operand()
        tested.get_summary()
        pass

    def test_Operand_summary_setter(self):
        tested = Operand()
        value = "value"
        tested.set_summary(value)
        pass

    def test_Operand_description_getter(self):
        tested = Operand()
        tested.get_description()
        pass

    def test_Operand_description_setter(self):
        tested = Operand()
        value = "value"
        tested.set_description(value)
        pass

    def test_Operand_status_getter(self):
        tested = Operand()
        tested.get_status()
        pass

    def test_Operand_status_setter(self):
        tested = Operand()
        value = "value"
        tested.set_status(value)
        pass

    def test_Operand_review_getter(self):
        tested = Operand()
        tested.get_review()
        pass

    def test_Operand_review_setter(self):
        tested = Operand()
        value = "value"
        tested.set_review(value)
        pass

    def test_Operand_visible_in_documentation_getter(self):
        tested = Operand()
        tested.get_visible_in_documentation()
        pass

    def test_Operand_visible_in_documentation_setter(self):
        tested = Operand()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_Operand_visible_for_traceability_getter(self):
        tested = Operand()
        tested.get_visible_for_traceability()
        pass

    def test_Operand_visible_for_traceability_setter(self):
        tested = Operand()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_Operand_owned_constraints_getter(self):
        tested = Operand()
        tested.get_owned_constraints()
        pass

    def test_Operand_constraints_getter(self):
        tested = Operand()
        tested.get_constraints()
        pass

    def test_Operand_constraints_setter(self):
        tested = Operand()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_Operand_owned_property_values_getter(self):
        tested = Operand()
        tested.get_owned_property_values()
        pass

    def test_Operand_applied_property_values_getter(self):
        tested = Operand()
        tested.get_applied_property_values()
        pass

    def test_Operand_applied_property_values_setter(self):
        tested = Operand()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_Operand_owned_property_value_groups_getter(self):
        tested = Operand()
        tested.get_owned_property_value_groups()
        pass

    def test_Operand_applied_property_value_groups_getter(self):
        tested = Operand()
        tested.get_applied_property_value_groups()
        pass

    def test_Operand_applied_property_value_groups_setter(self):
        tested = Operand()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_Operand_owned_enumeration_property_types_getter(self):
        tested = Operand()
        tested.get_owned_enumeration_property_types()
        pass

    def test_Operand_owned_diagrams_getter(self):
        tested = Operand()
        tested.get_owned_diagrams()
        pass

    def test_Operand_element_of_interest_for_diagrams_getter(self):
        tested = Operand()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_Operand_element_of_interest_for_diagrams_setter(self):
        tested = Operand()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_Operand_contextual_element_for_diagrams_getter(self):
        tested = Operand()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_Operand_contextual_element_for_diagrams_setter(self):
        tested = Operand()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_Operand_representing_diagrams_getter(self):
        tested = Operand()
        tested.get_representing_diagrams()
        pass

    def test_Operand__r_e_cs_getter(self):
        tested = Operand()
        tested.get__r_e_cs()
        pass

    def test_Operand__r_e_cs_setter(self):
        tested = Operand()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_Operand__r_p_ls_getter(self):
        tested = Operand()
        tested.get__r_p_ls()
        pass

    def test_Operand__r_p_ls_setter(self):
        tested = Operand()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_Operand_get_label(self):
        tested = Operand()
        tested.get_label()
        pass

    def test_Operand_get_element_type(self):
        tested = Operand()
        tested.get_element_type()
        pass

    def test_Operand_get_container(self):
        tested = Operand()
        tested.get_container()
        pass

    def test_Operand_get_contents(self):
        tested = Operand()
        tested.get_contents()
        pass

    def test_Operand_get_all_contents(self):
        tested = Operand()
        tested.get_all_contents()
        pass

    def test_Operand_get_all_contents_by_type(self):
        tested = Operand()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_Operand_get_available_s_b_queries(self):
        tested = Operand()
        tested.get_available_s_b_queries()
        pass

    def test_Operand_get_query_result(self):
        tested = Operand()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_Operand_guard_getter(self):
        tested = Operand()
        tested.get_guard()
        pass

    def test_Operand_guard_setter(self):
        tested = Operand()
        value = Constraint()
        tested.set_guard(value)
        pass

    def test_Operand_referenced_messages_getter(self):
        tested = Operand()
        tested.get_referenced_messages()
        pass

    def test_Operand_referenced_fragments_getter(self):
        tested = Operand()
        tested.get_referenced_fragments()
        pass

    def test_ConstraintDuration_id_getter(self):
        tested = ConstraintDuration()
        tested.get_id()
        pass

    def test_ConstraintDuration_id_setter(self):
        tested = ConstraintDuration()
        value = "value"
        tested.set_id(value)
        pass

    def test_ConstraintDuration_sid_getter(self):
        tested = ConstraintDuration()
        tested.get_sid()
        pass

    def test_ConstraintDuration_sid_setter(self):
        tested = ConstraintDuration()
        value = "value"
        tested.set_sid(value)
        pass

    def test_ConstraintDuration_name_getter(self):
        tested = ConstraintDuration()
        tested.get_name()
        pass

    def test_ConstraintDuration_name_setter(self):
        tested = ConstraintDuration()
        value = "value"
        tested.set_name(value)
        pass

    def test_ConstraintDuration_summary_getter(self):
        tested = ConstraintDuration()
        tested.get_summary()
        pass

    def test_ConstraintDuration_summary_setter(self):
        tested = ConstraintDuration()
        value = "value"
        tested.set_summary(value)
        pass

    def test_ConstraintDuration_description_getter(self):
        tested = ConstraintDuration()
        tested.get_description()
        pass

    def test_ConstraintDuration_description_setter(self):
        tested = ConstraintDuration()
        value = "value"
        tested.set_description(value)
        pass

    def test_ConstraintDuration_status_getter(self):
        tested = ConstraintDuration()
        tested.get_status()
        pass

    def test_ConstraintDuration_status_setter(self):
        tested = ConstraintDuration()
        value = "value"
        tested.set_status(value)
        pass

    def test_ConstraintDuration_review_getter(self):
        tested = ConstraintDuration()
        tested.get_review()
        pass

    def test_ConstraintDuration_review_setter(self):
        tested = ConstraintDuration()
        value = "value"
        tested.set_review(value)
        pass

    def test_ConstraintDuration_visible_in_documentation_getter(self):
        tested = ConstraintDuration()
        tested.get_visible_in_documentation()
        pass

    def test_ConstraintDuration_visible_in_documentation_setter(self):
        tested = ConstraintDuration()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_ConstraintDuration_visible_for_traceability_getter(self):
        tested = ConstraintDuration()
        tested.get_visible_for_traceability()
        pass

    def test_ConstraintDuration_visible_for_traceability_setter(self):
        tested = ConstraintDuration()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_ConstraintDuration_owned_constraints_getter(self):
        tested = ConstraintDuration()
        tested.get_owned_constraints()
        pass

    def test_ConstraintDuration_constraints_getter(self):
        tested = ConstraintDuration()
        tested.get_constraints()
        pass

    def test_ConstraintDuration_constraints_setter(self):
        tested = ConstraintDuration()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_ConstraintDuration_owned_property_values_getter(self):
        tested = ConstraintDuration()
        tested.get_owned_property_values()
        pass

    def test_ConstraintDuration_applied_property_values_getter(self):
        tested = ConstraintDuration()
        tested.get_applied_property_values()
        pass

    def test_ConstraintDuration_applied_property_values_setter(self):
        tested = ConstraintDuration()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_ConstraintDuration_owned_property_value_groups_getter(self):
        tested = ConstraintDuration()
        tested.get_owned_property_value_groups()
        pass

    def test_ConstraintDuration_applied_property_value_groups_getter(self):
        tested = ConstraintDuration()
        tested.get_applied_property_value_groups()
        pass

    def test_ConstraintDuration_applied_property_value_groups_setter(self):
        tested = ConstraintDuration()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_ConstraintDuration_owned_enumeration_property_types_getter(self):
        tested = ConstraintDuration()
        tested.get_owned_enumeration_property_types()
        pass

    def test_ConstraintDuration_owned_diagrams_getter(self):
        tested = ConstraintDuration()
        tested.get_owned_diagrams()
        pass

    def test_ConstraintDuration_element_of_interest_for_diagrams_getter(self):
        tested = ConstraintDuration()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_ConstraintDuration_element_of_interest_for_diagrams_setter(self):
        tested = ConstraintDuration()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_ConstraintDuration_contextual_element_for_diagrams_getter(self):
        tested = ConstraintDuration()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_ConstraintDuration_contextual_element_for_diagrams_setter(self):
        tested = ConstraintDuration()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_ConstraintDuration_representing_diagrams_getter(self):
        tested = ConstraintDuration()
        tested.get_representing_diagrams()
        pass

    def test_ConstraintDuration__r_e_cs_getter(self):
        tested = ConstraintDuration()
        tested.get__r_e_cs()
        pass

    def test_ConstraintDuration__r_e_cs_setter(self):
        tested = ConstraintDuration()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_ConstraintDuration__r_p_ls_getter(self):
        tested = ConstraintDuration()
        tested.get__r_p_ls()
        pass

    def test_ConstraintDuration__r_p_ls_setter(self):
        tested = ConstraintDuration()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_ConstraintDuration_get_label(self):
        tested = ConstraintDuration()
        tested.get_label()
        pass

    def test_ConstraintDuration_get_element_type(self):
        tested = ConstraintDuration()
        tested.get_element_type()
        pass

    def test_ConstraintDuration_get_container(self):
        tested = ConstraintDuration()
        tested.get_container()
        pass

    def test_ConstraintDuration_get_contents(self):
        tested = ConstraintDuration()
        tested.get_contents()
        pass

    def test_ConstraintDuration_get_all_contents(self):
        tested = ConstraintDuration()
        tested.get_all_contents()
        pass

    def test_ConstraintDuration_get_all_contents_by_type(self):
        tested = ConstraintDuration()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_ConstraintDuration_get_available_s_b_queries(self):
        tested = ConstraintDuration()
        tested.get_available_s_b_queries()
        pass

    def test_ConstraintDuration_get_query_result(self):
        tested = ConstraintDuration()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_ConstraintDuration_duration_getter(self):
        tested = ConstraintDuration()
        tested.get_duration()
        pass

    def test_ConstraintDuration_duration_setter(self):
        tested = ConstraintDuration()
        value = "value"
        tested.set_duration(value)
        pass

    def test_PhysicalPort_allocator_configuration_items_getter(self):
        tested = PhysicalPort()
        tested.get_allocator_configuration_items()
        pass

    def test_PhysicalPort_allocator_configuration_items_setter(self):
        tested = PhysicalPort()
        value = ConfigurationItem()
        tested.get_allocator_configuration_items().add(value)
        pass

    def test_PhysicalPort_id_getter(self):
        tested = PhysicalPort()
        tested.get_id()
        pass

    def test_PhysicalPort_id_setter(self):
        tested = PhysicalPort()
        value = "value"
        tested.set_id(value)
        pass

    def test_PhysicalPort_sid_getter(self):
        tested = PhysicalPort()
        tested.get_sid()
        pass

    def test_PhysicalPort_sid_setter(self):
        tested = PhysicalPort()
        value = "value"
        tested.set_sid(value)
        pass

    def test_PhysicalPort_name_getter(self):
        tested = PhysicalPort()
        tested.get_name()
        pass

    def test_PhysicalPort_name_setter(self):
        tested = PhysicalPort()
        value = "value"
        tested.set_name(value)
        pass

    def test_PhysicalPort_summary_getter(self):
        tested = PhysicalPort()
        tested.get_summary()
        pass

    def test_PhysicalPort_summary_setter(self):
        tested = PhysicalPort()
        value = "value"
        tested.set_summary(value)
        pass

    def test_PhysicalPort_description_getter(self):
        tested = PhysicalPort()
        tested.get_description()
        pass

    def test_PhysicalPort_description_setter(self):
        tested = PhysicalPort()
        value = "value"
        tested.set_description(value)
        pass

    def test_PhysicalPort_status_getter(self):
        tested = PhysicalPort()
        tested.get_status()
        pass

    def test_PhysicalPort_status_setter(self):
        tested = PhysicalPort()
        value = "value"
        tested.set_status(value)
        pass

    def test_PhysicalPort_review_getter(self):
        tested = PhysicalPort()
        tested.get_review()
        pass

    def test_PhysicalPort_review_setter(self):
        tested = PhysicalPort()
        value = "value"
        tested.set_review(value)
        pass

    def test_PhysicalPort_visible_in_documentation_getter(self):
        tested = PhysicalPort()
        tested.get_visible_in_documentation()
        pass

    def test_PhysicalPort_visible_in_documentation_setter(self):
        tested = PhysicalPort()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_PhysicalPort_visible_for_traceability_getter(self):
        tested = PhysicalPort()
        tested.get_visible_for_traceability()
        pass

    def test_PhysicalPort_visible_for_traceability_setter(self):
        tested = PhysicalPort()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_PhysicalPort_owned_constraints_getter(self):
        tested = PhysicalPort()
        tested.get_owned_constraints()
        pass

    def test_PhysicalPort_constraints_getter(self):
        tested = PhysicalPort()
        tested.get_constraints()
        pass

    def test_PhysicalPort_constraints_setter(self):
        tested = PhysicalPort()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_PhysicalPort_owned_property_values_getter(self):
        tested = PhysicalPort()
        tested.get_owned_property_values()
        pass

    def test_PhysicalPort_applied_property_values_getter(self):
        tested = PhysicalPort()
        tested.get_applied_property_values()
        pass

    def test_PhysicalPort_applied_property_values_setter(self):
        tested = PhysicalPort()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_PhysicalPort_owned_property_value_groups_getter(self):
        tested = PhysicalPort()
        tested.get_owned_property_value_groups()
        pass

    def test_PhysicalPort_applied_property_value_groups_getter(self):
        tested = PhysicalPort()
        tested.get_applied_property_value_groups()
        pass

    def test_PhysicalPort_applied_property_value_groups_setter(self):
        tested = PhysicalPort()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_PhysicalPort_owned_enumeration_property_types_getter(self):
        tested = PhysicalPort()
        tested.get_owned_enumeration_property_types()
        pass

    def test_PhysicalPort_owned_diagrams_getter(self):
        tested = PhysicalPort()
        tested.get_owned_diagrams()
        pass

    def test_PhysicalPort_element_of_interest_for_diagrams_getter(self):
        tested = PhysicalPort()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_PhysicalPort_element_of_interest_for_diagrams_setter(self):
        tested = PhysicalPort()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_PhysicalPort_contextual_element_for_diagrams_getter(self):
        tested = PhysicalPort()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_PhysicalPort_contextual_element_for_diagrams_setter(self):
        tested = PhysicalPort()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_PhysicalPort_representing_diagrams_getter(self):
        tested = PhysicalPort()
        tested.get_representing_diagrams()
        pass

    def test_PhysicalPort__r_e_cs_getter(self):
        tested = PhysicalPort()
        tested.get__r_e_cs()
        pass

    def test_PhysicalPort__r_e_cs_setter(self):
        tested = PhysicalPort()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_PhysicalPort__r_p_ls_getter(self):
        tested = PhysicalPort()
        tested.get__r_p_ls()
        pass

    def test_PhysicalPort__r_p_ls_setter(self):
        tested = PhysicalPort()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_PhysicalPort_get_label(self):
        tested = PhysicalPort()
        tested.get_label()
        pass

    def test_PhysicalPort_get_element_type(self):
        tested = PhysicalPort()
        tested.get_element_type()
        pass

    def test_PhysicalPort_get_container(self):
        tested = PhysicalPort()
        tested.get_container()
        pass

    def test_PhysicalPort_get_contents(self):
        tested = PhysicalPort()
        tested.get_contents()
        pass

    def test_PhysicalPort_get_all_contents(self):
        tested = PhysicalPort()
        tested.get_all_contents()
        pass

    def test_PhysicalPort_get_all_contents_by_type(self):
        tested = PhysicalPort()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_PhysicalPort_get_available_s_b_queries(self):
        tested = PhysicalPort()
        tested.get_available_s_b_queries()
        pass

    def test_PhysicalPort_get_query_result(self):
        tested = PhysicalPort()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_PhysicalPort_physical_links_getter(self):
        tested = PhysicalPort()
        tested.get_physical_links()
        pass

    def test_PhysicalPort_physical_links_setter(self):
        tested = PhysicalPort()
        value = PhysicalLink()
        tested.get_physical_links().add(value)
        pass

    def test_PhysicalPort_allocated_component_ports_getter(self):
        tested = PhysicalPort()
        tested.get_allocated_component_ports()
        pass

    def test_PhysicalPort_allocated_component_ports_setter(self):
        tested = PhysicalPort()
        value = ComponentPort()
        tested.get_allocated_component_ports().add(value)
        pass

    def test_PhysicalPort_realized_physical_ports_getter(self):
        tested = PhysicalPort()
        tested.get_realized_physical_ports()
        pass

    def test_PhysicalPort_realized_physical_ports_setter(self):
        tested = PhysicalPort()
        value = PhysicalPort()
        tested.get_realized_physical_ports().add(value)
        pass

    def test_PhysicalPort_realizing_physical_ports_getter(self):
        tested = PhysicalPort()
        tested.get_realizing_physical_ports()
        pass

    def test_PhysicalPort_realizing_physical_ports_setter(self):
        tested = PhysicalPort()
        value = PhysicalPort()
        tested.get_realizing_physical_ports().add(value)
        pass

    def test_PhysicalLink_allocator_configuration_items_getter(self):
        tested = PhysicalLink()
        tested.get_allocator_configuration_items()
        pass

    def test_PhysicalLink_allocator_configuration_items_setter(self):
        tested = PhysicalLink()
        value = ConfigurationItem()
        tested.get_allocator_configuration_items().add(value)
        pass

    def test_PhysicalLink_id_getter(self):
        tested = PhysicalLink()
        tested.get_id()
        pass

    def test_PhysicalLink_id_setter(self):
        tested = PhysicalLink()
        value = "value"
        tested.set_id(value)
        pass

    def test_PhysicalLink_sid_getter(self):
        tested = PhysicalLink()
        tested.get_sid()
        pass

    def test_PhysicalLink_sid_setter(self):
        tested = PhysicalLink()
        value = "value"
        tested.set_sid(value)
        pass

    def test_PhysicalLink_name_getter(self):
        tested = PhysicalLink()
        tested.get_name()
        pass

    def test_PhysicalLink_name_setter(self):
        tested = PhysicalLink()
        value = "value"
        tested.set_name(value)
        pass

    def test_PhysicalLink_summary_getter(self):
        tested = PhysicalLink()
        tested.get_summary()
        pass

    def test_PhysicalLink_summary_setter(self):
        tested = PhysicalLink()
        value = "value"
        tested.set_summary(value)
        pass

    def test_PhysicalLink_description_getter(self):
        tested = PhysicalLink()
        tested.get_description()
        pass

    def test_PhysicalLink_description_setter(self):
        tested = PhysicalLink()
        value = "value"
        tested.set_description(value)
        pass

    def test_PhysicalLink_status_getter(self):
        tested = PhysicalLink()
        tested.get_status()
        pass

    def test_PhysicalLink_status_setter(self):
        tested = PhysicalLink()
        value = "value"
        tested.set_status(value)
        pass

    def test_PhysicalLink_review_getter(self):
        tested = PhysicalLink()
        tested.get_review()
        pass

    def test_PhysicalLink_review_setter(self):
        tested = PhysicalLink()
        value = "value"
        tested.set_review(value)
        pass

    def test_PhysicalLink_visible_in_documentation_getter(self):
        tested = PhysicalLink()
        tested.get_visible_in_documentation()
        pass

    def test_PhysicalLink_visible_in_documentation_setter(self):
        tested = PhysicalLink()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_PhysicalLink_visible_for_traceability_getter(self):
        tested = PhysicalLink()
        tested.get_visible_for_traceability()
        pass

    def test_PhysicalLink_visible_for_traceability_setter(self):
        tested = PhysicalLink()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_PhysicalLink_owned_constraints_getter(self):
        tested = PhysicalLink()
        tested.get_owned_constraints()
        pass

    def test_PhysicalLink_constraints_getter(self):
        tested = PhysicalLink()
        tested.get_constraints()
        pass

    def test_PhysicalLink_constraints_setter(self):
        tested = PhysicalLink()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_PhysicalLink_owned_property_values_getter(self):
        tested = PhysicalLink()
        tested.get_owned_property_values()
        pass

    def test_PhysicalLink_applied_property_values_getter(self):
        tested = PhysicalLink()
        tested.get_applied_property_values()
        pass

    def test_PhysicalLink_applied_property_values_setter(self):
        tested = PhysicalLink()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_PhysicalLink_owned_property_value_groups_getter(self):
        tested = PhysicalLink()
        tested.get_owned_property_value_groups()
        pass

    def test_PhysicalLink_applied_property_value_groups_getter(self):
        tested = PhysicalLink()
        tested.get_applied_property_value_groups()
        pass

    def test_PhysicalLink_applied_property_value_groups_setter(self):
        tested = PhysicalLink()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_PhysicalLink_owned_enumeration_property_types_getter(self):
        tested = PhysicalLink()
        tested.get_owned_enumeration_property_types()
        pass

    def test_PhysicalLink_owned_diagrams_getter(self):
        tested = PhysicalLink()
        tested.get_owned_diagrams()
        pass

    def test_PhysicalLink_element_of_interest_for_diagrams_getter(self):
        tested = PhysicalLink()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_PhysicalLink_element_of_interest_for_diagrams_setter(self):
        tested = PhysicalLink()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_PhysicalLink_contextual_element_for_diagrams_getter(self):
        tested = PhysicalLink()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_PhysicalLink_contextual_element_for_diagrams_setter(self):
        tested = PhysicalLink()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_PhysicalLink_representing_diagrams_getter(self):
        tested = PhysicalLink()
        tested.get_representing_diagrams()
        pass

    def test_PhysicalLink__r_e_cs_getter(self):
        tested = PhysicalLink()
        tested.get__r_e_cs()
        pass

    def test_PhysicalLink__r_e_cs_setter(self):
        tested = PhysicalLink()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_PhysicalLink__r_p_ls_getter(self):
        tested = PhysicalLink()
        tested.get__r_p_ls()
        pass

    def test_PhysicalLink__r_p_ls_setter(self):
        tested = PhysicalLink()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_PhysicalLink_get_label(self):
        tested = PhysicalLink()
        tested.get_label()
        pass

    def test_PhysicalLink_get_element_type(self):
        tested = PhysicalLink()
        tested.get_element_type()
        pass

    def test_PhysicalLink_get_container(self):
        tested = PhysicalLink()
        tested.get_container()
        pass

    def test_PhysicalLink_get_contents(self):
        tested = PhysicalLink()
        tested.get_contents()
        pass

    def test_PhysicalLink_get_all_contents(self):
        tested = PhysicalLink()
        tested.get_all_contents()
        pass

    def test_PhysicalLink_get_all_contents_by_type(self):
        tested = PhysicalLink()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_PhysicalLink_get_available_s_b_queries(self):
        tested = PhysicalLink()
        tested.get_available_s_b_queries()
        pass

    def test_PhysicalLink_get_query_result(self):
        tested = PhysicalLink()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_PhysicalLink_connected_physical_ports_getter(self):
        tested = PhysicalLink()
        tested.get_connected_physical_ports()
        pass

    def test_PhysicalLink_connected_physical_ports_setter(self):
        tested = PhysicalLink()
        value = PhysicalPort()
        tested.get_connected_physical_ports().add(value)
        pass

    def test_PhysicalLink_categories_getter(self):
        tested = PhysicalLink()
        tested.get_categories()
        pass

    def test_PhysicalLink_categories_setter(self):
        tested = PhysicalLink()
        value = PhysicalLinkCategory()
        tested.get_categories().add(value)
        pass

    def test_PhysicalLink_involving_physical_paths_getter(self):
        tested = PhysicalLink()
        tested.get_involving_physical_paths()
        pass

    def test_PhysicalLink_connected_components_getter(self):
        tested = PhysicalLink()
        tested.get_connected_components()
        pass

    def test_PhysicalLink_connected_components_setter(self):
        tested = PhysicalLink()
        value = PhysicalActor()
        tested.get_connected_components().add(value)
        pass

    def test_PhysicalLink_allocated_component_exchanges_getter(self):
        tested = PhysicalLink()
        tested.get_allocated_component_exchanges()
        pass

    def test_PhysicalLink_allocated_component_exchanges_setter(self):
        tested = PhysicalLink()
        value = ComponentExchange()
        tested.get_allocated_component_exchanges().add(value)
        pass

    def test_PhysicalLink_realized_physical_links_getter(self):
        tested = PhysicalLink()
        tested.get_realized_physical_links()
        pass

    def test_PhysicalLink_realized_physical_links_setter(self):
        tested = PhysicalLink()
        value = PhysicalLink()
        tested.get_realized_physical_links().add(value)
        pass

    def test_PhysicalLink_realizing_physical_links_getter(self):
        tested = PhysicalLink()
        tested.get_realizing_physical_links()
        pass

    def test_PhysicalLink_realizing_physical_links_setter(self):
        tested = PhysicalLink()
        value = PhysicalLink()
        tested.get_realizing_physical_links().add(value)
        pass

    def test_PhysicalLinkCategory_id_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_id()
        pass

    def test_PhysicalLinkCategory_id_setter(self):
        tested = PhysicalLinkCategory()
        value = "value"
        tested.set_id(value)
        pass

    def test_PhysicalLinkCategory_sid_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_sid()
        pass

    def test_PhysicalLinkCategory_sid_setter(self):
        tested = PhysicalLinkCategory()
        value = "value"
        tested.set_sid(value)
        pass

    def test_PhysicalLinkCategory_name_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_name()
        pass

    def test_PhysicalLinkCategory_name_setter(self):
        tested = PhysicalLinkCategory()
        value = "value"
        tested.set_name(value)
        pass

    def test_PhysicalLinkCategory_summary_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_summary()
        pass

    def test_PhysicalLinkCategory_summary_setter(self):
        tested = PhysicalLinkCategory()
        value = "value"
        tested.set_summary(value)
        pass

    def test_PhysicalLinkCategory_description_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_description()
        pass

    def test_PhysicalLinkCategory_description_setter(self):
        tested = PhysicalLinkCategory()
        value = "value"
        tested.set_description(value)
        pass

    def test_PhysicalLinkCategory_status_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_status()
        pass

    def test_PhysicalLinkCategory_status_setter(self):
        tested = PhysicalLinkCategory()
        value = "value"
        tested.set_status(value)
        pass

    def test_PhysicalLinkCategory_review_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_review()
        pass

    def test_PhysicalLinkCategory_review_setter(self):
        tested = PhysicalLinkCategory()
        value = "value"
        tested.set_review(value)
        pass

    def test_PhysicalLinkCategory_visible_in_documentation_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_visible_in_documentation()
        pass

    def test_PhysicalLinkCategory_visible_in_documentation_setter(self):
        tested = PhysicalLinkCategory()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_PhysicalLinkCategory_visible_for_traceability_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_visible_for_traceability()
        pass

    def test_PhysicalLinkCategory_visible_for_traceability_setter(self):
        tested = PhysicalLinkCategory()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_PhysicalLinkCategory_owned_constraints_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_owned_constraints()
        pass

    def test_PhysicalLinkCategory_constraints_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_constraints()
        pass

    def test_PhysicalLinkCategory_constraints_setter(self):
        tested = PhysicalLinkCategory()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_PhysicalLinkCategory_owned_property_values_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_owned_property_values()
        pass

    def test_PhysicalLinkCategory_applied_property_values_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_applied_property_values()
        pass

    def test_PhysicalLinkCategory_applied_property_values_setter(self):
        tested = PhysicalLinkCategory()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_PhysicalLinkCategory_owned_property_value_groups_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_owned_property_value_groups()
        pass

    def test_PhysicalLinkCategory_applied_property_value_groups_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_applied_property_value_groups()
        pass

    def test_PhysicalLinkCategory_applied_property_value_groups_setter(self):
        tested = PhysicalLinkCategory()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_PhysicalLinkCategory_owned_enumeration_property_types_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_owned_enumeration_property_types()
        pass

    def test_PhysicalLinkCategory_owned_diagrams_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_owned_diagrams()
        pass

    def test_PhysicalLinkCategory_element_of_interest_for_diagrams_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_PhysicalLinkCategory_element_of_interest_for_diagrams_setter(self):
        tested = PhysicalLinkCategory()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_PhysicalLinkCategory_contextual_element_for_diagrams_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_PhysicalLinkCategory_contextual_element_for_diagrams_setter(self):
        tested = PhysicalLinkCategory()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_PhysicalLinkCategory_representing_diagrams_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_representing_diagrams()
        pass

    def test_PhysicalLinkCategory__r_e_cs_getter(self):
        tested = PhysicalLinkCategory()
        tested.get__r_e_cs()
        pass

    def test_PhysicalLinkCategory__r_e_cs_setter(self):
        tested = PhysicalLinkCategory()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_PhysicalLinkCategory__r_p_ls_getter(self):
        tested = PhysicalLinkCategory()
        tested.get__r_p_ls()
        pass

    def test_PhysicalLinkCategory__r_p_ls_setter(self):
        tested = PhysicalLinkCategory()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_PhysicalLinkCategory_get_label(self):
        tested = PhysicalLinkCategory()
        tested.get_label()
        pass

    def test_PhysicalLinkCategory_get_element_type(self):
        tested = PhysicalLinkCategory()
        tested.get_element_type()
        pass

    def test_PhysicalLinkCategory_get_container(self):
        tested = PhysicalLinkCategory()
        tested.get_container()
        pass

    def test_PhysicalLinkCategory_get_contents(self):
        tested = PhysicalLinkCategory()
        tested.get_contents()
        pass

    def test_PhysicalLinkCategory_get_all_contents(self):
        tested = PhysicalLinkCategory()
        tested.get_all_contents()
        pass

    def test_PhysicalLinkCategory_get_all_contents_by_type(self):
        tested = PhysicalLinkCategory()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_PhysicalLinkCategory_get_available_s_b_queries(self):
        tested = PhysicalLinkCategory()
        tested.get_available_s_b_queries()
        pass

    def test_PhysicalLinkCategory_get_query_result(self):
        tested = PhysicalLinkCategory()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_PhysicalLinkCategory_links_getter(self):
        tested = PhysicalLinkCategory()
        tested.get_links()
        pass

    def test_PhysicalLinkCategory_links_setter(self):
        tested = PhysicalLinkCategory()
        value = PhysicalLink()
        tested.get_links().add(value)
        pass

    def test_PhysicalPath_id_getter(self):
        tested = PhysicalPath()
        tested.get_id()
        pass

    def test_PhysicalPath_id_setter(self):
        tested = PhysicalPath()
        value = "value"
        tested.set_id(value)
        pass

    def test_PhysicalPath_sid_getter(self):
        tested = PhysicalPath()
        tested.get_sid()
        pass

    def test_PhysicalPath_sid_setter(self):
        tested = PhysicalPath()
        value = "value"
        tested.set_sid(value)
        pass

    def test_PhysicalPath_name_getter(self):
        tested = PhysicalPath()
        tested.get_name()
        pass

    def test_PhysicalPath_name_setter(self):
        tested = PhysicalPath()
        value = "value"
        tested.set_name(value)
        pass

    def test_PhysicalPath_summary_getter(self):
        tested = PhysicalPath()
        tested.get_summary()
        pass

    def test_PhysicalPath_summary_setter(self):
        tested = PhysicalPath()
        value = "value"
        tested.set_summary(value)
        pass

    def test_PhysicalPath_description_getter(self):
        tested = PhysicalPath()
        tested.get_description()
        pass

    def test_PhysicalPath_description_setter(self):
        tested = PhysicalPath()
        value = "value"
        tested.set_description(value)
        pass

    def test_PhysicalPath_status_getter(self):
        tested = PhysicalPath()
        tested.get_status()
        pass

    def test_PhysicalPath_status_setter(self):
        tested = PhysicalPath()
        value = "value"
        tested.set_status(value)
        pass

    def test_PhysicalPath_review_getter(self):
        tested = PhysicalPath()
        tested.get_review()
        pass

    def test_PhysicalPath_review_setter(self):
        tested = PhysicalPath()
        value = "value"
        tested.set_review(value)
        pass

    def test_PhysicalPath_visible_in_documentation_getter(self):
        tested = PhysicalPath()
        tested.get_visible_in_documentation()
        pass

    def test_PhysicalPath_visible_in_documentation_setter(self):
        tested = PhysicalPath()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_PhysicalPath_visible_for_traceability_getter(self):
        tested = PhysicalPath()
        tested.get_visible_for_traceability()
        pass

    def test_PhysicalPath_visible_for_traceability_setter(self):
        tested = PhysicalPath()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_PhysicalPath_owned_constraints_getter(self):
        tested = PhysicalPath()
        tested.get_owned_constraints()
        pass

    def test_PhysicalPath_constraints_getter(self):
        tested = PhysicalPath()
        tested.get_constraints()
        pass

    def test_PhysicalPath_constraints_setter(self):
        tested = PhysicalPath()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_PhysicalPath_owned_property_values_getter(self):
        tested = PhysicalPath()
        tested.get_owned_property_values()
        pass

    def test_PhysicalPath_applied_property_values_getter(self):
        tested = PhysicalPath()
        tested.get_applied_property_values()
        pass

    def test_PhysicalPath_applied_property_values_setter(self):
        tested = PhysicalPath()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_PhysicalPath_owned_property_value_groups_getter(self):
        tested = PhysicalPath()
        tested.get_owned_property_value_groups()
        pass

    def test_PhysicalPath_applied_property_value_groups_getter(self):
        tested = PhysicalPath()
        tested.get_applied_property_value_groups()
        pass

    def test_PhysicalPath_applied_property_value_groups_setter(self):
        tested = PhysicalPath()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_PhysicalPath_owned_enumeration_property_types_getter(self):
        tested = PhysicalPath()
        tested.get_owned_enumeration_property_types()
        pass

    def test_PhysicalPath_owned_diagrams_getter(self):
        tested = PhysicalPath()
        tested.get_owned_diagrams()
        pass

    def test_PhysicalPath_element_of_interest_for_diagrams_getter(self):
        tested = PhysicalPath()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_PhysicalPath_element_of_interest_for_diagrams_setter(self):
        tested = PhysicalPath()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_PhysicalPath_contextual_element_for_diagrams_getter(self):
        tested = PhysicalPath()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_PhysicalPath_contextual_element_for_diagrams_setter(self):
        tested = PhysicalPath()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_PhysicalPath_representing_diagrams_getter(self):
        tested = PhysicalPath()
        tested.get_representing_diagrams()
        pass

    def test_PhysicalPath__r_e_cs_getter(self):
        tested = PhysicalPath()
        tested.get__r_e_cs()
        pass

    def test_PhysicalPath__r_e_cs_setter(self):
        tested = PhysicalPath()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_PhysicalPath__r_p_ls_getter(self):
        tested = PhysicalPath()
        tested.get__r_p_ls()
        pass

    def test_PhysicalPath__r_p_ls_setter(self):
        tested = PhysicalPath()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_PhysicalPath_get_label(self):
        tested = PhysicalPath()
        tested.get_label()
        pass

    def test_PhysicalPath_get_element_type(self):
        tested = PhysicalPath()
        tested.get_element_type()
        pass

    def test_PhysicalPath_get_container(self):
        tested = PhysicalPath()
        tested.get_container()
        pass

    def test_PhysicalPath_get_contents(self):
        tested = PhysicalPath()
        tested.get_contents()
        pass

    def test_PhysicalPath_get_all_contents(self):
        tested = PhysicalPath()
        tested.get_all_contents()
        pass

    def test_PhysicalPath_get_all_contents_by_type(self):
        tested = PhysicalPath()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_PhysicalPath_get_available_s_b_queries(self):
        tested = PhysicalPath()
        tested.get_available_s_b_queries()
        pass

    def test_PhysicalPath_get_query_result(self):
        tested = PhysicalPath()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_PhysicalPath_involved_physical_links_getter(self):
        tested = PhysicalPath()
        tested.get_involved_physical_links()
        pass

    def test_PhysicalPath_involved_node_p_cs_getter(self):
        tested = PhysicalPath()
        tested.get_involved_node_p_cs()
        pass

    def test_PhysicalPath_allocated_component_exchanges_getter(self):
        tested = PhysicalPath()
        tested.get_allocated_component_exchanges()
        pass

    def test_PhysicalPath_allocated_component_exchanges_setter(self):
        tested = PhysicalPath()
        value = ComponentExchange()
        tested.get_allocated_component_exchanges().add(value)
        pass

    def test_PhysicalPath_realized_physical_paths_getter(self):
        tested = PhysicalPath()
        tested.get_realized_physical_paths()
        pass

    def test_PhysicalPath_realized_physical_paths_setter(self):
        tested = PhysicalPath()
        value = PhysicalPath()
        tested.get_realized_physical_paths().add(value)
        pass

    def test_PhysicalPath_realizing_physical_paths_getter(self):
        tested = PhysicalPath()
        tested.get_realizing_physical_paths()
        pass

    def test_PhysicalPath_realizing_physical_paths_setter(self):
        tested = PhysicalPath()
        value = PhysicalPath()
        tested.get_realizing_physical_paths().add(value)
        pass

    def test_InterfacePkg_owned_property_value_pkgs_getter(self):
        tested = InterfacePkg()
        tested.get_owned_property_value_pkgs()
        pass

    def test_InterfacePkg_id_getter(self):
        tested = InterfacePkg()
        tested.get_id()
        pass

    def test_InterfacePkg_id_setter(self):
        tested = InterfacePkg()
        value = "value"
        tested.set_id(value)
        pass

    def test_InterfacePkg_sid_getter(self):
        tested = InterfacePkg()
        tested.get_sid()
        pass

    def test_InterfacePkg_sid_setter(self):
        tested = InterfacePkg()
        value = "value"
        tested.set_sid(value)
        pass

    def test_InterfacePkg_name_getter(self):
        tested = InterfacePkg()
        tested.get_name()
        pass

    def test_InterfacePkg_name_setter(self):
        tested = InterfacePkg()
        value = "value"
        tested.set_name(value)
        pass

    def test_InterfacePkg_summary_getter(self):
        tested = InterfacePkg()
        tested.get_summary()
        pass

    def test_InterfacePkg_summary_setter(self):
        tested = InterfacePkg()
        value = "value"
        tested.set_summary(value)
        pass

    def test_InterfacePkg_description_getter(self):
        tested = InterfacePkg()
        tested.get_description()
        pass

    def test_InterfacePkg_description_setter(self):
        tested = InterfacePkg()
        value = "value"
        tested.set_description(value)
        pass

    def test_InterfacePkg_status_getter(self):
        tested = InterfacePkg()
        tested.get_status()
        pass

    def test_InterfacePkg_status_setter(self):
        tested = InterfacePkg()
        value = "value"
        tested.set_status(value)
        pass

    def test_InterfacePkg_review_getter(self):
        tested = InterfacePkg()
        tested.get_review()
        pass

    def test_InterfacePkg_review_setter(self):
        tested = InterfacePkg()
        value = "value"
        tested.set_review(value)
        pass

    def test_InterfacePkg_visible_in_documentation_getter(self):
        tested = InterfacePkg()
        tested.get_visible_in_documentation()
        pass

    def test_InterfacePkg_visible_in_documentation_setter(self):
        tested = InterfacePkg()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_InterfacePkg_visible_for_traceability_getter(self):
        tested = InterfacePkg()
        tested.get_visible_for_traceability()
        pass

    def test_InterfacePkg_visible_for_traceability_setter(self):
        tested = InterfacePkg()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_InterfacePkg_owned_constraints_getter(self):
        tested = InterfacePkg()
        tested.get_owned_constraints()
        pass

    def test_InterfacePkg_constraints_getter(self):
        tested = InterfacePkg()
        tested.get_constraints()
        pass

    def test_InterfacePkg_constraints_setter(self):
        tested = InterfacePkg()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_InterfacePkg_owned_property_values_getter(self):
        tested = InterfacePkg()
        tested.get_owned_property_values()
        pass

    def test_InterfacePkg_applied_property_values_getter(self):
        tested = InterfacePkg()
        tested.get_applied_property_values()
        pass

    def test_InterfacePkg_applied_property_values_setter(self):
        tested = InterfacePkg()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_InterfacePkg_owned_property_value_groups_getter(self):
        tested = InterfacePkg()
        tested.get_owned_property_value_groups()
        pass

    def test_InterfacePkg_applied_property_value_groups_getter(self):
        tested = InterfacePkg()
        tested.get_applied_property_value_groups()
        pass

    def test_InterfacePkg_applied_property_value_groups_setter(self):
        tested = InterfacePkg()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_InterfacePkg_owned_enumeration_property_types_getter(self):
        tested = InterfacePkg()
        tested.get_owned_enumeration_property_types()
        pass

    def test_InterfacePkg_owned_diagrams_getter(self):
        tested = InterfacePkg()
        tested.get_owned_diagrams()
        pass

    def test_InterfacePkg_element_of_interest_for_diagrams_getter(self):
        tested = InterfacePkg()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_InterfacePkg_element_of_interest_for_diagrams_setter(self):
        tested = InterfacePkg()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_InterfacePkg_contextual_element_for_diagrams_getter(self):
        tested = InterfacePkg()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_InterfacePkg_contextual_element_for_diagrams_setter(self):
        tested = InterfacePkg()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_InterfacePkg_representing_diagrams_getter(self):
        tested = InterfacePkg()
        tested.get_representing_diagrams()
        pass

    def test_InterfacePkg__r_e_cs_getter(self):
        tested = InterfacePkg()
        tested.get__r_e_cs()
        pass

    def test_InterfacePkg__r_e_cs_setter(self):
        tested = InterfacePkg()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_InterfacePkg__r_p_ls_getter(self):
        tested = InterfacePkg()
        tested.get__r_p_ls()
        pass

    def test_InterfacePkg__r_p_ls_setter(self):
        tested = InterfacePkg()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_InterfacePkg_get_label(self):
        tested = InterfacePkg()
        tested.get_label()
        pass

    def test_InterfacePkg_get_element_type(self):
        tested = InterfacePkg()
        tested.get_element_type()
        pass

    def test_InterfacePkg_get_container(self):
        tested = InterfacePkg()
        tested.get_container()
        pass

    def test_InterfacePkg_get_contents(self):
        tested = InterfacePkg()
        tested.get_contents()
        pass

    def test_InterfacePkg_get_all_contents(self):
        tested = InterfacePkg()
        tested.get_all_contents()
        pass

    def test_InterfacePkg_get_all_contents_by_type(self):
        tested = InterfacePkg()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_InterfacePkg_get_available_s_b_queries(self):
        tested = InterfacePkg()
        tested.get_available_s_b_queries()
        pass

    def test_InterfacePkg_get_query_result(self):
        tested = InterfacePkg()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_InterfacePkg_owned_interface_pkgs_getter(self):
        tested = InterfacePkg()
        tested.get_owned_interface_pkgs()
        pass

    def test_InterfacePkg_owned_interfaces_getter(self):
        tested = InterfacePkg()
        tested.get_owned_interfaces()
        pass

    def test_InterfacePkg_owned_exchange_items_getter(self):
        tested = InterfacePkg()
        tested.get_owned_exchange_items()
        pass

    def test_Interface_id_getter(self):
        tested = Interface()
        tested.get_id()
        pass

    def test_Interface_id_setter(self):
        tested = Interface()
        value = "value"
        tested.set_id(value)
        pass

    def test_Interface_sid_getter(self):
        tested = Interface()
        tested.get_sid()
        pass

    def test_Interface_sid_setter(self):
        tested = Interface()
        value = "value"
        tested.set_sid(value)
        pass

    def test_Interface_name_getter(self):
        tested = Interface()
        tested.get_name()
        pass

    def test_Interface_name_setter(self):
        tested = Interface()
        value = "value"
        tested.set_name(value)
        pass

    def test_Interface_summary_getter(self):
        tested = Interface()
        tested.get_summary()
        pass

    def test_Interface_summary_setter(self):
        tested = Interface()
        value = "value"
        tested.set_summary(value)
        pass

    def test_Interface_description_getter(self):
        tested = Interface()
        tested.get_description()
        pass

    def test_Interface_description_setter(self):
        tested = Interface()
        value = "value"
        tested.set_description(value)
        pass

    def test_Interface_status_getter(self):
        tested = Interface()
        tested.get_status()
        pass

    def test_Interface_status_setter(self):
        tested = Interface()
        value = "value"
        tested.set_status(value)
        pass

    def test_Interface_review_getter(self):
        tested = Interface()
        tested.get_review()
        pass

    def test_Interface_review_setter(self):
        tested = Interface()
        value = "value"
        tested.set_review(value)
        pass

    def test_Interface_visible_in_documentation_getter(self):
        tested = Interface()
        tested.get_visible_in_documentation()
        pass

    def test_Interface_visible_in_documentation_setter(self):
        tested = Interface()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_Interface_visible_for_traceability_getter(self):
        tested = Interface()
        tested.get_visible_for_traceability()
        pass

    def test_Interface_visible_for_traceability_setter(self):
        tested = Interface()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_Interface_owned_constraints_getter(self):
        tested = Interface()
        tested.get_owned_constraints()
        pass

    def test_Interface_constraints_getter(self):
        tested = Interface()
        tested.get_constraints()
        pass

    def test_Interface_constraints_setter(self):
        tested = Interface()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_Interface_owned_property_values_getter(self):
        tested = Interface()
        tested.get_owned_property_values()
        pass

    def test_Interface_applied_property_values_getter(self):
        tested = Interface()
        tested.get_applied_property_values()
        pass

    def test_Interface_applied_property_values_setter(self):
        tested = Interface()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_Interface_owned_property_value_groups_getter(self):
        tested = Interface()
        tested.get_owned_property_value_groups()
        pass

    def test_Interface_applied_property_value_groups_getter(self):
        tested = Interface()
        tested.get_applied_property_value_groups()
        pass

    def test_Interface_applied_property_value_groups_setter(self):
        tested = Interface()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_Interface_owned_enumeration_property_types_getter(self):
        tested = Interface()
        tested.get_owned_enumeration_property_types()
        pass

    def test_Interface_owned_diagrams_getter(self):
        tested = Interface()
        tested.get_owned_diagrams()
        pass

    def test_Interface_element_of_interest_for_diagrams_getter(self):
        tested = Interface()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_Interface_element_of_interest_for_diagrams_setter(self):
        tested = Interface()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_Interface_contextual_element_for_diagrams_getter(self):
        tested = Interface()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_Interface_contextual_element_for_diagrams_setter(self):
        tested = Interface()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_Interface_representing_diagrams_getter(self):
        tested = Interface()
        tested.get_representing_diagrams()
        pass

    def test_Interface__r_e_cs_getter(self):
        tested = Interface()
        tested.get__r_e_cs()
        pass

    def test_Interface__r_e_cs_setter(self):
        tested = Interface()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_Interface__r_p_ls_getter(self):
        tested = Interface()
        tested.get__r_p_ls()
        pass

    def test_Interface__r_p_ls_setter(self):
        tested = Interface()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_Interface_get_label(self):
        tested = Interface()
        tested.get_label()
        pass

    def test_Interface_get_element_type(self):
        tested = Interface()
        tested.get_element_type()
        pass

    def test_Interface_get_container(self):
        tested = Interface()
        tested.get_container()
        pass

    def test_Interface_get_contents(self):
        tested = Interface()
        tested.get_contents()
        pass

    def test_Interface_get_all_contents(self):
        tested = Interface()
        tested.get_all_contents()
        pass

    def test_Interface_get_all_contents_by_type(self):
        tested = Interface()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_Interface_get_available_s_b_queries(self):
        tested = Interface()
        tested.get_available_s_b_queries()
        pass

    def test_Interface_get_query_result(self):
        tested = Interface()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_Interface_visibility_getter(self):
        tested = Interface()
        tested.get_visibility()
        pass

    def test_Interface_visibility_setter(self):
        tested = Interface()
        value = VisibilityKind()
        tested.set_visibility(value)
        pass

    def test_Interface_owned_exchange_item_allocations_getter(self):
        tested = Interface()
        tested.get_owned_exchange_item_allocations()
        pass

    def test_Interface_exchange_items_getter(self):
        tested = Interface()
        tested.get_exchange_items()
        pass

    def test_Interface_exchange_items_setter(self):
        tested = Interface()
        value = ExchangeItem()
        tested.get_exchange_items().add(value)
        pass

    def test_Interface_providing_component_ports_getter(self):
        tested = Interface()
        tested.get_providing_component_ports()
        pass

    def test_Interface_providing_component_ports_setter(self):
        tested = Interface()
        value = ComponentPort()
        tested.get_providing_component_ports().add(value)
        pass

    def test_Interface_requiring_component_ports_getter(self):
        tested = Interface()
        tested.get_requiring_component_ports()
        pass

    def test_Interface_requiring_component_ports_setter(self):
        tested = Interface()
        value = ComponentPort()
        tested.get_requiring_component_ports().add(value)
        pass

    def test_Interface_user_components_getter(self):
        tested = Interface()
        tested.get_user_components()
        pass

    def test_Interface_user_components_setter(self):
        tested = Interface()
        value = PhysicalActor()
        tested.get_user_components().add(value)
        pass

    def test_Interface_implementor_components_getter(self):
        tested = Interface()
        tested.get_implementor_components()
        pass

    def test_Interface_implementor_components_setter(self):
        tested = Interface()
        value = PhysicalActor()
        tested.get_implementor_components().add(value)
        pass

    def test_Interface_super_getter(self):
        tested = Interface()
        tested.get_super()
        pass

    def test_Interface_super_setter(self):
        tested = Interface()
        value = Interface()
        tested.get_super().add(value)
        pass

    def test_Interface_sub_getter(self):
        tested = Interface()
        tested.get_sub()
        pass

    def test_Interface_sub_setter(self):
        tested = Interface()
        value = Interface()
        tested.get_sub().add(value)
        pass

    def test_ExchangeItemAllocation_id_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_id()
        pass

    def test_ExchangeItemAllocation_id_setter(self):
        tested = ExchangeItemAllocation()
        value = "value"
        tested.set_id(value)
        pass

    def test_ExchangeItemAllocation_sid_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_sid()
        pass

    def test_ExchangeItemAllocation_sid_setter(self):
        tested = ExchangeItemAllocation()
        value = "value"
        tested.set_sid(value)
        pass

    def test_ExchangeItemAllocation_name_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_name()
        pass

    def test_ExchangeItemAllocation_name_setter(self):
        tested = ExchangeItemAllocation()
        value = "value"
        tested.set_name(value)
        pass

    def test_ExchangeItemAllocation_summary_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_summary()
        pass

    def test_ExchangeItemAllocation_summary_setter(self):
        tested = ExchangeItemAllocation()
        value = "value"
        tested.set_summary(value)
        pass

    def test_ExchangeItemAllocation_description_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_description()
        pass

    def test_ExchangeItemAllocation_description_setter(self):
        tested = ExchangeItemAllocation()
        value = "value"
        tested.set_description(value)
        pass

    def test_ExchangeItemAllocation_status_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_status()
        pass

    def test_ExchangeItemAllocation_status_setter(self):
        tested = ExchangeItemAllocation()
        value = "value"
        tested.set_status(value)
        pass

    def test_ExchangeItemAllocation_review_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_review()
        pass

    def test_ExchangeItemAllocation_review_setter(self):
        tested = ExchangeItemAllocation()
        value = "value"
        tested.set_review(value)
        pass

    def test_ExchangeItemAllocation_visible_in_documentation_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_visible_in_documentation()
        pass

    def test_ExchangeItemAllocation_visible_in_documentation_setter(self):
        tested = ExchangeItemAllocation()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_ExchangeItemAllocation_visible_for_traceability_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_visible_for_traceability()
        pass

    def test_ExchangeItemAllocation_visible_for_traceability_setter(self):
        tested = ExchangeItemAllocation()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_ExchangeItemAllocation_owned_constraints_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_owned_constraints()
        pass

    def test_ExchangeItemAllocation_constraints_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_constraints()
        pass

    def test_ExchangeItemAllocation_constraints_setter(self):
        tested = ExchangeItemAllocation()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_ExchangeItemAllocation_owned_property_values_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_owned_property_values()
        pass

    def test_ExchangeItemAllocation_applied_property_values_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_applied_property_values()
        pass

    def test_ExchangeItemAllocation_applied_property_values_setter(self):
        tested = ExchangeItemAllocation()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_ExchangeItemAllocation_owned_property_value_groups_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_owned_property_value_groups()
        pass

    def test_ExchangeItemAllocation_applied_property_value_groups_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_applied_property_value_groups()
        pass

    def test_ExchangeItemAllocation_applied_property_value_groups_setter(self):
        tested = ExchangeItemAllocation()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_ExchangeItemAllocation_owned_enumeration_property_types_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_owned_enumeration_property_types()
        pass

    def test_ExchangeItemAllocation_owned_diagrams_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_owned_diagrams()
        pass

    def test_ExchangeItemAllocation_element_of_interest_for_diagrams_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_ExchangeItemAllocation_element_of_interest_for_diagrams_setter(self):
        tested = ExchangeItemAllocation()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_ExchangeItemAllocation_contextual_element_for_diagrams_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_ExchangeItemAllocation_contextual_element_for_diagrams_setter(self):
        tested = ExchangeItemAllocation()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_ExchangeItemAllocation_representing_diagrams_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_representing_diagrams()
        pass

    def test_ExchangeItemAllocation__r_e_cs_getter(self):
        tested = ExchangeItemAllocation()
        tested.get__r_e_cs()
        pass

    def test_ExchangeItemAllocation__r_e_cs_setter(self):
        tested = ExchangeItemAllocation()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_ExchangeItemAllocation__r_p_ls_getter(self):
        tested = ExchangeItemAllocation()
        tested.get__r_p_ls()
        pass

    def test_ExchangeItemAllocation__r_p_ls_setter(self):
        tested = ExchangeItemAllocation()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_ExchangeItemAllocation_get_label(self):
        tested = ExchangeItemAllocation()
        tested.get_label()
        pass

    def test_ExchangeItemAllocation_get_element_type(self):
        tested = ExchangeItemAllocation()
        tested.get_element_type()
        pass

    def test_ExchangeItemAllocation_get_container(self):
        tested = ExchangeItemAllocation()
        tested.get_container()
        pass

    def test_ExchangeItemAllocation_get_contents(self):
        tested = ExchangeItemAllocation()
        tested.get_contents()
        pass

    def test_ExchangeItemAllocation_get_all_contents(self):
        tested = ExchangeItemAllocation()
        tested.get_all_contents()
        pass

    def test_ExchangeItemAllocation_get_all_contents_by_type(self):
        tested = ExchangeItemAllocation()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_ExchangeItemAllocation_get_available_s_b_queries(self):
        tested = ExchangeItemAllocation()
        tested.get_available_s_b_queries()
        pass

    def test_ExchangeItemAllocation_get_query_result(self):
        tested = ExchangeItemAllocation()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_ExchangeItemAllocation_transmission_protocol_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_transmission_protocol()
        pass

    def test_ExchangeItemAllocation_transmission_protocol_setter(self):
        tested = ExchangeItemAllocation()
        value = CommunicationLinkProtocol()
        tested.set_transmission_protocol(value)
        pass

    def test_ExchangeItemAllocation_acquisition_protocol_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_acquisition_protocol()
        pass

    def test_ExchangeItemAllocation_acquisition_protocol_setter(self):
        tested = ExchangeItemAllocation()
        value = CommunicationLinkProtocol()
        tested.set_acquisition_protocol(value)
        pass

    def test_ExchangeItemAllocation_allocated_item_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_allocated_item()
        pass

    def test_ExchangeItemAllocation_allocated_item_setter(self):
        tested = ExchangeItemAllocation()
        value = ExchangeItem()
        tested.set_allocated_item(value)
        pass

    def test_ExchangeItemAllocation_invoking_sequence_messages_getter(self):
        tested = ExchangeItemAllocation()
        tested.get_invoking_sequence_messages()
        pass

    def test_ExchangeItemAllocation_invoking_sequence_messages_setter(self):
        tested = ExchangeItemAllocation()
        value = SequenceMessage()
        tested.get_invoking_sequence_messages().add(value)
        pass

    def test_ExchangeItem_id_getter(self):
        tested = ExchangeItem()
        tested.get_id()
        pass

    def test_ExchangeItem_id_setter(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_id(value)
        pass

    def test_ExchangeItem_sid_getter(self):
        tested = ExchangeItem()
        tested.get_sid()
        pass

    def test_ExchangeItem_sid_setter(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_sid(value)
        pass

    def test_ExchangeItem_name_getter(self):
        tested = ExchangeItem()
        tested.get_name()
        pass

    def test_ExchangeItem_name_setter(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_name(value)
        pass

    def test_ExchangeItem_summary_getter(self):
        tested = ExchangeItem()
        tested.get_summary()
        pass

    def test_ExchangeItem_summary_setter(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_summary(value)
        pass

    def test_ExchangeItem_description_getter(self):
        tested = ExchangeItem()
        tested.get_description()
        pass

    def test_ExchangeItem_description_setter(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_description(value)
        pass

    def test_ExchangeItem_status_getter(self):
        tested = ExchangeItem()
        tested.get_status()
        pass

    def test_ExchangeItem_status_setter(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_status(value)
        pass

    def test_ExchangeItem_review_getter(self):
        tested = ExchangeItem()
        tested.get_review()
        pass

    def test_ExchangeItem_review_setter(self):
        tested = ExchangeItem()
        value = "value"
        tested.set_review(value)
        pass

    def test_ExchangeItem_visible_in_documentation_getter(self):
        tested = ExchangeItem()
        tested.get_visible_in_documentation()
        pass

    def test_ExchangeItem_visible_in_documentation_setter(self):
        tested = ExchangeItem()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_ExchangeItem_visible_for_traceability_getter(self):
        tested = ExchangeItem()
        tested.get_visible_for_traceability()
        pass

    def test_ExchangeItem_visible_for_traceability_setter(self):
        tested = ExchangeItem()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_ExchangeItem_owned_constraints_getter(self):
        tested = ExchangeItem()
        tested.get_owned_constraints()
        pass

    def test_ExchangeItem_constraints_getter(self):
        tested = ExchangeItem()
        tested.get_constraints()
        pass

    def test_ExchangeItem_constraints_setter(self):
        tested = ExchangeItem()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_ExchangeItem_owned_property_values_getter(self):
        tested = ExchangeItem()
        tested.get_owned_property_values()
        pass

    def test_ExchangeItem_applied_property_values_getter(self):
        tested = ExchangeItem()
        tested.get_applied_property_values()
        pass

    def test_ExchangeItem_applied_property_values_setter(self):
        tested = ExchangeItem()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_ExchangeItem_owned_property_value_groups_getter(self):
        tested = ExchangeItem()
        tested.get_owned_property_value_groups()
        pass

    def test_ExchangeItem_applied_property_value_groups_getter(self):
        tested = ExchangeItem()
        tested.get_applied_property_value_groups()
        pass

    def test_ExchangeItem_applied_property_value_groups_setter(self):
        tested = ExchangeItem()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_ExchangeItem_owned_enumeration_property_types_getter(self):
        tested = ExchangeItem()
        tested.get_owned_enumeration_property_types()
        pass

    def test_ExchangeItem_owned_diagrams_getter(self):
        tested = ExchangeItem()
        tested.get_owned_diagrams()
        pass

    def test_ExchangeItem_element_of_interest_for_diagrams_getter(self):
        tested = ExchangeItem()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_ExchangeItem_element_of_interest_for_diagrams_setter(self):
        tested = ExchangeItem()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_ExchangeItem_contextual_element_for_diagrams_getter(self):
        tested = ExchangeItem()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_ExchangeItem_contextual_element_for_diagrams_setter(self):
        tested = ExchangeItem()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_ExchangeItem_representing_diagrams_getter(self):
        tested = ExchangeItem()
        tested.get_representing_diagrams()
        pass

    def test_ExchangeItem__r_e_cs_getter(self):
        tested = ExchangeItem()
        tested.get__r_e_cs()
        pass

    def test_ExchangeItem__r_e_cs_setter(self):
        tested = ExchangeItem()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_ExchangeItem__r_p_ls_getter(self):
        tested = ExchangeItem()
        tested.get__r_p_ls()
        pass

    def test_ExchangeItem__r_p_ls_setter(self):
        tested = ExchangeItem()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_ExchangeItem_get_label(self):
        tested = ExchangeItem()
        tested.get_label()
        pass

    def test_ExchangeItem_get_element_type(self):
        tested = ExchangeItem()
        tested.get_element_type()
        pass

    def test_ExchangeItem_get_container(self):
        tested = ExchangeItem()
        tested.get_container()
        pass

    def test_ExchangeItem_get_contents(self):
        tested = ExchangeItem()
        tested.get_contents()
        pass

    def test_ExchangeItem_get_all_contents(self):
        tested = ExchangeItem()
        tested.get_all_contents()
        pass

    def test_ExchangeItem_get_all_contents_by_type(self):
        tested = ExchangeItem()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_ExchangeItem_get_available_s_b_queries(self):
        tested = ExchangeItem()
        tested.get_available_s_b_queries()
        pass

    def test_ExchangeItem_get_query_result(self):
        tested = ExchangeItem()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_ExchangeItem_abstract_getter(self):
        tested = ExchangeItem()
        tested.get_abstract()
        pass

    def test_ExchangeItem_abstract_setter(self):
        tested = ExchangeItem()
        value = True
        tested.set_abstract(value)
        pass

    def test_ExchangeItem_final_getter(self):
        tested = ExchangeItem()
        tested.get_final()
        pass

    def test_ExchangeItem_final_setter(self):
        tested = ExchangeItem()
        value = True
        tested.set_final(value)
        pass

    def test_ExchangeItem_exchange_mechanism_getter(self):
        tested = ExchangeItem()
        tested.get_exchange_mechanism()
        pass

    def test_ExchangeItem_exchange_mechanism_setter(self):
        tested = ExchangeItem()
        value = "FLOW"
        tested.set_exchange_mechanism(value)
        pass

    def test_ExchangeItem_owned_elements_getter(self):
        tested = ExchangeItem()
        tested.get_owned_elements()
        pass

    def test_ExchangeItem_allocator_interfaces_getter(self):
        tested = ExchangeItem()
        tested.get_allocator_interfaces()
        pass

    def test_ExchangeItem_allocator_interfaces_setter(self):
        tested = ExchangeItem()
        value = Interface()
        tested.get_allocator_interfaces().add(value)
        pass

    def test_ExchangeItem_super_getter(self):
        tested = ExchangeItem()
        tested.get_super()
        pass

    def test_ExchangeItem_super_setter(self):
        tested = ExchangeItem()
        value = ExchangeItem()
        tested.get_super().add(value)
        pass

    def test_ExchangeItem_sub_getter(self):
        tested = ExchangeItem()
        tested.get_sub()
        pass

    def test_ExchangeItem_sub_setter(self):
        tested = ExchangeItem()
        value = ExchangeItem()
        tested.get_sub().add(value)
        pass

    def test_ExchangeItem_realized_exchange_items_getter(self):
        tested = ExchangeItem()
        tested.get_realized_exchange_items()
        pass

    def test_ExchangeItem_realized_exchange_items_setter(self):
        tested = ExchangeItem()
        value = ExchangeItem()
        tested.get_realized_exchange_items().add(value)
        pass

    def test_ExchangeItem_realizing_exchange_items_getter(self):
        tested = ExchangeItem()
        tested.get_realizing_exchange_items()
        pass

    def test_ExchangeItem_realizing_exchange_items_setter(self):
        tested = ExchangeItem()
        value = ExchangeItem()
        tested.get_realizing_exchange_items().add(value)
        pass

    def test_ExchangeItem_realizing_operations_getter(self):
        tested = ExchangeItem()
        tested.get_realizing_operations()
        pass

    def test_ExchangeItem_realizing_operations_setter(self):
        tested = ExchangeItem()
        value = Operation()
        tested.get_realizing_operations().add(value)
        pass

    def test_ExchangeItemElement_id_getter(self):
        tested = ExchangeItemElement()
        tested.get_id()
        pass

    def test_ExchangeItemElement_id_setter(self):
        tested = ExchangeItemElement()
        value = "value"
        tested.set_id(value)
        pass

    def test_ExchangeItemElement_sid_getter(self):
        tested = ExchangeItemElement()
        tested.get_sid()
        pass

    def test_ExchangeItemElement_sid_setter(self):
        tested = ExchangeItemElement()
        value = "value"
        tested.set_sid(value)
        pass

    def test_ExchangeItemElement_name_getter(self):
        tested = ExchangeItemElement()
        tested.get_name()
        pass

    def test_ExchangeItemElement_name_setter(self):
        tested = ExchangeItemElement()
        value = "value"
        tested.set_name(value)
        pass

    def test_ExchangeItemElement_summary_getter(self):
        tested = ExchangeItemElement()
        tested.get_summary()
        pass

    def test_ExchangeItemElement_summary_setter(self):
        tested = ExchangeItemElement()
        value = "value"
        tested.set_summary(value)
        pass

    def test_ExchangeItemElement_description_getter(self):
        tested = ExchangeItemElement()
        tested.get_description()
        pass

    def test_ExchangeItemElement_description_setter(self):
        tested = ExchangeItemElement()
        value = "value"
        tested.set_description(value)
        pass

    def test_ExchangeItemElement_status_getter(self):
        tested = ExchangeItemElement()
        tested.get_status()
        pass

    def test_ExchangeItemElement_status_setter(self):
        tested = ExchangeItemElement()
        value = "value"
        tested.set_status(value)
        pass

    def test_ExchangeItemElement_review_getter(self):
        tested = ExchangeItemElement()
        tested.get_review()
        pass

    def test_ExchangeItemElement_review_setter(self):
        tested = ExchangeItemElement()
        value = "value"
        tested.set_review(value)
        pass

    def test_ExchangeItemElement_visible_in_documentation_getter(self):
        tested = ExchangeItemElement()
        tested.get_visible_in_documentation()
        pass

    def test_ExchangeItemElement_visible_in_documentation_setter(self):
        tested = ExchangeItemElement()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_ExchangeItemElement_visible_for_traceability_getter(self):
        tested = ExchangeItemElement()
        tested.get_visible_for_traceability()
        pass

    def test_ExchangeItemElement_visible_for_traceability_setter(self):
        tested = ExchangeItemElement()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_ExchangeItemElement_owned_constraints_getter(self):
        tested = ExchangeItemElement()
        tested.get_owned_constraints()
        pass

    def test_ExchangeItemElement_constraints_getter(self):
        tested = ExchangeItemElement()
        tested.get_constraints()
        pass

    def test_ExchangeItemElement_constraints_setter(self):
        tested = ExchangeItemElement()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_ExchangeItemElement_owned_property_values_getter(self):
        tested = ExchangeItemElement()
        tested.get_owned_property_values()
        pass

    def test_ExchangeItemElement_applied_property_values_getter(self):
        tested = ExchangeItemElement()
        tested.get_applied_property_values()
        pass

    def test_ExchangeItemElement_applied_property_values_setter(self):
        tested = ExchangeItemElement()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_ExchangeItemElement_owned_property_value_groups_getter(self):
        tested = ExchangeItemElement()
        tested.get_owned_property_value_groups()
        pass

    def test_ExchangeItemElement_applied_property_value_groups_getter(self):
        tested = ExchangeItemElement()
        tested.get_applied_property_value_groups()
        pass

    def test_ExchangeItemElement_applied_property_value_groups_setter(self):
        tested = ExchangeItemElement()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_ExchangeItemElement_owned_enumeration_property_types_getter(self):
        tested = ExchangeItemElement()
        tested.get_owned_enumeration_property_types()
        pass

    def test_ExchangeItemElement_owned_diagrams_getter(self):
        tested = ExchangeItemElement()
        tested.get_owned_diagrams()
        pass

    def test_ExchangeItemElement_element_of_interest_for_diagrams_getter(self):
        tested = ExchangeItemElement()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_ExchangeItemElement_element_of_interest_for_diagrams_setter(self):
        tested = ExchangeItemElement()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_ExchangeItemElement_contextual_element_for_diagrams_getter(self):
        tested = ExchangeItemElement()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_ExchangeItemElement_contextual_element_for_diagrams_setter(self):
        tested = ExchangeItemElement()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_ExchangeItemElement_representing_diagrams_getter(self):
        tested = ExchangeItemElement()
        tested.get_representing_diagrams()
        pass

    def test_ExchangeItemElement__r_e_cs_getter(self):
        tested = ExchangeItemElement()
        tested.get__r_e_cs()
        pass

    def test_ExchangeItemElement__r_e_cs_setter(self):
        tested = ExchangeItemElement()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_ExchangeItemElement__r_p_ls_getter(self):
        tested = ExchangeItemElement()
        tested.get__r_p_ls()
        pass

    def test_ExchangeItemElement__r_p_ls_setter(self):
        tested = ExchangeItemElement()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_ExchangeItemElement_get_label(self):
        tested = ExchangeItemElement()
        tested.get_label()
        pass

    def test_ExchangeItemElement_get_element_type(self):
        tested = ExchangeItemElement()
        tested.get_element_type()
        pass

    def test_ExchangeItemElement_get_container(self):
        tested = ExchangeItemElement()
        tested.get_container()
        pass

    def test_ExchangeItemElement_get_contents(self):
        tested = ExchangeItemElement()
        tested.get_contents()
        pass

    def test_ExchangeItemElement_get_all_contents(self):
        tested = ExchangeItemElement()
        tested.get_all_contents()
        pass

    def test_ExchangeItemElement_get_all_contents_by_type(self):
        tested = ExchangeItemElement()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_ExchangeItemElement_get_available_s_b_queries(self):
        tested = ExchangeItemElement()
        tested.get_available_s_b_queries()
        pass

    def test_ExchangeItemElement_get_query_result(self):
        tested = ExchangeItemElement()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_ExchangeItemElement_type_getter(self):
        tested = ExchangeItemElement()
        tested.get_type()
        pass

    def test_ExchangeItemElement_type_setter(self):
        tested = ExchangeItemElement()
        value = PhysicalQuantity()
        tested.set_type(value)
        pass

    def test_FunctionInputPort_allocator_component_port_getter(self):
        tested = FunctionInputPort()
        tested.get_allocator_component_port()
        pass

    def test_FunctionInputPort_allocator_component_port_setter(self):
        tested = FunctionInputPort()
        value = ComponentPort()
        tested.set_allocator_component_port(value)
        pass

    def test_FunctionInputPort_id_getter(self):
        tested = FunctionInputPort()
        tested.get_id()
        pass

    def test_FunctionInputPort_id_setter(self):
        tested = FunctionInputPort()
        value = "value"
        tested.set_id(value)
        pass

    def test_FunctionInputPort_sid_getter(self):
        tested = FunctionInputPort()
        tested.get_sid()
        pass

    def test_FunctionInputPort_sid_setter(self):
        tested = FunctionInputPort()
        value = "value"
        tested.set_sid(value)
        pass

    def test_FunctionInputPort_name_getter(self):
        tested = FunctionInputPort()
        tested.get_name()
        pass

    def test_FunctionInputPort_name_setter(self):
        tested = FunctionInputPort()
        value = "value"
        tested.set_name(value)
        pass

    def test_FunctionInputPort_summary_getter(self):
        tested = FunctionInputPort()
        tested.get_summary()
        pass

    def test_FunctionInputPort_summary_setter(self):
        tested = FunctionInputPort()
        value = "value"
        tested.set_summary(value)
        pass

    def test_FunctionInputPort_description_getter(self):
        tested = FunctionInputPort()
        tested.get_description()
        pass

    def test_FunctionInputPort_description_setter(self):
        tested = FunctionInputPort()
        value = "value"
        tested.set_description(value)
        pass

    def test_FunctionInputPort_status_getter(self):
        tested = FunctionInputPort()
        tested.get_status()
        pass

    def test_FunctionInputPort_status_setter(self):
        tested = FunctionInputPort()
        value = "value"
        tested.set_status(value)
        pass

    def test_FunctionInputPort_review_getter(self):
        tested = FunctionInputPort()
        tested.get_review()
        pass

    def test_FunctionInputPort_review_setter(self):
        tested = FunctionInputPort()
        value = "value"
        tested.set_review(value)
        pass

    def test_FunctionInputPort_visible_in_documentation_getter(self):
        tested = FunctionInputPort()
        tested.get_visible_in_documentation()
        pass

    def test_FunctionInputPort_visible_in_documentation_setter(self):
        tested = FunctionInputPort()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_FunctionInputPort_visible_for_traceability_getter(self):
        tested = FunctionInputPort()
        tested.get_visible_for_traceability()
        pass

    def test_FunctionInputPort_visible_for_traceability_setter(self):
        tested = FunctionInputPort()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_FunctionInputPort_owned_constraints_getter(self):
        tested = FunctionInputPort()
        tested.get_owned_constraints()
        pass

    def test_FunctionInputPort_constraints_getter(self):
        tested = FunctionInputPort()
        tested.get_constraints()
        pass

    def test_FunctionInputPort_constraints_setter(self):
        tested = FunctionInputPort()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_FunctionInputPort_owned_property_values_getter(self):
        tested = FunctionInputPort()
        tested.get_owned_property_values()
        pass

    def test_FunctionInputPort_applied_property_values_getter(self):
        tested = FunctionInputPort()
        tested.get_applied_property_values()
        pass

    def test_FunctionInputPort_applied_property_values_setter(self):
        tested = FunctionInputPort()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_FunctionInputPort_owned_property_value_groups_getter(self):
        tested = FunctionInputPort()
        tested.get_owned_property_value_groups()
        pass

    def test_FunctionInputPort_applied_property_value_groups_getter(self):
        tested = FunctionInputPort()
        tested.get_applied_property_value_groups()
        pass

    def test_FunctionInputPort_applied_property_value_groups_setter(self):
        tested = FunctionInputPort()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_FunctionInputPort_owned_enumeration_property_types_getter(self):
        tested = FunctionInputPort()
        tested.get_owned_enumeration_property_types()
        pass

    def test_FunctionInputPort_owned_diagrams_getter(self):
        tested = FunctionInputPort()
        tested.get_owned_diagrams()
        pass

    def test_FunctionInputPort_element_of_interest_for_diagrams_getter(self):
        tested = FunctionInputPort()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_FunctionInputPort_element_of_interest_for_diagrams_setter(self):
        tested = FunctionInputPort()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_FunctionInputPort_contextual_element_for_diagrams_getter(self):
        tested = FunctionInputPort()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_FunctionInputPort_contextual_element_for_diagrams_setter(self):
        tested = FunctionInputPort()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_FunctionInputPort_representing_diagrams_getter(self):
        tested = FunctionInputPort()
        tested.get_representing_diagrams()
        pass

    def test_FunctionInputPort__r_e_cs_getter(self):
        tested = FunctionInputPort()
        tested.get__r_e_cs()
        pass

    def test_FunctionInputPort__r_e_cs_setter(self):
        tested = FunctionInputPort()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_FunctionInputPort__r_p_ls_getter(self):
        tested = FunctionInputPort()
        tested.get__r_p_ls()
        pass

    def test_FunctionInputPort__r_p_ls_setter(self):
        tested = FunctionInputPort()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_FunctionInputPort_get_label(self):
        tested = FunctionInputPort()
        tested.get_label()
        pass

    def test_FunctionInputPort_get_element_type(self):
        tested = FunctionInputPort()
        tested.get_element_type()
        pass

    def test_FunctionInputPort_get_container(self):
        tested = FunctionInputPort()
        tested.get_container()
        pass

    def test_FunctionInputPort_get_contents(self):
        tested = FunctionInputPort()
        tested.get_contents()
        pass

    def test_FunctionInputPort_get_all_contents(self):
        tested = FunctionInputPort()
        tested.get_all_contents()
        pass

    def test_FunctionInputPort_get_all_contents_by_type(self):
        tested = FunctionInputPort()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_FunctionInputPort_get_available_s_b_queries(self):
        tested = FunctionInputPort()
        tested.get_available_s_b_queries()
        pass

    def test_FunctionInputPort_get_query_result(self):
        tested = FunctionInputPort()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_FunctionInputPort_incoming_functional_exchanges_getter(self):
        tested = FunctionInputPort()
        tested.get_incoming_functional_exchanges()
        pass

    def test_FunctionInputPort_incoming_functional_exchanges_setter(self):
        tested = FunctionInputPort()
        value = FunctionalExchange()
        tested.get_incoming_functional_exchanges().add(value)
        pass

    def test_FunctionInputPort_incoming_exchange_items_getter(self):
        tested = FunctionInputPort()
        tested.get_incoming_exchange_items()
        pass

    def test_FunctionInputPort_incoming_exchange_items_setter(self):
        tested = FunctionInputPort()
        value = ExchangeItem()
        tested.get_incoming_exchange_items().add(value)
        pass

    def test_FunctionInputPort_realized_function_input_ports_getter(self):
        tested = FunctionInputPort()
        tested.get_realized_function_input_ports()
        pass

    def test_FunctionInputPort_realized_function_input_ports_setter(self):
        tested = FunctionInputPort()
        value = FunctionInputPort()
        tested.get_realized_function_input_ports().add(value)
        pass

    def test_FunctionInputPort_realizing_function_input_ports_getter(self):
        tested = FunctionInputPort()
        tested.get_realizing_function_input_ports()
        pass

    def test_FunctionInputPort_realizing_function_input_ports_setter(self):
        tested = FunctionInputPort()
        value = FunctionInputPort()
        tested.get_realizing_function_input_ports().add(value)
        pass

    def test_FunctionOutputPort_allocator_component_port_getter(self):
        tested = FunctionOutputPort()
        tested.get_allocator_component_port()
        pass

    def test_FunctionOutputPort_allocator_component_port_setter(self):
        tested = FunctionOutputPort()
        value = ComponentPort()
        tested.set_allocator_component_port(value)
        pass

    def test_FunctionOutputPort_id_getter(self):
        tested = FunctionOutputPort()
        tested.get_id()
        pass

    def test_FunctionOutputPort_id_setter(self):
        tested = FunctionOutputPort()
        value = "value"
        tested.set_id(value)
        pass

    def test_FunctionOutputPort_sid_getter(self):
        tested = FunctionOutputPort()
        tested.get_sid()
        pass

    def test_FunctionOutputPort_sid_setter(self):
        tested = FunctionOutputPort()
        value = "value"
        tested.set_sid(value)
        pass

    def test_FunctionOutputPort_name_getter(self):
        tested = FunctionOutputPort()
        tested.get_name()
        pass

    def test_FunctionOutputPort_name_setter(self):
        tested = FunctionOutputPort()
        value = "value"
        tested.set_name(value)
        pass

    def test_FunctionOutputPort_summary_getter(self):
        tested = FunctionOutputPort()
        tested.get_summary()
        pass

    def test_FunctionOutputPort_summary_setter(self):
        tested = FunctionOutputPort()
        value = "value"
        tested.set_summary(value)
        pass

    def test_FunctionOutputPort_description_getter(self):
        tested = FunctionOutputPort()
        tested.get_description()
        pass

    def test_FunctionOutputPort_description_setter(self):
        tested = FunctionOutputPort()
        value = "value"
        tested.set_description(value)
        pass

    def test_FunctionOutputPort_status_getter(self):
        tested = FunctionOutputPort()
        tested.get_status()
        pass

    def test_FunctionOutputPort_status_setter(self):
        tested = FunctionOutputPort()
        value = "value"
        tested.set_status(value)
        pass

    def test_FunctionOutputPort_review_getter(self):
        tested = FunctionOutputPort()
        tested.get_review()
        pass

    def test_FunctionOutputPort_review_setter(self):
        tested = FunctionOutputPort()
        value = "value"
        tested.set_review(value)
        pass

    def test_FunctionOutputPort_visible_in_documentation_getter(self):
        tested = FunctionOutputPort()
        tested.get_visible_in_documentation()
        pass

    def test_FunctionOutputPort_visible_in_documentation_setter(self):
        tested = FunctionOutputPort()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_FunctionOutputPort_visible_for_traceability_getter(self):
        tested = FunctionOutputPort()
        tested.get_visible_for_traceability()
        pass

    def test_FunctionOutputPort_visible_for_traceability_setter(self):
        tested = FunctionOutputPort()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_FunctionOutputPort_owned_constraints_getter(self):
        tested = FunctionOutputPort()
        tested.get_owned_constraints()
        pass

    def test_FunctionOutputPort_constraints_getter(self):
        tested = FunctionOutputPort()
        tested.get_constraints()
        pass

    def test_FunctionOutputPort_constraints_setter(self):
        tested = FunctionOutputPort()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_FunctionOutputPort_owned_property_values_getter(self):
        tested = FunctionOutputPort()
        tested.get_owned_property_values()
        pass

    def test_FunctionOutputPort_applied_property_values_getter(self):
        tested = FunctionOutputPort()
        tested.get_applied_property_values()
        pass

    def test_FunctionOutputPort_applied_property_values_setter(self):
        tested = FunctionOutputPort()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_FunctionOutputPort_owned_property_value_groups_getter(self):
        tested = FunctionOutputPort()
        tested.get_owned_property_value_groups()
        pass

    def test_FunctionOutputPort_applied_property_value_groups_getter(self):
        tested = FunctionOutputPort()
        tested.get_applied_property_value_groups()
        pass

    def test_FunctionOutputPort_applied_property_value_groups_setter(self):
        tested = FunctionOutputPort()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_FunctionOutputPort_owned_enumeration_property_types_getter(self):
        tested = FunctionOutputPort()
        tested.get_owned_enumeration_property_types()
        pass

    def test_FunctionOutputPort_owned_diagrams_getter(self):
        tested = FunctionOutputPort()
        tested.get_owned_diagrams()
        pass

    def test_FunctionOutputPort_element_of_interest_for_diagrams_getter(self):
        tested = FunctionOutputPort()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_FunctionOutputPort_element_of_interest_for_diagrams_setter(self):
        tested = FunctionOutputPort()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_FunctionOutputPort_contextual_element_for_diagrams_getter(self):
        tested = FunctionOutputPort()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_FunctionOutputPort_contextual_element_for_diagrams_setter(self):
        tested = FunctionOutputPort()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_FunctionOutputPort_representing_diagrams_getter(self):
        tested = FunctionOutputPort()
        tested.get_representing_diagrams()
        pass

    def test_FunctionOutputPort__r_e_cs_getter(self):
        tested = FunctionOutputPort()
        tested.get__r_e_cs()
        pass

    def test_FunctionOutputPort__r_e_cs_setter(self):
        tested = FunctionOutputPort()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_FunctionOutputPort__r_p_ls_getter(self):
        tested = FunctionOutputPort()
        tested.get__r_p_ls()
        pass

    def test_FunctionOutputPort__r_p_ls_setter(self):
        tested = FunctionOutputPort()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_FunctionOutputPort_get_label(self):
        tested = FunctionOutputPort()
        tested.get_label()
        pass

    def test_FunctionOutputPort_get_element_type(self):
        tested = FunctionOutputPort()
        tested.get_element_type()
        pass

    def test_FunctionOutputPort_get_container(self):
        tested = FunctionOutputPort()
        tested.get_container()
        pass

    def test_FunctionOutputPort_get_contents(self):
        tested = FunctionOutputPort()
        tested.get_contents()
        pass

    def test_FunctionOutputPort_get_all_contents(self):
        tested = FunctionOutputPort()
        tested.get_all_contents()
        pass

    def test_FunctionOutputPort_get_all_contents_by_type(self):
        tested = FunctionOutputPort()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_FunctionOutputPort_get_available_s_b_queries(self):
        tested = FunctionOutputPort()
        tested.get_available_s_b_queries()
        pass

    def test_FunctionOutputPort_get_query_result(self):
        tested = FunctionOutputPort()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_FunctionOutputPort_outgoing_functional_exchanges_getter(self):
        tested = FunctionOutputPort()
        tested.get_outgoing_functional_exchanges()
        pass

    def test_FunctionOutputPort_outgoing_functional_exchanges_setter(self):
        tested = FunctionOutputPort()
        value = FunctionalExchange()
        tested.get_outgoing_functional_exchanges().add(value)
        pass

    def test_FunctionOutputPort_outgoing_exchange_items_getter(self):
        tested = FunctionOutputPort()
        tested.get_outgoing_exchange_items()
        pass

    def test_FunctionOutputPort_outgoing_exchange_items_setter(self):
        tested = FunctionOutputPort()
        value = ExchangeItem()
        tested.get_outgoing_exchange_items().add(value)
        pass

    def test_FunctionOutputPort_realized_function_output_ports_getter(self):
        tested = FunctionOutputPort()
        tested.get_realized_function_output_ports()
        pass

    def test_FunctionOutputPort_realized_function_output_ports_setter(self):
        tested = FunctionOutputPort()
        value = FunctionOutputPort()
        tested.get_realized_function_output_ports().add(value)
        pass

    def test_FunctionOutputPort_realizing_function_output_ports_getter(self):
        tested = FunctionOutputPort()
        tested.get_realizing_function_output_ports()
        pass

    def test_FunctionOutputPort_realizing_function_output_ports_setter(self):
        tested = FunctionOutputPort()
        value = FunctionOutputPort()
        tested.get_realizing_function_output_ports().add(value)
        pass

    def test_FunctionalExchange_id_getter(self):
        tested = FunctionalExchange()
        tested.get_id()
        pass

    def test_FunctionalExchange_id_setter(self):
        tested = FunctionalExchange()
        value = "value"
        tested.set_id(value)
        pass

    def test_FunctionalExchange_sid_getter(self):
        tested = FunctionalExchange()
        tested.get_sid()
        pass

    def test_FunctionalExchange_sid_setter(self):
        tested = FunctionalExchange()
        value = "value"
        tested.set_sid(value)
        pass

    def test_FunctionalExchange_name_getter(self):
        tested = FunctionalExchange()
        tested.get_name()
        pass

    def test_FunctionalExchange_name_setter(self):
        tested = FunctionalExchange()
        value = "value"
        tested.set_name(value)
        pass

    def test_FunctionalExchange_summary_getter(self):
        tested = FunctionalExchange()
        tested.get_summary()
        pass

    def test_FunctionalExchange_summary_setter(self):
        tested = FunctionalExchange()
        value = "value"
        tested.set_summary(value)
        pass

    def test_FunctionalExchange_description_getter(self):
        tested = FunctionalExchange()
        tested.get_description()
        pass

    def test_FunctionalExchange_description_setter(self):
        tested = FunctionalExchange()
        value = "value"
        tested.set_description(value)
        pass

    def test_FunctionalExchange_status_getter(self):
        tested = FunctionalExchange()
        tested.get_status()
        pass

    def test_FunctionalExchange_status_setter(self):
        tested = FunctionalExchange()
        value = "value"
        tested.set_status(value)
        pass

    def test_FunctionalExchange_review_getter(self):
        tested = FunctionalExchange()
        tested.get_review()
        pass

    def test_FunctionalExchange_review_setter(self):
        tested = FunctionalExchange()
        value = "value"
        tested.set_review(value)
        pass

    def test_FunctionalExchange_visible_in_documentation_getter(self):
        tested = FunctionalExchange()
        tested.get_visible_in_documentation()
        pass

    def test_FunctionalExchange_visible_in_documentation_setter(self):
        tested = FunctionalExchange()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_FunctionalExchange_visible_for_traceability_getter(self):
        tested = FunctionalExchange()
        tested.get_visible_for_traceability()
        pass

    def test_FunctionalExchange_visible_for_traceability_setter(self):
        tested = FunctionalExchange()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_FunctionalExchange_owned_constraints_getter(self):
        tested = FunctionalExchange()
        tested.get_owned_constraints()
        pass

    def test_FunctionalExchange_constraints_getter(self):
        tested = FunctionalExchange()
        tested.get_constraints()
        pass

    def test_FunctionalExchange_constraints_setter(self):
        tested = FunctionalExchange()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_FunctionalExchange_owned_property_values_getter(self):
        tested = FunctionalExchange()
        tested.get_owned_property_values()
        pass

    def test_FunctionalExchange_applied_property_values_getter(self):
        tested = FunctionalExchange()
        tested.get_applied_property_values()
        pass

    def test_FunctionalExchange_applied_property_values_setter(self):
        tested = FunctionalExchange()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_FunctionalExchange_owned_property_value_groups_getter(self):
        tested = FunctionalExchange()
        tested.get_owned_property_value_groups()
        pass

    def test_FunctionalExchange_applied_property_value_groups_getter(self):
        tested = FunctionalExchange()
        tested.get_applied_property_value_groups()
        pass

    def test_FunctionalExchange_applied_property_value_groups_setter(self):
        tested = FunctionalExchange()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_FunctionalExchange_owned_enumeration_property_types_getter(self):
        tested = FunctionalExchange()
        tested.get_owned_enumeration_property_types()
        pass

    def test_FunctionalExchange_owned_diagrams_getter(self):
        tested = FunctionalExchange()
        tested.get_owned_diagrams()
        pass

    def test_FunctionalExchange_element_of_interest_for_diagrams_getter(self):
        tested = FunctionalExchange()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_FunctionalExchange_element_of_interest_for_diagrams_setter(self):
        tested = FunctionalExchange()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_FunctionalExchange_contextual_element_for_diagrams_getter(self):
        tested = FunctionalExchange()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_FunctionalExchange_contextual_element_for_diagrams_setter(self):
        tested = FunctionalExchange()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_FunctionalExchange_representing_diagrams_getter(self):
        tested = FunctionalExchange()
        tested.get_representing_diagrams()
        pass

    def test_FunctionalExchange__r_e_cs_getter(self):
        tested = FunctionalExchange()
        tested.get__r_e_cs()
        pass

    def test_FunctionalExchange__r_e_cs_setter(self):
        tested = FunctionalExchange()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_FunctionalExchange__r_p_ls_getter(self):
        tested = FunctionalExchange()
        tested.get__r_p_ls()
        pass

    def test_FunctionalExchange__r_p_ls_setter(self):
        tested = FunctionalExchange()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_FunctionalExchange_get_label(self):
        tested = FunctionalExchange()
        tested.get_label()
        pass

    def test_FunctionalExchange_get_element_type(self):
        tested = FunctionalExchange()
        tested.get_element_type()
        pass

    def test_FunctionalExchange_get_container(self):
        tested = FunctionalExchange()
        tested.get_container()
        pass

    def test_FunctionalExchange_get_contents(self):
        tested = FunctionalExchange()
        tested.get_contents()
        pass

    def test_FunctionalExchange_get_all_contents(self):
        tested = FunctionalExchange()
        tested.get_all_contents()
        pass

    def test_FunctionalExchange_get_all_contents_by_type(self):
        tested = FunctionalExchange()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_FunctionalExchange_get_available_s_b_queries(self):
        tested = FunctionalExchange()
        tested.get_available_s_b_queries()
        pass

    def test_FunctionalExchange_get_query_result(self):
        tested = FunctionalExchange()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_FunctionalExchange_invoking_sequence_messages_getter(self):
        tested = FunctionalExchange()
        tested.get_invoking_sequence_messages()
        pass

    def test_FunctionalExchange_source_port_getter(self):
        tested = FunctionalExchange()
        tested.get_source_port()
        pass

    def test_FunctionalExchange_source_port_setter(self):
        tested = FunctionalExchange()
        value = FunctionOutputPort()
        tested.set_source_port(value)
        pass

    def test_FunctionalExchange_target_port_getter(self):
        tested = FunctionalExchange()
        tested.get_target_port()
        pass

    def test_FunctionalExchange_target_port_setter(self):
        tested = FunctionalExchange()
        value = FunctionInputPort()
        tested.set_target_port(value)
        pass

    def test_FunctionalExchange_source_function_getter(self):
        tested = FunctionalExchange()
        tested.get_source_function()
        pass

    def test_FunctionalExchange_source_function_setter(self):
        tested = FunctionalExchange()
        value = PhysicalFunction()
        tested.set_source_function(value)
        pass

    def test_FunctionalExchange_target_function_getter(self):
        tested = FunctionalExchange()
        tested.get_target_function()
        pass

    def test_FunctionalExchange_target_function_setter(self):
        tested = FunctionalExchange()
        value = PhysicalFunction()
        tested.set_target_function(value)
        pass

    def test_FunctionalExchange_exchanged_items_getter(self):
        tested = FunctionalExchange()
        tested.get_exchanged_items()
        pass

    def test_FunctionalExchange_exchanged_items_setter(self):
        tested = FunctionalExchange()
        value = ExchangeItem()
        tested.get_exchanged_items().add(value)
        pass

    def test_FunctionalExchange_involving_functional_chains_getter(self):
        tested = FunctionalExchange()
        tested.get_involving_functional_chains()
        pass

    def test_FunctionalExchange_categories_getter(self):
        tested = FunctionalExchange()
        tested.get_categories()
        pass

    def test_FunctionalExchange_categories_setter(self):
        tested = FunctionalExchange()
        value = ExchangeCategory()
        tested.get_categories().add(value)
        pass

    def test_FunctionalExchange_allocating_component_exchange_getter(self):
        tested = FunctionalExchange()
        tested.get_allocating_component_exchange()
        pass

    def test_FunctionalExchange_allocating_component_exchange_setter(self):
        tested = FunctionalExchange()
        value = ComponentExchange()
        tested.set_allocating_component_exchange(value)
        pass

    def test_FunctionalExchange_realized_functional_exchanges_getter(self):
        tested = FunctionalExchange()
        tested.get_realized_functional_exchanges()
        pass

    def test_FunctionalExchange_realized_functional_exchanges_setter(self):
        tested = FunctionalExchange()
        value = FunctionalExchange()
        tested.get_realized_functional_exchanges().add(value)
        pass

    def test_FunctionalExchange_realizing_functional_exchanges_getter(self):
        tested = FunctionalExchange()
        tested.get_realizing_functional_exchanges()
        pass

    def test_FunctionalExchange_realizing_functional_exchanges_setter(self):
        tested = FunctionalExchange()
        value = FunctionalExchange()
        tested.get_realizing_functional_exchanges().add(value)
        pass

    def test_FunctionalExchange_realized_interactions_getter(self):
        tested = FunctionalExchange()
        tested.get_realized_interactions()
        pass

    def test_FunctionalExchange_realized_interactions_setter(self):
        tested = FunctionalExchange()
        value = Interaction()
        tested.get_realized_interactions().add(value)
        pass

    def test_ExchangeCategory_id_getter(self):
        tested = ExchangeCategory()
        tested.get_id()
        pass

    def test_ExchangeCategory_id_setter(self):
        tested = ExchangeCategory()
        value = "value"
        tested.set_id(value)
        pass

    def test_ExchangeCategory_sid_getter(self):
        tested = ExchangeCategory()
        tested.get_sid()
        pass

    def test_ExchangeCategory_sid_setter(self):
        tested = ExchangeCategory()
        value = "value"
        tested.set_sid(value)
        pass

    def test_ExchangeCategory_name_getter(self):
        tested = ExchangeCategory()
        tested.get_name()
        pass

    def test_ExchangeCategory_name_setter(self):
        tested = ExchangeCategory()
        value = "value"
        tested.set_name(value)
        pass

    def test_ExchangeCategory_summary_getter(self):
        tested = ExchangeCategory()
        tested.get_summary()
        pass

    def test_ExchangeCategory_summary_setter(self):
        tested = ExchangeCategory()
        value = "value"
        tested.set_summary(value)
        pass

    def test_ExchangeCategory_description_getter(self):
        tested = ExchangeCategory()
        tested.get_description()
        pass

    def test_ExchangeCategory_description_setter(self):
        tested = ExchangeCategory()
        value = "value"
        tested.set_description(value)
        pass

    def test_ExchangeCategory_status_getter(self):
        tested = ExchangeCategory()
        tested.get_status()
        pass

    def test_ExchangeCategory_status_setter(self):
        tested = ExchangeCategory()
        value = "value"
        tested.set_status(value)
        pass

    def test_ExchangeCategory_review_getter(self):
        tested = ExchangeCategory()
        tested.get_review()
        pass

    def test_ExchangeCategory_review_setter(self):
        tested = ExchangeCategory()
        value = "value"
        tested.set_review(value)
        pass

    def test_ExchangeCategory_visible_in_documentation_getter(self):
        tested = ExchangeCategory()
        tested.get_visible_in_documentation()
        pass

    def test_ExchangeCategory_visible_in_documentation_setter(self):
        tested = ExchangeCategory()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_ExchangeCategory_visible_for_traceability_getter(self):
        tested = ExchangeCategory()
        tested.get_visible_for_traceability()
        pass

    def test_ExchangeCategory_visible_for_traceability_setter(self):
        tested = ExchangeCategory()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_ExchangeCategory_owned_constraints_getter(self):
        tested = ExchangeCategory()
        tested.get_owned_constraints()
        pass

    def test_ExchangeCategory_constraints_getter(self):
        tested = ExchangeCategory()
        tested.get_constraints()
        pass

    def test_ExchangeCategory_constraints_setter(self):
        tested = ExchangeCategory()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_ExchangeCategory_owned_property_values_getter(self):
        tested = ExchangeCategory()
        tested.get_owned_property_values()
        pass

    def test_ExchangeCategory_applied_property_values_getter(self):
        tested = ExchangeCategory()
        tested.get_applied_property_values()
        pass

    def test_ExchangeCategory_applied_property_values_setter(self):
        tested = ExchangeCategory()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_ExchangeCategory_owned_property_value_groups_getter(self):
        tested = ExchangeCategory()
        tested.get_owned_property_value_groups()
        pass

    def test_ExchangeCategory_applied_property_value_groups_getter(self):
        tested = ExchangeCategory()
        tested.get_applied_property_value_groups()
        pass

    def test_ExchangeCategory_applied_property_value_groups_setter(self):
        tested = ExchangeCategory()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_ExchangeCategory_owned_enumeration_property_types_getter(self):
        tested = ExchangeCategory()
        tested.get_owned_enumeration_property_types()
        pass

    def test_ExchangeCategory_owned_diagrams_getter(self):
        tested = ExchangeCategory()
        tested.get_owned_diagrams()
        pass

    def test_ExchangeCategory_element_of_interest_for_diagrams_getter(self):
        tested = ExchangeCategory()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_ExchangeCategory_element_of_interest_for_diagrams_setter(self):
        tested = ExchangeCategory()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_ExchangeCategory_contextual_element_for_diagrams_getter(self):
        tested = ExchangeCategory()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_ExchangeCategory_contextual_element_for_diagrams_setter(self):
        tested = ExchangeCategory()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_ExchangeCategory_representing_diagrams_getter(self):
        tested = ExchangeCategory()
        tested.get_representing_diagrams()
        pass

    def test_ExchangeCategory__r_e_cs_getter(self):
        tested = ExchangeCategory()
        tested.get__r_e_cs()
        pass

    def test_ExchangeCategory__r_e_cs_setter(self):
        tested = ExchangeCategory()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_ExchangeCategory__r_p_ls_getter(self):
        tested = ExchangeCategory()
        tested.get__r_p_ls()
        pass

    def test_ExchangeCategory__r_p_ls_setter(self):
        tested = ExchangeCategory()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_ExchangeCategory_get_label(self):
        tested = ExchangeCategory()
        tested.get_label()
        pass

    def test_ExchangeCategory_get_element_type(self):
        tested = ExchangeCategory()
        tested.get_element_type()
        pass

    def test_ExchangeCategory_get_container(self):
        tested = ExchangeCategory()
        tested.get_container()
        pass

    def test_ExchangeCategory_get_contents(self):
        tested = ExchangeCategory()
        tested.get_contents()
        pass

    def test_ExchangeCategory_get_all_contents(self):
        tested = ExchangeCategory()
        tested.get_all_contents()
        pass

    def test_ExchangeCategory_get_all_contents_by_type(self):
        tested = ExchangeCategory()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_ExchangeCategory_get_available_s_b_queries(self):
        tested = ExchangeCategory()
        tested.get_available_s_b_queries()
        pass

    def test_ExchangeCategory_get_query_result(self):
        tested = ExchangeCategory()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_ExchangeCategory_exchanges_getter(self):
        tested = ExchangeCategory()
        tested.get_exchanges()
        pass

    def test_ExchangeCategory_exchanges_setter(self):
        tested = ExchangeCategory()
        value = FunctionalExchange()
        tested.get_exchanges().add(value)
        pass

    def test_FunctionalChain_id_getter(self):
        tested = FunctionalChain()
        tested.get_id()
        pass

    def test_FunctionalChain_id_setter(self):
        tested = FunctionalChain()
        value = "value"
        tested.set_id(value)
        pass

    def test_FunctionalChain_sid_getter(self):
        tested = FunctionalChain()
        tested.get_sid()
        pass

    def test_FunctionalChain_sid_setter(self):
        tested = FunctionalChain()
        value = "value"
        tested.set_sid(value)
        pass

    def test_FunctionalChain_name_getter(self):
        tested = FunctionalChain()
        tested.get_name()
        pass

    def test_FunctionalChain_name_setter(self):
        tested = FunctionalChain()
        value = "value"
        tested.set_name(value)
        pass

    def test_FunctionalChain_summary_getter(self):
        tested = FunctionalChain()
        tested.get_summary()
        pass

    def test_FunctionalChain_summary_setter(self):
        tested = FunctionalChain()
        value = "value"
        tested.set_summary(value)
        pass

    def test_FunctionalChain_description_getter(self):
        tested = FunctionalChain()
        tested.get_description()
        pass

    def test_FunctionalChain_description_setter(self):
        tested = FunctionalChain()
        value = "value"
        tested.set_description(value)
        pass

    def test_FunctionalChain_status_getter(self):
        tested = FunctionalChain()
        tested.get_status()
        pass

    def test_FunctionalChain_status_setter(self):
        tested = FunctionalChain()
        value = "value"
        tested.set_status(value)
        pass

    def test_FunctionalChain_review_getter(self):
        tested = FunctionalChain()
        tested.get_review()
        pass

    def test_FunctionalChain_review_setter(self):
        tested = FunctionalChain()
        value = "value"
        tested.set_review(value)
        pass

    def test_FunctionalChain_visible_in_documentation_getter(self):
        tested = FunctionalChain()
        tested.get_visible_in_documentation()
        pass

    def test_FunctionalChain_visible_in_documentation_setter(self):
        tested = FunctionalChain()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_FunctionalChain_visible_for_traceability_getter(self):
        tested = FunctionalChain()
        tested.get_visible_for_traceability()
        pass

    def test_FunctionalChain_visible_for_traceability_setter(self):
        tested = FunctionalChain()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_FunctionalChain_owned_constraints_getter(self):
        tested = FunctionalChain()
        tested.get_owned_constraints()
        pass

    def test_FunctionalChain_constraints_getter(self):
        tested = FunctionalChain()
        tested.get_constraints()
        pass

    def test_FunctionalChain_constraints_setter(self):
        tested = FunctionalChain()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_FunctionalChain_owned_property_values_getter(self):
        tested = FunctionalChain()
        tested.get_owned_property_values()
        pass

    def test_FunctionalChain_applied_property_values_getter(self):
        tested = FunctionalChain()
        tested.get_applied_property_values()
        pass

    def test_FunctionalChain_applied_property_values_setter(self):
        tested = FunctionalChain()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_FunctionalChain_owned_property_value_groups_getter(self):
        tested = FunctionalChain()
        tested.get_owned_property_value_groups()
        pass

    def test_FunctionalChain_applied_property_value_groups_getter(self):
        tested = FunctionalChain()
        tested.get_applied_property_value_groups()
        pass

    def test_FunctionalChain_applied_property_value_groups_setter(self):
        tested = FunctionalChain()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_FunctionalChain_owned_enumeration_property_types_getter(self):
        tested = FunctionalChain()
        tested.get_owned_enumeration_property_types()
        pass

    def test_FunctionalChain_owned_diagrams_getter(self):
        tested = FunctionalChain()
        tested.get_owned_diagrams()
        pass

    def test_FunctionalChain_element_of_interest_for_diagrams_getter(self):
        tested = FunctionalChain()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_FunctionalChain_element_of_interest_for_diagrams_setter(self):
        tested = FunctionalChain()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_FunctionalChain_contextual_element_for_diagrams_getter(self):
        tested = FunctionalChain()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_FunctionalChain_contextual_element_for_diagrams_setter(self):
        tested = FunctionalChain()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_FunctionalChain_representing_diagrams_getter(self):
        tested = FunctionalChain()
        tested.get_representing_diagrams()
        pass

    def test_FunctionalChain__r_e_cs_getter(self):
        tested = FunctionalChain()
        tested.get__r_e_cs()
        pass

    def test_FunctionalChain__r_e_cs_setter(self):
        tested = FunctionalChain()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_FunctionalChain__r_p_ls_getter(self):
        tested = FunctionalChain()
        tested.get__r_p_ls()
        pass

    def test_FunctionalChain__r_p_ls_setter(self):
        tested = FunctionalChain()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_FunctionalChain_get_label(self):
        tested = FunctionalChain()
        tested.get_label()
        pass

    def test_FunctionalChain_get_element_type(self):
        tested = FunctionalChain()
        tested.get_element_type()
        pass

    def test_FunctionalChain_get_container(self):
        tested = FunctionalChain()
        tested.get_container()
        pass

    def test_FunctionalChain_get_contents(self):
        tested = FunctionalChain()
        tested.get_contents()
        pass

    def test_FunctionalChain_get_all_contents(self):
        tested = FunctionalChain()
        tested.get_all_contents()
        pass

    def test_FunctionalChain_get_all_contents_by_type(self):
        tested = FunctionalChain()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_FunctionalChain_get_available_s_b_queries(self):
        tested = FunctionalChain()
        tested.get_available_s_b_queries()
        pass

    def test_FunctionalChain_get_query_result(self):
        tested = FunctionalChain()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_FunctionalChain_pre_condition_getter(self):
        tested = FunctionalChain()
        tested.get_pre_condition()
        pass

    def test_FunctionalChain_pre_condition_setter(self):
        tested = FunctionalChain()
        value = Constraint()
        tested.set_pre_condition(value)
        pass

    def test_FunctionalChain_post_condition_getter(self):
        tested = FunctionalChain()
        tested.get_post_condition()
        pass

    def test_FunctionalChain_post_condition_setter(self):
        tested = FunctionalChain()
        value = Constraint()
        tested.set_post_condition(value)
        pass

    def test_FunctionalChain_involved_functions_getter(self):
        tested = FunctionalChain()
        tested.get_involved_functions()
        pass

    def test_FunctionalChain_involved_functional_exchanges_getter(self):
        tested = FunctionalChain()
        tested.get_involved_functional_exchanges()
        pass

    def test_FunctionalChain_involved_functional_chains_getter(self):
        tested = FunctionalChain()
        tested.get_involved_functional_chains()
        pass

    def test_FunctionalChain_involving_capabilities_getter(self):
        tested = FunctionalChain()
        tested.get_involving_capabilities()
        pass

    def test_FunctionalChain_involving_capabilities_setter(self):
        tested = FunctionalChain()
        value = CapabilityRealization()
        tested.get_involving_capabilities().add(value)
        pass

    def test_FunctionalChain_available_in_states_getter(self):
        tested = FunctionalChain()
        tested.get_available_in_states()
        pass

    def test_FunctionalChain_available_in_states_setter(self):
        tested = FunctionalChain()
        value = State()
        tested.get_available_in_states().add(value)
        pass

    def test_FunctionalChain_realized_operational_processes_getter(self):
        tested = FunctionalChain()
        tested.get_realized_operational_processes()
        pass

    def test_FunctionalChain_realized_operational_processes_setter(self):
        tested = FunctionalChain()
        value = OperationalProcess()
        tested.get_realized_operational_processes().add(value)
        pass

    def test_FunctionalChain_realized_functional_chains_getter(self):
        tested = FunctionalChain()
        tested.get_realized_functional_chains()
        pass

    def test_FunctionalChain_realized_functional_chains_setter(self):
        tested = FunctionalChain()
        value = FunctionalChain()
        tested.get_realized_functional_chains().add(value)
        pass

    def test_FunctionalChain_realizing_functional_chains_getter(self):
        tested = FunctionalChain()
        tested.get_realizing_functional_chains()
        pass

    def test_FunctionalChain_realizing_functional_chains_setter(self):
        tested = FunctionalChain()
        value = FunctionalChain()
        tested.get_realizing_functional_chains().add(value)
        pass

    def test_ComponentPort_id_getter(self):
        tested = ComponentPort()
        tested.get_id()
        pass

    def test_ComponentPort_id_setter(self):
        tested = ComponentPort()
        value = "value"
        tested.set_id(value)
        pass

    def test_ComponentPort_sid_getter(self):
        tested = ComponentPort()
        tested.get_sid()
        pass

    def test_ComponentPort_sid_setter(self):
        tested = ComponentPort()
        value = "value"
        tested.set_sid(value)
        pass

    def test_ComponentPort_name_getter(self):
        tested = ComponentPort()
        tested.get_name()
        pass

    def test_ComponentPort_name_setter(self):
        tested = ComponentPort()
        value = "value"
        tested.set_name(value)
        pass

    def test_ComponentPort_summary_getter(self):
        tested = ComponentPort()
        tested.get_summary()
        pass

    def test_ComponentPort_summary_setter(self):
        tested = ComponentPort()
        value = "value"
        tested.set_summary(value)
        pass

    def test_ComponentPort_description_getter(self):
        tested = ComponentPort()
        tested.get_description()
        pass

    def test_ComponentPort_description_setter(self):
        tested = ComponentPort()
        value = "value"
        tested.set_description(value)
        pass

    def test_ComponentPort_status_getter(self):
        tested = ComponentPort()
        tested.get_status()
        pass

    def test_ComponentPort_status_setter(self):
        tested = ComponentPort()
        value = "value"
        tested.set_status(value)
        pass

    def test_ComponentPort_review_getter(self):
        tested = ComponentPort()
        tested.get_review()
        pass

    def test_ComponentPort_review_setter(self):
        tested = ComponentPort()
        value = "value"
        tested.set_review(value)
        pass

    def test_ComponentPort_visible_in_documentation_getter(self):
        tested = ComponentPort()
        tested.get_visible_in_documentation()
        pass

    def test_ComponentPort_visible_in_documentation_setter(self):
        tested = ComponentPort()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_ComponentPort_visible_for_traceability_getter(self):
        tested = ComponentPort()
        tested.get_visible_for_traceability()
        pass

    def test_ComponentPort_visible_for_traceability_setter(self):
        tested = ComponentPort()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_ComponentPort_owned_constraints_getter(self):
        tested = ComponentPort()
        tested.get_owned_constraints()
        pass

    def test_ComponentPort_constraints_getter(self):
        tested = ComponentPort()
        tested.get_constraints()
        pass

    def test_ComponentPort_constraints_setter(self):
        tested = ComponentPort()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_ComponentPort_owned_property_values_getter(self):
        tested = ComponentPort()
        tested.get_owned_property_values()
        pass

    def test_ComponentPort_applied_property_values_getter(self):
        tested = ComponentPort()
        tested.get_applied_property_values()
        pass

    def test_ComponentPort_applied_property_values_setter(self):
        tested = ComponentPort()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_ComponentPort_owned_property_value_groups_getter(self):
        tested = ComponentPort()
        tested.get_owned_property_value_groups()
        pass

    def test_ComponentPort_applied_property_value_groups_getter(self):
        tested = ComponentPort()
        tested.get_applied_property_value_groups()
        pass

    def test_ComponentPort_applied_property_value_groups_setter(self):
        tested = ComponentPort()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_ComponentPort_owned_enumeration_property_types_getter(self):
        tested = ComponentPort()
        tested.get_owned_enumeration_property_types()
        pass

    def test_ComponentPort_owned_diagrams_getter(self):
        tested = ComponentPort()
        tested.get_owned_diagrams()
        pass

    def test_ComponentPort_element_of_interest_for_diagrams_getter(self):
        tested = ComponentPort()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_ComponentPort_element_of_interest_for_diagrams_setter(self):
        tested = ComponentPort()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_ComponentPort_contextual_element_for_diagrams_getter(self):
        tested = ComponentPort()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_ComponentPort_contextual_element_for_diagrams_setter(self):
        tested = ComponentPort()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_ComponentPort_representing_diagrams_getter(self):
        tested = ComponentPort()
        tested.get_representing_diagrams()
        pass

    def test_ComponentPort__r_e_cs_getter(self):
        tested = ComponentPort()
        tested.get__r_e_cs()
        pass

    def test_ComponentPort__r_e_cs_setter(self):
        tested = ComponentPort()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_ComponentPort__r_p_ls_getter(self):
        tested = ComponentPort()
        tested.get__r_p_ls()
        pass

    def test_ComponentPort__r_p_ls_setter(self):
        tested = ComponentPort()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_ComponentPort_get_label(self):
        tested = ComponentPort()
        tested.get_label()
        pass

    def test_ComponentPort_get_element_type(self):
        tested = ComponentPort()
        tested.get_element_type()
        pass

    def test_ComponentPort_get_container(self):
        tested = ComponentPort()
        tested.get_container()
        pass

    def test_ComponentPort_get_contents(self):
        tested = ComponentPort()
        tested.get_contents()
        pass

    def test_ComponentPort_get_all_contents(self):
        tested = ComponentPort()
        tested.get_all_contents()
        pass

    def test_ComponentPort_get_all_contents_by_type(self):
        tested = ComponentPort()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_ComponentPort_get_available_s_b_queries(self):
        tested = ComponentPort()
        tested.get_available_s_b_queries()
        pass

    def test_ComponentPort_get_query_result(self):
        tested = ComponentPort()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_ComponentPort_orientation_getter(self):
        tested = ComponentPort()
        tested.get_orientation()
        pass

    def test_ComponentPort_orientation_setter(self):
        tested = ComponentPort()
        value = OrientationPortKind()
        tested.set_orientation(value)
        pass

    def test_ComponentPort_component_exchanges_getter(self):
        tested = ComponentPort()
        tested.get_component_exchanges()
        pass

    def test_ComponentPort_component_exchanges_setter(self):
        tested = ComponentPort()
        value = ComponentExchange()
        tested.get_component_exchanges().add(value)
        pass

    def test_ComponentPort_allocated_function_ports_getter(self):
        tested = ComponentPort()
        tested.get_allocated_function_ports()
        pass

    def test_ComponentPort_allocated_function_ports_setter(self):
        tested = ComponentPort()
        value = FunctionOutputPort()
        tested.get_allocated_function_ports().add(value)
        pass

    def test_ComponentPort_provided_interfaces_getter(self):
        tested = ComponentPort()
        tested.get_provided_interfaces()
        pass

    def test_ComponentPort_provided_interfaces_setter(self):
        tested = ComponentPort()
        value = Interface()
        tested.get_provided_interfaces().add(value)
        pass

    def test_ComponentPort_required_interfaces_getter(self):
        tested = ComponentPort()
        tested.get_required_interfaces()
        pass

    def test_ComponentPort_required_interfaces_setter(self):
        tested = ComponentPort()
        value = Interface()
        tested.get_required_interfaces().add(value)
        pass

    def test_ComponentPort_allocating_physical_ports_getter(self):
        tested = ComponentPort()
        tested.get_allocating_physical_ports()
        pass

    def test_ComponentPort_allocating_physical_ports_setter(self):
        tested = ComponentPort()
        value = PhysicalPort()
        tested.set_allocating_physical_ports(value)
        pass

    def test_ComponentPort_realized_component_ports_getter(self):
        tested = ComponentPort()
        tested.get_realized_component_ports()
        pass

    def test_ComponentPort_realized_component_ports_setter(self):
        tested = ComponentPort()
        value = ComponentPort()
        tested.get_realized_component_ports().add(value)
        pass

    def test_ComponentPort_realizing_component_ports_getter(self):
        tested = ComponentPort()
        tested.get_realizing_component_ports()
        pass

    def test_ComponentPort_realizing_component_ports_setter(self):
        tested = ComponentPort()
        value = ComponentPort()
        tested.get_realizing_component_ports().add(value)
        pass

    def test_ComponentExchange_id_getter(self):
        tested = ComponentExchange()
        tested.get_id()
        pass

    def test_ComponentExchange_id_setter(self):
        tested = ComponentExchange()
        value = "value"
        tested.set_id(value)
        pass

    def test_ComponentExchange_sid_getter(self):
        tested = ComponentExchange()
        tested.get_sid()
        pass

    def test_ComponentExchange_sid_setter(self):
        tested = ComponentExchange()
        value = "value"
        tested.set_sid(value)
        pass

    def test_ComponentExchange_name_getter(self):
        tested = ComponentExchange()
        tested.get_name()
        pass

    def test_ComponentExchange_name_setter(self):
        tested = ComponentExchange()
        value = "value"
        tested.set_name(value)
        pass

    def test_ComponentExchange_summary_getter(self):
        tested = ComponentExchange()
        tested.get_summary()
        pass

    def test_ComponentExchange_summary_setter(self):
        tested = ComponentExchange()
        value = "value"
        tested.set_summary(value)
        pass

    def test_ComponentExchange_description_getter(self):
        tested = ComponentExchange()
        tested.get_description()
        pass

    def test_ComponentExchange_description_setter(self):
        tested = ComponentExchange()
        value = "value"
        tested.set_description(value)
        pass

    def test_ComponentExchange_status_getter(self):
        tested = ComponentExchange()
        tested.get_status()
        pass

    def test_ComponentExchange_status_setter(self):
        tested = ComponentExchange()
        value = "value"
        tested.set_status(value)
        pass

    def test_ComponentExchange_review_getter(self):
        tested = ComponentExchange()
        tested.get_review()
        pass

    def test_ComponentExchange_review_setter(self):
        tested = ComponentExchange()
        value = "value"
        tested.set_review(value)
        pass

    def test_ComponentExchange_visible_in_documentation_getter(self):
        tested = ComponentExchange()
        tested.get_visible_in_documentation()
        pass

    def test_ComponentExchange_visible_in_documentation_setter(self):
        tested = ComponentExchange()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_ComponentExchange_visible_for_traceability_getter(self):
        tested = ComponentExchange()
        tested.get_visible_for_traceability()
        pass

    def test_ComponentExchange_visible_for_traceability_setter(self):
        tested = ComponentExchange()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_ComponentExchange_owned_constraints_getter(self):
        tested = ComponentExchange()
        tested.get_owned_constraints()
        pass

    def test_ComponentExchange_constraints_getter(self):
        tested = ComponentExchange()
        tested.get_constraints()
        pass

    def test_ComponentExchange_constraints_setter(self):
        tested = ComponentExchange()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_ComponentExchange_owned_property_values_getter(self):
        tested = ComponentExchange()
        tested.get_owned_property_values()
        pass

    def test_ComponentExchange_applied_property_values_getter(self):
        tested = ComponentExchange()
        tested.get_applied_property_values()
        pass

    def test_ComponentExchange_applied_property_values_setter(self):
        tested = ComponentExchange()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_ComponentExchange_owned_property_value_groups_getter(self):
        tested = ComponentExchange()
        tested.get_owned_property_value_groups()
        pass

    def test_ComponentExchange_applied_property_value_groups_getter(self):
        tested = ComponentExchange()
        tested.get_applied_property_value_groups()
        pass

    def test_ComponentExchange_applied_property_value_groups_setter(self):
        tested = ComponentExchange()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_ComponentExchange_owned_enumeration_property_types_getter(self):
        tested = ComponentExchange()
        tested.get_owned_enumeration_property_types()
        pass

    def test_ComponentExchange_owned_diagrams_getter(self):
        tested = ComponentExchange()
        tested.get_owned_diagrams()
        pass

    def test_ComponentExchange_element_of_interest_for_diagrams_getter(self):
        tested = ComponentExchange()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_ComponentExchange_element_of_interest_for_diagrams_setter(self):
        tested = ComponentExchange()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_ComponentExchange_contextual_element_for_diagrams_getter(self):
        tested = ComponentExchange()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_ComponentExchange_contextual_element_for_diagrams_setter(self):
        tested = ComponentExchange()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_ComponentExchange_representing_diagrams_getter(self):
        tested = ComponentExchange()
        tested.get_representing_diagrams()
        pass

    def test_ComponentExchange__r_e_cs_getter(self):
        tested = ComponentExchange()
        tested.get__r_e_cs()
        pass

    def test_ComponentExchange__r_e_cs_setter(self):
        tested = ComponentExchange()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_ComponentExchange__r_p_ls_getter(self):
        tested = ComponentExchange()
        tested.get__r_p_ls()
        pass

    def test_ComponentExchange__r_p_ls_setter(self):
        tested = ComponentExchange()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_ComponentExchange_get_label(self):
        tested = ComponentExchange()
        tested.get_label()
        pass

    def test_ComponentExchange_get_element_type(self):
        tested = ComponentExchange()
        tested.get_element_type()
        pass

    def test_ComponentExchange_get_container(self):
        tested = ComponentExchange()
        tested.get_container()
        pass

    def test_ComponentExchange_get_contents(self):
        tested = ComponentExchange()
        tested.get_contents()
        pass

    def test_ComponentExchange_get_all_contents(self):
        tested = ComponentExchange()
        tested.get_all_contents()
        pass

    def test_ComponentExchange_get_all_contents_by_type(self):
        tested = ComponentExchange()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_ComponentExchange_get_available_s_b_queries(self):
        tested = ComponentExchange()
        tested.get_available_s_b_queries()
        pass

    def test_ComponentExchange_get_query_result(self):
        tested = ComponentExchange()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_ComponentExchange_invoking_sequence_messages_getter(self):
        tested = ComponentExchange()
        tested.get_invoking_sequence_messages()
        pass

    def test_ComponentExchange_kind_getter(self):
        tested = ComponentExchange()
        tested.get_kind()
        pass

    def test_ComponentExchange_kind_setter(self):
        tested = ComponentExchange()
        value = ComponentExchangeKind()
        tested.set_kind(value)
        pass

    def test_ComponentExchange_connected_component_ports_getter(self):
        tested = ComponentExchange()
        tested.get_connected_component_ports()
        pass

    def test_ComponentExchange_connected_component_ports_setter(self):
        tested = ComponentExchange()
        value = ComponentPort()
        tested.get_connected_component_ports().add(value)
        pass

    def test_ComponentExchange_connected_components_getter(self):
        tested = ComponentExchange()
        tested.get_connected_components()
        pass

    def test_ComponentExchange_connected_components_setter(self):
        tested = ComponentExchange()
        value = PhysicalActor()
        tested.get_connected_components().add(value)
        pass

    def test_ComponentExchange_categories_getter(self):
        tested = ComponentExchange()
        tested.get_categories()
        pass

    def test_ComponentExchange_categories_setter(self):
        tested = ComponentExchange()
        value = ComponentExchangeCategory()
        tested.get_categories().add(value)
        pass

    def test_ComponentExchange_allocated_functional_exchanges_getter(self):
        tested = ComponentExchange()
        tested.get_allocated_functional_exchanges()
        pass

    def test_ComponentExchange_allocated_functional_exchanges_setter(self):
        tested = ComponentExchange()
        value = FunctionalExchange()
        tested.get_allocated_functional_exchanges().add(value)
        pass

    def test_ComponentExchange_convoyed_informations_getter(self):
        tested = ComponentExchange()
        tested.get_convoyed_informations()
        pass

    def test_ComponentExchange_convoyed_informations_setter(self):
        tested = ComponentExchange()
        value = ExchangeItem()
        tested.get_convoyed_informations().add(value)
        pass

    def test_ComponentExchange_allocating_physical_link_getter(self):
        tested = ComponentExchange()
        tested.get_allocating_physical_link()
        pass

    def test_ComponentExchange_allocating_physical_link_setter(self):
        tested = ComponentExchange()
        value = PhysicalLink()
        tested.set_allocating_physical_link(value)
        pass

    def test_ComponentExchange_allocating_physical_path_getter(self):
        tested = ComponentExchange()
        tested.get_allocating_physical_path()
        pass

    def test_ComponentExchange_allocating_physical_path_setter(self):
        tested = ComponentExchange()
        value = PhysicalPath()
        tested.set_allocating_physical_path(value)
        pass

    def test_ComponentExchange_realized_communication_means_getter(self):
        tested = ComponentExchange()
        tested.get_realized_communication_means()
        pass

    def test_ComponentExchange_realized_communication_means_setter(self):
        tested = ComponentExchange()
        value = CommunicationMean()
        tested.get_realized_communication_means().add(value)
        pass

    def test_ComponentExchange_realized_component_exchanges_getter(self):
        tested = ComponentExchange()
        tested.get_realized_component_exchanges()
        pass

    def test_ComponentExchange_realized_component_exchanges_setter(self):
        tested = ComponentExchange()
        value = ComponentExchange()
        tested.get_realized_component_exchanges().add(value)
        pass

    def test_ComponentExchange_realizing_component_exchanges_getter(self):
        tested = ComponentExchange()
        tested.get_realizing_component_exchanges()
        pass

    def test_ComponentExchange_realizing_component_exchanges_setter(self):
        tested = ComponentExchange()
        value = ComponentExchange()
        tested.get_realizing_component_exchanges().add(value)
        pass

    def test_ComponentExchangeCategory_id_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_id()
        pass

    def test_ComponentExchangeCategory_id_setter(self):
        tested = ComponentExchangeCategory()
        value = "value"
        tested.set_id(value)
        pass

    def test_ComponentExchangeCategory_sid_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_sid()
        pass

    def test_ComponentExchangeCategory_sid_setter(self):
        tested = ComponentExchangeCategory()
        value = "value"
        tested.set_sid(value)
        pass

    def test_ComponentExchangeCategory_name_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_name()
        pass

    def test_ComponentExchangeCategory_name_setter(self):
        tested = ComponentExchangeCategory()
        value = "value"
        tested.set_name(value)
        pass

    def test_ComponentExchangeCategory_summary_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_summary()
        pass

    def test_ComponentExchangeCategory_summary_setter(self):
        tested = ComponentExchangeCategory()
        value = "value"
        tested.set_summary(value)
        pass

    def test_ComponentExchangeCategory_description_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_description()
        pass

    def test_ComponentExchangeCategory_description_setter(self):
        tested = ComponentExchangeCategory()
        value = "value"
        tested.set_description(value)
        pass

    def test_ComponentExchangeCategory_status_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_status()
        pass

    def test_ComponentExchangeCategory_status_setter(self):
        tested = ComponentExchangeCategory()
        value = "value"
        tested.set_status(value)
        pass

    def test_ComponentExchangeCategory_review_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_review()
        pass

    def test_ComponentExchangeCategory_review_setter(self):
        tested = ComponentExchangeCategory()
        value = "value"
        tested.set_review(value)
        pass

    def test_ComponentExchangeCategory_visible_in_documentation_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_visible_in_documentation()
        pass

    def test_ComponentExchangeCategory_visible_in_documentation_setter(self):
        tested = ComponentExchangeCategory()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_ComponentExchangeCategory_visible_for_traceability_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_visible_for_traceability()
        pass

    def test_ComponentExchangeCategory_visible_for_traceability_setter(self):
        tested = ComponentExchangeCategory()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_ComponentExchangeCategory_owned_constraints_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_owned_constraints()
        pass

    def test_ComponentExchangeCategory_constraints_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_constraints()
        pass

    def test_ComponentExchangeCategory_constraints_setter(self):
        tested = ComponentExchangeCategory()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_ComponentExchangeCategory_owned_property_values_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_owned_property_values()
        pass

    def test_ComponentExchangeCategory_applied_property_values_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_applied_property_values()
        pass

    def test_ComponentExchangeCategory_applied_property_values_setter(self):
        tested = ComponentExchangeCategory()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_ComponentExchangeCategory_owned_property_value_groups_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_owned_property_value_groups()
        pass

    def test_ComponentExchangeCategory_applied_property_value_groups_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_applied_property_value_groups()
        pass

    def test_ComponentExchangeCategory_applied_property_value_groups_setter(self):
        tested = ComponentExchangeCategory()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_ComponentExchangeCategory_owned_enumeration_property_types_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_owned_enumeration_property_types()
        pass

    def test_ComponentExchangeCategory_owned_diagrams_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_owned_diagrams()
        pass

    def test_ComponentExchangeCategory_element_of_interest_for_diagrams_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_ComponentExchangeCategory_element_of_interest_for_diagrams_setter(self):
        tested = ComponentExchangeCategory()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_ComponentExchangeCategory_contextual_element_for_diagrams_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_ComponentExchangeCategory_contextual_element_for_diagrams_setter(self):
        tested = ComponentExchangeCategory()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_ComponentExchangeCategory_representing_diagrams_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_representing_diagrams()
        pass

    def test_ComponentExchangeCategory__r_e_cs_getter(self):
        tested = ComponentExchangeCategory()
        tested.get__r_e_cs()
        pass

    def test_ComponentExchangeCategory__r_e_cs_setter(self):
        tested = ComponentExchangeCategory()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_ComponentExchangeCategory__r_p_ls_getter(self):
        tested = ComponentExchangeCategory()
        tested.get__r_p_ls()
        pass

    def test_ComponentExchangeCategory__r_p_ls_setter(self):
        tested = ComponentExchangeCategory()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_ComponentExchangeCategory_get_label(self):
        tested = ComponentExchangeCategory()
        tested.get_label()
        pass

    def test_ComponentExchangeCategory_get_element_type(self):
        tested = ComponentExchangeCategory()
        tested.get_element_type()
        pass

    def test_ComponentExchangeCategory_get_container(self):
        tested = ComponentExchangeCategory()
        tested.get_container()
        pass

    def test_ComponentExchangeCategory_get_contents(self):
        tested = ComponentExchangeCategory()
        tested.get_contents()
        pass

    def test_ComponentExchangeCategory_get_all_contents(self):
        tested = ComponentExchangeCategory()
        tested.get_all_contents()
        pass

    def test_ComponentExchangeCategory_get_all_contents_by_type(self):
        tested = ComponentExchangeCategory()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_ComponentExchangeCategory_get_available_s_b_queries(self):
        tested = ComponentExchangeCategory()
        tested.get_available_s_b_queries()
        pass

    def test_ComponentExchangeCategory_get_query_result(self):
        tested = ComponentExchangeCategory()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_ComponentExchangeCategory_exchanges_getter(self):
        tested = ComponentExchangeCategory()
        tested.get_exchanges()
        pass

    def test_ComponentExchangeCategory_exchanges_setter(self):
        tested = ComponentExchangeCategory()
        value = ComponentExchange()
        tested.get_exchanges().add(value)
        pass

    def test_DataPkg_owned_classes_getter(self):
        tested = DataPkg()
        tested.get_owned_classes()
        pass

    def test_DataPkg_owned_classes_setter(self):
        tested = DataPkg()
        value = Class()
        tested.get_owned_classes().add(value)
        pass

    def test_DataPkg_owned_data_pkgs_getter(self):
        tested = DataPkg()
        tested.get_owned_data_pkgs()
        pass

    def test_DataPkg_owned_data_pkgs_setter(self):
        tested = DataPkg()
        value = DataPkg()
        tested.get_owned_data_pkgs().add(value)
        pass

    def test_Class_id_getter(self):
        tested = Class()
        tested.get_id()
        pass

    def test_Class_id_setter(self):
        tested = Class()
        value = "value"
        tested.set_id(value)
        pass

    def test_Class_sid_getter(self):
        tested = Class()
        tested.get_sid()
        pass

    def test_Class_sid_setter(self):
        tested = Class()
        value = "value"
        tested.set_sid(value)
        pass

    def test_Class_name_getter(self):
        tested = Class()
        tested.get_name()
        pass

    def test_Class_name_setter(self):
        tested = Class()
        value = "value"
        tested.set_name(value)
        pass

    def test_Class_summary_getter(self):
        tested = Class()
        tested.get_summary()
        pass

    def test_Class_summary_setter(self):
        tested = Class()
        value = "value"
        tested.set_summary(value)
        pass

    def test_Class_description_getter(self):
        tested = Class()
        tested.get_description()
        pass

    def test_Class_description_setter(self):
        tested = Class()
        value = "value"
        tested.set_description(value)
        pass

    def test_Class_status_getter(self):
        tested = Class()
        tested.get_status()
        pass

    def test_Class_status_setter(self):
        tested = Class()
        value = "value"
        tested.set_status(value)
        pass

    def test_Class_review_getter(self):
        tested = Class()
        tested.get_review()
        pass

    def test_Class_review_setter(self):
        tested = Class()
        value = "value"
        tested.set_review(value)
        pass

    def test_Class_visible_in_documentation_getter(self):
        tested = Class()
        tested.get_visible_in_documentation()
        pass

    def test_Class_visible_in_documentation_setter(self):
        tested = Class()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_Class_visible_for_traceability_getter(self):
        tested = Class()
        tested.get_visible_for_traceability()
        pass

    def test_Class_visible_for_traceability_setter(self):
        tested = Class()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_Class_owned_constraints_getter(self):
        tested = Class()
        tested.get_owned_constraints()
        pass

    def test_Class_constraints_getter(self):
        tested = Class()
        tested.get_constraints()
        pass

    def test_Class_constraints_setter(self):
        tested = Class()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_Class_owned_property_values_getter(self):
        tested = Class()
        tested.get_owned_property_values()
        pass

    def test_Class_applied_property_values_getter(self):
        tested = Class()
        tested.get_applied_property_values()
        pass

    def test_Class_applied_property_values_setter(self):
        tested = Class()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_Class_owned_property_value_groups_getter(self):
        tested = Class()
        tested.get_owned_property_value_groups()
        pass

    def test_Class_applied_property_value_groups_getter(self):
        tested = Class()
        tested.get_applied_property_value_groups()
        pass

    def test_Class_applied_property_value_groups_setter(self):
        tested = Class()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_Class_owned_enumeration_property_types_getter(self):
        tested = Class()
        tested.get_owned_enumeration_property_types()
        pass

    def test_Class_owned_diagrams_getter(self):
        tested = Class()
        tested.get_owned_diagrams()
        pass

    def test_Class_element_of_interest_for_diagrams_getter(self):
        tested = Class()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_Class_element_of_interest_for_diagrams_setter(self):
        tested = Class()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_Class_contextual_element_for_diagrams_getter(self):
        tested = Class()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_Class_contextual_element_for_diagrams_setter(self):
        tested = Class()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_Class_representing_diagrams_getter(self):
        tested = Class()
        tested.get_representing_diagrams()
        pass

    def test_Class__r_e_cs_getter(self):
        tested = Class()
        tested.get__r_e_cs()
        pass

    def test_Class__r_e_cs_setter(self):
        tested = Class()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_Class__r_p_ls_getter(self):
        tested = Class()
        tested.get__r_p_ls()
        pass

    def test_Class__r_p_ls_setter(self):
        tested = Class()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_Class_get_label(self):
        tested = Class()
        tested.get_label()
        pass

    def test_Class_get_element_type(self):
        tested = Class()
        tested.get_element_type()
        pass

    def test_Class_get_container(self):
        tested = Class()
        tested.get_container()
        pass

    def test_Class_get_contents(self):
        tested = Class()
        tested.get_contents()
        pass

    def test_Class_get_all_contents(self):
        tested = Class()
        tested.get_all_contents()
        pass

    def test_Class_get_all_contents_by_type(self):
        tested = Class()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_Class_get_available_s_b_queries(self):
        tested = Class()
        tested.get_available_s_b_queries()
        pass

    def test_Class_get_query_result(self):
        tested = Class()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_Class_abstract_getter(self):
        tested = Class()
        tested.get_abstract()
        pass

    def test_Class_abstract_setter(self):
        tested = Class()
        value = True
        tested.set_abstract(value)
        pass

    def test_Class_final_getter(self):
        tested = Class()
        tested.get_final()
        pass

    def test_Class_final_setter(self):
        tested = Class()
        value = True
        tested.set_final(value)
        pass

    def test_Class_primitive_getter(self):
        tested = Class()
        tested.get_primitive()
        pass

    def test_Class_primitive_setter(self):
        tested = Class()
        value = True
        tested.set_primitive(value)
        pass

    def test_Class_visibility_getter(self):
        tested = Class()
        tested.get_visibility()
        pass

    def test_Class_visibility_setter(self):
        tested = Class()
        value = VisibilityKind()
        tested.set_visibility(value)
        pass

    def test_Class_contained_properties_getter(self):
        tested = Class()
        tested.get_contained_properties()
        pass

    def test_Class_contained_operations_getter(self):
        tested = Class()
        tested.get_contained_operations()
        pass

    def test_Collection_id_getter(self):
        tested = Collection()
        tested.get_id()
        pass

    def test_Collection_id_setter(self):
        tested = Collection()
        value = "value"
        tested.set_id(value)
        pass

    def test_Collection_sid_getter(self):
        tested = Collection()
        tested.get_sid()
        pass

    def test_Collection_sid_setter(self):
        tested = Collection()
        value = "value"
        tested.set_sid(value)
        pass

    def test_Collection_name_getter(self):
        tested = Collection()
        tested.get_name()
        pass

    def test_Collection_name_setter(self):
        tested = Collection()
        value = "value"
        tested.set_name(value)
        pass

    def test_Collection_summary_getter(self):
        tested = Collection()
        tested.get_summary()
        pass

    def test_Collection_summary_setter(self):
        tested = Collection()
        value = "value"
        tested.set_summary(value)
        pass

    def test_Collection_description_getter(self):
        tested = Collection()
        tested.get_description()
        pass

    def test_Collection_description_setter(self):
        tested = Collection()
        value = "value"
        tested.set_description(value)
        pass

    def test_Collection_status_getter(self):
        tested = Collection()
        tested.get_status()
        pass

    def test_Collection_status_setter(self):
        tested = Collection()
        value = "value"
        tested.set_status(value)
        pass

    def test_Collection_review_getter(self):
        tested = Collection()
        tested.get_review()
        pass

    def test_Collection_review_setter(self):
        tested = Collection()
        value = "value"
        tested.set_review(value)
        pass

    def test_Collection_visible_in_documentation_getter(self):
        tested = Collection()
        tested.get_visible_in_documentation()
        pass

    def test_Collection_visible_in_documentation_setter(self):
        tested = Collection()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_Collection_visible_for_traceability_getter(self):
        tested = Collection()
        tested.get_visible_for_traceability()
        pass

    def test_Collection_visible_for_traceability_setter(self):
        tested = Collection()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_Collection_owned_constraints_getter(self):
        tested = Collection()
        tested.get_owned_constraints()
        pass

    def test_Collection_constraints_getter(self):
        tested = Collection()
        tested.get_constraints()
        pass

    def test_Collection_constraints_setter(self):
        tested = Collection()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_Collection_owned_property_values_getter(self):
        tested = Collection()
        tested.get_owned_property_values()
        pass

    def test_Collection_applied_property_values_getter(self):
        tested = Collection()
        tested.get_applied_property_values()
        pass

    def test_Collection_applied_property_values_setter(self):
        tested = Collection()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_Collection_owned_property_value_groups_getter(self):
        tested = Collection()
        tested.get_owned_property_value_groups()
        pass

    def test_Collection_applied_property_value_groups_getter(self):
        tested = Collection()
        tested.get_applied_property_value_groups()
        pass

    def test_Collection_applied_property_value_groups_setter(self):
        tested = Collection()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_Collection_owned_enumeration_property_types_getter(self):
        tested = Collection()
        tested.get_owned_enumeration_property_types()
        pass

    def test_Collection_owned_diagrams_getter(self):
        tested = Collection()
        tested.get_owned_diagrams()
        pass

    def test_Collection_element_of_interest_for_diagrams_getter(self):
        tested = Collection()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_Collection_element_of_interest_for_diagrams_setter(self):
        tested = Collection()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_Collection_contextual_element_for_diagrams_getter(self):
        tested = Collection()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_Collection_contextual_element_for_diagrams_setter(self):
        tested = Collection()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_Collection_representing_diagrams_getter(self):
        tested = Collection()
        tested.get_representing_diagrams()
        pass

    def test_Collection__r_e_cs_getter(self):
        tested = Collection()
        tested.get__r_e_cs()
        pass

    def test_Collection__r_e_cs_setter(self):
        tested = Collection()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_Collection__r_p_ls_getter(self):
        tested = Collection()
        tested.get__r_p_ls()
        pass

    def test_Collection__r_p_ls_setter(self):
        tested = Collection()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_Collection_get_label(self):
        tested = Collection()
        tested.get_label()
        pass

    def test_Collection_get_element_type(self):
        tested = Collection()
        tested.get_element_type()
        pass

    def test_Collection_get_container(self):
        tested = Collection()
        tested.get_container()
        pass

    def test_Collection_get_contents(self):
        tested = Collection()
        tested.get_contents()
        pass

    def test_Collection_get_all_contents(self):
        tested = Collection()
        tested.get_all_contents()
        pass

    def test_Collection_get_all_contents_by_type(self):
        tested = Collection()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_Collection_get_available_s_b_queries(self):
        tested = Collection()
        tested.get_available_s_b_queries()
        pass

    def test_Collection_get_query_result(self):
        tested = Collection()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_Collection_ordered_getter(self):
        tested = Collection()
        tested.get_ordered()
        pass

    def test_Collection_ordered_setter(self):
        tested = Collection()
        value = True
        tested.set_ordered(value)
        pass

    def test_Collection_unique_getter(self):
        tested = Collection()
        tested.get_unique()
        pass

    def test_Collection_unique_setter(self):
        tested = Collection()
        value = True
        tested.set_unique(value)
        pass

    def test_Collection_min_inclusive_getter(self):
        tested = Collection()
        tested.get_min_inclusive()
        pass

    def test_Collection_min_inclusive_setter(self):
        tested = Collection()
        value = True
        tested.set_min_inclusive(value)
        pass

    def test_Collection_max_inclusive_getter(self):
        tested = Collection()
        tested.get_max_inclusive()
        pass

    def test_Collection_max_inclusive_setter(self):
        tested = Collection()
        value = True
        tested.set_max_inclusive(value)
        pass

    def test_Collection_abstract_getter(self):
        tested = Collection()
        tested.get_abstract()
        pass

    def test_Collection_abstract_setter(self):
        tested = Collection()
        value = True
        tested.set_abstract(value)
        pass

    def test_Collection_final_getter(self):
        tested = Collection()
        tested.get_final()
        pass

    def test_Collection_final_setter(self):
        tested = Collection()
        value = True
        tested.set_final(value)
        pass

    def test_Collection_primitive_getter(self):
        tested = Collection()
        tested.get_primitive()
        pass

    def test_Collection_primitive_setter(self):
        tested = Collection()
        value = True
        tested.set_primitive(value)
        pass

    def test_Collection_collection_kind_getter(self):
        tested = Collection()
        tested.get_collection_kind()
        pass

    def test_Collection_collection_kind_setter(self):
        tested = Collection()
        value = CollectionKind()
        tested.set_collection_kind(value)
        pass

    def test_Collection_aggregation_kind_getter(self):
        tested = Collection()
        tested.get_aggregation_kind()
        pass

    def test_Collection_aggregation_kind_setter(self):
        tested = Collection()
        value = AggregationKind()
        tested.set_aggregation_kind(value)
        pass

    def test_Collection_visibility_getter(self):
        tested = Collection()
        tested.get_visibility()
        pass

    def test_Collection_visibility_setter(self):
        tested = Collection()
        value = VisibilityKind()
        tested.set_visibility(value)
        pass

    def test_Collection_contained_operations_getter(self):
        tested = Collection()
        tested.get_contained_operations()
        pass

    def test_Collection_min_card_getter(self):
        tested = Collection()
        tested.get_min_card()
        pass

    def test_Collection_max_card_getter(self):
        tested = Collection()
        tested.get_max_card()
        pass

    def test_Union_id_getter(self):
        tested = Union()
        tested.get_id()
        pass

    def test_Union_id_setter(self):
        tested = Union()
        value = "value"
        tested.set_id(value)
        pass

    def test_Union_sid_getter(self):
        tested = Union()
        tested.get_sid()
        pass

    def test_Union_sid_setter(self):
        tested = Union()
        value = "value"
        tested.set_sid(value)
        pass

    def test_Union_name_getter(self):
        tested = Union()
        tested.get_name()
        pass

    def test_Union_name_setter(self):
        tested = Union()
        value = "value"
        tested.set_name(value)
        pass

    def test_Union_summary_getter(self):
        tested = Union()
        tested.get_summary()
        pass

    def test_Union_summary_setter(self):
        tested = Union()
        value = "value"
        tested.set_summary(value)
        pass

    def test_Union_description_getter(self):
        tested = Union()
        tested.get_description()
        pass

    def test_Union_description_setter(self):
        tested = Union()
        value = "value"
        tested.set_description(value)
        pass

    def test_Union_status_getter(self):
        tested = Union()
        tested.get_status()
        pass

    def test_Union_status_setter(self):
        tested = Union()
        value = "value"
        tested.set_status(value)
        pass

    def test_Union_review_getter(self):
        tested = Union()
        tested.get_review()
        pass

    def test_Union_review_setter(self):
        tested = Union()
        value = "value"
        tested.set_review(value)
        pass

    def test_Union_visible_in_documentation_getter(self):
        tested = Union()
        tested.get_visible_in_documentation()
        pass

    def test_Union_visible_in_documentation_setter(self):
        tested = Union()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_Union_visible_for_traceability_getter(self):
        tested = Union()
        tested.get_visible_for_traceability()
        pass

    def test_Union_visible_for_traceability_setter(self):
        tested = Union()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_Union_owned_constraints_getter(self):
        tested = Union()
        tested.get_owned_constraints()
        pass

    def test_Union_constraints_getter(self):
        tested = Union()
        tested.get_constraints()
        pass

    def test_Union_constraints_setter(self):
        tested = Union()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_Union_owned_property_values_getter(self):
        tested = Union()
        tested.get_owned_property_values()
        pass

    def test_Union_applied_property_values_getter(self):
        tested = Union()
        tested.get_applied_property_values()
        pass

    def test_Union_applied_property_values_setter(self):
        tested = Union()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_Union_owned_property_value_groups_getter(self):
        tested = Union()
        tested.get_owned_property_value_groups()
        pass

    def test_Union_applied_property_value_groups_getter(self):
        tested = Union()
        tested.get_applied_property_value_groups()
        pass

    def test_Union_applied_property_value_groups_setter(self):
        tested = Union()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_Union_owned_enumeration_property_types_getter(self):
        tested = Union()
        tested.get_owned_enumeration_property_types()
        pass

    def test_Union_owned_diagrams_getter(self):
        tested = Union()
        tested.get_owned_diagrams()
        pass

    def test_Union_element_of_interest_for_diagrams_getter(self):
        tested = Union()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_Union_element_of_interest_for_diagrams_setter(self):
        tested = Union()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_Union_contextual_element_for_diagrams_getter(self):
        tested = Union()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_Union_contextual_element_for_diagrams_setter(self):
        tested = Union()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_Union_representing_diagrams_getter(self):
        tested = Union()
        tested.get_representing_diagrams()
        pass

    def test_Union__r_e_cs_getter(self):
        tested = Union()
        tested.get__r_e_cs()
        pass

    def test_Union__r_e_cs_setter(self):
        tested = Union()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_Union__r_p_ls_getter(self):
        tested = Union()
        tested.get__r_p_ls()
        pass

    def test_Union__r_p_ls_setter(self):
        tested = Union()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_Union_get_label(self):
        tested = Union()
        tested.get_label()
        pass

    def test_Union_get_element_type(self):
        tested = Union()
        tested.get_element_type()
        pass

    def test_Union_get_container(self):
        tested = Union()
        tested.get_container()
        pass

    def test_Union_get_contents(self):
        tested = Union()
        tested.get_contents()
        pass

    def test_Union_get_all_contents(self):
        tested = Union()
        tested.get_all_contents()
        pass

    def test_Union_get_all_contents_by_type(self):
        tested = Union()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_Union_get_available_s_b_queries(self):
        tested = Union()
        tested.get_available_s_b_queries()
        pass

    def test_Union_get_query_result(self):
        tested = Union()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_Union_final_getter(self):
        tested = Union()
        tested.get_final()
        pass

    def test_Union_final_setter(self):
        tested = Union()
        value = True
        tested.set_final(value)
        pass

    def test_Union_contained_union_properties_getter(self):
        tested = Union()
        tested.get_contained_union_properties()
        pass

    def test_Union_discriminant_getter(self):
        tested = Union()
        tested.get_discriminant()
        pass

    def test_Union_discriminant_setter(self):
        tested = Union()
        value = UnionProperty()
        tested.set_discriminant(value)
        pass

    def test_Union_default_property_getter(self):
        tested = Union()
        tested.get_default_property()
        pass

    def test_Union_default_property_setter(self):
        tested = Union()
        value = UnionProperty()
        tested.set_default_property(value)
        pass

    def test_Union_kind_getter(self):
        tested = Union()
        tested.get_kind()
        pass

    def test_Union_kind_setter(self):
        tested = Union()
        value = UnionKind()
        tested.set_kind(value)
        pass

    def test_Union_contained_operations_getter(self):
        tested = Union()
        tested.get_contained_operations()
        pass

    def test_Property_type_getter(self):
        tested = Property()
        tested.get_type()
        pass

    def test_Property_type_setter(self):
        tested = Property()
        value = PhysicalQuantity()
        tested.set_type(value)
        pass

    def test_UnionProperty_type_getter(self):
        tested = UnionProperty()
        tested.get_type()
        pass

    def test_UnionProperty_type_setter(self):
        tested = UnionProperty()
        value = PhysicalQuantity()
        tested.set_type(value)
        pass

    def test_Operation_visibility_getter(self):
        tested = Operation()
        tested.get_visibility()
        pass

    def test_Operation_visibility_setter(self):
        tested = Operation()
        value = VisibilityKind()
        tested.set_visibility(value)
        pass

    def test_Operation_realized_exchange_items_getter(self):
        tested = Operation()
        tested.get_realized_exchange_items()
        pass

    def test_Operation_realized_exchange_items_setter(self):
        tested = Operation()
        value = ExchangeItem()
        tested.get_realized_exchange_items().add(value)
        pass

    def test_Operation_owned_parameters_getter(self):
        tested = Operation()
        tested.get_owned_parameters()
        pass

    def test_Operation_thrown_exceptions_getter(self):
        tested = Operation()
        tested.get_thrown_exceptions()
        pass

    def test_Operation_thrown_exceptions_setter(self):
        tested = Operation()
        value = CapellaException()
        tested.get_thrown_exceptions().add(value)
        pass

    def test_CapellaException_abstract_getter(self):
        tested = CapellaException()
        tested.get_abstract()
        pass

    def test_CapellaException_abstract_setter(self):
        tested = CapellaException()
        value = True
        tested.set_abstract(value)
        pass

    def test_CapellaException_visibility_getter(self):
        tested = CapellaException()
        tested.get_visibility()
        pass

    def test_CapellaException_visibility_setter(self):
        tested = CapellaException()
        value = VisibilityKind()
        tested.set_visibility(value)
        pass

    def test_CapellaException_super_getter(self):
        tested = CapellaException()
        tested.get_super()
        pass

    def test_CapellaException_super_setter(self):
        tested = CapellaException()
        value = CapellaException()
        tested.get_super().add(value)
        pass

    def test_CapellaException_sub_getter(self):
        tested = CapellaException()
        tested.get_sub()
        pass

    def test_CapellaException_sub_setter(self):
        tested = CapellaException()
        value = CapellaException()
        tested.get_sub().add(value)
        pass

    def test_Enumeration_abstract_getter(self):
        tested = Enumeration()
        tested.get_abstract()
        pass

    def test_Enumeration_abstract_setter(self):
        tested = Enumeration()
        value = True
        tested.set_abstract(value)
        pass

    def test_Enumeration_final_getter(self):
        tested = Enumeration()
        tested.get_final()
        pass

    def test_Enumeration_final_setter(self):
        tested = Enumeration()
        value = True
        tested.set_final(value)
        pass

    def test_Enumeration_discrete_getter(self):
        tested = Enumeration()
        tested.get_discrete()
        pass

    def test_Enumeration_discrete_setter(self):
        tested = Enumeration()
        value = True
        tested.set_discrete(value)
        pass

    def test_Enumeration_visibility_getter(self):
        tested = Enumeration()
        tested.get_visibility()
        pass

    def test_Enumeration_visibility_setter(self):
        tested = Enumeration()
        value = VisibilityKind()
        tested.set_visibility(value)
        pass

    def test_Enumeration_super_getter(self):
        tested = Enumeration()
        tested.get_super()
        pass

    def test_Enumeration_super_setter(self):
        tested = Enumeration()
        value = PhysicalQuantity()
        tested.get_super().add(value)
        pass

    def test_Enumeration_sub_getter(self):
        tested = Enumeration()
        tested.get_sub()
        pass

    def test_Enumeration_sub_setter(self):
        tested = Enumeration()
        value = PhysicalQuantity()
        tested.get_sub().add(value)
        pass

    def test_Enumeration_realized_informations_getter(self):
        tested = Enumeration()
        tested.get_realized_informations()
        pass

    def test_Enumeration_realized_informations_setter(self):
        tested = Enumeration()
        value = PhysicalQuantity()
        tested.get_realized_informations().add(value)
        pass

    def test_Enumeration_realizing_informations_getter(self):
        tested = Enumeration()
        tested.get_realizing_informations()
        pass

    def test_Enumeration_realizing_informations_setter(self):
        tested = Enumeration()
        value = PhysicalQuantity()
        tested.get_realizing_informations().add(value)
        pass

    def test_Enumeration_owned_property_value_pkgs_getter(self):
        tested = Enumeration()
        tested.get_owned_property_value_pkgs()
        pass

    def test_Enumeration_id_getter(self):
        tested = Enumeration()
        tested.get_id()
        pass

    def test_Enumeration_id_setter(self):
        tested = Enumeration()
        value = "value"
        tested.set_id(value)
        pass

    def test_Enumeration_sid_getter(self):
        tested = Enumeration()
        tested.get_sid()
        pass

    def test_Enumeration_sid_setter(self):
        tested = Enumeration()
        value = "value"
        tested.set_sid(value)
        pass

    def test_Enumeration_name_getter(self):
        tested = Enumeration()
        tested.get_name()
        pass

    def test_Enumeration_name_setter(self):
        tested = Enumeration()
        value = "value"
        tested.set_name(value)
        pass

    def test_Enumeration_summary_getter(self):
        tested = Enumeration()
        tested.get_summary()
        pass

    def test_Enumeration_summary_setter(self):
        tested = Enumeration()
        value = "value"
        tested.set_summary(value)
        pass

    def test_Enumeration_description_getter(self):
        tested = Enumeration()
        tested.get_description()
        pass

    def test_Enumeration_description_setter(self):
        tested = Enumeration()
        value = "value"
        tested.set_description(value)
        pass

    def test_Enumeration_status_getter(self):
        tested = Enumeration()
        tested.get_status()
        pass

    def test_Enumeration_status_setter(self):
        tested = Enumeration()
        value = "value"
        tested.set_status(value)
        pass

    def test_Enumeration_review_getter(self):
        tested = Enumeration()
        tested.get_review()
        pass

    def test_Enumeration_review_setter(self):
        tested = Enumeration()
        value = "value"
        tested.set_review(value)
        pass

    def test_Enumeration_visible_in_documentation_getter(self):
        tested = Enumeration()
        tested.get_visible_in_documentation()
        pass

    def test_Enumeration_visible_in_documentation_setter(self):
        tested = Enumeration()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_Enumeration_visible_for_traceability_getter(self):
        tested = Enumeration()
        tested.get_visible_for_traceability()
        pass

    def test_Enumeration_visible_for_traceability_setter(self):
        tested = Enumeration()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_Enumeration_owned_constraints_getter(self):
        tested = Enumeration()
        tested.get_owned_constraints()
        pass

    def test_Enumeration_constraints_getter(self):
        tested = Enumeration()
        tested.get_constraints()
        pass

    def test_Enumeration_constraints_setter(self):
        tested = Enumeration()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_Enumeration_owned_property_values_getter(self):
        tested = Enumeration()
        tested.get_owned_property_values()
        pass

    def test_Enumeration_applied_property_values_getter(self):
        tested = Enumeration()
        tested.get_applied_property_values()
        pass

    def test_Enumeration_applied_property_values_setter(self):
        tested = Enumeration()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_Enumeration_owned_property_value_groups_getter(self):
        tested = Enumeration()
        tested.get_owned_property_value_groups()
        pass

    def test_Enumeration_applied_property_value_groups_getter(self):
        tested = Enumeration()
        tested.get_applied_property_value_groups()
        pass

    def test_Enumeration_applied_property_value_groups_setter(self):
        tested = Enumeration()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_Enumeration_owned_enumeration_property_types_getter(self):
        tested = Enumeration()
        tested.get_owned_enumeration_property_types()
        pass

    def test_Enumeration_owned_diagrams_getter(self):
        tested = Enumeration()
        tested.get_owned_diagrams()
        pass

    def test_Enumeration_element_of_interest_for_diagrams_getter(self):
        tested = Enumeration()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_Enumeration_element_of_interest_for_diagrams_setter(self):
        tested = Enumeration()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_Enumeration_contextual_element_for_diagrams_getter(self):
        tested = Enumeration()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_Enumeration_contextual_element_for_diagrams_setter(self):
        tested = Enumeration()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_Enumeration_representing_diagrams_getter(self):
        tested = Enumeration()
        tested.get_representing_diagrams()
        pass

    def test_Enumeration__r_e_cs_getter(self):
        tested = Enumeration()
        tested.get__r_e_cs()
        pass

    def test_Enumeration__r_e_cs_setter(self):
        tested = Enumeration()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_Enumeration__r_p_ls_getter(self):
        tested = Enumeration()
        tested.get__r_p_ls()
        pass

    def test_Enumeration__r_p_ls_setter(self):
        tested = Enumeration()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_Enumeration_get_label(self):
        tested = Enumeration()
        tested.get_label()
        pass

    def test_Enumeration_get_element_type(self):
        tested = Enumeration()
        tested.get_element_type()
        pass

    def test_Enumeration_get_container(self):
        tested = Enumeration()
        tested.get_container()
        pass

    def test_Enumeration_get_contents(self):
        tested = Enumeration()
        tested.get_contents()
        pass

    def test_Enumeration_get_all_contents(self):
        tested = Enumeration()
        tested.get_all_contents()
        pass

    def test_Enumeration_get_all_contents_by_type(self):
        tested = Enumeration()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_Enumeration_get_available_s_b_queries(self):
        tested = Enumeration()
        tested.get_available_s_b_queries()
        pass

    def test_Enumeration_get_query_result(self):
        tested = Enumeration()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_Enumeration_min_inclusive_getter(self):
        tested = Enumeration()
        tested.get_min_inclusive()
        pass

    def test_Enumeration_min_inclusive_setter(self):
        tested = Enumeration()
        value = True
        tested.set_min_inclusive(value)
        pass

    def test_Enumeration_max_inclusive_getter(self):
        tested = Enumeration()
        tested.get_max_inclusive()
        pass

    def test_Enumeration_max_inclusive_setter(self):
        tested = Enumeration()
        value = True
        tested.set_max_inclusive(value)
        pass

    def test_Enumeration_pattern_getter(self):
        tested = Enumeration()
        tested.get_pattern()
        pass

    def test_Enumeration_pattern_setter(self):
        tested = Enumeration()
        value = "value"
        tested.set_pattern(value)
        pass

    def test_Enumeration_owned_literals_getter(self):
        tested = Enumeration()
        tested.get_owned_literals()
        pass

    def test_Enumeration_default_value_getter(self):
        tested = Enumeration()
        tested.get_default_value()
        pass

    def test_Enumeration_default_value_setter(self):
        tested = Enumeration()
        value = EnumerationLiteral()
        tested.set_default_value(value)
        pass

    def test_Enumeration_min_value_getter(self):
        tested = Enumeration()
        tested.get_min_value()
        pass

    def test_Enumeration_min_value_setter(self):
        tested = Enumeration()
        value = EnumerationLiteral()
        tested.set_min_value(value)
        pass

    def test_Enumeration_max_value_getter(self):
        tested = Enumeration()
        tested.get_max_value()
        pass

    def test_Enumeration_max_value_setter(self):
        tested = Enumeration()
        value = EnumerationLiteral()
        tested.set_max_value(value)
        pass

    def test_Enumeration_null_value_getter(self):
        tested = Enumeration()
        tested.get_null_value()
        pass

    def test_Enumeration_null_value_setter(self):
        tested = Enumeration()
        value = EnumerationLiteral()
        tested.set_null_value(value)
        pass

    def test_Enumeration_domain_type_getter(self):
        tested = Enumeration()
        tested.get_domain_type()
        pass

    def test_Enumeration_domain_type_setter(self):
        tested = Enumeration()
        value = PhysicalQuantity()
        tested.set_domain_type(value)
        pass

    def test_BooleanType_abstract_getter(self):
        tested = BooleanType()
        tested.get_abstract()
        pass

    def test_BooleanType_abstract_setter(self):
        tested = BooleanType()
        value = True
        tested.set_abstract(value)
        pass

    def test_BooleanType_final_getter(self):
        tested = BooleanType()
        tested.get_final()
        pass

    def test_BooleanType_final_setter(self):
        tested = BooleanType()
        value = True
        tested.set_final(value)
        pass

    def test_BooleanType_discrete_getter(self):
        tested = BooleanType()
        tested.get_discrete()
        pass

    def test_BooleanType_discrete_setter(self):
        tested = BooleanType()
        value = True
        tested.set_discrete(value)
        pass

    def test_BooleanType_visibility_getter(self):
        tested = BooleanType()
        tested.get_visibility()
        pass

    def test_BooleanType_visibility_setter(self):
        tested = BooleanType()
        value = VisibilityKind()
        tested.set_visibility(value)
        pass

    def test_BooleanType_super_getter(self):
        tested = BooleanType()
        tested.get_super()
        pass

    def test_BooleanType_super_setter(self):
        tested = BooleanType()
        value = PhysicalQuantity()
        tested.get_super().add(value)
        pass

    def test_BooleanType_sub_getter(self):
        tested = BooleanType()
        tested.get_sub()
        pass

    def test_BooleanType_sub_setter(self):
        tested = BooleanType()
        value = PhysicalQuantity()
        tested.get_sub().add(value)
        pass

    def test_BooleanType_realized_informations_getter(self):
        tested = BooleanType()
        tested.get_realized_informations()
        pass

    def test_BooleanType_realized_informations_setter(self):
        tested = BooleanType()
        value = PhysicalQuantity()
        tested.get_realized_informations().add(value)
        pass

    def test_BooleanType_realizing_informations_getter(self):
        tested = BooleanType()
        tested.get_realizing_informations()
        pass

    def test_BooleanType_realizing_informations_setter(self):
        tested = BooleanType()
        value = PhysicalQuantity()
        tested.get_realizing_informations().add(value)
        pass

    def test_BooleanType_owned_property_value_pkgs_getter(self):
        tested = BooleanType()
        tested.get_owned_property_value_pkgs()
        pass

    def test_BooleanType_id_getter(self):
        tested = BooleanType()
        tested.get_id()
        pass

    def test_BooleanType_id_setter(self):
        tested = BooleanType()
        value = "value"
        tested.set_id(value)
        pass

    def test_BooleanType_sid_getter(self):
        tested = BooleanType()
        tested.get_sid()
        pass

    def test_BooleanType_sid_setter(self):
        tested = BooleanType()
        value = "value"
        tested.set_sid(value)
        pass

    def test_BooleanType_name_getter(self):
        tested = BooleanType()
        tested.get_name()
        pass

    def test_BooleanType_name_setter(self):
        tested = BooleanType()
        value = "value"
        tested.set_name(value)
        pass

    def test_BooleanType_summary_getter(self):
        tested = BooleanType()
        tested.get_summary()
        pass

    def test_BooleanType_summary_setter(self):
        tested = BooleanType()
        value = "value"
        tested.set_summary(value)
        pass

    def test_BooleanType_description_getter(self):
        tested = BooleanType()
        tested.get_description()
        pass

    def test_BooleanType_description_setter(self):
        tested = BooleanType()
        value = "value"
        tested.set_description(value)
        pass

    def test_BooleanType_status_getter(self):
        tested = BooleanType()
        tested.get_status()
        pass

    def test_BooleanType_status_setter(self):
        tested = BooleanType()
        value = "value"
        tested.set_status(value)
        pass

    def test_BooleanType_review_getter(self):
        tested = BooleanType()
        tested.get_review()
        pass

    def test_BooleanType_review_setter(self):
        tested = BooleanType()
        value = "value"
        tested.set_review(value)
        pass

    def test_BooleanType_visible_in_documentation_getter(self):
        tested = BooleanType()
        tested.get_visible_in_documentation()
        pass

    def test_BooleanType_visible_in_documentation_setter(self):
        tested = BooleanType()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_BooleanType_visible_for_traceability_getter(self):
        tested = BooleanType()
        tested.get_visible_for_traceability()
        pass

    def test_BooleanType_visible_for_traceability_setter(self):
        tested = BooleanType()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_BooleanType_owned_constraints_getter(self):
        tested = BooleanType()
        tested.get_owned_constraints()
        pass

    def test_BooleanType_constraints_getter(self):
        tested = BooleanType()
        tested.get_constraints()
        pass

    def test_BooleanType_constraints_setter(self):
        tested = BooleanType()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_BooleanType_owned_property_values_getter(self):
        tested = BooleanType()
        tested.get_owned_property_values()
        pass

    def test_BooleanType_applied_property_values_getter(self):
        tested = BooleanType()
        tested.get_applied_property_values()
        pass

    def test_BooleanType_applied_property_values_setter(self):
        tested = BooleanType()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_BooleanType_owned_property_value_groups_getter(self):
        tested = BooleanType()
        tested.get_owned_property_value_groups()
        pass

    def test_BooleanType_applied_property_value_groups_getter(self):
        tested = BooleanType()
        tested.get_applied_property_value_groups()
        pass

    def test_BooleanType_applied_property_value_groups_setter(self):
        tested = BooleanType()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_BooleanType_owned_enumeration_property_types_getter(self):
        tested = BooleanType()
        tested.get_owned_enumeration_property_types()
        pass

    def test_BooleanType_owned_diagrams_getter(self):
        tested = BooleanType()
        tested.get_owned_diagrams()
        pass

    def test_BooleanType_element_of_interest_for_diagrams_getter(self):
        tested = BooleanType()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_BooleanType_element_of_interest_for_diagrams_setter(self):
        tested = BooleanType()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_BooleanType_contextual_element_for_diagrams_getter(self):
        tested = BooleanType()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_BooleanType_contextual_element_for_diagrams_setter(self):
        tested = BooleanType()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_BooleanType_representing_diagrams_getter(self):
        tested = BooleanType()
        tested.get_representing_diagrams()
        pass

    def test_BooleanType__r_e_cs_getter(self):
        tested = BooleanType()
        tested.get__r_e_cs()
        pass

    def test_BooleanType__r_e_cs_setter(self):
        tested = BooleanType()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_BooleanType__r_p_ls_getter(self):
        tested = BooleanType()
        tested.get__r_p_ls()
        pass

    def test_BooleanType__r_p_ls_setter(self):
        tested = BooleanType()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_BooleanType_get_label(self):
        tested = BooleanType()
        tested.get_label()
        pass

    def test_BooleanType_get_element_type(self):
        tested = BooleanType()
        tested.get_element_type()
        pass

    def test_BooleanType_get_container(self):
        tested = BooleanType()
        tested.get_container()
        pass

    def test_BooleanType_get_contents(self):
        tested = BooleanType()
        tested.get_contents()
        pass

    def test_BooleanType_get_all_contents(self):
        tested = BooleanType()
        tested.get_all_contents()
        pass

    def test_BooleanType_get_all_contents_by_type(self):
        tested = BooleanType()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_BooleanType_get_available_s_b_queries(self):
        tested = BooleanType()
        tested.get_available_s_b_queries()
        pass

    def test_BooleanType_get_query_result(self):
        tested = BooleanType()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_BooleanType_owned_literals_getter(self):
        tested = BooleanType()
        tested.get_owned_literals()
        pass

    def test_BooleanType_default_value_getter(self):
        tested = BooleanType()
        tested.get_default_value()
        pass

    def test_BooleanType_default_value_setter(self):
        tested = BooleanType()
        value = LiteralBooleanValue()
        tested.set_default_value(value)
        pass

    def test_StringType_abstract_getter(self):
        tested = StringType()
        tested.get_abstract()
        pass

    def test_StringType_abstract_setter(self):
        tested = StringType()
        value = True
        tested.set_abstract(value)
        pass

    def test_StringType_final_getter(self):
        tested = StringType()
        tested.get_final()
        pass

    def test_StringType_final_setter(self):
        tested = StringType()
        value = True
        tested.set_final(value)
        pass

    def test_StringType_discrete_getter(self):
        tested = StringType()
        tested.get_discrete()
        pass

    def test_StringType_discrete_setter(self):
        tested = StringType()
        value = True
        tested.set_discrete(value)
        pass

    def test_StringType_visibility_getter(self):
        tested = StringType()
        tested.get_visibility()
        pass

    def test_StringType_visibility_setter(self):
        tested = StringType()
        value = VisibilityKind()
        tested.set_visibility(value)
        pass

    def test_StringType_super_getter(self):
        tested = StringType()
        tested.get_super()
        pass

    def test_StringType_super_setter(self):
        tested = StringType()
        value = PhysicalQuantity()
        tested.get_super().add(value)
        pass

    def test_StringType_sub_getter(self):
        tested = StringType()
        tested.get_sub()
        pass

    def test_StringType_sub_setter(self):
        tested = StringType()
        value = PhysicalQuantity()
        tested.get_sub().add(value)
        pass

    def test_StringType_realized_informations_getter(self):
        tested = StringType()
        tested.get_realized_informations()
        pass

    def test_StringType_realized_informations_setter(self):
        tested = StringType()
        value = PhysicalQuantity()
        tested.get_realized_informations().add(value)
        pass

    def test_StringType_realizing_informations_getter(self):
        tested = StringType()
        tested.get_realizing_informations()
        pass

    def test_StringType_realizing_informations_setter(self):
        tested = StringType()
        value = PhysicalQuantity()
        tested.get_realizing_informations().add(value)
        pass

    def test_StringType_owned_property_value_pkgs_getter(self):
        tested = StringType()
        tested.get_owned_property_value_pkgs()
        pass

    def test_StringType_id_getter(self):
        tested = StringType()
        tested.get_id()
        pass

    def test_StringType_id_setter(self):
        tested = StringType()
        value = "value"
        tested.set_id(value)
        pass

    def test_StringType_sid_getter(self):
        tested = StringType()
        tested.get_sid()
        pass

    def test_StringType_sid_setter(self):
        tested = StringType()
        value = "value"
        tested.set_sid(value)
        pass

    def test_StringType_name_getter(self):
        tested = StringType()
        tested.get_name()
        pass

    def test_StringType_name_setter(self):
        tested = StringType()
        value = "value"
        tested.set_name(value)
        pass

    def test_StringType_summary_getter(self):
        tested = StringType()
        tested.get_summary()
        pass

    def test_StringType_summary_setter(self):
        tested = StringType()
        value = "value"
        tested.set_summary(value)
        pass

    def test_StringType_description_getter(self):
        tested = StringType()
        tested.get_description()
        pass

    def test_StringType_description_setter(self):
        tested = StringType()
        value = "value"
        tested.set_description(value)
        pass

    def test_StringType_status_getter(self):
        tested = StringType()
        tested.get_status()
        pass

    def test_StringType_status_setter(self):
        tested = StringType()
        value = "value"
        tested.set_status(value)
        pass

    def test_StringType_review_getter(self):
        tested = StringType()
        tested.get_review()
        pass

    def test_StringType_review_setter(self):
        tested = StringType()
        value = "value"
        tested.set_review(value)
        pass

    def test_StringType_visible_in_documentation_getter(self):
        tested = StringType()
        tested.get_visible_in_documentation()
        pass

    def test_StringType_visible_in_documentation_setter(self):
        tested = StringType()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_StringType_visible_for_traceability_getter(self):
        tested = StringType()
        tested.get_visible_for_traceability()
        pass

    def test_StringType_visible_for_traceability_setter(self):
        tested = StringType()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_StringType_owned_constraints_getter(self):
        tested = StringType()
        tested.get_owned_constraints()
        pass

    def test_StringType_constraints_getter(self):
        tested = StringType()
        tested.get_constraints()
        pass

    def test_StringType_constraints_setter(self):
        tested = StringType()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_StringType_owned_property_values_getter(self):
        tested = StringType()
        tested.get_owned_property_values()
        pass

    def test_StringType_applied_property_values_getter(self):
        tested = StringType()
        tested.get_applied_property_values()
        pass

    def test_StringType_applied_property_values_setter(self):
        tested = StringType()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_StringType_owned_property_value_groups_getter(self):
        tested = StringType()
        tested.get_owned_property_value_groups()
        pass

    def test_StringType_applied_property_value_groups_getter(self):
        tested = StringType()
        tested.get_applied_property_value_groups()
        pass

    def test_StringType_applied_property_value_groups_setter(self):
        tested = StringType()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_StringType_owned_enumeration_property_types_getter(self):
        tested = StringType()
        tested.get_owned_enumeration_property_types()
        pass

    def test_StringType_owned_diagrams_getter(self):
        tested = StringType()
        tested.get_owned_diagrams()
        pass

    def test_StringType_element_of_interest_for_diagrams_getter(self):
        tested = StringType()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_StringType_element_of_interest_for_diagrams_setter(self):
        tested = StringType()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_StringType_contextual_element_for_diagrams_getter(self):
        tested = StringType()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_StringType_contextual_element_for_diagrams_setter(self):
        tested = StringType()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_StringType_representing_diagrams_getter(self):
        tested = StringType()
        tested.get_representing_diagrams()
        pass

    def test_StringType__r_e_cs_getter(self):
        tested = StringType()
        tested.get__r_e_cs()
        pass

    def test_StringType__r_e_cs_setter(self):
        tested = StringType()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_StringType__r_p_ls_getter(self):
        tested = StringType()
        tested.get__r_p_ls()
        pass

    def test_StringType__r_p_ls_setter(self):
        tested = StringType()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_StringType_get_label(self):
        tested = StringType()
        tested.get_label()
        pass

    def test_StringType_get_element_type(self):
        tested = StringType()
        tested.get_element_type()
        pass

    def test_StringType_get_container(self):
        tested = StringType()
        tested.get_container()
        pass

    def test_StringType_get_contents(self):
        tested = StringType()
        tested.get_contents()
        pass

    def test_StringType_get_all_contents(self):
        tested = StringType()
        tested.get_all_contents()
        pass

    def test_StringType_get_all_contents_by_type(self):
        tested = StringType()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_StringType_get_available_s_b_queries(self):
        tested = StringType()
        tested.get_available_s_b_queries()
        pass

    def test_StringType_get_query_result(self):
        tested = StringType()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_StringType_min_inclusive_getter(self):
        tested = StringType()
        tested.get_min_inclusive()
        pass

    def test_StringType_min_inclusive_setter(self):
        tested = StringType()
        value = True
        tested.set_min_inclusive(value)
        pass

    def test_StringType_max_inclusive_getter(self):
        tested = StringType()
        tested.get_max_inclusive()
        pass

    def test_StringType_max_inclusive_setter(self):
        tested = StringType()
        value = True
        tested.set_max_inclusive(value)
        pass

    def test_StringType_pattern_getter(self):
        tested = StringType()
        tested.get_pattern()
        pass

    def test_StringType_pattern_setter(self):
        tested = StringType()
        value = "value"
        tested.set_pattern(value)
        pass

    def test_StringType_min_length_getter(self):
        tested = StringType()
        tested.get_min_length()
        pass

    def test_StringType_max_length_getter(self):
        tested = StringType()
        tested.get_max_length()
        pass

    def test_StringType_default_value_getter(self):
        tested = StringType()
        tested.get_default_value()
        pass

    def test_StringType_null_value_getter(self):
        tested = StringType()
        tested.get_null_value()
        pass

    def test_NumericType_abstract_getter(self):
        tested = NumericType()
        tested.get_abstract()
        pass

    def test_NumericType_abstract_setter(self):
        tested = NumericType()
        value = True
        tested.set_abstract(value)
        pass

    def test_NumericType_final_getter(self):
        tested = NumericType()
        tested.get_final()
        pass

    def test_NumericType_final_setter(self):
        tested = NumericType()
        value = True
        tested.set_final(value)
        pass

    def test_NumericType_discrete_getter(self):
        tested = NumericType()
        tested.get_discrete()
        pass

    def test_NumericType_discrete_setter(self):
        tested = NumericType()
        value = True
        tested.set_discrete(value)
        pass

    def test_NumericType_visibility_getter(self):
        tested = NumericType()
        tested.get_visibility()
        pass

    def test_NumericType_visibility_setter(self):
        tested = NumericType()
        value = VisibilityKind()
        tested.set_visibility(value)
        pass

    def test_NumericType_super_getter(self):
        tested = NumericType()
        tested.get_super()
        pass

    def test_NumericType_super_setter(self):
        tested = NumericType()
        value = PhysicalQuantity()
        tested.get_super().add(value)
        pass

    def test_NumericType_sub_getter(self):
        tested = NumericType()
        tested.get_sub()
        pass

    def test_NumericType_sub_setter(self):
        tested = NumericType()
        value = PhysicalQuantity()
        tested.get_sub().add(value)
        pass

    def test_NumericType_realized_informations_getter(self):
        tested = NumericType()
        tested.get_realized_informations()
        pass

    def test_NumericType_realized_informations_setter(self):
        tested = NumericType()
        value = PhysicalQuantity()
        tested.get_realized_informations().add(value)
        pass

    def test_NumericType_realizing_informations_getter(self):
        tested = NumericType()
        tested.get_realizing_informations()
        pass

    def test_NumericType_realizing_informations_setter(self):
        tested = NumericType()
        value = PhysicalQuantity()
        tested.get_realizing_informations().add(value)
        pass

    def test_NumericType_owned_property_value_pkgs_getter(self):
        tested = NumericType()
        tested.get_owned_property_value_pkgs()
        pass

    def test_NumericType_id_getter(self):
        tested = NumericType()
        tested.get_id()
        pass

    def test_NumericType_id_setter(self):
        tested = NumericType()
        value = "value"
        tested.set_id(value)
        pass

    def test_NumericType_sid_getter(self):
        tested = NumericType()
        tested.get_sid()
        pass

    def test_NumericType_sid_setter(self):
        tested = NumericType()
        value = "value"
        tested.set_sid(value)
        pass

    def test_NumericType_name_getter(self):
        tested = NumericType()
        tested.get_name()
        pass

    def test_NumericType_name_setter(self):
        tested = NumericType()
        value = "value"
        tested.set_name(value)
        pass

    def test_NumericType_summary_getter(self):
        tested = NumericType()
        tested.get_summary()
        pass

    def test_NumericType_summary_setter(self):
        tested = NumericType()
        value = "value"
        tested.set_summary(value)
        pass

    def test_NumericType_description_getter(self):
        tested = NumericType()
        tested.get_description()
        pass

    def test_NumericType_description_setter(self):
        tested = NumericType()
        value = "value"
        tested.set_description(value)
        pass

    def test_NumericType_status_getter(self):
        tested = NumericType()
        tested.get_status()
        pass

    def test_NumericType_status_setter(self):
        tested = NumericType()
        value = "value"
        tested.set_status(value)
        pass

    def test_NumericType_review_getter(self):
        tested = NumericType()
        tested.get_review()
        pass

    def test_NumericType_review_setter(self):
        tested = NumericType()
        value = "value"
        tested.set_review(value)
        pass

    def test_NumericType_visible_in_documentation_getter(self):
        tested = NumericType()
        tested.get_visible_in_documentation()
        pass

    def test_NumericType_visible_in_documentation_setter(self):
        tested = NumericType()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_NumericType_visible_for_traceability_getter(self):
        tested = NumericType()
        tested.get_visible_for_traceability()
        pass

    def test_NumericType_visible_for_traceability_setter(self):
        tested = NumericType()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_NumericType_owned_constraints_getter(self):
        tested = NumericType()
        tested.get_owned_constraints()
        pass

    def test_NumericType_constraints_getter(self):
        tested = NumericType()
        tested.get_constraints()
        pass

    def test_NumericType_constraints_setter(self):
        tested = NumericType()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_NumericType_owned_property_values_getter(self):
        tested = NumericType()
        tested.get_owned_property_values()
        pass

    def test_NumericType_applied_property_values_getter(self):
        tested = NumericType()
        tested.get_applied_property_values()
        pass

    def test_NumericType_applied_property_values_setter(self):
        tested = NumericType()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_NumericType_owned_property_value_groups_getter(self):
        tested = NumericType()
        tested.get_owned_property_value_groups()
        pass

    def test_NumericType_applied_property_value_groups_getter(self):
        tested = NumericType()
        tested.get_applied_property_value_groups()
        pass

    def test_NumericType_applied_property_value_groups_setter(self):
        tested = NumericType()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_NumericType_owned_enumeration_property_types_getter(self):
        tested = NumericType()
        tested.get_owned_enumeration_property_types()
        pass

    def test_NumericType_owned_diagrams_getter(self):
        tested = NumericType()
        tested.get_owned_diagrams()
        pass

    def test_NumericType_element_of_interest_for_diagrams_getter(self):
        tested = NumericType()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_NumericType_element_of_interest_for_diagrams_setter(self):
        tested = NumericType()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_NumericType_contextual_element_for_diagrams_getter(self):
        tested = NumericType()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_NumericType_contextual_element_for_diagrams_setter(self):
        tested = NumericType()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_NumericType_representing_diagrams_getter(self):
        tested = NumericType()
        tested.get_representing_diagrams()
        pass

    def test_NumericType__r_e_cs_getter(self):
        tested = NumericType()
        tested.get__r_e_cs()
        pass

    def test_NumericType__r_e_cs_setter(self):
        tested = NumericType()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_NumericType__r_p_ls_getter(self):
        tested = NumericType()
        tested.get__r_p_ls()
        pass

    def test_NumericType__r_p_ls_setter(self):
        tested = NumericType()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_NumericType_get_label(self):
        tested = NumericType()
        tested.get_label()
        pass

    def test_NumericType_get_element_type(self):
        tested = NumericType()
        tested.get_element_type()
        pass

    def test_NumericType_get_container(self):
        tested = NumericType()
        tested.get_container()
        pass

    def test_NumericType_get_contents(self):
        tested = NumericType()
        tested.get_contents()
        pass

    def test_NumericType_get_all_contents(self):
        tested = NumericType()
        tested.get_all_contents()
        pass

    def test_NumericType_get_all_contents_by_type(self):
        tested = NumericType()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_NumericType_get_available_s_b_queries(self):
        tested = NumericType()
        tested.get_available_s_b_queries()
        pass

    def test_NumericType_get_query_result(self):
        tested = NumericType()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_NumericType_min_inclusive_getter(self):
        tested = NumericType()
        tested.get_min_inclusive()
        pass

    def test_NumericType_min_inclusive_setter(self):
        tested = NumericType()
        value = True
        tested.set_min_inclusive(value)
        pass

    def test_NumericType_max_inclusive_getter(self):
        tested = NumericType()
        tested.get_max_inclusive()
        pass

    def test_NumericType_max_inclusive_setter(self):
        tested = NumericType()
        value = True
        tested.set_max_inclusive(value)
        pass

    def test_NumericType_pattern_getter(self):
        tested = NumericType()
        tested.get_pattern()
        pass

    def test_NumericType_pattern_setter(self):
        tested = NumericType()
        value = "value"
        tested.set_pattern(value)
        pass

    def test_NumericType_kind_getter(self):
        tested = NumericType()
        tested.get_kind()
        pass

    def test_NumericType_kind_setter(self):
        tested = NumericType()
        value = NumericTypeKind()
        tested.set_kind(value)
        pass

    def test_NumericType_min_value_getter(self):
        tested = NumericType()
        tested.get_min_value()
        pass

    def test_NumericType_max_value_getter(self):
        tested = NumericType()
        tested.get_max_value()
        pass

    def test_NumericType_default_value_getter(self):
        tested = NumericType()
        tested.get_default_value()
        pass

    def test_NumericType_null_value_getter(self):
        tested = NumericType()
        tested.get_null_value()
        pass

    def test_PhysicalQuantity_min_inclusive_getter(self):
        tested = PhysicalQuantity()
        tested.get_min_inclusive()
        pass

    def test_PhysicalQuantity_min_inclusive_setter(self):
        tested = PhysicalQuantity()
        value = True
        tested.set_min_inclusive(value)
        pass

    def test_PhysicalQuantity_max_inclusive_getter(self):
        tested = PhysicalQuantity()
        tested.get_max_inclusive()
        pass

    def test_PhysicalQuantity_max_inclusive_setter(self):
        tested = PhysicalQuantity()
        value = True
        tested.set_max_inclusive(value)
        pass

    def test_PhysicalQuantity_pattern_getter(self):
        tested = PhysicalQuantity()
        tested.get_pattern()
        pass

    def test_PhysicalQuantity_pattern_setter(self):
        tested = PhysicalQuantity()
        value = "value"
        tested.set_pattern(value)
        pass

    def test_PhysicalQuantity_kind_getter(self):
        tested = PhysicalQuantity()
        tested.get_kind()
        pass

    def test_PhysicalQuantity_kind_setter(self):
        tested = PhysicalQuantity()
        value = NumericTypeKind()
        tested.set_kind(value)
        pass

    def test_PhysicalQuantity_min_value_getter(self):
        tested = PhysicalQuantity()
        tested.get_min_value()
        pass

    def test_PhysicalQuantity_max_value_getter(self):
        tested = PhysicalQuantity()
        tested.get_max_value()
        pass

    def test_PhysicalQuantity_default_value_getter(self):
        tested = PhysicalQuantity()
        tested.get_default_value()
        pass

    def test_PhysicalQuantity_null_value_getter(self):
        tested = PhysicalQuantity()
        tested.get_null_value()
        pass

    def test_PhysicalQuantity_abstract_getter(self):
        tested = PhysicalQuantity()
        tested.get_abstract()
        pass

    def test_PhysicalQuantity_abstract_setter(self):
        tested = PhysicalQuantity()
        value = True
        tested.set_abstract(value)
        pass

    def test_PhysicalQuantity_final_getter(self):
        tested = PhysicalQuantity()
        tested.get_final()
        pass

    def test_PhysicalQuantity_final_setter(self):
        tested = PhysicalQuantity()
        value = True
        tested.set_final(value)
        pass

    def test_PhysicalQuantity_discrete_getter(self):
        tested = PhysicalQuantity()
        tested.get_discrete()
        pass

    def test_PhysicalQuantity_discrete_setter(self):
        tested = PhysicalQuantity()
        value = True
        tested.set_discrete(value)
        pass

    def test_PhysicalQuantity_visibility_getter(self):
        tested = PhysicalQuantity()
        tested.get_visibility()
        pass

    def test_PhysicalQuantity_visibility_setter(self):
        tested = PhysicalQuantity()
        value = VisibilityKind()
        tested.set_visibility(value)
        pass

    def test_PhysicalQuantity_super_getter(self):
        tested = PhysicalQuantity()
        tested.get_super()
        pass

    def test_PhysicalQuantity_super_setter(self):
        tested = PhysicalQuantity()
        value = PhysicalQuantity()
        tested.get_super().add(value)
        pass

    def test_PhysicalQuantity_sub_getter(self):
        tested = PhysicalQuantity()
        tested.get_sub()
        pass

    def test_PhysicalQuantity_sub_setter(self):
        tested = PhysicalQuantity()
        value = PhysicalQuantity()
        tested.get_sub().add(value)
        pass

    def test_PhysicalQuantity_realized_informations_getter(self):
        tested = PhysicalQuantity()
        tested.get_realized_informations()
        pass

    def test_PhysicalQuantity_realized_informations_setter(self):
        tested = PhysicalQuantity()
        value = PhysicalQuantity()
        tested.get_realized_informations().add(value)
        pass

    def test_PhysicalQuantity_realizing_informations_getter(self):
        tested = PhysicalQuantity()
        tested.get_realizing_informations()
        pass

    def test_PhysicalQuantity_realizing_informations_setter(self):
        tested = PhysicalQuantity()
        value = PhysicalQuantity()
        tested.get_realizing_informations().add(value)
        pass

    def test_PhysicalQuantity_owned_property_value_pkgs_getter(self):
        tested = PhysicalQuantity()
        tested.get_owned_property_value_pkgs()
        pass

    def test_PhysicalQuantity_id_getter(self):
        tested = PhysicalQuantity()
        tested.get_id()
        pass

    def test_PhysicalQuantity_id_setter(self):
        tested = PhysicalQuantity()
        value = "value"
        tested.set_id(value)
        pass

    def test_PhysicalQuantity_sid_getter(self):
        tested = PhysicalQuantity()
        tested.get_sid()
        pass

    def test_PhysicalQuantity_sid_setter(self):
        tested = PhysicalQuantity()
        value = "value"
        tested.set_sid(value)
        pass

    def test_PhysicalQuantity_name_getter(self):
        tested = PhysicalQuantity()
        tested.get_name()
        pass

    def test_PhysicalQuantity_name_setter(self):
        tested = PhysicalQuantity()
        value = "value"
        tested.set_name(value)
        pass

    def test_PhysicalQuantity_summary_getter(self):
        tested = PhysicalQuantity()
        tested.get_summary()
        pass

    def test_PhysicalQuantity_summary_setter(self):
        tested = PhysicalQuantity()
        value = "value"
        tested.set_summary(value)
        pass

    def test_PhysicalQuantity_description_getter(self):
        tested = PhysicalQuantity()
        tested.get_description()
        pass

    def test_PhysicalQuantity_description_setter(self):
        tested = PhysicalQuantity()
        value = "value"
        tested.set_description(value)
        pass

    def test_PhysicalQuantity_status_getter(self):
        tested = PhysicalQuantity()
        tested.get_status()
        pass

    def test_PhysicalQuantity_status_setter(self):
        tested = PhysicalQuantity()
        value = "value"
        tested.set_status(value)
        pass

    def test_PhysicalQuantity_review_getter(self):
        tested = PhysicalQuantity()
        tested.get_review()
        pass

    def test_PhysicalQuantity_review_setter(self):
        tested = PhysicalQuantity()
        value = "value"
        tested.set_review(value)
        pass

    def test_PhysicalQuantity_visible_in_documentation_getter(self):
        tested = PhysicalQuantity()
        tested.get_visible_in_documentation()
        pass

    def test_PhysicalQuantity_visible_in_documentation_setter(self):
        tested = PhysicalQuantity()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_PhysicalQuantity_visible_for_traceability_getter(self):
        tested = PhysicalQuantity()
        tested.get_visible_for_traceability()
        pass

    def test_PhysicalQuantity_visible_for_traceability_setter(self):
        tested = PhysicalQuantity()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_PhysicalQuantity_owned_constraints_getter(self):
        tested = PhysicalQuantity()
        tested.get_owned_constraints()
        pass

    def test_PhysicalQuantity_constraints_getter(self):
        tested = PhysicalQuantity()
        tested.get_constraints()
        pass

    def test_PhysicalQuantity_constraints_setter(self):
        tested = PhysicalQuantity()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_PhysicalQuantity_owned_property_values_getter(self):
        tested = PhysicalQuantity()
        tested.get_owned_property_values()
        pass

    def test_PhysicalQuantity_applied_property_values_getter(self):
        tested = PhysicalQuantity()
        tested.get_applied_property_values()
        pass

    def test_PhysicalQuantity_applied_property_values_setter(self):
        tested = PhysicalQuantity()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_PhysicalQuantity_owned_property_value_groups_getter(self):
        tested = PhysicalQuantity()
        tested.get_owned_property_value_groups()
        pass

    def test_PhysicalQuantity_applied_property_value_groups_getter(self):
        tested = PhysicalQuantity()
        tested.get_applied_property_value_groups()
        pass

    def test_PhysicalQuantity_applied_property_value_groups_setter(self):
        tested = PhysicalQuantity()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_PhysicalQuantity_owned_enumeration_property_types_getter(self):
        tested = PhysicalQuantity()
        tested.get_owned_enumeration_property_types()
        pass

    def test_PhysicalQuantity_owned_diagrams_getter(self):
        tested = PhysicalQuantity()
        tested.get_owned_diagrams()
        pass

    def test_PhysicalQuantity_element_of_interest_for_diagrams_getter(self):
        tested = PhysicalQuantity()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_PhysicalQuantity_element_of_interest_for_diagrams_setter(self):
        tested = PhysicalQuantity()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_PhysicalQuantity_contextual_element_for_diagrams_getter(self):
        tested = PhysicalQuantity()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_PhysicalQuantity_contextual_element_for_diagrams_setter(self):
        tested = PhysicalQuantity()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_PhysicalQuantity_representing_diagrams_getter(self):
        tested = PhysicalQuantity()
        tested.get_representing_diagrams()
        pass

    def test_PhysicalQuantity__r_e_cs_getter(self):
        tested = PhysicalQuantity()
        tested.get__r_e_cs()
        pass

    def test_PhysicalQuantity__r_e_cs_setter(self):
        tested = PhysicalQuantity()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_PhysicalQuantity__r_p_ls_getter(self):
        tested = PhysicalQuantity()
        tested.get__r_p_ls()
        pass

    def test_PhysicalQuantity__r_p_ls_setter(self):
        tested = PhysicalQuantity()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_PhysicalQuantity_get_label(self):
        tested = PhysicalQuantity()
        tested.get_label()
        pass

    def test_PhysicalQuantity_get_element_type(self):
        tested = PhysicalQuantity()
        tested.get_element_type()
        pass

    def test_PhysicalQuantity_get_container(self):
        tested = PhysicalQuantity()
        tested.get_container()
        pass

    def test_PhysicalQuantity_get_contents(self):
        tested = PhysicalQuantity()
        tested.get_contents()
        pass

    def test_PhysicalQuantity_get_all_contents(self):
        tested = PhysicalQuantity()
        tested.get_all_contents()
        pass

    def test_PhysicalQuantity_get_all_contents_by_type(self):
        tested = PhysicalQuantity()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_PhysicalQuantity_get_available_s_b_queries(self):
        tested = PhysicalQuantity()
        tested.get_available_s_b_queries()
        pass

    def test_PhysicalQuantity_get_query_result(self):
        tested = PhysicalQuantity()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_PhysicalQuantity_unit_getter(self):
        tested = PhysicalQuantity()
        tested.get_unit()
        pass

    def test_PhysicalQuantity_unit_setter(self):
        tested = PhysicalQuantity()
        value = Unit()
        tested.set_unit(value)
        pass

    def test_Unit_id_getter(self):
        tested = Unit()
        tested.get_id()
        pass

    def test_Unit_id_setter(self):
        tested = Unit()
        value = "value"
        tested.set_id(value)
        pass

    def test_Unit_sid_getter(self):
        tested = Unit()
        tested.get_sid()
        pass

    def test_Unit_sid_setter(self):
        tested = Unit()
        value = "value"
        tested.set_sid(value)
        pass

    def test_Unit_name_getter(self):
        tested = Unit()
        tested.get_name()
        pass

    def test_Unit_name_setter(self):
        tested = Unit()
        value = "value"
        tested.set_name(value)
        pass

    def test_Unit_summary_getter(self):
        tested = Unit()
        tested.get_summary()
        pass

    def test_Unit_summary_setter(self):
        tested = Unit()
        value = "value"
        tested.set_summary(value)
        pass

    def test_Unit_description_getter(self):
        tested = Unit()
        tested.get_description()
        pass

    def test_Unit_description_setter(self):
        tested = Unit()
        value = "value"
        tested.set_description(value)
        pass

    def test_Unit_status_getter(self):
        tested = Unit()
        tested.get_status()
        pass

    def test_Unit_status_setter(self):
        tested = Unit()
        value = "value"
        tested.set_status(value)
        pass

    def test_Unit_review_getter(self):
        tested = Unit()
        tested.get_review()
        pass

    def test_Unit_review_setter(self):
        tested = Unit()
        value = "value"
        tested.set_review(value)
        pass

    def test_Unit_visible_in_documentation_getter(self):
        tested = Unit()
        tested.get_visible_in_documentation()
        pass

    def test_Unit_visible_in_documentation_setter(self):
        tested = Unit()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_Unit_visible_for_traceability_getter(self):
        tested = Unit()
        tested.get_visible_for_traceability()
        pass

    def test_Unit_visible_for_traceability_setter(self):
        tested = Unit()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_Unit_owned_constraints_getter(self):
        tested = Unit()
        tested.get_owned_constraints()
        pass

    def test_Unit_constraints_getter(self):
        tested = Unit()
        tested.get_constraints()
        pass

    def test_Unit_constraints_setter(self):
        tested = Unit()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_Unit_owned_property_values_getter(self):
        tested = Unit()
        tested.get_owned_property_values()
        pass

    def test_Unit_applied_property_values_getter(self):
        tested = Unit()
        tested.get_applied_property_values()
        pass

    def test_Unit_applied_property_values_setter(self):
        tested = Unit()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_Unit_owned_property_value_groups_getter(self):
        tested = Unit()
        tested.get_owned_property_value_groups()
        pass

    def test_Unit_applied_property_value_groups_getter(self):
        tested = Unit()
        tested.get_applied_property_value_groups()
        pass

    def test_Unit_applied_property_value_groups_setter(self):
        tested = Unit()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_Unit_owned_enumeration_property_types_getter(self):
        tested = Unit()
        tested.get_owned_enumeration_property_types()
        pass

    def test_Unit_owned_diagrams_getter(self):
        tested = Unit()
        tested.get_owned_diagrams()
        pass

    def test_Unit_element_of_interest_for_diagrams_getter(self):
        tested = Unit()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_Unit_element_of_interest_for_diagrams_setter(self):
        tested = Unit()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_Unit_contextual_element_for_diagrams_getter(self):
        tested = Unit()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_Unit_contextual_element_for_diagrams_setter(self):
        tested = Unit()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_Unit_representing_diagrams_getter(self):
        tested = Unit()
        tested.get_representing_diagrams()
        pass

    def test_Unit__r_e_cs_getter(self):
        tested = Unit()
        tested.get__r_e_cs()
        pass

    def test_Unit__r_e_cs_setter(self):
        tested = Unit()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_Unit__r_p_ls_getter(self):
        tested = Unit()
        tested.get__r_p_ls()
        pass

    def test_Unit__r_p_ls_setter(self):
        tested = Unit()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_Unit_get_label(self):
        tested = Unit()
        tested.get_label()
        pass

    def test_Unit_get_element_type(self):
        tested = Unit()
        tested.get_element_type()
        pass

    def test_Unit_get_container(self):
        tested = Unit()
        tested.get_container()
        pass

    def test_Unit_get_contents(self):
        tested = Unit()
        tested.get_contents()
        pass

    def test_Unit_get_all_contents(self):
        tested = Unit()
        tested.get_all_contents()
        pass

    def test_Unit_get_all_contents_by_type(self):
        tested = Unit()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_Unit_get_available_s_b_queries(self):
        tested = Unit()
        tested.get_available_s_b_queries()
        pass

    def test_Unit_get_query_result(self):
        tested = Unit()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_PVMT_get_p_v_names(self):
        tested = PVMT()
        param1 = RelationType()
        tested.get_p_v_names(param1)
        pass

    def test_PVMT_is_p_v_defined(self):
        tested = PVMT()
        param1 = RelationType()
        param2 = "value"
        tested.is_p_v_defined(param1, param2)
        pass

    def test_PVMT_get_p_v_value(self):
        tested = PVMT()
        param1 = RelationType()
        param2 = "value"
        tested.get_p_v_value(param1, param2)
        pass

    def test_RequirementAddOn_get_requirement_modules(self):
        tested = RequirementAddOn()
        param1 = CapellaModel()
        param1.open("/In-Flight Entertainment System/In-Flight Entertainment System.aird")
        tested.get_requirement_modules(param1)
        pass

    def test_RequirementAddOn_get_incoming_requirements(self):
        tested = RequirementAddOn()
        param1 = RelationType()
        tested.get_incoming_requirements(param1)
        pass

    def test_RequirementAddOn_get_outgoing_requirements(self):
        tested = RequirementAddOn()
        param1 = RelationType()
        tested.get_outgoing_requirements(param1)
        pass

    def test_RequirementAddOn_get_relation_type(self):
        tested = RequirementAddOn()
        param1 = RelationType()
        param2 = RelationType()
        tested.get_relation_type(param1, param2)
        pass

    def test_CapellaModule_owned_diagrams_getter(self):
        tested = CapellaModule()
        tested.get_owned_diagrams()
        pass

    def test_CapellaModule_element_of_interest_for_diagrams_getter(self):
        tested = CapellaModule()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_CapellaModule_element_of_interest_for_diagrams_setter(self):
        tested = CapellaModule()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_CapellaModule_contextual_element_for_diagrams_getter(self):
        tested = CapellaModule()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_CapellaModule_contextual_element_for_diagrams_setter(self):
        tested = CapellaModule()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_CapellaModule_representing_diagrams_getter(self):
        tested = CapellaModule()
        tested.get_representing_diagrams()
        pass

    def test_CapellaModule__r_e_cs_getter(self):
        tested = CapellaModule()
        tested.get__r_e_cs()
        pass

    def test_CapellaModule__r_e_cs_setter(self):
        tested = CapellaModule()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_CapellaModule__r_p_ls_getter(self):
        tested = CapellaModule()
        tested.get__r_p_ls()
        pass

    def test_CapellaModule__r_p_ls_setter(self):
        tested = CapellaModule()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_CapellaModule_get_label(self):
        tested = CapellaModule()
        tested.get_label()
        pass

    def test_CapellaModule_get_element_type(self):
        tested = CapellaModule()
        tested.get_element_type()
        pass

    def test_CapellaModule_get_container(self):
        tested = CapellaModule()
        tested.get_container()
        pass

    def test_CapellaModule_get_contents(self):
        tested = CapellaModule()
        tested.get_contents()
        pass

    def test_CapellaModule_get_all_contents(self):
        tested = CapellaModule()
        tested.get_all_contents()
        pass

    def test_CapellaModule_get_all_contents_by_type(self):
        tested = CapellaModule()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_CapellaModule_get_available_s_b_queries(self):
        tested = CapellaModule()
        tested.get_available_s_b_queries()
        pass

    def test_CapellaModule_get_query_result(self):
        tested = CapellaModule()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_CapellaModule_owned_requirements_getter(self):
        tested = CapellaModule()
        tested.get_owned_requirements()
        pass

    def test_CapellaModule_id_getter(self):
        tested = CapellaModule()
        tested.get_id()
        pass

    def test_CapellaModule_id_setter(self):
        tested = CapellaModule()
        value = "value"
        tested.set_id(value)
        pass

    def test_CapellaModule_long_name_getter(self):
        tested = CapellaModule()
        tested.get_long_name()
        pass

    def test_CapellaModule_long_name_setter(self):
        tested = CapellaModule()
        value = "value"
        tested.set_long_name(value)
        pass

    def test_CapellaModule_name_getter(self):
        tested = CapellaModule()
        tested.get_name()
        pass

    def test_CapellaModule_name_setter(self):
        tested = CapellaModule()
        value = "value"
        tested.set_name(value)
        pass

    def test_CapellaModule_prefix_getter(self):
        tested = CapellaModule()
        tested.get_prefix()
        pass

    def test_CapellaModule_prefix_setter(self):
        tested = CapellaModule()
        value = "value"
        tested.set_prefix(value)
        pass

    def test_Requirement_owned_diagrams_getter(self):
        tested = Requirement()
        tested.get_owned_diagrams()
        pass

    def test_Requirement_element_of_interest_for_diagrams_getter(self):
        tested = Requirement()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_Requirement_element_of_interest_for_diagrams_setter(self):
        tested = Requirement()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_Requirement_contextual_element_for_diagrams_getter(self):
        tested = Requirement()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_Requirement_contextual_element_for_diagrams_setter(self):
        tested = Requirement()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_Requirement_representing_diagrams_getter(self):
        tested = Requirement()
        tested.get_representing_diagrams()
        pass

    def test_Requirement__r_e_cs_getter(self):
        tested = Requirement()
        tested.get__r_e_cs()
        pass

    def test_Requirement__r_e_cs_setter(self):
        tested = Requirement()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_Requirement__r_p_ls_getter(self):
        tested = Requirement()
        tested.get__r_p_ls()
        pass

    def test_Requirement__r_p_ls_setter(self):
        tested = Requirement()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_Requirement_get_label(self):
        tested = Requirement()
        tested.get_label()
        pass

    def test_Requirement_get_element_type(self):
        tested = Requirement()
        tested.get_element_type()
        pass

    def test_Requirement_get_container(self):
        tested = Requirement()
        tested.get_container()
        pass

    def test_Requirement_get_contents(self):
        tested = Requirement()
        tested.get_contents()
        pass

    def test_Requirement_get_all_contents(self):
        tested = Requirement()
        tested.get_all_contents()
        pass

    def test_Requirement_get_all_contents_by_type(self):
        tested = Requirement()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_Requirement_get_available_s_b_queries(self):
        tested = Requirement()
        tested.get_available_s_b_queries()
        pass

    def test_Requirement_get_query_result(self):
        tested = Requirement()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_Requirement_id_getter(self):
        tested = Requirement()
        tested.get_id()
        pass

    def test_Requirement_id_setter(self):
        tested = Requirement()
        value = "value"
        tested.set_id(value)
        pass

    def test_Requirement_long_name_getter(self):
        tested = Requirement()
        tested.get_long_name()
        pass

    def test_Requirement_long_name_setter(self):
        tested = Requirement()
        value = "value"
        tested.set_long_name(value)
        pass

    def test_Requirement_name_getter(self):
        tested = Requirement()
        tested.get_name()
        pass

    def test_Requirement_name_setter(self):
        tested = Requirement()
        value = "value"
        tested.set_name(value)
        pass

    def test_Requirement_chapter_name_getter(self):
        tested = Requirement()
        tested.get_chapter_name()
        pass

    def test_Requirement_chapter_name_setter(self):
        tested = Requirement()
        value = "value"
        tested.set_chapter_name(value)
        pass

    def test_Requirement_description_getter(self):
        tested = Requirement()
        tested.get_description()
        pass

    def test_Requirement_description_setter(self):
        tested = Requirement()
        value = "value"
        tested.set_description(value)
        pass

    def test_Requirement_prefix_getter(self):
        tested = Requirement()
        tested.get_prefix()
        pass

    def test_Requirement_prefix_setter(self):
        tested = Requirement()
        value = "value"
        tested.set_prefix(value)
        pass

    def test_Requirement_text_getter(self):
        tested = Requirement()
        tested.get_text()
        pass

    def test_Requirement_text_setter(self):
        tested = Requirement()
        value = "value"
        tested.set_text(value)
        pass

    def test_Requirement_owned_attributes_getter(self):
        tested = Requirement()
        tested.get_owned_attributes()
        pass

    def test_Requirement_owned_relations_getter(self):
        tested = Requirement()
        tested.get_owned_relations()
        pass

    def test_Requirement_get_all_attributes(self):
        tested = Requirement()
        tested.get_all_attributes()
        pass

    def test_Requirement_get_attribute(self):
        tested = Requirement()
        param1 = "value"
        tested.get_attribute(param1)
        pass

    def test_Requirement_set_attribute(self):
        tested = Requirement()
        param1 = "value"
        param2 = "value"
        tested.set_attribute(param1, param2)
        pass

    def test_Requirement_get_incoming_linked_elems(self):
        tested = Requirement()
        tested.get_incoming_linked_elems()
        pass

    def test_Requirement_get_outgoing_linked_elems(self):
        tested = Requirement()
        tested.get_outgoing_linked_elems()
        pass

    def test_Folder_id_getter(self):
        tested = Folder()
        tested.get_id()
        pass

    def test_Folder_id_setter(self):
        tested = Folder()
        value = "value"
        tested.set_id(value)
        pass

    def test_Folder_long_name_getter(self):
        tested = Folder()
        tested.get_long_name()
        pass

    def test_Folder_long_name_setter(self):
        tested = Folder()
        value = "value"
        tested.set_long_name(value)
        pass

    def test_Folder_name_getter(self):
        tested = Folder()
        tested.get_name()
        pass

    def test_Folder_name_setter(self):
        tested = Folder()
        value = "value"
        tested.set_name(value)
        pass

    def test_Folder_chapter_name_getter(self):
        tested = Folder()
        tested.get_chapter_name()
        pass

    def test_Folder_chapter_name_setter(self):
        tested = Folder()
        value = "value"
        tested.set_chapter_name(value)
        pass

    def test_Folder_description_getter(self):
        tested = Folder()
        tested.get_description()
        pass

    def test_Folder_description_setter(self):
        tested = Folder()
        value = "value"
        tested.set_description(value)
        pass

    def test_Folder_prefix_getter(self):
        tested = Folder()
        tested.get_prefix()
        pass

    def test_Folder_prefix_setter(self):
        tested = Folder()
        value = "value"
        tested.set_prefix(value)
        pass

    def test_Folder_text_getter(self):
        tested = Folder()
        tested.get_text()
        pass

    def test_Folder_text_setter(self):
        tested = Folder()
        value = "value"
        tested.set_text(value)
        pass

    def test_Folder_owned_attributes_getter(self):
        tested = Folder()
        tested.get_owned_attributes()
        pass

    def test_Folder_owned_relations_getter(self):
        tested = Folder()
        tested.get_owned_relations()
        pass

    def test_Folder_get_all_attributes(self):
        tested = Folder()
        tested.get_all_attributes()
        pass

    def test_Folder_get_attribute(self):
        tested = Folder()
        param1 = "value"
        tested.get_attribute(param1)
        pass

    def test_Folder_set_attribute(self):
        tested = Folder()
        param1 = "value"
        param2 = "value"
        tested.set_attribute(param1, param2)
        pass

    def test_Folder_get_incoming_linked_elems(self):
        tested = Folder()
        tested.get_incoming_linked_elems()
        pass

    def test_Folder_get_outgoing_linked_elems(self):
        tested = Folder()
        tested.get_outgoing_linked_elems()
        pass

    def test_Folder_owned_diagrams_getter(self):
        tested = Folder()
        tested.get_owned_diagrams()
        pass

    def test_Folder_element_of_interest_for_diagrams_getter(self):
        tested = Folder()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_Folder_element_of_interest_for_diagrams_setter(self):
        tested = Folder()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_Folder_contextual_element_for_diagrams_getter(self):
        tested = Folder()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_Folder_contextual_element_for_diagrams_setter(self):
        tested = Folder()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_Folder_representing_diagrams_getter(self):
        tested = Folder()
        tested.get_representing_diagrams()
        pass

    def test_Folder__r_e_cs_getter(self):
        tested = Folder()
        tested.get__r_e_cs()
        pass

    def test_Folder__r_e_cs_setter(self):
        tested = Folder()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_Folder__r_p_ls_getter(self):
        tested = Folder()
        tested.get__r_p_ls()
        pass

    def test_Folder__r_p_ls_setter(self):
        tested = Folder()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_Folder_get_label(self):
        tested = Folder()
        tested.get_label()
        pass

    def test_Folder_get_element_type(self):
        tested = Folder()
        tested.get_element_type()
        pass

    def test_Folder_get_container(self):
        tested = Folder()
        tested.get_container()
        pass

    def test_Folder_get_contents(self):
        tested = Folder()
        tested.get_contents()
        pass

    def test_Folder_get_all_contents(self):
        tested = Folder()
        tested.get_all_contents()
        pass

    def test_Folder_get_all_contents_by_type(self):
        tested = Folder()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_Folder_get_available_s_b_queries(self):
        tested = Folder()
        tested.get_available_s_b_queries()
        pass

    def test_Folder_get_query_result(self):
        tested = Folder()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_Folder_owned_requirements_getter(self):
        tested = Folder()
        tested.get_owned_requirements()
        pass

    def test_Attribute_owned_diagrams_getter(self):
        tested = Attribute()
        tested.get_owned_diagrams()
        pass

    def test_Attribute_element_of_interest_for_diagrams_getter(self):
        tested = Attribute()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_Attribute_element_of_interest_for_diagrams_setter(self):
        tested = Attribute()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_Attribute_contextual_element_for_diagrams_getter(self):
        tested = Attribute()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_Attribute_contextual_element_for_diagrams_setter(self):
        tested = Attribute()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_Attribute_representing_diagrams_getter(self):
        tested = Attribute()
        tested.get_representing_diagrams()
        pass

    def test_Attribute__r_e_cs_getter(self):
        tested = Attribute()
        tested.get__r_e_cs()
        pass

    def test_Attribute__r_e_cs_setter(self):
        tested = Attribute()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_Attribute__r_p_ls_getter(self):
        tested = Attribute()
        tested.get__r_p_ls()
        pass

    def test_Attribute__r_p_ls_setter(self):
        tested = Attribute()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_Attribute_get_label(self):
        tested = Attribute()
        tested.get_label()
        pass

    def test_Attribute_get_element_type(self):
        tested = Attribute()
        tested.get_element_type()
        pass

    def test_Attribute_get_container(self):
        tested = Attribute()
        tested.get_container()
        pass

    def test_Attribute_get_contents(self):
        tested = Attribute()
        tested.get_contents()
        pass

    def test_Attribute_get_all_contents(self):
        tested = Attribute()
        tested.get_all_contents()
        pass

    def test_Attribute_get_all_contents_by_type(self):
        tested = Attribute()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_Attribute_get_available_s_b_queries(self):
        tested = Attribute()
        tested.get_available_s_b_queries()
        pass

    def test_Attribute_get_query_result(self):
        tested = Attribute()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_Attribute_definition_getter(self):
        tested = Attribute()
        tested.get_definition()
        pass

    def test_Attribute_definition_setter(self):
        tested = Attribute()
        value = "value"
        tested.set_definition(value)
        pass

    def test_Attribute_value_getter(self):
        tested = Attribute()
        tested.get_value()
        pass

    def test_Attribute_value_setter(self):
        tested = Attribute()
        value = "value"
        tested.set_value(value)
        pass

    def test_ReqIFElement_owned_diagrams_getter(self):
        tested = ReqIFElement()
        tested.get_owned_diagrams()
        pass

    def test_ReqIFElement_element_of_interest_for_diagrams_getter(self):
        tested = ReqIFElement()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_ReqIFElement_element_of_interest_for_diagrams_setter(self):
        tested = ReqIFElement()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_ReqIFElement_contextual_element_for_diagrams_getter(self):
        tested = ReqIFElement()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_ReqIFElement_contextual_element_for_diagrams_setter(self):
        tested = ReqIFElement()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_ReqIFElement_representing_diagrams_getter(self):
        tested = ReqIFElement()
        tested.get_representing_diagrams()
        pass

    def test_ReqIFElement__r_e_cs_getter(self):
        tested = ReqIFElement()
        tested.get__r_e_cs()
        pass

    def test_ReqIFElement__r_e_cs_setter(self):
        tested = ReqIFElement()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_ReqIFElement__r_p_ls_getter(self):
        tested = ReqIFElement()
        tested.get__r_p_ls()
        pass

    def test_ReqIFElement__r_p_ls_setter(self):
        tested = ReqIFElement()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_ReqIFElement_get_label(self):
        tested = ReqIFElement()
        tested.get_label()
        pass

    def test_ReqIFElement_get_element_type(self):
        tested = ReqIFElement()
        tested.get_element_type()
        pass

    def test_ReqIFElement_get_container(self):
        tested = ReqIFElement()
        tested.get_container()
        pass

    def test_ReqIFElement_get_contents(self):
        tested = ReqIFElement()
        tested.get_contents()
        pass

    def test_ReqIFElement_get_all_contents(self):
        tested = ReqIFElement()
        tested.get_all_contents()
        pass

    def test_ReqIFElement_get_all_contents_by_type(self):
        tested = ReqIFElement()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_ReqIFElement_get_available_s_b_queries(self):
        tested = ReqIFElement()
        tested.get_available_s_b_queries()
        pass

    def test_ReqIFElement_get_query_result(self):
        tested = ReqIFElement()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_AbstractRelation_owned_diagrams_getter(self):
        tested = AbstractRelation()
        tested.get_owned_diagrams()
        pass

    def test_AbstractRelation_element_of_interest_for_diagrams_getter(self):
        tested = AbstractRelation()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_AbstractRelation_element_of_interest_for_diagrams_setter(self):
        tested = AbstractRelation()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_AbstractRelation_contextual_element_for_diagrams_getter(self):
        tested = AbstractRelation()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_AbstractRelation_contextual_element_for_diagrams_setter(self):
        tested = AbstractRelation()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_AbstractRelation_representing_diagrams_getter(self):
        tested = AbstractRelation()
        tested.get_representing_diagrams()
        pass

    def test_AbstractRelation__r_e_cs_getter(self):
        tested = AbstractRelation()
        tested.get__r_e_cs()
        pass

    def test_AbstractRelation__r_e_cs_setter(self):
        tested = AbstractRelation()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_AbstractRelation__r_p_ls_getter(self):
        tested = AbstractRelation()
        tested.get__r_p_ls()
        pass

    def test_AbstractRelation__r_p_ls_setter(self):
        tested = AbstractRelation()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_AbstractRelation_get_label(self):
        tested = AbstractRelation()
        tested.get_label()
        pass

    def test_AbstractRelation_get_element_type(self):
        tested = AbstractRelation()
        tested.get_element_type()
        pass

    def test_AbstractRelation_get_container(self):
        tested = AbstractRelation()
        tested.get_container()
        pass

    def test_AbstractRelation_get_contents(self):
        tested = AbstractRelation()
        tested.get_contents()
        pass

    def test_AbstractRelation_get_all_contents(self):
        tested = AbstractRelation()
        tested.get_all_contents()
        pass

    def test_AbstractRelation_get_all_contents_by_type(self):
        tested = AbstractRelation()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_AbstractRelation_get_available_s_b_queries(self):
        tested = AbstractRelation()
        tested.get_available_s_b_queries()
        pass

    def test_AbstractRelation_get_query_result(self):
        tested = AbstractRelation()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_AbstractRelation_relation_type_getter(self):
        tested = AbstractRelation()
        tested.get_relation_type()
        pass

    def test_CapellaIncomingRelation_relation_type_getter(self):
        tested = CapellaIncomingRelation()
        tested.get_relation_type()
        pass

    def test_CapellaIncomingRelation_owned_diagrams_getter(self):
        tested = CapellaIncomingRelation()
        tested.get_owned_diagrams()
        pass

    def test_CapellaIncomingRelation_element_of_interest_for_diagrams_getter(self):
        tested = CapellaIncomingRelation()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_CapellaIncomingRelation_element_of_interest_for_diagrams_setter(self):
        tested = CapellaIncomingRelation()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_CapellaIncomingRelation_contextual_element_for_diagrams_getter(self):
        tested = CapellaIncomingRelation()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_CapellaIncomingRelation_contextual_element_for_diagrams_setter(self):
        tested = CapellaIncomingRelation()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_CapellaIncomingRelation_representing_diagrams_getter(self):
        tested = CapellaIncomingRelation()
        tested.get_representing_diagrams()
        pass

    def test_CapellaIncomingRelation__r_e_cs_getter(self):
        tested = CapellaIncomingRelation()
        tested.get__r_e_cs()
        pass

    def test_CapellaIncomingRelation__r_e_cs_setter(self):
        tested = CapellaIncomingRelation()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_CapellaIncomingRelation__r_p_ls_getter(self):
        tested = CapellaIncomingRelation()
        tested.get__r_p_ls()
        pass

    def test_CapellaIncomingRelation__r_p_ls_setter(self):
        tested = CapellaIncomingRelation()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_CapellaIncomingRelation_get_label(self):
        tested = CapellaIncomingRelation()
        tested.get_label()
        pass

    def test_CapellaIncomingRelation_get_element_type(self):
        tested = CapellaIncomingRelation()
        tested.get_element_type()
        pass

    def test_CapellaIncomingRelation_get_container(self):
        tested = CapellaIncomingRelation()
        tested.get_container()
        pass

    def test_CapellaIncomingRelation_get_contents(self):
        tested = CapellaIncomingRelation()
        tested.get_contents()
        pass

    def test_CapellaIncomingRelation_get_all_contents(self):
        tested = CapellaIncomingRelation()
        tested.get_all_contents()
        pass

    def test_CapellaIncomingRelation_get_all_contents_by_type(self):
        tested = CapellaIncomingRelation()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_CapellaIncomingRelation_get_available_s_b_queries(self):
        tested = CapellaIncomingRelation()
        tested.get_available_s_b_queries()
        pass

    def test_CapellaIncomingRelation_get_query_result(self):
        tested = CapellaIncomingRelation()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_CapellaIncomingRelation_source_getter(self):
        tested = CapellaIncomingRelation()
        tested.get_source()
        pass

    def test_CapellaIncomingRelation_target_getter(self):
        tested = CapellaIncomingRelation()
        tested.get_target()
        pass

    def test_CapellaOutgoingRelation_relation_type_getter(self):
        tested = CapellaOutgoingRelation()
        tested.get_relation_type()
        pass

    def test_CapellaOutgoingRelation_owned_diagrams_getter(self):
        tested = CapellaOutgoingRelation()
        tested.get_owned_diagrams()
        pass

    def test_CapellaOutgoingRelation_element_of_interest_for_diagrams_getter(self):
        tested = CapellaOutgoingRelation()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_CapellaOutgoingRelation_element_of_interest_for_diagrams_setter(self):
        tested = CapellaOutgoingRelation()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_CapellaOutgoingRelation_contextual_element_for_diagrams_getter(self):
        tested = CapellaOutgoingRelation()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_CapellaOutgoingRelation_contextual_element_for_diagrams_setter(self):
        tested = CapellaOutgoingRelation()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_CapellaOutgoingRelation_representing_diagrams_getter(self):
        tested = CapellaOutgoingRelation()
        tested.get_representing_diagrams()
        pass

    def test_CapellaOutgoingRelation__r_e_cs_getter(self):
        tested = CapellaOutgoingRelation()
        tested.get__r_e_cs()
        pass

    def test_CapellaOutgoingRelation__r_e_cs_setter(self):
        tested = CapellaOutgoingRelation()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_CapellaOutgoingRelation__r_p_ls_getter(self):
        tested = CapellaOutgoingRelation()
        tested.get__r_p_ls()
        pass

    def test_CapellaOutgoingRelation__r_p_ls_setter(self):
        tested = CapellaOutgoingRelation()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_CapellaOutgoingRelation_get_label(self):
        tested = CapellaOutgoingRelation()
        tested.get_label()
        pass

    def test_CapellaOutgoingRelation_get_element_type(self):
        tested = CapellaOutgoingRelation()
        tested.get_element_type()
        pass

    def test_CapellaOutgoingRelation_get_container(self):
        tested = CapellaOutgoingRelation()
        tested.get_container()
        pass

    def test_CapellaOutgoingRelation_get_contents(self):
        tested = CapellaOutgoingRelation()
        tested.get_contents()
        pass

    def test_CapellaOutgoingRelation_get_all_contents(self):
        tested = CapellaOutgoingRelation()
        tested.get_all_contents()
        pass

    def test_CapellaOutgoingRelation_get_all_contents_by_type(self):
        tested = CapellaOutgoingRelation()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_CapellaOutgoingRelation_get_available_s_b_queries(self):
        tested = CapellaOutgoingRelation()
        tested.get_available_s_b_queries()
        pass

    def test_CapellaOutgoingRelation_get_query_result(self):
        tested = CapellaOutgoingRelation()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_CapellaOutgoingRelation_source_getter(self):
        tested = CapellaOutgoingRelation()
        tested.get_source()
        pass

    def test_CapellaOutgoingRelation_target_getter(self):
        tested = CapellaOutgoingRelation()
        tested.get_target()
        pass

    def test_AbstractType_id_getter(self):
        tested = AbstractType()
        tested.get_id()
        pass

    def test_AbstractType_id_setter(self):
        tested = AbstractType()
        value = "value"
        tested.set_id(value)
        pass

    def test_AbstractType_sid_getter(self):
        tested = AbstractType()
        tested.get_sid()
        pass

    def test_AbstractType_sid_setter(self):
        tested = AbstractType()
        value = "value"
        tested.set_sid(value)
        pass

    def test_AbstractType_name_getter(self):
        tested = AbstractType()
        tested.get_name()
        pass

    def test_AbstractType_name_setter(self):
        tested = AbstractType()
        value = "value"
        tested.set_name(value)
        pass

    def test_AbstractType_summary_getter(self):
        tested = AbstractType()
        tested.get_summary()
        pass

    def test_AbstractType_summary_setter(self):
        tested = AbstractType()
        value = "value"
        tested.set_summary(value)
        pass

    def test_AbstractType_description_getter(self):
        tested = AbstractType()
        tested.get_description()
        pass

    def test_AbstractType_description_setter(self):
        tested = AbstractType()
        value = "value"
        tested.set_description(value)
        pass

    def test_AbstractType_status_getter(self):
        tested = AbstractType()
        tested.get_status()
        pass

    def test_AbstractType_status_setter(self):
        tested = AbstractType()
        value = "value"
        tested.set_status(value)
        pass

    def test_AbstractType_review_getter(self):
        tested = AbstractType()
        tested.get_review()
        pass

    def test_AbstractType_review_setter(self):
        tested = AbstractType()
        value = "value"
        tested.set_review(value)
        pass

    def test_AbstractType_visible_in_documentation_getter(self):
        tested = AbstractType()
        tested.get_visible_in_documentation()
        pass

    def test_AbstractType_visible_in_documentation_setter(self):
        tested = AbstractType()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_AbstractType_visible_for_traceability_getter(self):
        tested = AbstractType()
        tested.get_visible_for_traceability()
        pass

    def test_AbstractType_visible_for_traceability_setter(self):
        tested = AbstractType()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_AbstractType_owned_constraints_getter(self):
        tested = AbstractType()
        tested.get_owned_constraints()
        pass

    def test_AbstractType_constraints_getter(self):
        tested = AbstractType()
        tested.get_constraints()
        pass

    def test_AbstractType_constraints_setter(self):
        tested = AbstractType()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_AbstractType_owned_property_values_getter(self):
        tested = AbstractType()
        tested.get_owned_property_values()
        pass

    def test_AbstractType_applied_property_values_getter(self):
        tested = AbstractType()
        tested.get_applied_property_values()
        pass

    def test_AbstractType_applied_property_values_setter(self):
        tested = AbstractType()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_AbstractType_owned_property_value_groups_getter(self):
        tested = AbstractType()
        tested.get_owned_property_value_groups()
        pass

    def test_AbstractType_applied_property_value_groups_getter(self):
        tested = AbstractType()
        tested.get_applied_property_value_groups()
        pass

    def test_AbstractType_applied_property_value_groups_setter(self):
        tested = AbstractType()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_AbstractType_owned_enumeration_property_types_getter(self):
        tested = AbstractType()
        tested.get_owned_enumeration_property_types()
        pass

    def test_AbstractType_owned_diagrams_getter(self):
        tested = AbstractType()
        tested.get_owned_diagrams()
        pass

    def test_AbstractType_element_of_interest_for_diagrams_getter(self):
        tested = AbstractType()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_AbstractType_element_of_interest_for_diagrams_setter(self):
        tested = AbstractType()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_AbstractType_contextual_element_for_diagrams_getter(self):
        tested = AbstractType()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_AbstractType_contextual_element_for_diagrams_setter(self):
        tested = AbstractType()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_AbstractType_representing_diagrams_getter(self):
        tested = AbstractType()
        tested.get_representing_diagrams()
        pass

    def test_AbstractType__r_e_cs_getter(self):
        tested = AbstractType()
        tested.get__r_e_cs()
        pass

    def test_AbstractType__r_e_cs_setter(self):
        tested = AbstractType()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_AbstractType__r_p_ls_getter(self):
        tested = AbstractType()
        tested.get__r_p_ls()
        pass

    def test_AbstractType__r_p_ls_setter(self):
        tested = AbstractType()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_AbstractType_get_label(self):
        tested = AbstractType()
        tested.get_label()
        pass

    def test_AbstractType_get_element_type(self):
        tested = AbstractType()
        tested.get_element_type()
        pass

    def test_AbstractType_get_container(self):
        tested = AbstractType()
        tested.get_container()
        pass

    def test_AbstractType_get_contents(self):
        tested = AbstractType()
        tested.get_contents()
        pass

    def test_AbstractType_get_all_contents(self):
        tested = AbstractType()
        tested.get_all_contents()
        pass

    def test_AbstractType_get_all_contents_by_type(self):
        tested = AbstractType()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_AbstractType_get_available_s_b_queries(self):
        tested = AbstractType()
        tested.get_available_s_b_queries()
        pass

    def test_AbstractType_get_query_result(self):
        tested = AbstractType()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_RelationType_id_getter(self):
        tested = RelationType()
        tested.get_id()
        pass

    def test_RelationType_id_setter(self):
        tested = RelationType()
        value = "value"
        tested.set_id(value)
        pass

    def test_RelationType_sid_getter(self):
        tested = RelationType()
        tested.get_sid()
        pass

    def test_RelationType_sid_setter(self):
        tested = RelationType()
        value = "value"
        tested.set_sid(value)
        pass

    def test_RelationType_name_getter(self):
        tested = RelationType()
        tested.get_name()
        pass

    def test_RelationType_name_setter(self):
        tested = RelationType()
        value = "value"
        tested.set_name(value)
        pass

    def test_RelationType_summary_getter(self):
        tested = RelationType()
        tested.get_summary()
        pass

    def test_RelationType_summary_setter(self):
        tested = RelationType()
        value = "value"
        tested.set_summary(value)
        pass

    def test_RelationType_description_getter(self):
        tested = RelationType()
        tested.get_description()
        pass

    def test_RelationType_description_setter(self):
        tested = RelationType()
        value = "value"
        tested.set_description(value)
        pass

    def test_RelationType_status_getter(self):
        tested = RelationType()
        tested.get_status()
        pass

    def test_RelationType_status_setter(self):
        tested = RelationType()
        value = "value"
        tested.set_status(value)
        pass

    def test_RelationType_review_getter(self):
        tested = RelationType()
        tested.get_review()
        pass

    def test_RelationType_review_setter(self):
        tested = RelationType()
        value = "value"
        tested.set_review(value)
        pass

    def test_RelationType_visible_in_documentation_getter(self):
        tested = RelationType()
        tested.get_visible_in_documentation()
        pass

    def test_RelationType_visible_in_documentation_setter(self):
        tested = RelationType()
        value = True
        tested.set_visible_in_documentation(value)
        pass

    def test_RelationType_visible_for_traceability_getter(self):
        tested = RelationType()
        tested.get_visible_for_traceability()
        pass

    def test_RelationType_visible_for_traceability_setter(self):
        tested = RelationType()
        value = True
        tested.set_visible_for_traceability(value)
        pass

    def test_RelationType_owned_constraints_getter(self):
        tested = RelationType()
        tested.get_owned_constraints()
        pass

    def test_RelationType_constraints_getter(self):
        tested = RelationType()
        tested.get_constraints()
        pass

    def test_RelationType_constraints_setter(self):
        tested = RelationType()
        value = Constraint()
        tested.get_constraints().add(value)
        pass

    def test_RelationType_owned_property_values_getter(self):
        tested = RelationType()
        tested.get_owned_property_values()
        pass

    def test_RelationType_applied_property_values_getter(self):
        tested = RelationType()
        tested.get_applied_property_values()
        pass

    def test_RelationType_applied_property_values_setter(self):
        tested = RelationType()
        value = PropertyValue()
        tested.get_applied_property_values().add(value)
        pass

    def test_RelationType_owned_property_value_groups_getter(self):
        tested = RelationType()
        tested.get_owned_property_value_groups()
        pass

    def test_RelationType_applied_property_value_groups_getter(self):
        tested = RelationType()
        tested.get_applied_property_value_groups()
        pass

    def test_RelationType_applied_property_value_groups_setter(self):
        tested = RelationType()
        value = PropertyValueGroup()
        tested.get_applied_property_value_groups().add(value)
        pass

    def test_RelationType_owned_enumeration_property_types_getter(self):
        tested = RelationType()
        tested.get_owned_enumeration_property_types()
        pass

    def test_RelationType_owned_diagrams_getter(self):
        tested = RelationType()
        tested.get_owned_diagrams()
        pass

    def test_RelationType_element_of_interest_for_diagrams_getter(self):
        tested = RelationType()
        tested.get_element_of_interest_for_diagrams()
        pass

    def test_RelationType_element_of_interest_for_diagrams_setter(self):
        tested = RelationType()
        value = Diagram()
        tested.get_element_of_interest_for_diagrams().add(value)
        pass

    def test_RelationType_contextual_element_for_diagrams_getter(self):
        tested = RelationType()
        tested.get_contextual_element_for_diagrams()
        pass

    def test_RelationType_contextual_element_for_diagrams_setter(self):
        tested = RelationType()
        value = Diagram()
        tested.get_contextual_element_for_diagrams().add(value)
        pass

    def test_RelationType_representing_diagrams_getter(self):
        tested = RelationType()
        tested.get_representing_diagrams()
        pass

    def test_RelationType__r_e_cs_getter(self):
        tested = RelationType()
        tested.get__r_e_cs()
        pass

    def test_RelationType__r_e_cs_setter(self):
        tested = RelationType()
        value = REC()
        tested.get__r_e_cs().add(value)
        pass

    def test_RelationType__r_p_ls_getter(self):
        tested = RelationType()
        tested.get__r_p_ls()
        pass

    def test_RelationType__r_p_ls_setter(self):
        tested = RelationType()
        value = RPL()
        tested.get__r_p_ls().add(value)
        pass

    def test_RelationType_get_label(self):
        tested = RelationType()
        tested.get_label()
        pass

    def test_RelationType_get_element_type(self):
        tested = RelationType()
        tested.get_element_type()
        pass

    def test_RelationType_get_container(self):
        tested = RelationType()
        tested.get_container()
        pass

    def test_RelationType_get_contents(self):
        tested = RelationType()
        tested.get_contents()
        pass

    def test_RelationType_get_all_contents(self):
        tested = RelationType()
        tested.get_all_contents()
        pass

    def test_RelationType_get_all_contents_by_type(self):
        tested = RelationType()
        param1 = "value"
        tested.get_all_contents_by_type(param1)
        pass

    def test_RelationType_get_available_s_b_queries(self):
        tested = RelationType()
        tested.get_available_s_b_queries()
        pass

    def test_RelationType_get_query_result(self):
        tested = RelationType()
        param1 = "value"
        tested.get_query_result(param1)
        pass

    def test_RelationType_long_name_getter(self):
        tested = RelationType()
        tested.get_long_name()
        pass

    def test_RelationType_long_name_setter(self):
        tested = RelationType()
        value = "value"
        tested.set_long_name(value)
        pass

    def test_RelationType_name_getter(self):
        tested = RelationType()
        tested.get_name()
        pass

    def test_RelationType_name_setter(self):
        tested = RelationType()
        value = "value"
        tested.set_name(value)
        pass

    def test_RelationType_get_relation_types(self):
        tested = RelationType()
        tested.get_relation_types()
        pass

    def test_RelationType_get_relation_type_by_long_name(self):
        tested = RelationType()
        tested.get_relation_type_by_long_name()
        pass

    def test_RelationType_get_relation_type_by_name(self):
        tested = RelationType()
        tested.get_relation_type_by_name()
        pass



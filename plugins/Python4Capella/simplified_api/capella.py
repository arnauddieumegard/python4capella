include('workspace://Python4Capella/java_api/EMF_API.py')
if False:
    from java_api.EMF_API import *
include('workspace://Python4Capella/java_api/Capella_API.py')
if False:
    from java_api.Capella_API import *
include('workspace://Python4Capella/java_api/Sirius_API.py')
if False:
    from java_api.Sirius_API import *


class CapellaModel(JavaObject):
    def __init__(self, aird_path):
        self.session = Sirius.load_session(aird_path)
    def get_system_engineering(self):
        if self.session is None:
            return None
        else:
            return SystemEngineering(Sirius.get_system_engineering(self.session))
    def get_referenced_libraries(self):
        return create_e_list(self.get_java_object().getReferencedLibraries(), CapellaLibrary)
    def get_all_diagrams(self):
        res = []
        descriptors = Sirius.get_all_diagrams(self.session)
        for descriptor in descriptors:
            res.append(Diagram(descriptor))
        return res
    def get_diagrams(self, diagram_type):
        res = []
        descriptors = Sirius.get_diagrams(self.session, diagram_type)
        for descriptor in descriptors:
            res.append(Diagram(descriptor))
        return res
class CapellaLibrary(CapellaModel):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, CapellaLibrary):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class EObject(JavaObject):
    def get_owned_diagrams(self):
        res = []
        for element in Sirius.get_representation_descriptors(self.get_java_object()):
            res.append(Diagram(element))
        return res
    def get_element_of_interest_for_diagrams(eObject):
        return capella_query("org.polarsys.capella.core.semantic.queries.sirius.annotation.eoi.ElementToRepresentation", self, Diagram)
    def get_contextual_element_for_diagrams(self):
        return create_e_list(self.get_java_object().getContextualElementForDiagrams(), Diagram)
    def get_representing_diagrams(self):
        return create_e_list(self.get_java_object().getRepresentingDiagrams(), Diagram)

class CapellaElement(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/" + capella_version(), "CapellaElement"))
        elif isinstance(java_object, CapellaElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_id(self):
        return self.get_java_object().getId()
    def set_id(self, value):
        self.get_java_object().setId(value)
    def get_sid(self):
        return self.get_java_object().getSid()
    def set_sid(self, value):
        self.get_java_object().setSid(value)
    def get_name(self):
        return self.get_java_object().getName()
    def set_name(self, value):
        self.get_java_object().setName(value)
    def get_summary(self):
        return self.get_java_object().getSummary()
    def set_summary(self, value):
        self.get_java_object().setSummary(value)
    def get_description(self):
        return self.get_java_object().getDescription()
    def set_description(self, value):
        self.get_java_object().setDescription(value)
    def get_status(self):
        value =  self.get_java_object().getStatus()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_status(self, value):
        return self.get_java_object().setStatus(value.get_java_object())
    def get_review(self):
        return self.get_java_object().getReview()
    def set_review(self, value):
        self.get_java_object().setReview(value)
    def get_visible_in_documentation(self):
        return self.get_java_object().isVisibleInDoc()
    def set_visible_in_documentation(self, value):
        self.get_java_object().setVisibleInDoc(value)
    def get_visible_for_traceability(self):
        return self.get_java_object().isVisibleInLM()
    def set_visible_for_traceability(self, value):
        self.get_java_object().setVisibleInLM(value)
    def get_owned_constraints(self):
        return create_e_list(self.get_java_object().getOwnedConstraints(), Constraint)
    def get_constraints(self):
        return create_e_list(self.get_java_object().getConstraints(), Constraint)
    def get_owned_property_values(self):
        return create_e_list(self.get_java_object().getOwnedPropertyValues(), PropertyValue)
    def get_applied_property_values(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaElement_applied_property_values", self)
    def get_owned_property_value_groups(self):
        return create_e_list(self.get_java_object().getOwnedPropertyValueGroups(), PropertyValueGroup)
    def get_applied_property_value_groups(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapellaElement_applied_property_value_groups", self)
    def get_owned_enumeration_property_types(self):
        return create_e_list(self.get_java_object().getOwnedEnumerationPropertyTypes(), EnumerationPropertyType)

class Constraint(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/" + capella_version(), "Constraint"))
        elif isinstance(java_object, Constraint):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_specification(self):
        return self.get_java_object().getSpecification()
    def set_specification(self, value):
        self.get_java_object().setSpecification(value)
    def get_constrained_elements(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ConstraintModelElements", self)

class PropertyValue(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, PropertyValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_kind(self, value):
        return self.get_java_object().setKind(value.get_java_object())
    def get_value(self):
        return self.get_java_object().getValue()
    def set_value(self, value):
        self.get_java_object().setValue(value)
    def get_valued_elements(self):
        return create_e_list(self.get_java_object().getValuedElements(), CapellaElement)
    def get_type(self):
        value =  self.get_java_object().getType()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_type(self, value):
        return self.get_java_object().setType(value.get_java_object())

class PropertyValueGroup(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/" + capella_version(), "PropertyValueGroup"))
        elif isinstance(java_object, PropertyValueGroup):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_valued_elements(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PropertyValueGroup_applying_valued_element", self)

class EnumerationPropertyType(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/" + capella_version(), "EnumerationPropertyType"))
        elif isinstance(java_object, EnumerationPropertyType):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_literals(self):
        return create_e_list(self.get_java_object().getOwnedLiterals(), EnumerationPropertyLiteral)

class EnumerationPropertyLiteral(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/" + capella_version(), "EnumerationPropertyLiteral"))
        elif isinstance(java_object, EnumerationPropertyLiteral):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class PropertyValuePkgContainer(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, PropertyValuePkgContainer):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_property_value_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedPropertyValuePkgs(), PropertyValuePkg)

class Diagram(JavaObject):
    def __init__(self, java_object = None):
        if java_object is None:
            JavaObject.__init__(self, create_e_object("http://www.eclipse.org/sirius/1.1.0", "DRepresentationDescriptor"))
        elif isinstance(java_object, PhysicalFunction):
            JavaObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_uid(self):
        return self.get_java_object().getUid()
    def set_uid(self, value):
        self.get_java_object().setUid(value)
    def get_name(self):
        return self.get_java_object().getName()
    def set_name(self, value):
        self.get_java_object().setName(value)
    def get_type(self):
        if self.getDescription() is None:
            return None
        else:
            return self.getDescription().getName()
    def get_package(self):
        if self.getTarget() is None:
            return None
        else:
            return self.getTarget().eClass().getEPackage().getName()
    def get_description(self):
        return self.get_java_object().getDocumentation()
    def set_description(self, value):
        self.get_java_object().setDocumentation(value)
    def get_status(self):
        value = Sirius.get_status(self.get_java_object())
        if value is None:
            return value
        else:
            return Status(value)
    def get_review(self):
        return Sirius.get_review(self.get_java_object())
    def get_visible_in_documentation(self):
        return Sirius.is_visible_in_documentation(self.get_java_object())
    def get_visible_for_traceability(self):
        return Sirius.is_visible_for_traceability(self.get_java_object())
    def get_synchronized(self):
        return Sirius.is_synchronized(self.get_java_object())
    def get_target(self):
        value =  self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_target(self, value):
        return self.get_java_object().setTarget(value.get_java_object())
    def get_represented_elements(self):
        res = []
        for element in Sirius.get_represented_elements(self.get_java_object()):
            specific_cls = getattr(sys.modules["__main__"], element.eClass().getName())
            if specific_cls is not None:
                res.append(specific_cls())
        return res
    def get_contextual_elements(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.sirius.annotation.eoi.RepresentationToContextualElement", self)
    def get_elements_of_interest(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.sirius.annotation.eoi.RepresentationToElement", self)
    def export_as_image(self, file_path):
        Sirius.export_image(self.get_java_object(), file_path)

class AbstractReElement(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, AbstractReElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_id(self):
        return self.get_java_object().getId()
    def set_id(self, value):
        self.get_java_object().setId(value)
    def get_name(self):
        return self.get_java_object().getName()
    def set_name(self, value):
        self.get_java_object().setName(value)

class AbstractCatalogElement(AbstractReElement):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, AbstractCatalogElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_decription(self):
        return self.get_java_object().getDecription()
    def set_decription(self, value):
        self.get_java_object().setDecription(value)
    def get_author(self):
        return self.get_java_object().getAuthor()
    def set_author(self, value):
        self.get_java_object().setAuthor(value)
    def get_environment(self):
        return self.get_java_object().getEnvironment()
    def set_environment(self, value):
        self.get_java_object().setEnvironment(value)
    def get_tags(self):
        return self.get_java_object().getTags()
    def set_tags(self, value):
        self.get_java_object().setTags(value)
    def get_referenced_elements(self):
        return create_e_list(self.get_java_object().getReferencedElements(), EObject)

class REC(AbstractCatalogElement):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, REC):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_default_replica_compliancy(self):
        value =  self.get_java_object().getDefaultReplicaCompliancy()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_default_replica_compliancy(self, value):
        return self.get_java_object().setDefaultReplicaCompliancy(value.get_java_object())
    def get_replicated_elements(self):
        return create_e_list(self.get_java_object().getReplicatedElements(), RPL)

class RPL(AbstractCatalogElement):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, RPL):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_suffix(self):
        return self.get_java_object().getSuffix()
    def set_suffix(self, value):
        self.get_java_object().setSuffix(value)
    def get_read_only(self):
        return self.get_java_object().isReadOnly()
    def set_read_only(self, value):
        self.get_java_object().setReadOnly(value)
    def get_origin(self):
        value =  self.get_java_object().getOrigin()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_origin(self, value):
        return self.get_java_object().setOrigin(value.get_java_object())
    def get_current_compliancy(self):
        value =  self.get_java_object().getCurrentCompliancy()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_current_compliancy(self, value):
        return self.get_java_object().setCurrentCompliancy(value.get_java_object())

class CatalogElementPkg(AbstractReElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/" + capella_version(), "CatalogElementPkg"))
        elif isinstance(java_object, CatalogElementPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_element_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedElementPkgs(), CatalogElementPkg)
    def get_owned_recs(self):
        return create_e_list(self.get_java_object().getOwnedRecs(), REC)
    def get_owned_rpls(self):
        return create_e_list(self.get_java_object().getOwnedRpls(), RPL)

class RecCatalog(CatalogElementPkg):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/" + capella_version(), "RecCatalog"))
        elif isinstance(java_object, RecCatalog):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_compliancy_definition_pkg(self):
        value =  self.get_java_object().getOwnedCompliancyDefinitionPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_owned_compliancy_definition_pkg(self, value):
        return self.get_java_object().setOwnedCompliancyDefinitionPkg(value.get_java_object())

class CompliancyDefinitionPkg(AbstractReElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/" + capella_version(), "CompliancyDefinitionPkg"))
        elif isinstance(java_object, CompliancyDefinitionPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_definitions(self):
        return create_e_list(self.get_java_object().getOwnedDefinitions(), CompliancyDefinition)

class CompliancyDefinition(AbstractReElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/re/" + capella_version(), "CompliancyDefinition"))
        elif isinstance(java_object, CompliancyDefinition):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_description(self):
        return self.get_java_object().getDescription()
    def set_description(self, value):
        self.get_java_object().setDescription(value)

class OperationalAnalysis(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/" + capella_version(), "OperationalAnalysis"))
        elif isinstance(java_object, OperationalAnalysis):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_operational_activity_pkg(self):
        value =  self.get_java_object().getContainedOperationalActivityPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_operational_activity_pkg(self, value):
        return self.get_java_object().setContainedOperationalActivityPkg(value.get_java_object())
    def get_operational_capability_pkg(self):
        value =  self.get_java_object().getContainedOperationalCapabilityPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_operational_capability_pkg(self, value):
        return self.get_java_object().setContainedOperationalCapabilityPkg(value.get_java_object())
    def get_interface_pkg(self):
        value =  self.get_java_object().getOwnedInterfacePkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_interface_pkg(self, value):
        return self.get_java_object().setOwnedInterfacePkg(value.get_java_object())
    def get_data_pkg(self):
        value =  self.get_java_object().getOwnedDataPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_data_pkg(self, value):
        return self.get_java_object().setOwnedDataPkg(value.get_java_object())
    def get_entity_pkg(self):
        value =  self.get_java_object().getOwnedEntityPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_entity_pkg(self, value):
        return self.get_java_object().setOwnedEntityPkg(value.get_java_object())

class OperationalActivityPkg(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/" + capella_version(), "OperationalActivityPkg"))
        elif isinstance(java_object, OperationalActivityPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_operational_activity_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedOperationalActivityPkgs(), OperationalActivityPkg)
    def get_owned_operational_activities(self):
        return create_e_list(self.get_java_object().getOwnedOperationalActivities(), OperationalActivity)

class OperationalProcess(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/" + capella_version(), "OperationalProcess"))
        elif isinstance(java_object, OperationalProcess):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_involved_operational_activities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.OperationalProcessInvolvedOperationalActivities", self)
    def get_involved_interactions(self):
        return create_e_list(self.get_java_object().getInvolvedInteractions(), Interaction)
    def get_involved_operational_processes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.OperationalProcessChildren", self)
    def get_pre_condition(self):
        value =  self.get_java_object().getPreCondition()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_pre_condition(self, value):
        return self.get_java_object().setPreCondition(value.get_java_object())
    def get_post_condition(self):
        value =  self.get_java_object().getPostCondition()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_post_condition(self, value):
        return self.get_java_object().setPostCondition(value.get_java_object())
    def get_available_in_states(self):
        return create_e_list(self.get_java_object().getAvailableInStates(), State)
    def get_involving_operational_capabilities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainInvolvingCapability", self)
    def get_realizing_functional_chains(self):
        return create_e_list(self.get_java_object().getRealizingFunctionalChains(), FunctionalChain)

class OperationalCapabilityPkg(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/" + capella_version(), "OperationalCapabilityPkg"))
        elif isinstance(java_object, OperationalCapabilityPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_operational_capability_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedOperationalCapabilityPkgs(), OperationalCapabilityPkg)
    def get_owned_operational_capabilities(self):
        return create_e_list(self.get_java_object().getOwnedOperationalCapabilities(), OperationalCapability)

class EntityPkg(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/" + capella_version(), "EntityPkg"))
        elif isinstance(java_object, EntityPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_entity_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedEntityPkgs(), EntityPkg)
    def get_owned_entities(self):
        return create_e_list(self.get_java_object().getOwnedEntities(), OperationalActor)

class OperationalActor(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, OperationalActor):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_incoming_communication_means(self):
        return create_e_list(self.get_java_object().getIncomingCommunicationMeans(), CommunicationMean)
    def get_outgoing_communication_means(self):
        return create_e_list(self.get_java_object().getOutgoingCommunicationMeans(), CommunicationMean)
    def get_allocated_operational_activities(self):
        return create_e_list(self.get_java_object().getAllocatedOperationalActivities(), OperationalActivity)
    def get_involving_operational_capabilities(self):
        return create_e_list(self.get_java_object().getInvolvingOperationalCapabilities(), OperationalCapability)
    def get_owned_state_machines(self):
        return create_e_list(self.get_java_object().getOwnedStateMachines(), StateMachine)
    def get_realizing_system_actors(self):
        return create_e_list(self.get_java_object().getRealizingSystemActors(), SystemActor)

class CommunicationMean(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/" + capella_version(), "CommunicationMean"))
        elif isinstance(java_object, CommunicationMean):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_source_entity(self):
        value =  self.get_java_object().getSourceEntity()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_source_entity(self, value):
        return self.get_java_object().setSourceEntity(value.get_java_object())
    def get_target_entity(self):
        value =  self.get_java_object().getTargetEntity()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_target_entity(self, value):
        return self.get_java_object().setTargetEntity(value.get_java_object())
    def get_allocated_interactions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CommunicationMean_AllocatedExchanges", self)
    def get_convoyed_informations(self):
        return create_e_list(self.get_java_object().getConvoyedInformations(), ExchangeItem)
    def get_realizing_component_exchanges(self):
        return create_e_list(self.get_java_object().getRealizingComponentExchanges(), ComponentExchange)

class SystemAnalysis(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "SystemAnalysis"))
        elif isinstance(java_object, SystemAnalysis):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_system_function_pkg(self):
        value =  self.get_java_object().getContainedSystemFunctionPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_system_function_pkg(self, value):
        return self.get_java_object().setContainedSystemFunctionPkg(value.get_java_object())
    def get_capability_pkg(self):
        value =  self.get_java_object().getContainedCapabilityPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_capability_pkg(self, value):
        return self.get_java_object().setContainedCapabilityPkg(value.get_java_object())
    def get_interface_pkg(self):
        value =  self.get_java_object().getOwnedInterfacePkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_interface_pkg(self, value):
        return self.get_java_object().setOwnedInterfacePkg(value.get_java_object())
    def get_data_pkg(self):
        value =  self.get_java_object().getOwnedDataPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_data_pkg(self, value):
        return self.get_java_object().setOwnedDataPkg(value.get_java_object())
    def get_system_component_pkg(self):
        value =  self.get_java_object().getOwnedSystemComponentPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_system_component_pkg(self, value):
        return self.get_java_object().setOwnedSystemComponentPkg(value.get_java_object())
    def get_mission_pkg(self):
        value =  self.get_java_object().getOwnedMissionPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_mission_pkg(self, value):
        return self.get_java_object().setOwnedMissionPkg(value.get_java_object())

class SystemFunctionPkg(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "SystemFunctionPkg"))
        elif isinstance(java_object, SystemFunctionPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_system_function_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedSystemFunctionPkgs(), SystemFunctionPkg)
    def get_owned_system_functions(self):
        return create_e_list(self.get_java_object().getOwnedSystemFunctions(), SystemFunction)

class CapabilityPkg(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "CapabilityPkg"))
        elif isinstance(java_object, CapabilityPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_capability_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedCapabilityPkgs(), CapabilityPkg)
    def get_owned_capabilities(self):
        return create_e_list(self.get_java_object().getOwnedCapabilities(), Capability)

class SystemComponentPkg(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "SystemComponentPkg"))
        elif isinstance(java_object, SystemComponentPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_system_component_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedSystemComponentPkgs(), SystemComponentPkg)
    def get_owned_system(self):
        value =  self.get_java_object().getOwnedSystem()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_owned_system(self, value):
        return self.get_java_object().setOwnedSystem(value.get_java_object())
    def get_owned_actors(self):
        return create_e_list(self.get_java_object().getOwnedActors(), SystemActor)

class MissionPkg(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "MissionPkg"))
        elif isinstance(java_object, MissionPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_mission_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedMissionPkgs(), MissionPkg)
    def get_owned_missions(self):
        return create_e_list(self.get_java_object().getOwnedMissions(), Mission)

class Mission(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "Mission"))
        elif isinstance(java_object, Mission):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_exploited_capabilities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Mission_ExploitedCapabilities", self)
    def get_involved_actors(self):
        return create_e_list(self.get_java_object().getInvolvedActors(), SystemActor)

class LogicalArchitecture(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalArchitecture"))
        elif isinstance(java_object, LogicalArchitecture):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_logical_function_pkg(self):
        value =  self.get_java_object().getContainedLogicalFunctionPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_logical_function_pkg(self, value):
        return self.get_java_object().setContainedLogicalFunctionPkg(value.get_java_object())
    def get_capability_realization_pkg(self):
        value =  self.get_java_object().getContainedCapabilityRealizationPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_capability_realization_pkg(self, value):
        return self.get_java_object().setContainedCapabilityRealizationPkg(value.get_java_object())
    def get_interface_pkg(self):
        value =  self.get_java_object().getOwnedInterfacePkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_interface_pkg(self, value):
        return self.get_java_object().setOwnedInterfacePkg(value.get_java_object())
    def get_data_pkg(self):
        value =  self.get_java_object().getOwnedDataPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_data_pkg(self, value):
        return self.get_java_object().setOwnedDataPkg(value.get_java_object())
    def get_logical_component_pkg(self):
        value =  self.get_java_object().getOwnedLogicalComponentPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_logical_component_pkg(self, value):
        return self.get_java_object().setOwnedLogicalComponentPkg(value.get_java_object())

class LogicalFunctionPkg(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalFunctionPkg"))
        elif isinstance(java_object, LogicalFunctionPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_logical_function_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedLogicalFunctionPkgs(), LogicalFunctionPkg)
    def get_owned_logical_functions(self):
        return create_e_list(self.get_java_object().getOwnedLogicalFunctions(), LogicalFunction)

class CapabilityRealizationPkg(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/" + capella_version(), "CapabilityRealizationPkg"))
        elif isinstance(java_object, CapabilityRealizationPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_capability_realization_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedCapabilityRealizationPkgs(), CapabilityRealizationPkg)
    def get_owned_capability_realizations(self):
        return create_e_list(self.get_java_object().getOwnedCapabilityRealizations(), CapabilityRealization)

class LogicalComponentPkg(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalComponentPkg"))
        elif isinstance(java_object, LogicalComponentPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_logical_component_pkgs(self):
        value =  self.get_java_object().getOwnedLogicalComponentPkgs()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_owned_logical_component_pkgs(self, value):
        return self.get_java_object().setOwnedLogicalComponentPkgs(value.get_java_object())
    def get_owned_logical_system(self):
        value =  self.get_java_object().getOwnedLogicalSystem()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_owned_logical_system(self, value):
        return self.get_java_object().setOwnedLogicalSystem(value.get_java_object())
    def get_owned_logical_actors(self):
        return create_e_list(self.get_java_object().getOwnedLogicalActors(), LogicalActor)
    def get_owned_logical_components(self):
        return create_e_list(self.get_java_object().getOwnedLogicalComponents(), LogicalComponent)

class PhysicalArchitecture(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalArchitecture"))
        elif isinstance(java_object, PhysicalArchitecture):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_physical_function_pkg(self):
        value =  self.get_java_object().getContainedPhysicalFunctionPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_physical_function_pkg(self, value):
        return self.get_java_object().setContainedPhysicalFunctionPkg(value.get_java_object())
    def get_capability_realization_pkg(self):
        value =  self.get_java_object().getContainedCapabilityRealizationPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_capability_realization_pkg(self, value):
        return self.get_java_object().setContainedCapabilityRealizationPkg(value.get_java_object())
    def get_interface_pkg(self):
        value =  self.get_java_object().getOwnedInterfacePkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_interface_pkg(self, value):
        return self.get_java_object().setOwnedInterfacePkg(value.get_java_object())
    def get_data_pkg(self):
        value =  self.get_java_object().getOwnedDataPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_data_pkg(self, value):
        return self.get_java_object().setOwnedDataPkg(value.get_java_object())
    def get_physical_component_pkg(self):
        value =  self.get_java_object().getOwnedPhysicalComponentPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_physical_component_pkg(self, value):
        return self.get_java_object().setOwnedPhysicalComponentPkg(value.get_java_object())

class PhysicalFunctionPkg(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalFunctionPkg"))
        elif isinstance(java_object, PhysicalFunctionPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_physical_function_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalFunctionPkgs(), PhysicalFunctionPkg)
    def get_owned_physical_functions(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalFunctions(), PhysicalFunction)

class PhysicalComponentPkg(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponentPkg"))
        elif isinstance(java_object, PhysicalComponentPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_physical_component_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalComponentPkgs(), PhysicalComponentPkg)
    def get_owned_physical_system(self):
        value =  self.get_java_object().getOwnedPhysicalSystem()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_owned_physical_system(self, value):
        return self.get_java_object().setOwnedPhysicalSystem(value.get_java_object())
    def get_owned_physical_actors(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalActors(), PhysicalActor)
    def get_owned_physical_components(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalComponents(), PhysicalComponent)

class PhysicalSystem(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, PhysicalSystem):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_physical_components(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalComponents(), PhysicalComponent)
    def get_owned_physical_component_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalComponentPkgs(), PhysicalComponentPkg)

class AbstractPhysicalArtifact(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/" + capella_version(), "AbstractPhysicalArtifact"))
        elif isinstance(java_object, AbstractPhysicalArtifact):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_allocator_configuration_items(self):
        return create_e_list(self.get_java_object().getAllocatorConfigurationItems(), ConfigurationItem)

class PhysicalComponent(AbstractPhysicalArtifact):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalComponent"))
        elif isinstance(java_object, PhysicalComponent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_kind(self, value):
        return self.get_java_object().setKind(value.get_java_object())
    def get_owned_physical_components(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalComponents(), PhysicalComponent)
    def get_owned_physical_component_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalComponentPkgs(), PhysicalComponentPkg)
    def get_is_human(self):
        return self.get_java_object().isIsHuman()
    def set_is_human(self, value):
        self.get_java_object().setIsHuman(value)
    def get_involving_capability_realizations(self):
        return create_e_list(self.get_java_object().getInvolvingCapabilityRealizations(), CapabilityRealization)

class EPBSArchitecture(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/epbs/" + capella_version(), "EPBSArchitecture"))
        elif isinstance(java_object, EPBSArchitecture):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_capability_realization_pkg(self):
        value =  self.get_java_object().getContainedCapabilityRealizationPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_capability_realization_pkg(self, value):
        return self.get_java_object().setContainedCapabilityRealizationPkg(value.get_java_object())
    def get_configuration_item_pkg(self):
        value =  self.get_java_object().getOwnedConfigurationItemPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_configuration_item_pkg(self, value):
        return self.get_java_object().setOwnedConfigurationItemPkg(value.get_java_object())
    def get_data_pkg(self):
        value =  self.get_java_object().getOwnedDataPkg()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_data_pkg(self, value):
        return self.get_java_object().setOwnedDataPkg(value.get_java_object())

class ConfigurationItemPkg(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/epbs/" + capella_version(), "ConfigurationItemPkg"))
        elif isinstance(java_object, ConfigurationItemPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_configuration_item_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedConfigurationItemPkgs(), ConfigurationItemPkg)
    def get_owned_configuration_items(self):
        return create_e_list(self.get_java_object().getOwnedConfigurationItems(), ConfigurationItem)

class ConfigurationItem(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/epbs/" + capella_version(), "ConfigurationItem"))
        elif isinstance(java_object, ConfigurationItem):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_item_identifier(self):
        return self.get_java_object().getItemIdentifier()
    def set_item_identifier(self, value):
        self.get_java_object().setItemIdentifier(value)
    def get_kind(self):
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_kind(self, value):
        return self.get_java_object().setKind(value.get_java_object())
    def get_owned_configuration_items(self):
        return create_e_list(self.get_java_object().getOwnedConfigurationItems(), ConfigurationItem)
    def get_owned_configuration_item_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedConfigurationItemPkgs(), ConfigurationItemPkg)
    def get_allocated_physical_artifacts(self):
        return create_e_list(self.get_java_object().getAllocatedPhysicalArtifacts(), AbstractPhysicalArtifact)

class StateMachine(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), "StateMachine"))
        elif isinstance(java_object, StateMachine):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_regions(self):
        return create_e_list(self.get_java_object().getOwnedRegions(), Region)

class AbstractState(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), "AbstractState"))
        elif isinstance(java_object, AbstractState):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_incoming(self):
        return create_e_list(self.get_java_object().getIncoming(), StateTransition)
    def get_outgoing(self):
        return create_e_list(self.get_java_object().getOutgoing(), StateTransition)
    def get_realized_states(self):
        return create_e_list(self.get_java_object().getRealizedAbstractStates(), AbstractState)
    def get_realizing_states(self):
        return create_e_list(self.get_java_object().getRealizingAbstractStates(), AbstractState)

class State(AbstractState):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), "State"))
        elif isinstance(java_object, State):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_regions(self):
        return create_e_list(self.get_java_object().getOwnedRegions(), Region)
    def get_available_activities__functions(self):
        return create_e_list(self.get_java_object().getAvailableActivities_Functions(), AbstractActivityFunction)
    def get_entry(self):
        return create_e_list(self.get_java_object().getEntry(), AbstractAction)
    def get_do(self):
        return create_e_list(self.get_java_object().getDo(), AbstractAction)
    def get_exit(self):
        return create_e_list(self.get_java_object().getExit(), AbstractAction)
    def get_available_functional_chains(self):
        return create_e_list(self.get_java_object().getAvailableFunctionalChains(), FunctionalChain)
    def get_available_operational_processes(self):
        return create_e_list(self.get_java_object().getAvailableOperationalProcesses(), OperationalProcess)
    def get_available_capabilities(self):
        return create_e_list(self.get_java_object().getAvailableAbstractCapabilities(), AbstractCapability)

class Mode(State):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), "Mode"))
        elif isinstance(java_object, Mode):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Pseudostate(AbstractState):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), "Pseudostate"))
        elif isinstance(java_object, Pseudostate):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_kind(self, value):
        return self.get_java_object().setKind(value.get_java_object())

class Region(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), "Region"))
        elif isinstance(java_object, Region):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_states(self):
        return create_e_list(self.get_java_object().getOwnedStates(), AbstractState)

class StateTransition(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), "StateTransition"))
        elif isinstance(java_object, StateTransition):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_trigger_description(self):
        return self.get_java_object().getTriggerDescription()
    def set_trigger_description(self, value):
        self.get_java_object().setTriggerDescription(value)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.StateTransitionInComingIState", self)
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.StateTransitionOutGoingIState", self)
    def get_triggers(self):
        return create_e_list(self.get_java_object().getTriggers(), AbstractEvent)
    def get_guard(self):
        value =  self.get_java_object().getGuard()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_guard(self, value):
        return self.get_java_object().setGuard(value.get_java_object())
    def get_effects(self):
        return create_e_list(self.get_java_object().getEffects(), AbstractAction)
    def get_realized_state_transitions(self):
        return create_e_list(self.get_java_object().getRealizedStateTransitions(), StateTransition)
    def get_realizing_state_transitions(self):
        return create_e_list(self.get_java_object().getRealizingStateTransitions(), StateTransition)

class AbstractAction(JavaObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/activity/" + capella_version(), "AbstractAction"))
        elif isinstance(java_object, AbstractAction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class AbstractEvent(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/common/behavior/" + capella_version(), "AbstractEvent"))
        elif isinstance(java_object, AbstractEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Scenario(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "Scenario"))
        elif isinstance(java_object, Scenario):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_kind(self, value):
        return self.get_java_object().setKind(value.get_java_object())
    def get_pre_condition(self):
        value =  self.get_java_object().getPreCondition()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_pre_condition(self, value):
        return self.get_java_object().setPreCondition(value.get_java_object())
    def get_post_condition(self):
        value =  self.get_java_object().getPostCondition()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_post_condition(self, value):
        return self.get_java_object().setPostCondition(value.get_java_object())
    def get_owned_instance_roles(self):
        return create_e_list(self.get_java_object().getOwnedInstanceRoles(), InstanceRole)
    def get_owned_messages(self):
        return create_e_list(self.get_java_object().getOwnedMessages(), SequenceMessage)
    def get_owned_state_fragments(self):
        return create_e_list(self.get_java_object().getOwnedStateFragments(), StateFragment)
    def get_owned_combined_fragments(self):
        return create_e_list(self.get_java_object().getOwnedCombinedFragments(), CombinedFragment)
    def get_owned_constraint_durations(self):
        return create_e_list(self.get_java_object().getOwnedConstraintDurations(), ConstraintDuration)
    def get_referenced_scenarios(self):
        return create_e_list(self.get_java_object().getReferencedScenarios(), Scenario)
    def get_realized_scenarios(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Scenario_realizedScenario", self)
    def get_realizing_scenarios(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Scenario_realizingScenario", self)

class InstanceRole(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "InstanceRole"))
        elif isinstance(java_object, InstanceRole):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_represented_instance(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.InstanceRole_representedInstance", self)

class AbstractInstance(JavaObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "AbstractInstance"))
        elif isinstance(java_object, AbstractInstance):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class SequenceMessage(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "SequenceMessage"))
        elif isinstance(java_object, SequenceMessage):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_kind(self, value):
        return self.get_java_object().setKind(value.get_java_object())
    def get_sending_instance_role(self):
        value =  self.get_java_object().getSendingInstanceRole()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_sending_instance_role(self, value):
        return self.get_java_object().setSendingInstanceRole(value.get_java_object())
    def get_receiving_instance_role(self):
        value =  self.get_java_object().getReceivingInstanceRole()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_receiving_instance_role(self, value):
        return self.get_java_object().setReceivingInstanceRole(value.get_java_object())
    def get_invoked_exchange(self):
        value =  self.get_java_object().getInvokedExchange()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_invoked_exchange(self, value):
        return self.get_java_object().setInvokedExchange(value.get_java_object())
    def get_exchanged_items(self):
        return create_e_list(self.get_java_object().getExchangedItems(), ExchangeItem)
    def get_invoked_operation(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SequenceMessage_invokedOperation", self)
    def get_exchange_context(self):
        value =  self.get_java_object().getExchangeContext()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_exchange_context(self, value):
        return self.get_java_object().setExchangeContext(value.get_java_object())

class AbstractExchange(JavaObject):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, AbstractExchange):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_invoking_sequence_messages(self):
        return create_e_list(self.get_java_object().getInvokingSequenceMessages(), SequenceMessage)

class StateFragment(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "StateFragment"))
        elif isinstance(java_object, StateFragment):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_covered_instance_role(self):
        value =  self.get_java_object().getCoveredInstanceRole()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_covered_instance_role(self, value):
        return self.get_java_object().setCoveredInstanceRole(value.get_java_object())
    def get_related_state(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.StateFragmentRelatedStates", self)
    def get_related_activity_function(self):
        value =  self.get_java_object().getRelatedActivityFunction()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_related_activity_function(self, value):
        return self.get_java_object().setRelatedActivityFunction(value.get_java_object())

class CombinedFragment(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "CombinedFragment"))
        elif isinstance(java_object, CombinedFragment):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_operator(self):
        value =  self.get_java_object().getOperator()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_operator(self, value):
        return self.get_java_object().setOperator(value.get_java_object())
    def get_operands(self):
        return create_e_list(self.get_java_object().getOperands(), Operand)
    def get_covered_instance_roles(self):
        return create_e_list(self.get_java_object().getCoveredInstanceRoles(), InstanceRole)

class Operand(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, Operand):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_guard(self):
        value =  self.get_java_object().getGuard()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_guard(self, value):
        return self.get_java_object().setGuard(value.get_java_object())
    def get_referenced_messages(self):
        return create_e_list(self.get_java_object().getReferencedMessages(), SequenceMessage)
    def get_referenced_fragments(self):
        return create_e_list(self.get_java_object().getReferencedFragments(), StateFragment)

class ConstraintDuration(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "ConstraintDuration"))
        elif isinstance(java_object, ConstraintDuration):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_duration(self):
        return self.get_java_object().getDuration()
    def set_duration(self, value):
        self.get_java_object().setDuration(value)

class Node(AbstractInstance):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, Node):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_contained_physical_ports(self):
        return create_e_list(self.get_java_object().getContainedPhysicalPorts(), PhysicalPort)
    def get_physical_links(self):
        return create_e_list(self.get_java_object().getInvolvedLinks(), PhysicalLink)
    def get_involving_physical_paths(self):
        return create_e_list(self.get_java_object().getInvolvingPhysicalPaths(), PhysicalPath)

class PhysicalPort(AbstractPhysicalArtifact):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/" + capella_version(), "PhysicalPort"))
        elif isinstance(java_object, PhysicalPort):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_physical_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalPortIncomingPhysicalLinks", self)
    def get_allocated_component_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalPortAllocatedComponentPorts", self)
    def get_realized_physical_ports(self):
        return create_e_list(self.get_java_object().getRealizedPhysicalPorts(), PhysicalPort)
    def get_realizing_physical_ports(self):
        return create_e_list(self.get_java_object().getRealizingPhysicalPorts(), PhysicalPort)

class PhysicalLink(AbstractPhysicalArtifact):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/" + capella_version(), "PhysicalLink"))
        elif isinstance(java_object, PhysicalLink):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_connected_physical_ports(self):
        return create_e_list(self.get_java_object().getConnectedPhysicalPorts(), PhysicalPort)
    def get_categories(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalLinkCategories", self)
    def get_involving_physical_paths(self):
        return create_e_list(self.get_java_object().getInvolvingPhysicalPaths(), PhysicalPath)
    def get_connected_components(self):
        return create_e_list(self.get_java_object().getConnectedComponents(), Node)
    def get_allocated_component_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalLinksRealizedConnection", self)
    def get_realized_physical_links(self):
        return create_e_list(self.get_java_object().getRealizedPhysicalLinks(), PhysicalLink)
    def get_realizing_physical_links(self):
        return create_e_list(self.get_java_object().getRealizingPhysicalLinks(), PhysicalLink)

class PhysicalLinkCategory(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/" + capella_version(), "PhysicalLinkCategory"))
        elif isinstance(java_object, PhysicalLinkCategory):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_links(self):
        return create_e_list(self.get_java_object().getLinks(), PhysicalLink)

class PhysicalPath(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/" + capella_version(), "PhysicalPath"))
        elif isinstance(java_object, PhysicalPath):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_involved_physical_links(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalPath_PhysicalLinks", self)
    def get_involved_node_p_cs(self):
        return create_e_list(self.get_java_object().getInvolvedNodePCs(), Node)
    def get_allocated_component_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.PhysicalPath_RealisedConnection", self)
    def get_realized_physical_paths(self):
        return create_e_list(self.get_java_object().getRealizedPhysicalPaths(), PhysicalPath)
    def get_realizing_physical_paths(self):
        return create_e_list(self.get_java_object().getRealizingPhysicalPaths(), PhysicalPath)

class InterfacePkg(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/" + capella_version(), "InterfacePkg"))
        elif isinstance(java_object, InterfacePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_interface_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedInterfacePkgs(), InterfacePkg)
    def get_owned_interfaces(self):
        return create_e_list(self.get_java_object().getOwnedInterfaces(), Interface)
    def get_owned_exchange_items(self):
        return create_e_list(self.get_java_object().getOwnedExchangeItems(), ExchangeItem)

class Interface(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/" + capella_version(), "Interface"))
        elif isinstance(java_object, Interface):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_visibility(self):
        value =  self.get_java_object().getVisibility()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_visibility(self, value):
        return self.get_java_object().setVisibility(value.get_java_object())
    def get_owned_exchange_item_allocations(self):
        return create_e_list(self.get_java_object().getOwnedExchangeItemAllocations(), ExchangeItemAllocation)
    def get_exchange_items(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.InterfaceExchangesItems", self)
    def get_providing_component_ports(self):
        return create_e_list(self.get_java_object().getProvidingComponentPorts(), ComponentPort)
    def get_requiring_component_ports(self):
        return create_e_list(self.get_java_object().getRequiringComponentPorts(), ComponentPort)
    def get_user_components(self):
        return create_e_list(self.get_java_object().getUserComponents(), BehavioralComponent)
    def get_implementor_components(self):
        return create_e_list(self.get_java_object().getImplementorComponents(), BehavioralComponent)
    def get_super(self):
        return create_e_list(self.get_java_object().getSuper(), Interface)
    def get_sub(self):
        return create_e_list(self.get_java_object().getSub(), Interface)

class ExchangeItemAllocation(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/cs/" + capella_version(), "ExchangeItemAllocation"))
        elif isinstance(java_object, ExchangeItemAllocation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_transmission_protocol(self):
        value =  self.get_java_object().getTransmissionProtocol()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_transmission_protocol(self, value):
        return self.get_java_object().setTransmissionProtocol(value.get_java_object())
    def get_acquisition_protocol(self):
        value =  self.get_java_object().getAcquisitionProtocol()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_acquisition_protocol(self, value):
        return self.get_java_object().setAcquisitionProtocol(value.get_java_object())
    def get_allocated_item(self):
        value =  self.get_java_object().getAllocatedItem()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_allocated_item(self, value):
        return self.get_java_object().setAllocatedItem(value.get_java_object())
    def get_invoking_sequence_messages(self):
        return create_e_list(self.get_java_object().getInvokingSequenceMessages(), SequenceMessage)

class ExchangeItem(CapellaElement, AbstractAction, AbstractEvent, AbstractInstance):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "ExchangeItem"))
        elif isinstance(java_object, ExchangeItem):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_abstract(self):
        return self.get_java_object().isAbstract()
    def set_abstract(self, value):
        self.get_java_object().setAbstract(value)
    def get_final(self):
        return self.get_java_object().isFinal()
    def set_final(self, value):
        self.get_java_object().setFinal(value)
    def get_exchange_mechanism(self):
        value =  self.get_java_object().getExchangeMechanism()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_exchange_mechanism(self, value):
        return self.get_java_object().setExchangeMechanism(value.get_java_object())
    def get_owned_elements(self):
        return create_e_list(self.get_java_object().getOwnedElements(), ExchangeItemElement)
    def get_allocator_interfaces(self):
        return create_e_list(self.get_java_object().getAllocatorInterfaces(), Interface)
    def get_super(self):
        return create_e_list(self.get_java_object().getSuper(), ExchangeItem)
    def get_sub(self):
        return create_e_list(self.get_java_object().getSub(), ExchangeItem)
    def get_realized_exchange_items(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangeItem_realizedEI", self)
    def get_realizing_exchange_items(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangeItem_realizingEI", self)
    def get_realizing_operations(self):
        return create_e_list(self.get_java_object().getRealizingOperations(), Operation)

class ExchangeItemElement(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "ExchangeItemElement"))
        elif isinstance(java_object, ExchangeItemElement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_type(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangeItemElementType", self)

class FunctionPort(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionPort"))
        elif isinstance(java_object, FunctionPort):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_allocator_component_port(self):
        value =  self.get_java_object().getRepresentedComponentPort()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_allocator_component_port(self, value):
        return self.get_java_object().setRepresentedComponentPort(value.get_java_object())

class FunctionInputPort(FunctionPort):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionInputPort"))
        elif isinstance(java_object, FunctionInputPort):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_incoming_functional_exchanges(self):
        return create_e_list(self.get_java_object().getIncomingFunctionalExchanges(), FunctionalExchange)
    def get_incoming_exchange_items(self):
        return create_e_list(self.get_java_object().getIncomingExchangeItems(), ExchangeItem)
    def get_realized_function_input_ports(self):
        return create_e_list(self.get_java_object().getRealizedFunctionInputPorts(), FunctionInputPort)
    def get_realizing_function_input_ports(self):
        return create_e_list(self.get_java_object().getRealizingFunctionInputPorts(), FunctionInputPort)

class FunctionOutputPort(FunctionPort):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionOutputPort"))
        elif isinstance(java_object, FunctionOutputPort):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_outgoing_functional_exchanges(self):
        return create_e_list(self.get_java_object().getOutgoingFunctionalExchanges(), FunctionalExchange)
    def get_outgoing_exchange_items(self):
        return create_e_list(self.get_java_object().getOutgoingExchangeItems(), ExchangeItem)
    def get_realized_function_output_ports(self):
        return create_e_list(self.get_java_object().getRealizedFunctionOutputPorts(), FunctionOutputPort)
    def get_realizing_function_output_ports(self):
        return create_e_list(self.get_java_object().getRealizingFunctionOutputPorts(), FunctionOutputPort)

class FunctionalExchange(AbstractEvent, AbstractExchange):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionalExchange"))
        elif isinstance(java_object, FunctionalExchange):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_source(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalExchange_dataflowSource", self)
    def get_target(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalExchange_dataflowTarget", self)
    def get_exchanged_items(self):
        return create_e_list(self.get_java_object().getExchangedItems(), ExchangeItem)
    def get_involving_functional_chains(self):
        return create_e_list(self.get_java_object().getInvolvingFunctionalChains(), FunctionalChain)
    def get_categories(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalExchangeCategory", self)
    def get_allocating_component_exchange(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalExchangeAllocatingComponentExchange", self)
    def get_realized_functional_exchanges(self):
        return create_e_list(self.get_java_object().getRealizedFunctionalExchanges(), FunctionalExchange)
    def get_realizing_functional_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalExchange_realizingDataflow", self)
    def get_realized_interactions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalExchangeRealizedInteractions", self)

class ExchangeCategory(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "ExchangeCategory"))
        elif isinstance(java_object, ExchangeCategory):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_exchanges(self):
        return create_e_list(self.get_java_object().getExchanges(), FunctionalExchange)

class FunctionalChain(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "FunctionalChain"))
        elif isinstance(java_object, FunctionalChain):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_pre_condition(self):
        value =  self.get_java_object().getPreCondition()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_pre_condition(self, value):
        return self.get_java_object().setPreCondition(value.get_java_object())
    def get_post_condition(self):
        value =  self.get_java_object().getPostCondition()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_post_condition(self, value):
        return self.get_java_object().setPostCondition(value.get_java_object())
    def get_involved_functions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainInvolvementFunctions", self)
    def get_involved_functional_exchanges(self):
        return create_e_list(self.get_java_object().getInvolvedFunctionalExchanges(), FunctionalExchange)
    def get_involved_functional_chains(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainChildren", self)
    def get_involving_capabilities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.SAFunctionalChainInvolvingCapability", self)
    def get_available_in_states(self):
        return create_e_list(self.get_java_object().getAvailableInStates(), State)
    def get_realized_operational_processes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainRealizedOperationalProcess", self)
    def get_realized_functional_chains(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainRealizedFunctionalChains", self)
    def get_realizing_functional_chains(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionalChainRealizingFunctionalChains", self)

class BehavioralComponent(CapellaElement, AbstractInstance):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, BehavioralComponent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_contained_component_ports(self):
        return create_e_list(self.get_java_object().getContainedComponentPorts(), ComponentPort)
    def get_incoming_component_exchanges(self):
        return create_e_list(self.get_java_object().getIncomingComponentExchanges(), ComponentExchange)
    def get_outgoing_component_exchanges(self):
        return create_e_list(self.get_java_object().getOutgoingComponentExchanges(), ComponentExchange)
    def get_inout_component_exchanges(self):
        return create_e_list(self.get_java_object().getInoutComponentExchanges(), ComponentExchange)
    def get_allocated_functions(self):
        return create_e_list(self.get_java_object().getAllocatedFunctions(), Function)
    def get_used_interfaces(self):
        return create_e_list(self.get_java_object().getUsedInterfaces(), Interface)
    def get_implemented_interfaces(self):
        return create_e_list(self.get_java_object().getImplementedInterfaces(), Interface)
    def get_owned_state_machines(self):
        return create_e_list(self.get_java_object().getOwnedStateMachines(), StateMachine)

class ComponentPort(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "ComponentPort"))
        elif isinstance(java_object, ComponentPort):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_orientation(self):
        value =  self.get_java_object().getOrientation()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_orientation(self, value):
        return self.get_java_object().setOrientation(value.get_java_object())
    def get_component_exchanges(self):
        return create_e_list(self.get_java_object().getComponentExchanges(), ComponentExchange)
    def get_allocated_function_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentPort_realizedFunctionPort", self)
    def get_provided_interfaces(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentPort_providedInterfaces", self)
    def get_required_interfaces(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentPort_requiredInterfaces", self)
    def get_allocating_physical_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentPortAllocatingPhysicalPorts", self)
    def get_realized_component_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentPort_realizedComponentPort", self)
    def get_realizing_component_ports(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentPort_realizingComponentPort", self)

class ComponentExchange(CapellaElement, AbstractExchange):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "ComponentExchange"))
        elif isinstance(java_object, ComponentExchange):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_connected_component_ports(self):
        return create_e_list(self.get_java_object().getConnectedComponentPorts(), ComponentPort)
    def get_connected_components(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Connection_connectedComponents", self)
    def get_categories(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentExchangeCategories", self)
    def get_allocated_functional_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentExchangeAllocatedFunctionalExchanges", self)
    def get_convoyed_informations(self):
        return create_e_list(self.get_java_object().getConvoyedInformations(), ExchangeItem)
    def get_allocating_physical_link(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentExchangeAllocatingPhysicalLink", self)
    def get_allocating_physical_path(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ComponentExchangeAllocatingPhysicalPath", self)
    def get_realized_communication_means(self):
        return create_e_list(self.get_java_object().getRealizedCommunicationMeans(), CommunicationMean)
    def get_realized_component_exchanges(self):
        return create_e_list(self.get_java_object().getRealizedComponentExchanges(), ComponentExchange)
    def get_realizing_component_exchanges(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.ExchangeSpecification_realizingDataflow", self)
    def get_kind(self):
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_kind(self, value):
        return self.get_java_object().setKind(value.get_java_object())

class ComponentExchangeCategory(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/fa/" + capella_version(), "ComponentExchangeCategory"))
        elif isinstance(java_object, ComponentExchangeCategory):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_exchanges(self):
        return create_e_list(self.get_java_object().getExchanges(), ComponentExchange)

class AbstractCapability(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/interaction/" + capella_version(), "AbstractCapability"))
        elif isinstance(java_object, AbstractCapability):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_pre_condition(self):
        value =  self.get_java_object().getPreCondition()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_pre_condition(self, value):
        return self.get_java_object().setPreCondition(value.get_java_object())
    def get_post_condition(self):
        value =  self.get_java_object().getPostCondition()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_post_condition(self, value):
        return self.get_java_object().setPostCondition(value.get_java_object())
    def get_owned_scenarios(self):
        return create_e_list(self.get_java_object().getOwnedScenarios(), Scenario)
    def get_super(self):
        return create_e_list(self.get_java_object().getSuper(), AbstractCapability)
    def get_sub(self):
        return create_e_list(self.get_java_object().getSub(), AbstractCapability)
    def get_included_capabilities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Capability_includedCapabilities", self)
    def get_including_capabilities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Capability_includingCapabilities", self)
    def get_extended_capabilities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Capability_extendedCapabilities", self)
    def get_extending_capabilities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Capability_extendingCapabilities", self)
    def get_available_in_states(self):
        return create_e_list(self.get_java_object().getAvailableInStates(), State)

class AbstractSystemCapability(AbstractCapability):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, AbstractSystemCapability):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_functional_chains(self):
        return create_e_list(self.get_java_object().getOwnedFunctionalChains(), FunctionalChain)
    def get_involved_functional_chains(self):
        return create_e_list(self.get_java_object().getRealizedFunctionalChains(), FunctionalChain)
    def get_involved_functions(self):
        return create_e_list(self.get_java_object().getInvolvedFunctions(), Function)

class DataValue(JavaObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "DataValue"))
        elif isinstance(java_object, DataValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class LiteralBooleanValue(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "LiteralBooleanValue"))
        elif isinstance(java_object, LiteralBooleanValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class BooleanReference(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "BooleanReference"))
        elif isinstance(java_object, BooleanReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class EnumerationReference(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "EnumerationReference"))
        elif isinstance(java_object, EnumerationReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class LiteralStringValue(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "LiteralStringValue"))
        elif isinstance(java_object, LiteralStringValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class StringReference(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "StringReference"))
        elif isinstance(java_object, StringReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class LiteralNumericValue(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "LiteralNumericValue"))
        elif isinstance(java_object, LiteralNumericValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class NumericReference(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "NumericReference"))
        elif isinstance(java_object, NumericReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ComplexValue(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "ComplexValue"))
        elif isinstance(java_object, ComplexValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class ComplexValueReference(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "ComplexValueReference"))
        elif isinstance(java_object, ComplexValueReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class BinaryExpression(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "BinaryExpression"))
        elif isinstance(java_object, BinaryExpression):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class UnaryExpression(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "UnaryExpression"))
        elif isinstance(java_object, UnaryExpression):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class CollectionValueReference(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "CollectionValueReference"))
        elif isinstance(java_object, CollectionValueReference):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class CollectionValue(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "CollectionValue"))
        elif isinstance(java_object, CollectionValue):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class DataPkg(JavaObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "DataPkg"))
        elif isinstance(java_object, DataPkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class DataType(JavaObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/" + capella_version(), "DataType"))
        elif isinstance(java_object, DataType):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Class(DataType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "Class"))
        elif isinstance(java_object, Class):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_abstract(self):
        return self.get_java_object().isAbstract()
    def set_abstract(self, value):
        self.get_java_object().setAbstract(value)
    def get_final(self):
        return self.get_java_object().isFinal()
    def set_final(self, value):
        self.get_java_object().setFinal(value)
    def get_primitive(self):
        return self.get_java_object().isPrimitive()
    def set_primitive(self, value):
        self.get_java_object().setPrimitive(value)
    def get_visibility(self):
        value =  self.get_java_object().getVisibility()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_visibility(self, value):
        return self.get_java_object().setVisibility(value.get_java_object())
    def get_contained_properties(self):
        return create_e_list(self.get_java_object().getContainedProperties(), Property)
    def get_contained_operations(self):
        return create_e_list(self.get_java_object().getContainedOperations(), Operation)

class Collection(DataType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "Collection"))
        elif isinstance(java_object, Collection):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_ordered(self):
        return self.get_java_object().isOrdered()
    def set_ordered(self, value):
        self.get_java_object().setOrdered(value)
    def get_unique(self):
        return self.get_java_object().isUnique()
    def set_unique(self, value):
        self.get_java_object().setUnique(value)
    def get_min_inclusive(self):
        return self.get_java_object().isMinInclusive()
    def set_min_inclusive(self, value):
        self.get_java_object().setMinInclusive(value)
    def get_max_inclusive(self):
        return self.get_java_object().isMaxInclusive()
    def set_max_inclusive(self, value):
        self.get_java_object().setMaxInclusive(value)
    def get_abstract(self):
        return self.get_java_object().isAbstract()
    def set_abstract(self, value):
        self.get_java_object().setAbstract(value)
    def get_final(self):
        return self.get_java_object().isFinal()
    def set_final(self, value):
        self.get_java_object().setFinal(value)
    def get_primitive(self):
        return self.get_java_object().isPrimitive()
    def set_primitive(self, value):
        self.get_java_object().setPrimitive(value)
    def get_collection_kind(self):
        value =  self.get_java_object().getCollectionKind()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_collection_kind(self, value):
        return self.get_java_object().setCollectionKind(value.get_java_object())
    def get_aggregation_kind(self):
        value =  self.get_java_object().getAggregationKind()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_aggregation_kind(self, value):
        return self.get_java_object().setAggregationKind(value.get_java_object())
    def get_visibility(self):
        value =  self.get_java_object().getVisibility()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_visibility(self, value):
        return self.get_java_object().setVisibility(value.get_java_object())
    def get_contained_operations(self):
        return create_e_list(self.get_java_object().getContainedOperations(), Operation)
    def get_min_card(self):
        value =  self.get_java_object().getMinCard()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_min_card(self, value):
        return self.get_java_object().setMinCard(value.get_java_object())
    def get_max_card(self):
        value =  self.get_java_object().getMaxCard()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_max_card(self, value):
        return self.get_java_object().setMaxCard(value.get_java_object())

class Union(DataType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "Union"))
        elif isinstance(java_object, Union):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_final(self):
        return self.get_java_object().isFinal()
    def set_final(self, value):
        self.get_java_object().setFinal(value)
    def get_contained_union_properties(self):
        return create_e_list(self.get_java_object().getContainedUnionProperties(), UnionProperty)
    def get_discriminant(self):
        value =  self.get_java_object().getDiscriminant()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_discriminant(self, value):
        return self.get_java_object().setDiscriminant(value.get_java_object())
    def get_default_property(self):
        value =  self.get_java_object().getDefaultProperty()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_default_property(self, value):
        return self.get_java_object().setDefaultProperty(value.get_java_object())
    def get_kind(self):
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_kind(self, value):
        return self.get_java_object().setKind(value.get_java_object())
    def get_contained_operations(self):
        return create_e_list(self.get_java_object().getContainedOperations(), Operation)

class Association(JavaObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "Association"))
        elif isinstance(java_object, Association):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Property(JavaObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/ad/viewpoint/1.0.0", "Property"))
        elif isinstance(java_object, Property):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_type(self):
        value =  self.get_java_object().getType()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_type(self, value):
        return self.get_java_object().setType(value.get_java_object())

class UnionProperty(Property):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "UnionProperty"))
        elif isinstance(java_object, UnionProperty):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Operation(JavaObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "Operation"))
        elif isinstance(java_object, Operation):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_visibility(self):
        value =  self.get_java_object().getVisibility()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_visibility(self, value):
        return self.get_java_object().setVisibility(value.get_java_object())
    def get_realized_exchange_items(self):
        return create_e_list(self.get_java_object().getRealizedExchangeItems(), ExchangeItem)
    def get_owned_parameters(self):
        return create_e_list(self.get_java_object().getOwnedParameters(), Parameter)
    def get_thrown_exceptions(self):
        return create_e_list(self.get_java_object().getThrownExceptions(), Exception)

class Parameter(JavaObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "Parameter"))
        elif isinstance(java_object, Parameter):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Exception(JavaObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/communication/" + capella_version(), "Exception"))
        elif isinstance(java_object, Exception):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_abstract(self):
        return self.get_java_object().isAbstract()
    def set_abstract(self, value):
        self.get_java_object().setAbstract(value)
    def get_visibility(self):
        value =  self.get_java_object().getVisibility()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_visibility(self, value):
        return self.get_java_object().setVisibility(value.get_java_object())
    def get_super(self):
        return create_e_list(self.get_java_object().getSuper(), Exception)
    def get_sub(self):
        return create_e_list(self.get_java_object().getSub(), Exception)

class PrimitiveDataType(PropertyValuePkgContainer, DataType):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, PrimitiveDataType):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_abstract(self):
        return self.get_java_object().isAbstract()
    def set_abstract(self, value):
        self.get_java_object().setAbstract(value)
    def get_final(self):
        return self.get_java_object().isFinal()
    def set_final(self, value):
        self.get_java_object().setFinal(value)
    def get_discrete(self):
        return self.get_java_object().isDiscrete()
    def set_discrete(self, value):
        self.get_java_object().setDiscrete(value)
    def get_visibility(self):
        value =  self.get_java_object().getVisibility()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_visibility(self, value):
        return self.get_java_object().setVisibility(value.get_java_object())
    def get_super(self):
        return create_e_list(self.get_java_object().getSuper(), PrimitiveDataType)
    def get_sub(self):
        return create_e_list(self.get_java_object().getSub(), PrimitiveDataType)
    def get_realized_informations(self):
        return create_e_list(self.get_java_object().getRealizedInformations(), PrimitiveDataType)
    def get_realizing_informations(self):
        return create_e_list(self.get_java_object().getRealizingInformations(), PrimitiveDataType)

class Enumeration(PrimitiveDataType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/" + capella_version(), "Enumeration"))
        elif isinstance(java_object, Enumeration):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_min_inclusive(self):
        return self.get_java_object().isMinInclusive()
    def set_min_inclusive(self, value):
        self.get_java_object().setMinInclusive(value)
    def get_max_inclusive(self):
        return self.get_java_object().isMaxInclusive()
    def set_max_inclusive(self, value):
        self.get_java_object().setMaxInclusive(value)
    def get_pattern(self):
        return self.get_java_object().getPattern()
    def set_pattern(self, value):
        self.get_java_object().setPattern(value)
    def get_owned_literals(self):
        return create_e_list(self.get_java_object().getOwnedLiterals(), EnumerationLiteral)
    def get_default_value(self):
        value =  self.get_java_object().getDefaultValue()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_default_value(self, value):
        return self.get_java_object().setDefaultValue(value.get_java_object())
    def get_min_value(self):
        value =  self.get_java_object().getMinValue()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_min_value(self, value):
        return self.get_java_object().setMinValue(value.get_java_object())
    def get_max_value(self):
        value =  self.get_java_object().getMaxValue()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_max_value(self, value):
        return self.get_java_object().setMaxValue(value.get_java_object())
    def get_null_value(self):
        value =  self.get_java_object().getNullValue()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_null_value(self, value):
        return self.get_java_object().setNullValue(value.get_java_object())
    def get_domain_type(self):
        value =  self.get_java_object().getDomainType()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_domain_type(self, value):
        return self.get_java_object().setDomainType(value.get_java_object())

class EnumerationLiteral(DataValue):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datavalue/" + capella_version(), "EnumerationLiteral"))
        elif isinstance(java_object, EnumerationLiteral):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class BooleanType(PrimitiveDataType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/" + capella_version(), "BooleanType"))
        elif isinstance(java_object, BooleanType):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_literals(self):
        return create_e_list(self.get_java_object().getOwnedLiterals(), LiteralBooleanValue)
    def get_default_value(self):
        value =  self.get_java_object().getDefaultValue()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_default_value(self, value):
        return self.get_java_object().setDefaultValue(value.get_java_object())

class StringType(PrimitiveDataType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/" + capella_version(), "StringType"))
        elif isinstance(java_object, StringType):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_min_inclusive(self):
        return self.get_java_object().isMinInclusive()
    def set_min_inclusive(self, value):
        self.get_java_object().setMinInclusive(value)
    def get_max_inclusive(self):
        return self.get_java_object().isMaxInclusive()
    def set_max_inclusive(self, value):
        self.get_java_object().setMaxInclusive(value)
    def get_pattern(self):
        return self.get_java_object().getPattern()
    def set_pattern(self, value):
        self.get_java_object().setPattern(value)
    def get_min_length(self):
        value =  self.get_java_object().getMinLength()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_min_length(self, value):
        return self.get_java_object().setMinLength(value.get_java_object())
    def get_max_length(self):
        value =  self.get_java_object().getMaxLength()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_max_length(self, value):
        return self.get_java_object().setMaxLength(value.get_java_object())
    def get_default_value(self):
        value =  self.get_java_object().getDefaultValue()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_default_value(self, value):
        return self.get_java_object().setDefaultValue(value.get_java_object())
    def get_null_value(self):
        value =  self.get_java_object().getNullValue()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_null_value(self, value):
        return self.get_java_object().setNullValue(value.get_java_object())

class NumericType(PrimitiveDataType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/" + capella_version(), "NumericType"))
        elif isinstance(java_object, NumericType):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_min_inclusive(self):
        return self.get_java_object().isMinInclusive()
    def set_min_inclusive(self, value):
        self.get_java_object().setMinInclusive(value)
    def get_max_inclusive(self):
        return self.get_java_object().isMaxInclusive()
    def set_max_inclusive(self, value):
        self.get_java_object().setMaxInclusive(value)
    def get_pattern(self):
        return self.get_java_object().getPattern()
    def set_pattern(self, value):
        self.get_java_object().setPattern(value)
    def get_kind(self):
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_kind(self, value):
        return self.get_java_object().setKind(value.get_java_object())
    def get_min_value(self):
        value =  self.get_java_object().getMinValue()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_min_value(self, value):
        return self.get_java_object().setMinValue(value.get_java_object())
    def get_max_value(self):
        value =  self.get_java_object().getMaxValue()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_max_value(self, value):
        return self.get_java_object().setMaxValue(value.get_java_object())
    def get_default_value(self):
        value =  self.get_java_object().getDefaultValue()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_default_value(self, value):
        return self.get_java_object().setDefaultValue(value.get_java_object())
    def get_null_value(self):
        value =  self.get_java_object().getNullValue()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_null_value(self, value):
        return self.get_java_object().setNullValue(value.get_java_object())

class PhysicalQuantity(NumericType):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/datatype/" + capella_version(), "PhysicalQuantity"))
        elif isinstance(java_object, PhysicalQuantity):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_unit(self):
        value =  self.get_java_object().getUnit()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_unit(self, value):
        return self.get_java_object().setUnit(value.get_java_object())

class Unit(CapellaElement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/information/" + capella_version(), "Unit"))
        elif isinstance(java_object, Unit):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class PVMT(JavaObject):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, PVMT):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_p_v_names(self, elem):
        raise AttributeError("TODO")
    def is_p_v_defined(self, elem, PVName):
        raise AttributeError("TODO")
    def get_p_v_value(self, elem, PVName):
        raise AttributeError("TODO")

class RequirementAddOn(JavaObject):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, RequirementAddOn):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    @staticmethod
    def get_requirement_modules(capellaModel):
        #: :type capellaModel: CapellaModel
        res = []
        se = capellaModel.get_system_engineering()
        for modelArchitecture in se.get_java_object().getOwnedArchitectures():
            for extension in modelArchitecture.getOwnedExtensions():
                if extension.eClass().getName() == "CapellaModule" and extension.eClass().getEPackage().getNsURI() == "http://www.polarsys.org/capella/requirements":
                    res.append(CapellaModule(extension))
        return res
    @staticmethod
    def get_incoming_requirements(capellaModel):
        #: :type capellaModel: CapellaModel
        res = []
        modules = RequirementAddOn.get_requirement_modules(capellaModel)
        for module in modules:
            for requirement in module.get_java_object().getOwnedRequirements():
                for relation in requirement.getOwnedRelations():
                    if relation.eClass().getName() == "CapellaIncomingRelation" and relation.eClass().getEPackage().getNsURI() == "http://www.polarsys.org/capella/requirements":
                        res.append(Requirement(requirement))
                        break
                try:
                    res.index(requirement)
                    break
                except ValueError:
                    continue
        return res
    @staticmethod
    def get_outgoing_requirements(capellaModel):
        #: :type capellaModel: CapellaModel
        res = []
        modules = RequirementAddOn.get_requirement_modules(capellaModel)
        for module in modules:
            for requirement in module.get_java_object().getOwnedRequirements():
                for relation in requirement.getOwnedRelations():
                    if relation.eClass().getName() == "CapellaOutgoingRelation" and relation.eClass().getEPackage().getNsURI() == "http://www.polarsys.org/capella/requirements":
                        res.append(Requirement(requirement))
                        break
                try:
                    res.index(requirement)
                    break
                except ValueError:
                    continue
        return res
    def get_relation_type(self, elem1, elem2):
        raise AttributeError("TODO")

class CapellaModule(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/requirements", "CapellaModule"))
        elif isinstance(java_object, Requirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_requirements(self):
        return create_e_list(self.get_java_object().getOwnedRequirements(), Requirement)
    def get_id(self):
        return self.get_java_object().getReqIFIdentifier()
    def set_id(self, value):
        self.get_java_object().setReqIFIdentifier(value)
    def get_long_name(self):
        return self.get_java_object().getReqIFLongName()
    def set_long_name(self, value):
        self.get_java_object().setReqIFLongName(value)
    def get_name(self):
        return self.get_java_object().getReqIFName()
    def set_name(self, value):
        self.get_java_object().setReqIFName(value)
    def get_prefix(self):
        return self.get_java_object().getReqIFPrefix()
    def set_prefix(self, value):
        self.get_java_object().setReqIFPrefix(value)

class Requirement(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "Requirement"))
        elif isinstance(java_object, Requirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_id(self):
        return self.get_java_object().getReqIFIdentifier()
    def set_id(self, value):
        self.get_java_object().setReqIFIdentifier(value)
    def get_long_name(self):
        return self.get_java_object().getReqIFLongName()
    def set_long_name(self, value):
        self.get_java_object().setReqIFLongName(value)
    def get_name(self):
        return self.get_java_object().getReqIFName()
    def set_name(self, value):
        self.get_java_object().setReqIFName(value)
    def get_chapter_name(self):
        return self.get_java_object().getReqIFChapterName()
    def set_chapter_name(self, value):
        self.get_java_object().setReqIFChapterName(value)
    def get_prefix(self):
        return self.get_java_object().getReqIFPrefix()
    def set_prefix(self, value):
        self.get_java_object().setReqIFPrefix(value)
    def get_text(self):
        return self.get_java_object().getReqIFText()
    def set_text(self, value):
        self.get_java_object().setReqIFText(value)
    def get_owned_attributes(self):
        return create_e_list(self.get_java_object().getOwnedAttributes(), Attribute)
    def get_incoming_linked_elems(self):
        raise AttributeError("TODO")
    def get_outgoing_linked_elems(self):
        raise AttributeError("TODO")

class Folder(Requirement):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "Folder"))
        elif isinstance(java_object, Requirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_requirements(self):
        return create_e_list(self.get_java_object().getOwnedRequirements(), Requirement)

class Attribute(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/kitalpha/requirements", "Attribute"))
        elif isinstance(java_object, Requirement):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_name(self):
        return self.get_java_object().getReqIFName()
    def set_name(self, value):
        self.get_java_object().setReqIFName(value)
    def get_value(self):
        return self.get_java_object().getValue()
    def set_value(self, value):
        self.get_java_object().setValue(value)
    def get_kind(self):
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_kind(self, value):
        return self.get_java_object().setKind(value.get_java_object())

class SystemEngineering(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/modeller/" + capella_version(), "SystemEngineering"))
        elif isinstance(java_object, SystemEngineering):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_rec_catalogs(self):
        return create_e_list(self.get_java_object().getRecCatalogs(), RecCatalog)
    def get_operational_analysis(self):
        value =  self.get_java_object().getOperationalAnalysis()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_operational_analysis(self, value):
        return self.get_java_object().setOperationalAnalysis(value.get_java_object())
    def get_system_analysis(self):
        value =  self.get_java_object().getSystemAnalysis()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_system_analysis(self, value):
        return self.get_java_object().setSystemAnalysis(value.get_java_object())
    def get_logical_architecture(self):
        value =  self.get_java_object().getLogicalArchitecture()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_logical_architecture(self, value):
        return self.get_java_object().setLogicalArchitecture(value.get_java_object())
    def get_physical_architecture(self):
        value =  self.get_java_object().getPhysicalArchitecture()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_physical_architecture(self, value):
        return self.get_java_object().setPhysicalArchitecture(value.get_java_object())
    def get_e_p_b_s_architecture(self):
        value =  self.get_java_object().getEPBSArchitecture()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_e_p_b_s_architecture(self, value):
        return self.get_java_object().setEPBSArchitecture(value.get_java_object())

class PropertyValuePkg(PropertyValuePkgContainer):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/" + capella_version(), "PropertyValuePkg"))
        elif isinstance(java_object, PropertyValuePkg):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class Interaction(AbstractEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, Interaction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_source(self):
        value =  self.get_java_object().getSource()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_source(self, value):
        return self.get_java_object().setSource(value.get_java_object())
    def get_target(self):
        value =  self.get_java_object().getTarget()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_target(self, value):
        return self.get_java_object().setTarget(value.get_java_object())
    def get_allocating_communication_mean(self):
        value =  self.get_java_object().getAllocatingCommunicationMean()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_allocating_communication_mean(self, value):
        return self.get_java_object().setAllocatingCommunicationMean(value.get_java_object())
    def get_involving_operational_processes(self):
        return create_e_list(self.get_java_object().getInvolvingOperationalProcesses(), OperationalProcess)
    def get_exchanged_items(self):
        return create_e_list(self.get_java_object().getExchangedItems(), ExchangeItem)
    def get_realizing_functional_exchanges(self):
        return create_e_list(self.get_java_object().getRealizingFunctionalExchanges(), FunctionalExchange)

class OperationalCapability(AbstractCapability):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/" + capella_version(), "OperationalCapability"))
        elif isinstance(java_object, OperationalCapability):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_operational_processes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractCapabilityOwnedFunctionalChains", self)
    def get_involved_operational_processes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractCapabilityInvolvedFunctionalChains", self)
    def get_involved_operational_activities(self):
        return create_e_list(self.get_java_object().getInvolvedOperationalActivities(), OperationalActivity)
    def get_involved_entities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.OperationalCapability_InvolvedEntity", self)
    def get_realizing_capabilities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.OCapabilityRealizingCapability", self)

class OperationalEntity(OperationalActor):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, OperationalEntity):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_entities(self):
        return create_e_list(self.get_java_object().getOwnedEntities(), OperationalEntity)

class Capability(AbstractSystemCapability):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "Capability"))
        elif isinstance(java_object, Capability):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_purpose_missions(self):
        return create_e_list(self.get_java_object().getPurposeMissions(), Mission)
    def get_realized_operational_capabilities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapabilityRealizedOC", self)
    def get_realizing_capability_realizations(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapabilityRealizingCR", self)
    def get_involved_system_actors(self):
        return create_e_list(self.get_java_object().getInvolvedSystemActors(), SystemActor)

class System(BehavioralComponent, Node):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, System):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

class SystemActor(BehavioralComponent, Node):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, SystemActor):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_is_human(self):
        return self.get_java_object().isIsHuman()
    def set_is_human(self, value):
        self.get_java_object().setIsHuman(value)
    def get_owned_actors(self):
        return create_e_list(self.get_java_object().getOwnedActors(), SystemActor)
    def get_owned_system_component_pkgs(self):
        value =  self.get_java_object().getOwnedSystemComponentPkgs()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_owned_system_component_pkgs(self, value):
        return self.get_java_object().setOwnedSystemComponentPkgs(value.get_java_object())
    def get_involving_missions(self):
        return create_e_list(self.get_java_object().getInvolvingMissions(), Mission)
    def get_realized_operational_entities(self):
        return create_e_list(self.get_java_object().getRealizedOperationalEntities(), OperationalActor)
    def get_involving_capabilities(self):
        return create_e_list(self.get_java_object().getInvolvingCapabilities(), Capability)
    def get_realizing_logical_actors(self):
        return create_e_list(self.get_java_object().getRealizingLogicalActors(), LogicalActor)

class CapabilityRealization(AbstractSystemCapability):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/" + capella_version(), "CapabilityRealization"))
        elif isinstance(java_object, CapabilityRealization):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_realized_capabilities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapabilityRealization_RealizedCapability", self)
    def get_realized_capability_realizations(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapabilityRealization_RealizedCapabilityRealization", self)
    def get_realizing_capability_realizations(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.CapabilityRealization_RealizingCapabilityRealization", self)
    def get_involved_logical_actors(self):
        return create_e_list(self.get_java_object().getInvolvedLogicalActors(), LogicalActor)
    def get_involved_logical_components(self):
        return create_e_list(self.get_java_object().getInvolvedLogicalComponents(), LogicalComponent)
    def get_involved_physical_components(self):
        return create_e_list(self.get_java_object().getInvolvedPhysicalComponents(), PhysicalComponent)
    def get_involved_physical_actors(self):
        return create_e_list(self.get_java_object().getInvolvedPhysicalActors(), PhysicalActor)

class LogicalSystem(BehavioralComponent, Node):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, LogicalSystem):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_logical_components(self):
        return create_e_list(self.get_java_object().getOwnedLogicalComponents(), LogicalComponent)
    def get_owned_logical_component_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedLogicalComponentPkgs(), LogicalComponentPkg)

class LogicalComponent(BehavioralComponent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalComponent"))
        elif isinstance(java_object, LogicalComponent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_logical_components(self):
        return create_e_list(self.get_java_object().getOwnedLogicalComponents(), LogicalComponent)
    def get_owned_logical_component_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedLogicalComponentPkgs(), LogicalComponentPkg)
    def get_is_human(self):
        return self.get_java_object().isIsHuman()
    def set_is_human(self, value):
        self.get_java_object().setIsHuman(value)
    def get_realizing_behavior_p_cs(self):
        return create_e_list(self.get_java_object().getRealizingBehaviorPCs(), BehaviorPC)
    def get_involving_capability_realizations(self):
        return create_e_list(self.get_java_object().getInvolvingCapabilityRealizations(), CapabilityRealization)

class LogicalActor(BehavioralComponent, Node):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, LogicalActor):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_logical_actors(self):
        return create_e_list(self.get_java_object().getOwnedLogicalActors(), LogicalActor)
    def get_owned_logical_component_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedLogicalComponentPkgs(), LogicalComponentPkg)
    def get_realized_system_actors(self):
        return create_e_list(self.get_java_object().getRealizedSystemActors(), SystemActor)
    def get_is_human(self):
        return self.get_java_object().isIsHuman()
    def set_is_human(self, value):
        self.get_java_object().setIsHuman(value)
    def get_realizing_physical_actors(self):
        return create_e_list(self.get_java_object().getRealizingPhysicalActors(), PhysicalActor)
    def get_involving_capability_realizations(self):
        return create_e_list(self.get_java_object().getInvolvingCapabilityRealizations(), CapabilityRealization)

class BehaviorPC(PhysicalComponent, BehavioralComponent):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, BehaviorPC):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_deploying_node_p_c(self):
        value =  self.get_java_object().getDeployingNodePC()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_deploying_node_p_c(self, value):
        return self.get_java_object().setDeployingNodePC(value.get_java_object())
    def get_realized_logical_components(self):
        return create_e_list(self.get_java_object().getRealizedLogicalComponents(), LogicalComponent)

class NodePC(PhysicalComponent, CapellaElement, Node):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, NodePC):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_deployed_behavior_p_cs(self):
        return create_e_list(self.get_java_object().getDeployedBehaviorPCs(), BehaviorPC)
    def get_owned_state_machines(self):
        return create_e_list(self.get_java_object().getOwnedStateMachines(), StateMachine)

class PhysicalActor(BehavioralComponent, Node):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, PhysicalActor):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_owned_physical_actors(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalActors(), PhysicalActor)
    def get_owned_physical_component_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalComponentPkgs(), PhysicalComponentPkg)
    def get_realized_logical_actors(self):
        return create_e_list(self.get_java_object().getRealizedLogicalActors(), LogicalActor)
    def get_is_human(self):
        return self.get_java_object().isIsHuman()
    def set_is_human(self, value):
        self.get_java_object().setIsHuman(value)
    def get_involving_capability_realizations(self):
        return create_e_list(self.get_java_object().getInvolvingCapabilityRealizations(), CapabilityRealization)

class ChangeEvent(AbstractEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), "ChangeEvent"))
        elif isinstance(java_object, ChangeEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_expression(self):
        return self.get_java_object().getExpression()
    def set_expression(self, value):
        self.get_java_object().setExpression(value)

class TimeEvent(AbstractEvent):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/common/" + capella_version(), "TimeEvent"))
        elif isinstance(java_object, TimeEvent):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_kind(self, value):
        return self.get_java_object().setKind(value.get_java_object())
    def get_expression(self):
        return self.get_java_object().getExpression()
    def set_expression(self, value):
        self.get_java_object().setExpression(value)

class AbstractActivityFunction(CapellaElement, AbstractAction, AbstractEvent, AbstractInstance):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, AbstractActivityFunction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_available_in_states(self):
        return create_e_list(self.get_java_object().getAvailableInStates(), State)

class Function(AbstractActivityFunction):
    def __init__(self, java_object = None):
        if java_object is None:
            raise ValueError("No matching EClass for this type")
        elif isinstance(java_object, Function):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_kind(self):
        value =  self.get_java_object().getKind()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_kind(self, value):
        return self.get_java_object().setKind(value.get_java_object())
    def get_condition(self):
        return self.get_java_object().getCondition()
    def set_condition(self, value):
        self.get_java_object().setCondition(value)
    def get_inputs(self):
        return create_e_list(self.get_java_object().getInputs(), FunctionInputPort)
    def get_outputs(self):
        return create_e_list(self.get_java_object().getOutputs(), FunctionOutputPort)
    def get_incoming(self):
        return create_e_list(self.get_java_object().getIncoming(), FunctionalExchange)
    def get_outgoing(self):
        return create_e_list(self.get_java_object().getOutgoing(), FunctionalExchange)
    def get_allocating_component(self):
        value =  self.get_java_object().getAllocatingComponent()
        if value is None:
            return value
        else:
            specific_cls = getattr(sys.modules["__main__"], value.eClass().getName())
            return specific_cls(value)
    def set_allocating_component(self, value):
        return self.get_java_object().setAllocatingComponent(value.get_java_object())
    def get_owned_functional_chains(self):
        return create_e_list(self.get_java_object().getOwnedFunctionalChains(), FunctionalChain)
    def get_involving_functional_chains(self):
        return create_e_list(self.get_java_object().getInvolvingFunctionalChains(), FunctionalChain)
    def get_involving_capabilities(self):
        return create_e_list(self.get_java_object().getInvolvingCapabilities(), AbstractSystemCapability)

class OperationalActivity(AbstractActivityFunction):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/oa/" + capella_version(), "OperationalActivity"))
        elif isinstance(java_object, OperationalActivity):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_contained_operational_activities(self):
        return create_e_list(self.get_java_object().getContainedOperationalActivities(), OperationalActivity)
    def get_owned_operational_activity_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedOperationalActivityPkgs(), OperationalActivityPkg)
    def get_incoming(self):
        return create_e_list(self.get_java_object().getIncoming(), Interaction)
    def get_outgoing(self):
        return create_e_list(self.get_java_object().getOutgoing(), Interaction)
    def get_allocating_entity(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.FunctionAllocatingComponent", self)
    def get_owned_operational_processes(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.Function_ownedFunctionalChains", self)
    def get_involving_operational_processes(self):
        return create_e_list(self.get_java_object().getInvolvingOperationalProcesses(), OperationalProcess)
    def get_involving_operational_capabilities(self):
        return create_e_list(self.get_java_object().getInvolvingOperationalCapabilities(), OperationalCapability)
    def get_realizing_system_functions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_realizingFunctions", self)

class SystemFunction(Function):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/ctx/" + capella_version(), "SystemFunction"))
        elif isinstance(java_object, SystemFunction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_contained_system_functions(self):
        return create_e_list(self.get_java_object().getContainedSystemFunctions(), SystemFunction)
    def get_owned_system_function_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedSystemFunctionPkgs(), SystemFunctionPkg)
    def get_realized_operational_activities(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_realizedFunctions", self)
    def get_realizing_logical_functions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_realizingFunctions", self)

class LogicalFunction(Function):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/la/" + capella_version(), "LogicalFunction"))
        elif isinstance(java_object, LogicalFunction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_contained_logical_functions(self):
        return create_e_list(self.get_java_object().getContainedLogicalFunctions(), LogicalFunction)
    def get_owned_logical_function_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedLogicalFunctionPkgs(), LogicalFunctionPkg)
    def get_realized_system_functions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_realizedFunctions", self)
    def get_realizing_physical_functions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_realizingFunctions", self)

class PhysicalFunction(Function):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/pa/" + capella_version(), "PhysicalFunction"))
        elif isinstance(java_object, PhysicalFunction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)
    def get_contained_physical_functions(self):
        return create_e_list(self.get_java_object().getContainedPhysicalFunctions(), PhysicalFunction)
    def get_owned_physical_function_pkgs(self):
        return create_e_list(self.get_java_object().getOwnedPhysicalFunctionPkgs(), PhysicalFunctionPkg)
    def get_realized_logical_functions(self):
        return capella_query("org.polarsys.capella.core.semantic.queries.basic.queries.AbstractFunction_realizedFunctions", self)

class Status(EObject):
    def __init__(self, java_object = None):
        if java_object is None:
            EObject.__init__(self, create_e_object("http://www.polarsys.org/capella/core/core/" + capella_version(), "EnumerationPropertyLiteral"))
        elif isinstance(java_object, PhysicalFunction):
            EObject.__init__(self, java_object.get_java_object())
        else:
            EObject.__init__(self, java_object)

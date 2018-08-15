from src.main.common.model import endpoint
from src.main.admin_api.utils.descriptor_utils import DescriptorUtils
from src.main.admin_api.model.database import Database


class DatabaseEndpoint(endpoint.Endpoint):

    @classmethod
    def do_get(cls, *args, **kwargs):
        db_system_name = kwargs.get("db_system_name", None)
        response = None
        if db_system_name is None:
            descriptor_dicts = []
            descriptors = DescriptorUtils.get_dbs_descriptor()
            for d in descriptors:
                descriptor_dicts.append(d.to_dict())
            response = descriptor_dicts
        else:
            descriptor = DescriptorUtils.get_db_descriptor_by_system_name(db_system_name)
            if descriptor is not None:
                response = descriptor.to_dict(True)
        return response

    @classmethod
    def do_post(cls, *args, **kwargs):
        response = None
        body = DatabaseEndpoint.get_body()
        name = body.get("name", None)
        if name is not None:
            descriptor = Database.from_json(body)
            if not DescriptorUtils.does_db_descriptor_exist(descriptor):
                descriptor.save()
                response = descriptor.to_dict()
        return response

    @classmethod
    def do_put(cls, *args, **kwargs):
        db_system_name = kwargs.get("db_system_name", None)
        response = None
        body = DatabaseEndpoint.get_body()
        if db_system_name is not None:
            descriptor = DescriptorUtils.get_db_descriptor_by_system_name(db_system_name)
            if descriptor is not None:
                name = body.get("name", None)
                if name is not None:
                    descriptor.set_name(name)
                description = body.get("description", None)
                if description is not None:
                    descriptor.set_description(description)
                descriptor.save()
                response = descriptor.to_dict()
        return response

    @classmethod
    def do_delete(cls, *args, **kwargs):
        db_system_name = kwargs.get("db_system_name")
        response = None
        descriptor = DescriptorUtils.get_db_descriptor_by_system_name(db_system_name)
        if descriptor is not None:
            response = descriptor.delete()
        return response

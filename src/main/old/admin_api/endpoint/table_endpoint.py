from src.main.old.common.model import endpoint


class TableEndpoint(endpoint.Endpoint):

    @classmethod
    def do_get(cls, *args, **kwargs):
        from src.main.old.admin_api.utils.descriptor_utils import DescriptorUtils

        db_system_name = kwargs.get("db_system_name")
        tb_system_name = kwargs.get("tb_system_name", None)
        response = None
        if tb_system_name is None:
            descriptor_dicts = []
            descriptors = DescriptorUtils.get_tbs_descriptor(db_system_name)
            for d in descriptors:
                descriptor_dicts.append(d.to_dict())
            response = descriptor_dicts
        else:
            descriptor = DescriptorUtils.get_tb_descriptor_by_system_name(db_system_name, tb_system_name)
            if descriptor is not None:
                response = descriptor.to_dict()
        return response

    @classmethod
    def do_post(cls, *args, **kwargs):
        from src.main.old.admin_api.utils.descriptor_utils import DescriptorUtils
        from src.main.old.admin_api.model.table import Table

        db_system_name = kwargs.get("db_system_name")
        response = None
        body = TableEndpoint.get_body()
        name = body.get("name", None)
        if name is not None:
            descriptor = Table.from_json(body)
            if not DescriptorUtils.does_tb_descriptor_exist(db_system_name, descriptor):
                descriptor.save(db_system_name)
                response = descriptor.to_dict()
        return response

    @classmethod
    def do_put(cls, *args, **kwargs):
        from src.main.old.admin_api.utils.descriptor_utils import DescriptorUtils

        db_system_name = kwargs.get("db_system_name")
        tb_system_name = kwargs.get("tb_system_name")
        response = None
        body = TableEndpoint.get_body()
        if tb_system_name is not None:
            descriptor = DescriptorUtils.get_tb_descriptor_by_system_name(db_system_name, tb_system_name)
            if descriptor is not None:
                name = body.get("name", None)
                if name is not None:
                    descriptor.set_name(name)
                description = body.get("description", None)
                if description is not None:
                    descriptor.set_description(description)
                fields = body.get("fields", None)
                if fields is not None:
                    descriptor.set_fields(fields)
                descriptor.save(db_system_name)
                response = descriptor.to_dict()
        return response

    @classmethod
    def do_delete(cls, *args, **kwargs):
        from src.main.old.admin_api.utils.descriptor_utils import DescriptorUtils

        db_system_name = kwargs.get("db_system_name")
        tb_system_name = kwargs.get("tb_system_name")
        response = None
        descriptor = DescriptorUtils.get_tb_descriptor_by_system_name(db_system_name, tb_system_name)
        if descriptor is not None:
            response = descriptor.delete(db_system_name)
        return response

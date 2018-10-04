from src.main.old.common.model import endpoint


class FieldEndpoint(endpoint.Endpoint):

    @classmethod
    def do_get(cls, *args, **kwargs):
        from src.main.old.admin_api.utils.descriptor_utils import DescriptorUtils

        db_system_name = kwargs.get("db_system_name")
        tb_system_name = kwargs.get("tb_system_name")
        fd_system_name = kwargs.get("fd_system_name", None)
        response = None
        descriptor = DescriptorUtils.get_tb_descriptor_by_system_name(db_system_name, tb_system_name)
        if descriptor is not None:
            if fd_system_name is None:
                fields = []
                for f in descriptor.get_fields():
                    fields.append(f.to_dict())
                response = fields
            else:
                field = descriptor.get_field_by_system_name(fd_system_name)
                if field is not None:
                    response = field.to_dict()
        return response

    @classmethod
    def do_post(cls, *args, **kwargs):
        from src.main.old.common.utils.cleaner_utils import CleanerUtils
        from src.main.old.admin_api.utils.descriptor_utils import DescriptorUtils
        from src.main.old.admin_api.model.field import Field

        db_system_name = kwargs.get("db_system_name")
        tb_system_name = kwargs.get("tb_system_name")
        response = None
        descriptor = DescriptorUtils.get_tb_descriptor_by_system_name(db_system_name, tb_system_name)
        if descriptor is not None:
            body = FieldEndpoint.get_body()
            name = body.get("name", None)
            if name is not None:
                fd_system_name = CleanerUtils.generate_system_name(name)
                if descriptor.get_field_by_system_name(fd_system_name) is None:
                    id_ = body.get("id", False)
                    description = body.get("description", None)
                    type_ = body.get("type", "string")
                    field = Field(
                        id=id_,
                        name=name,
                        description=description,
                        type=type_
                    )
                    descriptor.add_field(field)
                    descriptor.save(db_system_name)
                    response = field.to_dict()
        return response

    @classmethod
    def do_put(cls, *args, **kwargs):
        from src.main.old.admin_api.utils.descriptor_utils import DescriptorUtils

        db_system_name = kwargs.get("db_system_name")
        tb_system_name = kwargs.get("tb_system_name")
        fd_system_name = kwargs.get("fd_system_name")
        response = None
        descriptor = DescriptorUtils.get_tb_descriptor_by_system_name(db_system_name, tb_system_name)
        if descriptor is not None:
            body = FieldEndpoint.get_body()
            if fd_system_name is not None:
                field = descriptor.get_field_by_system_name(fd_system_name)
                if field is not None:
                    id_ = body.get("id", None)
                    if id_ is not None:
                        field.set_id(id_)
                    name = body.get("name", None)
                    if name is not None:
                        field.set_name(name)
                    description = body.get("description", None)
                    if description is not None:
                        field.set_description(description)
                    type_ = body.get("type", None)
                    if type_ is not None:
                        field.set_type(type_)
                    if descriptor.update_field(field):
                        response = field.to_dict()
                        descriptor.save(db_system_name)
        return response

    @classmethod
    def do_delete(cls, *args, **kwargs):
        from src.main.old.admin_api.utils.descriptor_utils import DescriptorUtils

        db_system_name = kwargs.get("db_system_name")
        tb_system_name = kwargs.get("tb_system_name")
        fd_system_name = kwargs.get("fd_system_name")
        response = None
        descriptor = DescriptorUtils.get_tb_descriptor_by_system_name(db_system_name, tb_system_name)
        if descriptor is not None:
            response = descriptor.remove_field(fd_system_name)
            descriptor.save(db_system_name)
        return response

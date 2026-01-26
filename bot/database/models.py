def import_all_models():
    """Импортирует все модели для регистрации в SQLAlchemy"""
    from bot.user.infra.database.models.users import Users
    from bot.groups.infra.database.models.groups import Group
    return Users, Group
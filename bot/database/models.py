def import_all_models():
    """Импортирует все модели для регистрации в SQLAlchemy"""
    from bot.user.models import User
    from bot.groups.models.groups import Group
    return User, Group
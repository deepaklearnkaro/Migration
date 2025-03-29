from sqlalchemy.orm import sessionmaker
from database import engine
from models import Role, User, Permission
import uuid

# Create a new session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Insert Roles
admin_role = Role(id=str(uuid.uuid4()), name="Admin")
user_role = Role(id=str(uuid.uuid4()), name="User")

session.add_all([admin_role, user_role])
session.commit()

# Insert Users
admin_user = User(id=str(uuid.uuid4()), username="admin", password="admin123", role_id=admin_role.id)
normal_user = User(id=str(uuid.uuid4()), username="user", password="user123", role_id=user_role.id)

session.add_all([admin_user, normal_user])
session.commit()

# Insert Permissions
admin_permission = Permission(id=str(uuid.uuid4()), user_id=admin_user.id, permission_name="manage_users", is_enabled=True)
user_permission = Permission(id=str(uuid.uuid4()), user_id=normal_user.id, permission_name="view_data", is_enabled=True)

session.add_all([admin_permission, user_permission])
session.commit()

print("✅ Data inserted successfully!")

# Close session
session.close()



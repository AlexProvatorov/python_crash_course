"""
Множественные модули: сохраните класс User в одном модуле, а классы Privileges и
Admin в другом модуле. В отдельном файле создайте экземпляр Admin и вызовите 
метод show_privileges(), чтобы показать, что все работает правильно.

"""
import admin_and_privileges

admin = admin_and_privileges.Admin('alex', 'satan', 22, 'rostov', 'karate')
admin.describe_user()
admin.privileges.show_privileges()
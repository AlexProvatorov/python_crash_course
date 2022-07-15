"""
Импортирование класса Admin: начните с версии класса из упражнения 9.8. 
Сохраните классы User, Privileges и Admin в одном модуле. Создайте отдельный 
файл, создайте экземпляр Admin и вызовите метод show_privileges(), 
чтобы показать, что все работает правильно.

"""
import admin_and_privileges

admin = admin_and_privileges.Admin('alex', 'satan', 22, 'rostov', 'karate')
admin.describe_user()
admin.privileges.show_privileges()
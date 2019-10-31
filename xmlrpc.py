import xmlrpclib

spacewalk_login = ''
spacewalk_password = ''
system_name = 'gcappprd200.c020.dgtlrvr.net'
spacewalk_url = "https://iaas-repoapp-04.c022.dgtlrvr.net/rpc/api"

server = xmlrpclib.Server(spacewalk_url)
key = server.auth.login(spacewalk_login, spacewalk_password)

system_id = server.system.getId(key,system_name) # dict inside of list
available_groups = server.system.listGroups(key,system_id[0]['id'])
server.auth.logout(key)
